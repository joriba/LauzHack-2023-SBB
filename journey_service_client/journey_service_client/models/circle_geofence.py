from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.coordinates_wgs84 import CoordinatesWGS84


T = TypeVar("T", bound="CircleGeofence")


@_attrs_define
class CircleGeofence:
    """Geofence expressed by a circle.

    Attributes:
        center (CoordinatesWGS84): World Geodetic System 1984 (WGS 84) coordinates (latitude: specifies the north–south
            position of a point on the earth's surface; longitude: specifies the east-west position of a point on the
            earth's surface). For e.g. Bern CH (lat=46.947974,lon=7.447447).
        radius_min (Union[Unset, int]): @Deprecated If minRadius [m] is unset or zero, it is described as circle.
        radius_max (Union[Unset, int]): Maximum radius [m].
    """

    center: "CoordinatesWGS84"
    radius_min: Union[Unset, int] = UNSET
    radius_max: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        center = self.center.to_dict()

        radius_min = self.radius_min
        radius_max = self.radius_max

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "center": center,
            }
        )
        if radius_min is not UNSET:
            field_dict["radiusMin"] = radius_min
        if radius_max is not UNSET:
            field_dict["radiusMax"] = radius_max

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.coordinates_wgs84 import CoordinatesWGS84

        d = src_dict.copy()
        center = CoordinatesWGS84.from_dict(d.pop("center"))

        radius_min = d.pop("radiusMin", UNSET)

        radius_max = d.pop("radiusMax", UNSET)

        circle_geofence = cls(
            center=center,
            radius_min=radius_min,
            radius_max=radius_max,
        )

        circle_geofence.additional_properties = d
        return circle_geofence

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
