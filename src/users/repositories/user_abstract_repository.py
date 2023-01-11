from abc import abstractmethod

from src.common.abstract_repositories import AbstractSQLRepository
from src.users.schemas.user_schema import UserSchema


class UserAbstractRepository(AbstractSQLRepository):
	@abstractmethod
	def get_user_by_nickname(self, nickname: str) -> UserSchema:
		pass
