from typing import Any

from pydantic import PrivateAttr, BaseModel


class FilterProperty(BaseModel):
	_column: PrivateAttr()

	def get_column(self) -> str:
		return self._column


class FilterPropertyBetween(FilterProperty):
	value_from: Any | None
	value_to: Any | None


class FilterPropertyILike(FilterProperty):
	value: str
