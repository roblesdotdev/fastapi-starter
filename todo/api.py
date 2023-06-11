from datetime import datetime
import uuid

from fastapi import HTTPException
from starlette import status
from starlette.responses import Response

from todo.server import server
from todo.schema import ListTasksSchema, GetTaskSchema, CreateTaskSchema

TODOS = []


@server.get("/todo", response_model=ListTasksSchema)
def healthcheck():
    return {"tasks": TODOS}


@server.post(
    "/todo",
    response_model=GetTaskSchema,
    status_code=status.HTTP_201_CREATED,
)
def create_task(payload: CreateTaskSchema):
    task = payload.dict()
    task["id"] = uuid.uuid4()
    task["created"] = datetime.now()
    task["status"] = task["status"].value
    task["priority"] = task["priority"].value
    TODOS.append(task)
    return task


@server.get("/todo/{task_id}", response_model=GetTaskSchema)
def get_task(task_id: uuid.UUID):
    for task in TODOS:
        if task["id"] == task_id:
            return task
    raise HTTPException(
        status_code=404,
        detail=f"Task with ID {task_id} not found",
    )


@server.put("/todo/{task_id}", response_model=GetTaskSchema)
def update_task(task_id: uuid.UUID, payload: CreateTaskSchema):
    for task in TODOS:
        if task["id"] == task_id:
            task.update(payload.dict())
            task["status"] = task["status"].value
            task["priority"] = task["priority"].value
            return task
    raise HTTPException(
        status_code=404,
        detail=f"Task with ID {task_id} not found",
    )


@server.delete(
    "/todo/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    response_class=Response,
)
def delete_task(task_id: uuid.UUID):
    for index, task in enumerate(TODOS):
        if task["id"] == task_id:
            TODOS.pop(index)
            return
    raise HTTPException(status_code=404, detail=f"Task with ID {task_id} not found")
