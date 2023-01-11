from abc import ABC, abstractmethod

from src.image_loader.models.image_meta_data import ImageMetaData
from src.image_loader.schemas.image_meta_data_schema import ImageMetaDataSchema


class ImageMetaDataAbstractRepository(ABC):
	@abstractmethod
	def save(self, image_meta_data: ImageMetaDataSchema) -> None:
		pass
