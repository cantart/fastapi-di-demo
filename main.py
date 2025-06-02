from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


def add(x: int, y: int) -> int:
    return x + y

class AddRequest(BaseModel):
    x: int
    y: int
    
class AddResponse(BaseModel):
    result: int

@app.post("/add")
def do_add(request: AddRequest) -> AddResponse:
    """
    Adds two integers provided in the request body.
    """
    return AddResponse(result=add(request.x, request.y))