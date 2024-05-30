from fastapi import FastAPI
import database_connection as mydb

from models import User, PV, Group, GroupMember, Message
app = FastAPI()


# @app.get("/insert-user")
# def insert_user():
#     return {"message": "Hello World"}


@app.post("/user_create/")
def user_create(user: User):
    # save the user in db
    mydb.user_insertion(user)
    # what should be returned

    # return the user
    # return user


@app.post("/pv_create/")
def user_create(pv: PV):
    # save the user in db
    mydb.pv_chat_insertion(pv)
    # what should be returned

    # return the user
    # return user


@app.post("/group_create/")
def user_create(group: Group):
    # save the user in db
    mydb.group_chat_insertion(group)
    # what should be returned

    # return the user
    # return user
