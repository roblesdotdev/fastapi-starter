## Getting started with fastapi

### Setup Python Environment

```
pipenv --python 3.10
pipenv shell
pipenv install pytest pylint black --dev
```

### Create makefile with useful commands.

- install
- format
- lint
- test

### Create Open Api Specification

[The Swagger Editor](https://editor.swagger.io) provides a user-friendly interface
that allows you to efficiently add and edit the components of your OAS. You can
specify detailed information such as descriptions, examples, and validation
constraints for each element of your API.

### Generate schema from oas

```
mkdir todo
pipenv install datamodel-code-generator --dev
datamodel-codegen --input oas.yaml output todo/schema.py
```

### Setup fastapi

```
pipenv install fastapi uvicorn
```

```
# todo/server.py
from fastapi import FastApi

server = FastApi(debug=True)

from todo import api
```

```
# todo/api.py

from todo.server import server

@server.get("/hello")
def hello():
  return {
    'message': 'Hello World'
  }
```
