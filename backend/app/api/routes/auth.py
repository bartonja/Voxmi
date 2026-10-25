from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session, select

from app.database import get_session
from app.models import User
from app.core.security import verify_password, create_access_token


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)

SessionDependency = Annotated[Session, Depends(get_session)]

@router.post('/login')
def login(
        session: SessionDependency,
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    '''Validate user credentials and returns access token'''


    statement = select(User).where(
        User.username == form_data.username
    )

    user = session.exec(statement).first()

    if user is None or not verify_password(
            form_data.password,
            user.hashed_password
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(user_id=user.id)

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }



