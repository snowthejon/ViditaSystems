import datetime

from pydantic import BaseModel, PositiveInt


class ImageUploadSchema(BaseModel):
	user_id: PositiveInt
	data: bytes


class ImageSchema(BaseModel):
	id: PositiveInt
	user_id: PositiveInt

	cdn_url: str
	created_at: datetime.datetime

	class Config:
		orm_mode = True
