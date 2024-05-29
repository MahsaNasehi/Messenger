from fastapi import FastAPI

from models import User
app = FastAPI()


@app.get("/insert-user")
def insert_user():
    return {"message": "Hello World"}


@app.post("/user_create/")
def user_create(user: User):
    # save the user in db

    # return the user
    return user
