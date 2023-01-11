from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship

from src.database.alchemy import Base


class User(Base):
	__tablename__ = "users"

	id = Column(Integer, primary_key=True, index=True)
	name = Column(String, nullable=False)
	username = Column(String, nullable=False)
	hashed_password = Column(String, nullable=False)

	created_at = Column(DateTime, nullable=False, default=func.now(), server_default=func.now())
