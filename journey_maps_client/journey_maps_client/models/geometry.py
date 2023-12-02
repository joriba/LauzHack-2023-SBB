from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.geometry_type import GeometryType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Geometry")


@_attrs_define
class Geometry:
    """Abstract type for all GeoJSon object except Feature and FeatureCollection

    Attributes:
        type (GeometryType):
        bbox (Union[Unset, List[float]]): A GeoJSON object MAY have a member named "bbox" to include information on the
            coordinate range for its Geometries, Features, or FeatureCollections. The value of the bbox member MUST be an
            array of length 2*n where n is the number of dimensions represented in the contained geometries, with all axes
            of the most southwesterly point followed by all axes of the more northeasterly point. The axes order of a bbox
            follows the axes order of geometries.
    """

    type: GeometryType
    bbox: Union[Unset, List[float]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        bbox: Union[Unset, List[float]] = UNSET
        if not isinstance(self.bbox, Unset):
            bbox = self.bbox

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if bbox is not UNSET:
            field_dict["bbox"] = bbox

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = GeometryType(d.pop("type"))

        bbox = cast(List[float], d.pop("bbox", UNSET))

        geometry = cls(
            type=type,
            bbox=bbox,
        )

        geometry.additional_properties = d
        return geometry

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
