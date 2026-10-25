from sqlmodel import SQLModel, Field
from pydantic import EmailStr


class UserCreateSchema(SQLModel):
    '''Data the user will input at the create api endpoint'''
    username: str = Field(nullable=False)
    email: EmailStr = Field(max_length=100, nullable=False)
    password: str = Field(
        min_length = 10,
        max_length = 128,
        nullable=False
    )
    full_name: str = Field(min_length =1, max_length = 64, nullable=False)

class UserReadSchema(SQLModel):
    id: int
    username: str
    email: EmailStr
    full_name: str

