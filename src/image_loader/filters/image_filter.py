import datetime

from src.common.entity_filter import EntityFilter
from src.common.entity_filter_property_types import FilterPropertyBetween
from src.image_loader.models.image import Image


class _FilterImageCreatedAt(FilterPropertyBetween):
	_column = Image.created_at.key

	value_from: datetime.datetime | None
	value_to: datetime.datetime | None


class ImageFilter(EntityFilter):
	_bounded_model = Image

	created_at: _FilterImageCreatedAt | None
