from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LineString")


@_attrs_define
class LineString:
    """LineString in [GeoJSON](https://datatracker.ietf.org/doc/html/rfc7946) format.

    Attributes:
        type (str): Type as per GeoJSON, always constant _LineString_. Default: 'LineString'.
        coordinates (Union[Unset, List[List[float]]]): List of coordinates as [longitude, latitude] resp.
            easting/northing. Example: [[7.4385, 46.9488], [7.9363, 46.915], [7.936, 46.802]].
    """

    type: str = "LineString"
    coordinates: Union[Unset, List[List[float]]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        coordinates: Union[Unset, List[List[float]]] = UNSET
        if not isinstance(self.coordinates, Unset):
            coordinates = []
            for coordinates_item_data in self.coordinates:
                coordinates_item = coordinates_item_data

                coordinates.append(coordinates_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if coordinates is not UNSET:
            field_dict["coordinates"] = coordinates

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        coordinates = []
        _coordinates = d.pop("coordinates", UNSET)
        for coordinates_item_data in _coordinates or []:
            coordinates_item = cast(List[float], coordinates_item_data)

            coordinates.append(coordinates_item)

        line_string = cls(
            type=type,
            coordinates=coordinates,
        )

        line_string.additional_properties = d
        return line_string

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
