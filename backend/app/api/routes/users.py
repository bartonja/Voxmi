from typing import Annotated
from fastapi import APIRouter, Depends, status, HTTPException
from sqlmodel import Session, select
from app.database import get_session
from app.models.users import User
from app.schemas.users import UserCreateSchema, UserReadSchema
from app.core.security import hash_password

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

SessionDependency = Annotated[
    Session,
    Depends(get_session)
]

@router.post('/',response_model=UserReadSchema, status_code=status.HTTP_201_CREATED)
def create_user(
        session: SessionDependency,
        user_data: UserCreateSchema,
)->User:
    '''Creation of a new user based on create user schema'''

    email_statement = select(User).where(User.email == user_data.email)
    email_check = session.exec(email_statement).first()

    username_statement = select(User).where(User.username == user_data.username)
    username_check = session.exec(username_statement).first()

    if email_check is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Credentials conflict"
        )

    if username_check is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Credentials conflict"
        )

    user = User(
        username=user_data.username,
        email=user_data.email,
        hashed_password=hash_password(user_data.password),
        full_name= user_data.full_name
    )

    session.add(user)
    session.commit()
    session.refresh(user)

    return user

@router.get('/{user_id}', response_model=UserReadSchema, status_code=status.HTTP_200_OK)
def get_user(
        session: SessionDependency,
        user_id: int,
)->User:

    statement = select(User).where(User.id == user_id)
    user = session.exec(statement).first()

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user


