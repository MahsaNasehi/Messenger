from pydantic import BaseModel


# declare all classes
class User(BaseModel):
    id: str
    first_name: str
    last_name: str
    phone_number: str


class Email:
    pass