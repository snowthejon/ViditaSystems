from pydantic import BaseModel, PositiveInt, PositiveFloat, root_validator
from starlette import status
from starlette.exceptions import HTTPException


class __ImageMetaDataBaseSchema(BaseModel):
	latitude: PositiveFloat | None
	longitude: PositiveFloat | None
	description: str | None

	@root_validator
	def root_validator(cls, values):
		latitude_exist = True if values.get("latitude") else False
		longitude_exist = True if values.get("longitude") else False

		if latitude_exist + longitude_exist not in [0, 2]:
			raise HTTPException(
				status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
				detail="Longitude and Latitude should be either both null or both not null"
			)

		return values


class ImageMetaDataUploadSchema(__ImageMetaDataBaseSchema):
	persons: list[str] | None


class ImageMetaDataSchema(__ImageMetaDataBaseSchema):
	image_id: PositiveInt | None

	class Config:
		orm_mode = True
