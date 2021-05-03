from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

def serialize(obj: object, pretty_print: bool = False) -> str:
	ns_map = __get_ns_map(obj)
	schema_location = __get_ns_schema_location(obj)
	config = SerializerConfig(
		xml_version='1.0',
		encoding='UTF-8',
		schema_location=schema_location,
		pretty_print=pretty_print
	)
	serializer = XmlSerializer(config=config)

	return serializer.render(obj, ns_map=ns_map)

def __get_ns_map(obj: object) -> dict:
	meta_classes = __get_meta_classes(obj)
	ns_map = {}

	for meta in meta_classes:
		ns_map[getattr(meta, 'namespace_prefix', None)] = getattr(meta, 'namespace', None)

	ns_map['xsd'] = 'http://www.w3.org/2001/XMLSchema'
	ns_map['xsi'] = 'http://www.w3.org/2001/XMLSchema-instance'

	return ns_map

def __get_meta_classes(obj: object) -> list:
	meta_classes = []
	if hasattr(obj, 'Meta'):
		meta_classes.append(obj.Meta)

	return meta_classes

def __get_ns_schema_location(obj: object) -> str:
	meta_classes = __get_meta_classes(obj)
	schema_locations = [
		getattr(meta, 'namespace', '') + ' ' + getattr(meta, 'schema_location', '')
		for meta in meta_classes if hasattr(meta, 'schema_location')
	]

	return ' '.join(schema_locations)