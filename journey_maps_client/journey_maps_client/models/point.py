from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.point_type import PointType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Point")


@_attrs_define
class Point:
    """GeoJSon geometry

    Attributes:
        type (PointType):
        coordinates (List[float]): GeoJSon fundamental geometry construct.
            A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and
            latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY
            be included as an optional third element.
            Implementations SHOULD NOT extend positions beyond three elements because the semantics of extra elements are
            unspecified and ambiguous. Historically, some implementations have used a fourth element to carry a linear
            referencing measure (sometimes denoted as "M") or a numerical timestamp, but in most situations a parser will
            not be able to properly interpret these values. The interpretation and meaning of additional elements is beyond
            the scope of this specification, and additional elements MAY be ignored by parsers.
        bbox (Union[Unset, List[float]]): A GeoJSON object MAY have a member named "bbox" to include information on the
            coordinate range for its Geometries, Features, or FeatureCollections. The value of the bbox member MUST be an
            array of length 2*n where n is the number of dimensions represented in the contained geometries, with all axes
            of the most southwesterly point followed by all axes of the more northeasterly point. The axes order of a bbox
            follows the axes order of geometries.
    """

    type: PointType
    coordinates: List[float]
    bbox: Union[Unset, List[float]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        coordinates = self.coordinates

        bbox: Union[Unset, List[float]] = UNSET
        if not isinstance(self.bbox, Unset):
            bbox = self.bbox

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "coordinates": coordinates,
            }
        )
        if bbox is not UNSET:
            field_dict["bbox"] = bbox

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = PointType(d.pop("type"))

        coordinates = cast(List[float], d.pop("coordinates"))

        bbox = cast(List[float], d.pop("bbox", UNSET))

        point = cls(
            type=type,
            coordinates=coordinates,
            bbox=bbox,
        )

        point.additional_properties = d
        return point

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
