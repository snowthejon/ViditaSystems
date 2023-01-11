from abc import ABC, abstractmethod

from src.image_loader.schemas.image_schema import ImageSchema
from src.image_loader.schemas.image_search_filter_schema import ImageSearchFilterSchema


class ImageAbstractRepository(ABC):
	@abstractmethod
	def save(self, cdn_url: str,  user_id: int) -> ImageSchema:
		pass

	@abstractmethod
	def get_user_images(self, user_id: int, image_search_filter: ImageSearchFilterSchema = None) -> list[ImageSchema] | None:
		pass
