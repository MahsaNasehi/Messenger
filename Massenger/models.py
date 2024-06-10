from pydantic import BaseModel


# declare all classes
class User(BaseModel):
    user_name: str
    first_name: str
    last_name: str
    phone_number: str
    join_date: str


class Group(BaseModel):
    chat_name: str


class PV(BaseModel):
    first_user_id: int
    second_user_id: int


class GroupMember(BaseModel):
    group_chat_id: int
    member_id: int


class Contact(BaseModel):
    users_id: int
    users_contact_id: int

class Message(BaseModel):
    chat_id: int
    is_group_chat: bool
    sender_id: int
    content: str
