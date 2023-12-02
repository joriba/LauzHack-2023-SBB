from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.message_edge_direction import MessageEdgeDirection
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.coordinates_wgs84 import CoordinatesWGS84


T = TypeVar("T", bound="MessageEdge")


@_attrs_define
class MessageEdge:
    """Edge related to HIM-Message.

    Attributes:
        polyline_formatted (List[str]):
        direction (MessageEdgeDirection): Direction a vehicle is going to on the affected edge where HIM message
            applies, relates to `polylineFormatted`.
        icon_coordinates (Union[Unset, CoordinatesWGS84]): World Geodetic System 1984 (WGS 84) coordinates (latitude:
            specifies the north–south position of a point on the earth's surface; longitude: specifies the east-west
            position of a point on the earth's surface). For e.g. Bern CH (lat=46.947974,lon=7.447447).
    """

    polyline_formatted: List[str]
    direction: MessageEdgeDirection
    icon_coordinates: Union[Unset, "CoordinatesWGS84"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        polyline_formatted = self.polyline_formatted

        direction = self.direction.value

        icon_coordinates: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.icon_coordinates, Unset):
            icon_coordinates = self.icon_coordinates.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "polylineFormatted": polyline_formatted,
                "direction": direction,
            }
        )
        if icon_coordinates is not UNSET:
            field_dict["iconCoordinates"] = icon_coordinates

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.coordinates_wgs84 import CoordinatesWGS84

        d = src_dict.copy()
        polyline_formatted = cast(List[str], d.pop("polylineFormatted"))

        direction = MessageEdgeDirection(d.pop("direction"))

        _icon_coordinates = d.pop("iconCoordinates", UNSET)
        icon_coordinates: Union[Unset, CoordinatesWGS84]
        if isinstance(_icon_coordinates, Unset):
            icon_coordinates = UNSET
        else:
            icon_coordinates = CoordinatesWGS84.from_dict(_icon_coordinates)

        message_edge = cls(
            polyline_formatted=polyline_formatted,
            direction=direction,
            icon_coordinates=icon_coordinates,
        )

        message_edge.additional_properties = d
        return message_edge

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
