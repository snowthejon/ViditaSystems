from sqlalchemy import Column, Integer, DateTime, func, ForeignKey, String

from src.database.alchemy import Base
from src.users.models.user import User


class Image(Base):
	__tablename__ = "images"

	id = Column(Integer, primary_key=True, index=True)
	user_id = Column(Integer, ForeignKey(column=User.id), nullable=False)
	cdn_url = Column(String, nullable=False)

	created_at = Column(DateTime, nullable=False, default=func.now(), server_default=func.now())
