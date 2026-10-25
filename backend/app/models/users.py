from sqlmodel import Field, SQLModel

class User(SQLModel, table=True):
    id: int | None = Field(default= None, primary_key=True)
    username: str = Field(sa_column_kwargs = {"unique": True}, nullable=False)
    email: str = Field(sa_column_kwargs = {"unique": True}, nullable=False)
    hashed_password: str
    full_name: str

