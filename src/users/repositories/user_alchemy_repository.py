from sqlalchemy.orm import Session

from src.database.alchemy import engine
from src.users.models.user import User
from src.users.repositories.user_abstract_repository import UserAbstractRepository
from src.users.schemas.user_schema import UserSchema


class UserAlchemyRepository(UserAbstractRepository):
	def get_user_by_nickname(self, username: str) -> UserSchema | None:
		with Session(engine) as session:
			user = session.query(User).filter(User.username == username).first()
			if user: return UserSchema.from_orm(user)
