import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.realtime_mode_enum import RealtimeModeEnum
from ..models.transport_mode_enum import TransportModeEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dated_vehicle_journey_reference import DatedVehicleJourneyReference
    from ..models.pt_via_reference import PTViaReference
    from ..models.scheduled_stop_point_reference import ScheduledStopPointReference


T = TypeVar("T", bound="TripsByLegRequestBody")


@_attrs_define
class TripsByLegRequestBody:
    """Request parameters (POST body).

    Attributes:
        pt_ride_leg_reference (DatedVehicleJourneyReference): Reference to a `DatedVehicleJourney` (aka OJP
            DatedJourneyRef). See [complex JSON parameter
            **DatedVehicleJourneyReference**](https://github.com/SchweizerischeBundesbahnen/journey-
            service/blob/master/JSON-Objects.md#datedvehiclejourneyreference)
        destination (str): Final destination **`StopPlace`** of the planned Trip, relates to current position in
            `ptRideLegReference`. See [**PlaceReference**](https://github.com/SchweizerischeBundesbahnen/journey-
            service/blob/master/JSON-Objects.md#placereference) Example: 8507000.
        date (Union[Unset, datetime.date]): Current date of passenger on `ptRideLegReference` related to `time`,
            defaults to TODAY. Example: 2023-04-18.
        time (Union[Unset, str]): Current (local) time of passenger on `ptRideLegReference` related to `date`, defaults
            to NOW. Example: 13:07.
        transfer_stop_point (Union[Unset, ScheduledStopPointReference]): ScheduledStopPoint reference to a StopPlace
            (PlaceReference) with a departure or arrival dateTime, see
            [ScheduledStopPointReference](https://github.com/SchweizerischeBundesbahnen/journey-service/blob/master/JSON-
            Objects.md#scheduledstoppointreference).
        transfer_stop_point_at_arrival (Union[Unset, bool]): Relates to `transferStopPoint::dateTime`. Distinguishes
            between arrival or departure dateTime at `transferStopPoint`.
        operators (Union[Unset, List[str]]):
        vias (Union[Unset, List['PTViaReference']]):
        realtime_mode (Union[Unset, RealtimeModeEnum]): <br>x-extensible-enum:
            - `REALTIME` potentially planned and RT **including non-rideable** (like cancelled)
            - `REALTIME_RIDEABLE` as `REALTIME` but **excluding non-rideable**
            - `OFF` **planned only** Default: RealtimeModeEnum.REALTIME.
        limit (Union[Unset, int]): Maximum number of results to be returned, related to parameter `duration` and may
            reduce or expand `limit` settings. Default: 10.
        duration (Union[Unset, int]): Duration of interval in minutes. Choose wisely, in most cases next 120min are
            sufficient!<br>This parameter has an impact on performance and/or response volume, set wisely! Default: 60.
        include_transport_modes (Union[Unset, List[TransportModeEnum]]):
        exclude_dated_vehicle_journeys (Union[Unset, List['DatedVehicleJourneyReference']]):
    """

    pt_ride_leg_reference: "DatedVehicleJourneyReference"
    destination: str
    date: Union[Unset, datetime.date] = UNSET
    time: Union[Unset, str] = UNSET
    transfer_stop_point: Union[Unset, "ScheduledStopPointReference"] = UNSET
    transfer_stop_point_at_arrival: Union[Unset, bool] = False
    operators: Union[Unset, List[str]] = UNSET
    vias: Union[Unset, List["PTViaReference"]] = UNSET
    realtime_mode: Union[Unset, RealtimeModeEnum] = RealtimeModeEnum.REALTIME
    limit: Union[Unset, int] = 10
    duration: Union[Unset, int] = 60
    include_transport_modes: Union[Unset, List[TransportModeEnum]] = UNSET
    exclude_dated_vehicle_journeys: Union[Unset, List["DatedVehicleJourneyReference"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pt_ride_leg_reference = self.pt_ride_leg_reference.to_dict()

        destination = self.destination
        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        time = self.time
        transfer_stop_point: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.transfer_stop_point, Unset):
            transfer_stop_point = self.transfer_stop_point.to_dict()

        transfer_stop_point_at_arrival = self.transfer_stop_point_at_arrival
        operators: Union[Unset, List[str]] = UNSET
        if not isinstance(self.operators, Unset):
            operators = self.operators

        vias: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.vias, Unset):
            vias = []
            for vias_item_data in self.vias:
                vias_item = vias_item_data.to_dict()

                vias.append(vias_item)

        realtime_mode: Union[Unset, str] = UNSET
        if not isinstance(self.realtime_mode, Unset):
            realtime_mode = self.realtime_mode.value

        limit = self.limit
        duration = self.duration
        include_transport_modes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.include_transport_modes, Unset):
            include_transport_modes = []
            for include_transport_modes_item_data in self.include_transport_modes:
                include_transport_modes_item = include_transport_modes_item_data.value

                include_transport_modes.append(include_transport_modes_item)

        exclude_dated_vehicle_journeys: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.exclude_dated_vehicle_journeys, Unset):
            exclude_dated_vehicle_journeys = []
            for exclude_dated_vehicle_journeys_item_data in self.exclude_dated_vehicle_journeys:
                exclude_dated_vehicle_journeys_item = exclude_dated_vehicle_journeys_item_data.to_dict()

                exclude_dated_vehicle_journeys.append(exclude_dated_vehicle_journeys_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ptRideLegReference": pt_ride_leg_reference,
                "destination": destination,
            }
        )
        if date is not UNSET:
            field_dict["date"] = date
        if time is not UNSET:
            field_dict["time"] = time
        if transfer_stop_point is not UNSET:
            field_dict["transferStopPoint"] = transfer_stop_point
        if transfer_stop_point_at_arrival is not UNSET:
            field_dict["transferStopPointAtArrival"] = transfer_stop_point_at_arrival
        if operators is not UNSET:
            field_dict["operators"] = operators
        if vias is not UNSET:
            field_dict["vias"] = vias
        if realtime_mode is not UNSET:
            field_dict["realtimeMode"] = realtime_mode
        if limit is not UNSET:
            field_dict["limit"] = limit
        if duration is not UNSET:
            field_dict["duration"] = duration
        if include_transport_modes is not UNSET:
            field_dict["includeTransportModes"] = include_transport_modes
        if exclude_dated_vehicle_journeys is not UNSET:
            field_dict["excludeDatedVehicleJourneys"] = exclude_dated_vehicle_journeys

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dated_vehicle_journey_reference import DatedVehicleJourneyReference
        from ..models.pt_via_reference import PTViaReference
        from ..models.scheduled_stop_point_reference import ScheduledStopPointReference

        d = src_dict.copy()
        pt_ride_leg_reference = DatedVehicleJourneyReference.from_dict(d.pop("ptRideLegReference"))

        destination = d.pop("destination")

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.date]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()

        time = d.pop("time", UNSET)

        _transfer_stop_point = d.pop("transferStopPoint", UNSET)
        transfer_stop_point: Union[Unset, ScheduledStopPointReference]
        if isinstance(_transfer_stop_point, Unset):
            transfer_stop_point = UNSET
        else:
            transfer_stop_point = ScheduledStopPointReference.from_dict(_transfer_stop_point)

        transfer_stop_point_at_arrival = d.pop("transferStopPointAtArrival", UNSET)

        operators = cast(List[str], d.pop("operators", UNSET))

        vias = []
        _vias = d.pop("vias", UNSET)
        for vias_item_data in _vias or []:
            vias_item = PTViaReference.from_dict(vias_item_data)

            vias.append(vias_item)

        _realtime_mode = d.pop("realtimeMode", UNSET)
        realtime_mode: Union[Unset, RealtimeModeEnum]
        if isinstance(_realtime_mode, Unset):
            realtime_mode = UNSET
        else:
            realtime_mode = RealtimeModeEnum(_realtime_mode)

        limit = d.pop("limit", UNSET)

        duration = d.pop("duration", UNSET)

        include_transport_modes = []
        _include_transport_modes = d.pop("includeTransportModes", UNSET)
        for include_transport_modes_item_data in _include_transport_modes or []:
            include_transport_modes_item = TransportModeEnum(include_transport_modes_item_data)

            include_transport_modes.append(include_transport_modes_item)

        exclude_dated_vehicle_journeys = []
        _exclude_dated_vehicle_journeys = d.pop("excludeDatedVehicleJourneys", UNSET)
        for exclude_dated_vehicle_journeys_item_data in _exclude_dated_vehicle_journeys or []:
            exclude_dated_vehicle_journeys_item = DatedVehicleJourneyReference.from_dict(
                exclude_dated_vehicle_journeys_item_data
            )

            exclude_dated_vehicle_journeys.append(exclude_dated_vehicle_journeys_item)

        trips_by_leg_request_body = cls(
            pt_ride_leg_reference=pt_ride_leg_reference,
            destination=destination,
            date=date,
            time=time,
            transfer_stop_point=transfer_stop_point,
            transfer_stop_point_at_arrival=transfer_stop_point_at_arrival,
            operators=operators,
            vias=vias,
            realtime_mode=realtime_mode,
            limit=limit,
            duration=duration,
            include_transport_modes=include_transport_modes,
            exclude_dated_vehicle_journeys=exclude_dated_vehicle_journeys,
        )

        trips_by_leg_request_body.additional_properties = d
        return trips_by_leg_request_body

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
