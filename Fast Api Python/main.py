from fastapi import FastAPI

app = FastAPI()

dataBase = {
    1: {
        "name": "John Doe",
        "address": "123 Main St",
        "email": "johndoe@example.com"
    },
    2: {
        "name": "Jane Doe",
        "address": "456 Side St",
        "email": "janedoe@example.com"
    },
    3: {
        "name": "John Smith",
        "address": "789 Back St",
        "email": "SmithJohn@hotexample.com"
    }
}


@app.get("/get-user/{user_id}")
def get_user(user_id: int):

    return dataBase[user_id]
