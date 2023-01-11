from pydantic import BaseModel

from src.image_loader.schemas.image_schema import ImageSchema
from src.image_loader.schemas.image_meta_data_schema import ImageMetaDataSchema


class ImageWithMetaDataSchema(BaseModel):
	image: ImageSchema
	meta_data: ImageMetaDataSchema
