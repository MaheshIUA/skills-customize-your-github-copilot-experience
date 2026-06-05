from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="FastAPI REST Assignment")


class ItemIn(BaseModel):
    name: str
    description: str | None = None


# In-memory store for assignment practice.
items = {
    1: {"id": 1, "name": "Notebook", "description": "A ruled notebook"},
    2: {"id": 2, "name": "Pen", "description": "Blue ink pen"},
}


@app.get("/")
def read_root():
    return {"message": "Welcome to your FastAPI assignment API!"}


@app.get("/items")
def get_items():
    return list(items.values())


@app.get("/items/{item_id}")
def get_item(item_id: int):
    item = items.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.post("/items", status_code=201)
def create_item(item: ItemIn):
    new_id = max(items.keys(), default=0) + 1
    new_item = {"id": new_id, **item.model_dump()}
    items[new_id] = new_item
    return new_item


@app.put("/items/{item_id}")
def update_item(item_id: int, item: ItemIn):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")

    updated = {"id": item_id, **item.model_dump()}
    items[item_id] = updated
    return updated
