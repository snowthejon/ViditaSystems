from src.common.entity_filter import EntityFilter
from src.common.entity_filter_property_types import FilterPropertyILike
from src.image_loader.models.image_meta_data import ImageMetaDataPerson


class _FilterImageMetaDataPersonName(FilterPropertyILike):
	_column = "name"


class ImageMetaDataPersonFilter(EntityFilter):
	_bounded_model = ImageMetaDataPerson

	person: _FilterImageMetaDataPersonName | None
