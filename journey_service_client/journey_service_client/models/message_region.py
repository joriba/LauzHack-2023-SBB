from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.circle_geofence import CircleGeofence
    from ..models.coordinates_wgs84 import CoordinatesWGS84


T = TypeVar("T", bound="MessageRegion")


@_attrs_define
class MessageRegion:
    """Region-Information.

    Attributes:
        polyline_formatted (List[str]):
        name (Union[Unset, str]): Name of region. Example: BVI2.
        id (Union[Unset, str]): Id of region. Example: BVI 2.
        icon_coordinates (Union[Unset, CoordinatesWGS84]): World Geodetic System 1984 (WGS 84) coordinates (latitude:
            specifies the north–south position of a point on the earth's surface; longitude: specifies the east-west
            position of a point on the earth's surface). For e.g. Bern CH (lat=46.947974,lon=7.447447).
        geofence (Union[Unset, CircleGeofence]): Geofence expressed by a circle.
    """

    polyline_formatted: List[str]
    name: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    icon_coordinates: Union[Unset, "CoordinatesWGS84"] = UNSET
    geofence: Union[Unset, "CircleGeofence"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        polyline_formatted = self.polyline_formatted

        name = self.name
        id = self.id
        icon_coordinates: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.icon_coordinates, Unset):
            icon_coordinates = self.icon_coordinates.to_dict()

        geofence: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.geofence, Unset):
            geofence = self.geofence.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "polylineFormatted": polyline_formatted,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if id is not UNSET:
            field_dict["id"] = id
        if icon_coordinates is not UNSET:
            field_dict["iconCoordinates"] = icon_coordinates
        if geofence is not UNSET:
            field_dict["geofence"] = geofence

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.circle_geofence import CircleGeofence
        from ..models.coordinates_wgs84 import CoordinatesWGS84

        d = src_dict.copy()
        polyline_formatted = cast(List[str], d.pop("polylineFormatted"))

        name = d.pop("name", UNSET)

        id = d.pop("id", UNSET)

        _icon_coordinates = d.pop("iconCoordinates", UNSET)
        icon_coordinates: Union[Unset, CoordinatesWGS84]
        if isinstance(_icon_coordinates, Unset):
            icon_coordinates = UNSET
        else:
            icon_coordinates = CoordinatesWGS84.from_dict(_icon_coordinates)

        _geofence = d.pop("geofence", UNSET)
        geofence: Union[Unset, CircleGeofence]
        if isinstance(_geofence, Unset):
            geofence = UNSET
        else:
            geofence = CircleGeofence.from_dict(_geofence)

        message_region = cls(
            polyline_formatted=polyline_formatted,
            name=name,
            id=id,
            icon_coordinates=icon_coordinates,
            geofence=geofence,
        )

        message_region.additional_properties = d
        return message_region

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
