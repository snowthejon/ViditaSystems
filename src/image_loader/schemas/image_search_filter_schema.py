from pydantic import BaseModel, PrivateAttr

from src.image_loader.filters.image_filter import ImageFilter
from src.image_loader.filters.image_meta_data_filter import ImageMetaDataFilter
from src.image_loader.filters.image_meta_data_person_filter import ImageMetaDataPersonFilter


class ImageSearchFilterSchema(BaseModel):
	image: ImageFilter | None
	image_meta_data: ImageMetaDataFilter | None
	image_meta_data_person: ImageMetaDataPersonFilter | None
