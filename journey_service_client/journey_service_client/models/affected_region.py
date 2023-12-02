from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.geofence_circle import GeofenceCircle
    from ..models.line_string import LineString
    from ..models.point import Point


T = TypeVar("T", bound="AffectedRegion")


@_attrs_define
class AffectedRegion:
    """Region-Information related to a `PTSituation::affectedScope`.

    Attributes:
        id (Union[Unset, str]): Id of region (by underlying system HIM).
        name (Union[Unset, str]): Name of region in underlying system (HIM) terminology, see related `nameFormatted` for
            a more speaking value, like:<br>- BVI1: CH_WEST
            - BVI2: CH_MID
            - BVI3: CH_TICINO
            - BVI4: CH_ZURICH
            - BVI5: CH_EAST
            - CSTRI1: GERMANY
            - CSTRI2: AUSTRIA
            - CSTRI3: ITALY
            - CSTRI4: FRANCE
             Example: BVI2.
        name_formatted (Union[Unset, str]): Speaking equivalent value if known for related `name` of the region,
            like:<br>- CH_WEST: BVI1
            - CH_MID: BVI2
            - CH_TICINO: BVI3
            - CH_ZURICH: BVI4
            - CH_EAST: BVI5
            - GERMANY: CSTRI1
            - AUSTRIA: CSTRI2
            - ITALY: CSTRI3
            - FRANCE: CSTRI4
             Example: CH_ZURICH.
        icon_position (Union[Unset, Point]): Point in [GeoJSON](https://datatracker.ietf.org/doc/html/rfc7946) format.
        spatial_projection (Union[Unset, LineString]): LineString in
            [GeoJSON](https://datatracker.ietf.org/doc/html/rfc7946) format.
        geofence (Union[Unset, GeofenceCircle]): Geofence expressed by a circle.
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    name_formatted: Union[Unset, str] = UNSET
    icon_position: Union[Unset, "Point"] = UNSET
    spatial_projection: Union[Unset, "LineString"] = UNSET
    geofence: Union[Unset, "GeofenceCircle"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        name_formatted = self.name_formatted
        icon_position: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.icon_position, Unset):
            icon_position = self.icon_position.to_dict()

        spatial_projection: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.spatial_projection, Unset):
            spatial_projection = self.spatial_projection.to_dict()

        geofence: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.geofence, Unset):
            geofence = self.geofence.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if name_formatted is not UNSET:
            field_dict["nameFormatted"] = name_formatted
        if icon_position is not UNSET:
            field_dict["iconPosition"] = icon_position
        if spatial_projection is not UNSET:
            field_dict["spatialProjection"] = spatial_projection
        if geofence is not UNSET:
            field_dict["geofence"] = geofence

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.geofence_circle import GeofenceCircle
        from ..models.line_string import LineString
        from ..models.point import Point

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        name_formatted = d.pop("nameFormatted", UNSET)

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

        _geofence = d.pop("geofence", UNSET)
        geofence: Union[Unset, GeofenceCircle]
        if isinstance(_geofence, Unset):
            geofence = UNSET
        else:
            geofence = GeofenceCircle.from_dict(_geofence)

        affected_region = cls(
            id=id,
            name=name,
            name_formatted=name_formatted,
            icon_position=icon_position,
            spatial_projection=spatial_projection,
            geofence=geofence,
        )

        affected_region.additional_properties = d
        return affected_region

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
