from sqlalchemy import Column, Integer, ForeignKey, String, Float
from sqlalchemy.dialects.postgresql import ARRAY

from src.database.alchemy import Base


class ImageMetaData(Base):
	__tablename__ = "images_meta_data"

	image_id = Column(Integer, ForeignKey(column="images.id"), primary_key=True, index=True)

	latitude = Column(Float, nullable=True)
	longitude = Column(Float, nullable=True)
	description = Column(String, nullable=True)


class ImageMetaDataPerson(Base):
	__tablename__ = "images_meta_data_persons"

	image_meta_data_id = Column(Integer, ForeignKey(column=ImageMetaData.image_id), primary_key=True, index=True)
	name = Column(String, nullable=False)
