from fastapi import FastAPI, Path
app = FastAPI()
database = {
    1: {
        "name": "John",
        "age": 31,
        "city": "New York"
    },
    2: {
        "name": "John",
        "age": 31,
        "city": "New York"
    },
    3: {
        "name": "John",
        "age": 31,
        "city": "New York"
    },
}


@app.get("/get-users/{user_id}")
def get_id(user_id: int = Path(None, description="The ID of the user you'd like to view", gt=0, lt=2)):
    return database[user_id]


@app.get("/get-by-name")
def get_user(name: str):
    for user_id in database:
        if database[user_id]["name"] == name:
            return database[user_id]
    return {"Error": "User not found"}
