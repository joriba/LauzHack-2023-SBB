from enum import Enum


class GeoJsonObjectType(str, Enum):
    FEATURE = "Feature"
    FEATURECOLLECTION = "FeatureCollection"
    GEOMETRYCOLLECTION = "GeometryCollection"
    LINESTRING = "LineString"
    MULTILINESTRING = "MultiLineString"
    MULTIPOINT = "MultiPoint"
    MULTIPOLYGON = "MultiPolygon"
    POINT = "Point"
    POLYGON = "Polygon"

    def __str__(self) -> str:
        return str(self.value)
