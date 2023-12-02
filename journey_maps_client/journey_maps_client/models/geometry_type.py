from enum import Enum


class GeometryType(str, Enum):
    GEOMETRYCOLLECTION = "GeometryCollection"
    LINESTRING = "LineString"
    MULTILINESTRING = "MultiLineString"
    MULTIPOINT = "MultiPoint"
    MULTIPOLYGON = "MultiPolygon"
    POINT = "Point"
    POLYGON = "Polygon"

    def __str__(self) -> str:
        return str(self.value)
