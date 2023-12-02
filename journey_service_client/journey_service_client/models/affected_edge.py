from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.line_string import LineString
    from ..models.point import Point


T = TypeVar("T", bound="AffectedEdge")


@_attrs_define
class AffectedEdge:
    """Geometrical polyline related to a `PTSituation::affectedScope`.

    Attributes:
        direction (str): Direction a vehicle is going to on the affected edge where `PTSituationMessage` applies,
            relates to `spatialProjection`.<br>x-extensible-enum: [UNKNOWN,STRAIGHT,OPPOSITE,BIDIRECTIONAL] Example:
            BIDIRECTIONAL.
        icon_position (Union[Unset, Point]): Point in [GeoJSON](https://datatracker.ietf.org/doc/html/rfc7946) format.
        spatial_projection (Union[Unset, LineString]): LineString in
            [GeoJSON](https://datatracker.ietf.org/doc/html/rfc7946) format.
    """

    direction: str
    icon_position: Union[Unset, "Point"] = UNSET
    spatial_projection: Union[Unset, "LineString"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        direction = self.direction
        icon_position: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.icon_position, Unset):
            icon_position = self.icon_position.to_dict()

        spatial_projection: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.spatial_projection, Unset):
            spatial_projection = self.spatial_projection.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "direction": direction,
            }
        )
        if icon_position is not UNSET:
            field_dict["iconPosition"] = icon_position
        if spatial_projection is not UNSET:
            field_dict["spatialProjection"] = spatial_projection

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.line_string import LineString
        from ..models.point import Point

        d = src_dict.copy()
        direction = d.pop("direction")

        _icon_position = d.pop("iconPosition", UNSET)
        icon_position: Union[Unset, Point]
        if isinstance(_icon_position, Unset):
            icon_position = UNSET
        else:
            icon_position = Point.from_dict(_icon_position)

        _spatial_projection = d.pop("spatialProjection", UNSET)
        spatial_projection: Union[Unset, LineString]
        if isinstance(_spatial_projection, Unset):
            spatial_projection = UNSET
        else:
            spatial_projection = LineString.from_dict(_spatial_projection)

        affected_edge = cls(
            direction=direction,
            icon_position=icon_position,
            spatial_projection=spatial_projection,
        )

        affected_edge.additional_properties = d
        return affected_edge

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
