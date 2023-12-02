from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CoordinatesWGS84")


@_attrs_define
class CoordinatesWGS84:
    """World Geodetic System 1984 (WGS 84) coordinates (latitude: specifies the north–south position of a point on the
    earth's surface; longitude: specifies the east-west position of a point on the earth's surface). For e.g. Bern CH
    (lat=46.947974,lon=7.447447).

        Attributes:
            longitude (Union[Unset, float]):
            latitude (Union[Unset, float]):
            latitude_decimal_degrees (Union[Unset, float]):
            longitude_decimal_degrees (Union[Unset, float]):
    """

    longitude: Union[Unset, float] = UNSET
    latitude: Union[Unset, float] = UNSET
    latitude_decimal_degrees: Union[Unset, float] = UNSET
    longitude_decimal_degrees: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        longitude = self.longitude
        latitude = self.latitude
        latitude_decimal_degrees = self.latitude_decimal_degrees
        longitude_decimal_degrees = self.longitude_decimal_degrees

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if latitude_decimal_degrees is not UNSET:
            field_dict["latitudeDecimalDegrees"] = latitude_decimal_degrees
        if longitude_decimal_degrees is not UNSET:
            field_dict["longitudeDecimalDegrees"] = longitude_decimal_degrees

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        longitude = d.pop("longitude", UNSET)

        latitude = d.pop("latitude", UNSET)

        latitude_decimal_degrees = d.pop("latitudeDecimalDegrees", UNSET)

        longitude_decimal_degrees = d.pop("longitudeDecimalDegrees", UNSET)

        coordinates_wgs84 = cls(
            longitude=longitude,
            latitude=latitude,
            latitude_decimal_degrees=latitude_decimal_degrees,
            longitude_decimal_degrees=longitude_decimal_degrees,
        )

        coordinates_wgs84.additional_properties = d
        return coordinates_wgs84

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
