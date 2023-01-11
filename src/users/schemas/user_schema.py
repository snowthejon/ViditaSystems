import datetime

from pydantic import BaseModel, PositiveInt


class UserSchema(BaseModel):
	id: PositiveInt
	name: str
	username: str
	created_at: datetime.datetime

	class Config:
		orm_mode = True
