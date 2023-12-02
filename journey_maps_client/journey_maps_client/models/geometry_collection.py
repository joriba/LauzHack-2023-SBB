from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.geometry_type import GeometryType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.geometry_element import GeometryElement


T = TypeVar("T", bound="GeometryCollection")


@_attrs_define
class GeometryCollection:
    """GeoJSon geometry collection
    GeometryCollections composed of a single part or a number of parts of a single type SHOULD be avoided when that
    single part or a single object of multipart type (MultiPoint, MultiLineString, or MultiPolygon) could be used
    instead.

        Attributes:
            type (GeometryType):
            geometries (List['GeometryElement']):
            bbox (Union[Unset, List[float]]): A GeoJSON object MAY have a member named "bbox" to include information on the
                coordinate range for its Geometries, Features, or FeatureCollections. The value of the bbox member MUST be an
                array of length 2*n where n is the number of dimensions represented in the contained geometries, with all axes
                of the most southwesterly point followed by all axes of the more northeasterly point. The axes order of a bbox
                follows the axes order of geometries.
    """

    type: GeometryType
    geometries: List["GeometryElement"]
    bbox: Union[Unset, List[float]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        geometries = []
        for geometries_item_data in self.geometries:
            geometries_item = geometries_item_data.to_dict()

            geometries.append(geometries_item)

        bbox: Union[Unset, List[float]] = UNSET
        if not isinstance(self.bbox, Unset):
            bbox = self.bbox

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "geometries": geometries,
            }
        )
        if bbox is not UNSET:
            field_dict["bbox"] = bbox

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.geometry_element import GeometryElement

        d = src_dict.copy()
        type = GeometryType(d.pop("type"))

        geometries = []
        _geometries = d.pop("geometries")
        for geometries_item_data in _geometries:
            geometries_item = GeometryElement.from_dict(geometries_item_data)

            geometries.append(geometries_item)

        bbox = cast(List[float], d.pop("bbox", UNSET))

        geometry_collection = cls(
            type=type,
            geometries=geometries,
            bbox=bbox,
        )

        geometry_collection.additional_properties = d
        return geometry_collection

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
