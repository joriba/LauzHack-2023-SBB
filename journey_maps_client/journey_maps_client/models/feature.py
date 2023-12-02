from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.geo_json_object_type import GeoJsonObjectType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.feature_geometry import FeatureGeometry
    from ..models.feature_properties import FeatureProperties


T = TypeVar("T", bound="Feature")


@_attrs_define
class Feature:
    """GeoJSon 'Feature' object

    Attributes:
        type (GeoJsonObjectType):
        geometry (FeatureGeometry):
        bbox (Union[Unset, List[float]]): A GeoJSON object MAY have a member named "bbox" to include information on the
            coordinate range for its Geometries, Features, or FeatureCollections. The value of the bbox member MUST be an
            array of length 2*n where n is the number of dimensions represented in the contained geometries, with all axes
            of the most southwesterly point followed by all axes of the more northeasterly point. The axes order of a bbox
            follows the axes order of geometries.
        properties (Optional[FeatureProperties]):
        id (Union[Unset, str]):
    """

    type: GeoJsonObjectType
    geometry: "FeatureGeometry"
    properties: Optional["FeatureProperties"]
    bbox: Union[Unset, List[float]] = UNSET
    id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        geometry = self.geometry.to_dict()

        bbox: Union[Unset, List[float]] = UNSET
        if not isinstance(self.bbox, Unset):
            bbox = self.bbox

        properties = self.properties.to_dict() if self.properties else None

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "geometry": geometry,
                "properties": properties,
            }
        )
        if bbox is not UNSET:
            field_dict["bbox"] = bbox
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.feature_geometry import FeatureGeometry
        from ..models.feature_properties import FeatureProperties

        d = src_dict.copy()
        type = GeoJsonObjectType(d.pop("type"))

        geometry = FeatureGeometry.from_dict(d.pop("geometry"))

        bbox = cast(List[float], d.pop("bbox", UNSET))

        _properties = d.pop("properties")
        properties: Optional[FeatureProperties]
        if _properties is None:
            properties = None
        else:
            properties = FeatureProperties.from_dict(_properties)

        id = d.pop("id", UNSET)

        feature = cls(
            type=type,
            geometry=geometry,
            bbox=bbox,
            properties=properties,
            id=id,
        )

        feature.additional_properties = d
        return feature

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
