from sqlalchemy.orm import Session

from src.database.alchemy import engine
from src.image_loader.models.image_meta_data import ImageMetaData, ImageMetaDataPerson
from src.image_loader.repositories.image_meta_data_abstract_repository import ImageMetaDataAbstractRepository
from src.image_loader.schemas.image_meta_data_schema import ImageMetaDataSchema


class ImageMetaDataAlchemyRepository(ImageMetaDataAbstractRepository):
	def save(self, image_meta_data: ImageMetaDataSchema) -> None:
		with Session(engine) as session:
			new_image_meta_data = ImageMetaData(**image_meta_data.dict())

			session.add(new_image_meta_data)
			session.commit()
			session.refresh(new_image_meta_data)

			if persons := image_meta_data.persons:
				session.add_all([
					ImageMetaDataPerson(
						image_meta_data_id=new_image_meta_data.image_id,
						value=person
					) for person in persons
				])
				session.commit()
