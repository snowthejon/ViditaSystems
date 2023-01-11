from pydantic import BaseModel, PrivateAttr


class EntityFilter(BaseModel):
	_bounded_model: PrivateAttr()

	def get_bounded_model(self):
		return self._bounded_model
