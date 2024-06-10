from fastapi import FastAPI
import database_connection as mydb
import insertion

from models import User, PV, Group, GroupMember, Message, Contact

app = FastAPI()


# insertion and creation
@app.post("/user_create/")
def user_create(user: User):
    # save the user in db
    result = insertion.user_insertion(user)
    return result


@app.post("/pv_create/")
def pv_create(pv: PV):
    # save the user in db
    result = insertion.pv_chat_insertion(pv)
    return result


@app.post("/group_create/")
def group_create(group: Group):
    # save the user in db
    result = insertion.group_chat_insertion(group)
    return result


@app.post("/group_member_addition/")
def group_member_create(member: GroupMember):
    # save the user in db
    result = insertion.group_member_insertion(member)
    return result


@app.post("/msg_create/")
def msg_create(msg: Message):
    # save the user in db
    result = insertion.message_insertion(msg)
    return result


@app.post("/contact_create/")
def contact_create(cnct: Contact):
    # save the user in db
    result = insertion.contacts_insertion(cnct)
    return result


# read and select
@app.get("/read_user_by_id/")
def select_user_by_id(id: int):
    result = mydb.select_usertable_by_userid(id)
    return result


@app.get("/read_contact_by_id/")
def select_contact_by_id(id: int):
    result = mydb.select_contactstable_by_userid(id)
    return result


@app.get("/read_group_by_id/")
def select_group_by_id(id: int):
    result = mydb.select_grouptable_by_id(id)
    return result


@app.get("/read_group_member_by_id/")
def select_group_member_by_id(id: int):
    result = mydb.select_group_membertable_by_userid(id)
    return result


@app.get("/read_msg_by_id/")
def select_msg_by_id(id: int):
    result = mydb.select_msgtable_by_userid(id)
    return result


@app.get("/read_pv_by_id/")
def select_pv_by_id(id: int):
    result = mydb.select_pvtable_by_userid(id)
    return result


# update methods
@app.patch("/update_user/")
def update_user(user_id, field_to_update, new_value):
    result = mydb.update_user(user_id, field_to_update, new_value)
    return result


@app.patch("/update_group/")
def update_group(group_id, field_to_update, new_value):
    result = mydb.update_group(group_id, field_to_update, new_value)
    return result


# update msg means editing its content
@app.patch("/update_msg_content/")
def update_message(msg_id, field_to_update, new_value):
    result = mydb.update_massage(msg_id, field_to_update, new_value)
    return result


# delete methods
@app.delete("/delete_user_by_id/")
def delete_user_by_id(id: int):
    result = mydb.delete_user_by_userid(id)
    return result


@app.delete("/delete_contact_by_ids/")
def delete_contact_by_id(user_id: int, contact_id: int):
    result = mydb.delete_contact(user_id, contact_id)
    return result


@app.delete("/delete_group_by_id/")
def delete_group_by_id(chat_id: int):
    result = mydb.delete_group(chat_id)
    return result


@app.delete("/delete_group_member_by_ids/")
def delete_group_member_by_id(chat_id: int, member_id: int):
    result = mydb.delete_group_member(chat_id, member_id)
    return result


@app.delete("/delete_msg_by_id/")
def delete_msg_by_id(msg_id: int):
    result = mydb.delete_msg(msg_id)
    return result


@app.delete("/delete_pv_by_id/")
def delete_pv_by_id(chat_id: int):
    result = mydb.delete_pv(chat_id)
    return result
