from src.common.entity_filter import EntityFilter
from src.common.entity_filter_property_types import FilterPropertyBetween
from src.image_loader.models.image_meta_data import ImageMetaData


class _FilterImageMetaDataLongitude(FilterPropertyBetween):
	_column = ImageMetaData.longitude.key

	value_from: float | None
	value_to: float | None


class _FilterImageMetaDataLatitude(FilterPropertyBetween):
	_column = ImageMetaData.latitude.key

	value_from: float | None
	value_to: float | None


class ImageMetaDataFilter(EntityFilter):
	_bounded_model = ImageMetaData

	longitude: _FilterImageMetaDataLongitude | None
	latitude: _FilterImageMetaDataLatitude | None
