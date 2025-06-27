from datetime import date
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union


app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


class User(BaseModel):
    id: int
    name: str
    joined: date


@app.get("/")
def read_root():
    return {"hello": "World!"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_price": item.price, "item_id": item_id}


def get_full_name(first_name: str, last_name: str) -> str:
    return f"{first_name.title()} {last_name.title()}"

def get_name_with_age(name: str, age: int):
    return name + " is this old: " + str(age)

def test_list_of_str_params(items: list[str]):
    for item in items:
        print(f"Processing item: {item.title()}")

    return {"items": items.insert(0, "first_item") or items}

def test_tuple_and_set_params(items: tuple[str, ...], tags: set[str]):
    return {
        "items": items,
        "tags": tags
    }

@app.get("/test/")
def testing():
    my_user: User = User(id=3, name="John Doe", joined="2018-07-19")

    second_user_data = {
        "id": 4,
        "name": "Mary",
        "joined": "2018-11-30"
    }

    my_second_user: User = User(**second_user_data)

    return {
        "my_user": my_user,
        "my_second_user": my_second_user
    }