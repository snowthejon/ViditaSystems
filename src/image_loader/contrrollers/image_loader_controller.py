import random
from typing import Type, List

from fastapi import UploadFile

from src.image_loader.repositories.image_abstract_repository import ImageAbstractRepository
from src.image_loader.repositories.image_meta_data_abstract_repository import ImageMetaDataAbstractRepository
from src.image_loader.schemas.image_meta_data_schema import ImageMetaDataSchema, ImageMetaDataUploadSchema
from src.image_loader.schemas.image_schema import ImageSchema
from src.image_loader.schemas.image_search_filter_schema import ImageSearchFilterSchema
from src.image_loader.schemas.image_with_meta_data_schema import ImageWithMetaDataSchema
from src.image_loader.validators import validate_image_loader_image
from src.users.schemas.user_schema import UserSchema


class ImageLoaderController:
	def __init__(
			self,
			image_repository: Type[ImageAbstractRepository],
			image_meta_data_repository: Type[ImageMetaDataAbstractRepository]):
		self._image_repository = image_repository()
		self._image_meta_data_repository = image_meta_data_repository()

	def save_image(self, image: UploadFile, user: UserSchema, image_meta_data: ImageMetaDataUploadSchema) -> None:
		"""
		Загрузка изображения.
		Указание мета-даты опционально.

		:param image:					изображение для загрузки
		:param user:					схема текущего пользователя
		:param image_meta_data:			мета-дата изображения
		:return:						None
		"""
		validate_image_loader_image(image=image)

		new_image = self._image_repository.save(
			cdn_url=f"https://www.cdn.com/{random.randint(1, 100000)}",		# предположим изображения будут храниться на CDN
			user_id=user.id
		)

		self._image_meta_data_repository.save(
			image_meta_data=ImageMetaDataSchema(
				image_id=new_image.id,
				**image_meta_data.dict(exclude_unset=True)
			)
		)

	def get_images(self, user: UserSchema, image_search_filter: ImageSearchFilterSchema) -> List[ImageSchema]:
		return self._image_repository.get_user_images(user_id=user.id, image_search_filter=image_search_filter)
