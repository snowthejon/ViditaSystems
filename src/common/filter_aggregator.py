from src.common.entity_filter_property_types import FilterPropertyBetween, FilterPropertyILike


def aggregate_query_filter(query, filter):
	# TODO add validate

	filter_dict = filter.dict(exclude_unset=True)

	for key in filter_dict.keys():
		filter_entity_field = getattr(filter, key)

		for filter_field in filter_entity_field.__fields__:
			field = getattr(filter_entity_field, filter_field)

			if field is None:
				continue

			field_class_parents = field.__class__.__bases__
			field_filter_attribute = getattr(filter_entity_field.get_bounded_model(), field.get_column())

			if FilterPropertyBetween in field_class_parents:
				if field.value_from and field.value_to:
					query = query.filter(field_filter_attribute.between(field.value_from, field.value_to))
				elif field.value_from:
					query = query.filter(field_filter_attribute >= field.value_from)
				elif field.value_to:
					query = query.filter(field_filter_attribute <= field.value_to)

			if FilterPropertyILike in field_class_parents:
				query = query.filter(field_filter_attribute.ilike(f"%{field.value}%"))

	return query
