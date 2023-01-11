import datetime

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from starlette import status
from starlette.exceptions import HTTPException

from src.users.schemas.user_schema import UserSchema


def get_user(token: str = Depends(OAuth2PasswordBearer(tokenUrl="token"))) -> UserSchema:
	if token != "kapibara":
		raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

	# Здесь как то вытаскивается пользователь из БД

	return UserSchema(id=1, name="Bogdan", username="Bogdan", created_at=datetime.datetime.now())
