from fastapi import FastAPI, Path, Query
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    name: str
    age: int
    city: str
    state: Optional[str] = None


class UpdateUser(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    city: Optional[str] = None
    state: Optional[str] = None


database = {}


@app.get("/get-user/{user_id}")
def get_id(user_id: int = Path(None, description="The ID of the user you'd like to view", gt=0, lt=2)):
    return database[user_id]


@app.get("/get-by-name/{user_id}")
def get_user(*, user_id: int, name: Optional[str] = None, test: int):
    for user_id in database:
        if database[user_id].name == name:
            return database[user_id]
    return {"Error": "User not found"}


@app.post("/create-user/{user_id}")
def create_user(user_id: int, user: User):
    if user_id in database:
        return {"Error": "User exists"}

    database[user_id] = {"name": user.name, "age": user.age,
                         "city": user.city, "state": user.state}
    return database[user_id]


@app.put("/update-user/{user_id}")
def update_user(user_id: int, user: User):
    if user_id not in database:
        return {"Error": "User does not exist"}

    if user.name != None:
        database[user_id]["name"] = user.name

    if user.age != None:
        database[user_id]["age"] = user.age

    if user.city != None:
        database[user_id]["city"] = user.city

    return database[user_id]


@app.delete("/delete-user")
def delete_user(user_id: int = Query(..., description="The ID of the user you'd like to delete", gt=0, lt=2)):
    if user_id not in database:
        return {"Error": "User does not exist"}

    del database[user_id]
    return {"Message": "User deleted successfully"}
