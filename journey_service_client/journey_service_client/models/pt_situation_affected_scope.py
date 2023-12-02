import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.affected_edge import AffectedEdge
    from ..models.affected_region import AffectedRegion
    from ..models.scheduled_stop_point import ScheduledStopPoint
    from ..models.vehicle_mode import VehicleMode


T = TypeVar("T", bound="PTSituationAffectedScope")


@_attrs_define
class PTSituationAffectedScope:
    """An extent directly involved in the PT situation such as a set of `ServiceJourney` or `StopPlace`.

    Attributes:
        vehicle_modes (List['VehicleMode']):
        operating_days (List[datetime.date]):
        edges (List['AffectedEdge']):
        regions (List['AffectedRegion']):
        stop_point_from (Union[Unset, ScheduledStopPoint]): Passenger relevant stop-point on a `ServiceJourney`. Some
            properties may further by distinguished on either `arrival` and/or `departure StopCall` aspects.
        stop_point_to (Union[Unset, ScheduledStopPoint]): Passenger relevant stop-point on a `ServiceJourney`. Some
            properties may further by distinguished on either `arrival` and/or `departure StopCall` aspects.
    """

    vehicle_modes: List["VehicleMode"]
    operating_days: List[datetime.date]
    edges: List["AffectedEdge"]
    regions: List["AffectedRegion"]
    stop_point_from: Union[Unset, "ScheduledStopPoint"] = UNSET
    stop_point_to: Union[Unset, "ScheduledStopPoint"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        vehicle_modes = []
        for vehicle_modes_item_data in self.vehicle_modes:
            vehicle_modes_item = vehicle_modes_item_data.to_dict()

            vehicle_modes.append(vehicle_modes_item)

        operating_days = []
        for operating_days_item_data in self.operating_days:
            operating_days_item = operating_days_item_data.isoformat()
            operating_days.append(operating_days_item)

        edges = []
        for edges_item_data in self.edges:
            edges_item = edges_item_data.to_dict()

            edges.append(edges_item)

        regions = []
        for regions_item_data in self.regions:
            regions_item = regions_item_data.to_dict()

            regions.append(regions_item)

        stop_point_from: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.stop_point_from, Unset):
            stop_point_from = self.stop_point_from.to_dict()

        stop_point_to: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.stop_point_to, Unset):
            stop_point_to = self.stop_point_to.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "vehicleModes": vehicle_modes,
                "operatingDays": operating_days,
                "edges": edges,
                "regions": regions,
            }
        )
        if stop_point_from is not UNSET:
            field_dict["stopPointFrom"] = stop_point_from
        if stop_point_to is not UNSET:
            field_dict["stopPointTo"] = stop_point_to

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.affected_edge import AffectedEdge
        from ..models.affected_region import AffectedRegion
        from ..models.scheduled_stop_point import ScheduledStopPoint
        from ..models.vehicle_mode import VehicleMode

        d = src_dict.copy()
        vehicle_modes = []
        _vehicle_modes = d.pop("vehicleModes")
        for vehicle_modes_item_data in _vehicle_modes:
            vehicle_modes_item = VehicleMode.from_dict(vehicle_modes_item_data)

            vehicle_modes.append(vehicle_modes_item)

        operating_days = []
        _operating_days = d.pop("operatingDays")
        for operating_days_item_data in _operating_days:
            operating_days_item = isoparse(operating_days_item_data).date()

            operating_days.append(operating_days_item)

        edges = []
        _edges = d.pop("edges")
        for edges_item_data in _edges:
            edges_item = AffectedEdge.from_dict(edges_item_data)

            edges.append(edges_item)

        regions = []
        _regions = d.pop("regions")
        for regions_item_data in _regions:
            regions_item = AffectedRegion.from_dict(regions_item_data)

            regions.append(regions_item)

        _stop_point_from = d.pop("stopPointFrom", UNSET)
        stop_point_from: Union[Unset, ScheduledStopPoint]
        if isinstance(_stop_point_from, Unset):
            stop_point_from = UNSET
        else:
            stop_point_from = ScheduledStopPoint.from_dict(_stop_point_from)

        _stop_point_to = d.pop("stopPointTo", UNSET)
        stop_point_to: Union[Unset, ScheduledStopPoint]
        if isinstance(_stop_point_to, Unset):
            stop_point_to = UNSET
        else:
            stop_point_to = ScheduledStopPoint.from_dict(_stop_point_to)

        pt_situation_affected_scope = cls(
            vehicle_modes=vehicle_modes,
            operating_days=operating_days,
            edges=edges,
            regions=regions,
            stop_point_from=stop_point_from,
            stop_point_to=stop_point_to,
        )

        pt_situation_affected_scope.additional_properties = d
        return pt_situation_affected_scope

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
