from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum
app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    count: int
    id: int
    category: str
    

items = {
    0: Item(name="Pizza", price=2.53, count=3, id=1, category="Food"),
    1: Item(name="Lollipop", price=0.25, count=100, id=2, category = "Candy"),
    2: Item(name="Pepsi", price=1.99, count=2, id=1, category="drink")
}


@app.get("/get_items")
def index() -> dict[str,dict[int,Item]]:
    return {"items": items}

@app.post("/add_items")
def add_items(new_item: Item) -> dict[str, dict[int, Item]]:
    new_id = max(items.keys()) + 1  # Generate new ID
    items[new_id] = new_item
    return {"message": "Item added successfully", "items": items}
