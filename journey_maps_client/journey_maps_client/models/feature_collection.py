from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.geo_json_object_type import GeoJsonObjectType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.feature import Feature


T = TypeVar("T", bound="FeatureCollection")


@_attrs_define
class FeatureCollection:
    """GeoJSon 'FeatureCollection' object

    Attributes:
        type (GeoJsonObjectType):
        features (List['Feature']):
        bbox (Union[Unset, List[float]]): A GeoJSON object MAY have a member named "bbox" to include information on the
            coordinate range for its Geometries, Features, or FeatureCollections. The value of the bbox member MUST be an
            array of length 2*n where n is the number of dimensions represented in the contained geometries, with all axes
            of the most southwesterly point followed by all axes of the more northeasterly point. The axes order of a bbox
            follows the axes order of geometries.
    """

    type: GeoJsonObjectType
    features: List["Feature"]
    bbox: Union[Unset, List[float]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        features = []
        for features_item_data in self.features:
            features_item = features_item_data.to_dict()

            features.append(features_item)

        bbox: Union[Unset, List[float]] = UNSET
        if not isinstance(self.bbox, Unset):
            bbox = self.bbox

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "features": features,
            }
        )
        if bbox is not UNSET:
            field_dict["bbox"] = bbox

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.feature import Feature

        d = src_dict.copy()
        type = GeoJsonObjectType(d.pop("type"))

        features = []
        _features = d.pop("features")
        for features_item_data in _features:
            features_item = Feature.from_dict(features_item_data)

            features.append(features_item)

        bbox = cast(List[float], d.pop("bbox", UNSET))

        feature_collection = cls(
            type=type,
            features=features,
            bbox=bbox,
        )

        feature_collection.additional_properties = d
        return feature_collection

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
