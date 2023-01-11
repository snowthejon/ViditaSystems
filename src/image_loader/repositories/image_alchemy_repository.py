from sqlalchemy.orm import Session

from src.common.filter_aggregator import aggregate_query_filter
from src.database.alchemy import engine
from src.image_loader.models.image import Image
from src.image_loader.models.image_meta_data import ImageMetaData, ImageMetaDataPerson
from src.image_loader.repositories.image_abstract_repository import ImageAbstractRepository
from src.image_loader.schemas.image_schema import ImageSchema
from src.image_loader.schemas.image_search_filter_schema import ImageSearchFilterSchema


class ImageAlchemyRepository(ImageAbstractRepository):
	def get_user_images(self, user_id: int, image_search_filter: ImageSearchFilterSchema = None) -> list[ImageSchema] | None:
		with Session(engine) as session:
			query = session.query(Image).\
				join(ImageMetaData, ImageMetaData.image_id == Image.id).\
				join(ImageMetaDataPerson, ImageMetaDataPerson.image_meta_data_id == ImageMetaData.image_id, isouter=True).\
				filter(Image.user_id == user_id)

			if image_search_filter:
				query = aggregate_query_filter(query=query, filter=image_search_filter)

			images = query.all()

		return [ImageSchema.from_orm(image) for image in images]

	def save(self, cdn_url: str, user_id: int) -> ImageSchema:
		with Session(engine) as session:
			new_image = Image(user_id=user_id, cdn_url=cdn_url)

			session.add(new_image)
			session.commit()
			session.flush(new_image)

			return ImageSchema.from_orm(new_image)
