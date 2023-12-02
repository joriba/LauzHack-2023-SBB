import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.stop_v2_accessibility_item import StopV2AccessibilityItem
from ..models.stop_v2_accessibility_most_relevant import StopV2AccessibilityMostRelevant
from ..models.stop_v2_arrival_prognosis_type import StopV2ArrivalPrognosisType
from ..models.stop_v2_avg_occupancy_first_class import StopV2AvgOccupancyFirstClass
from ..models.stop_v2_avg_occupancy_second_class import StopV2AvgOccupancySecondClass
from ..models.stop_v2_boarding_alighting_status import StopV2BoardingAlightingStatus
from ..models.stop_v2_departure_prognosis_type import StopV2DeparturePrognosisType
from ..models.stop_v2_exit_side import StopV2ExitSide
from ..models.stop_v2_stop_status import StopV2StopStatus
from ..models.stop_v2_type import StopV2Type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.coordinates_wgs84 import CoordinatesWGS84


T = TypeVar("T", bound="StopV2")


@_attrs_define
class StopV2:
    """A stop represents a specific location (typically a STATION) of a leg or a complete journey-detail of a transport-
    product (aka v3.ScheduledStopPoint, OJP StopPoint).

        Attributes:
            type (StopV2Type): Origin and Destination: STATION, ADDRESS or POI; STATION: any stop between Origin and
                Destination
            uic_or_id (str): Unique identifier of STATION (case uic) or ADDRESS/POI (case id).
            name (str): Name of STATION (locale naming, non- translated).
            stop_status (StopV2StopStatus): Status at stop if STATION (like on plan, cancelled, partially cancelled). Null
                if ADDRESS or POI.
                This is is useful when iterating from stop to stop getting appropriate state symbols (de:Perlenschnur), see
                [Routing-Basics](https://github.com/SchweizerischeBundesbahnen/journey-service/blob/master/RoutingBasics.md).
            boarding_alighting_status (StopV2BoardingAlightingStatus): Boarding (de:einsteigen) and alighting
                (de:aussteigen) status for this Stop; see [Routing-
                Basics](https://github.com/SchweizerischeBundesbahnen/journey-service/blob/master/RoutingBasics.md)
            not_serviced (bool): @Deprecated Check StopStatus.NOT_SERVICED instead.
            request_stop (bool): Passenger needs to call for a vehicle stop (aka OJP `RequestStop`, resp. de:Halt auf
                Verlangen).
            arrival_platform_changed (bool): Related to arrivalTrackRt and arrivalTrack. **false** even if the rt track is
                set, this is not considered a realtime change (acc. to SBB busines rules); **true** real track change (typically
                drawn red in SBB UIs).
            departure_platform_changed (bool): Related to departureTrackRt and departureTrack. **false** even if the rt
                track is set, this is not considered a realtime change (acc. to SBB busines rules); **true** real track change
                (typically drawn red in SBB UIs).
            delay_undefined (bool): true: After a long amount of delay, according to SBB business rules (useful for channel
                to present the appropriate symbol).
            avg_occupancy_first_class (StopV2AvgOccupancyFirstClass): 1st class de:Belegung (average)
            avg_occupancy_second_class (StopV2AvgOccupancySecondClass): 2nd class de:Belegung (average)
            coordinates (Union[Unset, CoordinatesWGS84]): World Geodetic System 1984 (WGS 84) coordinates (latitude:
                specifies the north–south position of a point on the earth's surface; longitude: specifies the east-west
                position of a point on the earth's surface). For e.g. Bern CH (lat=46.947974,lon=7.447447).
            canton_ch (Union[Unset, str]): Canton abbreviation for locations within Switzerland. Example: BE.
            route_index (Union[Unset, int]): Route index of a stop/station in a journey-segment (depends on StopBehaviour).
                Usually starting from 0 or 1 and incrementing by 1. However if the route index value jumps:
                - it is most likely that the journey was rerouted
                - or a virtual Stop
            arrival_prognosis_type (Union[Unset, StopV2ArrivalPrognosisType]): Provides the type of the prognosis like if it
                was reported by an external provider or calculated or corrected by the system. Related to arrival date/time.
            departure_prognosis_type (Union[Unset, StopV2DeparturePrognosisType]): Provides the type of the prognosis like
                if it was reported by an external provider or calculated or corrected by the system. Related to departure
                date/time.
            boarding (Union[Unset, bool]): @Deprecated use boardingAlightingStatus exclusively
            boarding_rt (Union[Unset, bool]): @Deprecated use boardingAlightingStatus exclusively
            alighting (Union[Unset, bool]): @Deprecated use boardingAlightingStatus exclusively
            alighting_rt (Union[Unset, bool]): @Deprecated use boardingAlightingStatus exclusively
            virtual (Union[Unset, bool]): @Deprecated Use boardingAlightingStatus exclusively.
            arrival_track (Union[Unset, str]): Arriving platform planned. Example: 12A.
            arrival_track_rt (Union[Unset, str]): Arriving platform in realtime (oversteers arrivalTrack!). Whether this
                means a realtime change or just more detailed information has to be checked in related arrivalPlatformChanged!
                Example: 7.
            departure_track (Union[Unset, str]): Departing platform planned. Example: 12.
            departure_track_formatted (Union[Unset, str]): Principally same as departingTrack but with direction specific
                boarding-sections. Useful for e.g. in wing-trains (de:Flügelzug) such as Bern-Zweisimmen with a split of partial
                compositions at Spiez where customers might reach the wrong destination if they board the wrong boarding car.
                For end-customer-info prefer this value to display in UIs. Example: 12CD.
            departure_track_rt (Union[Unset, str]): Departing platform in realtime (oversteers departureTrack!). Whether
                this means a realtime change or just more detailed information has to be checked in related
                departurePlatformChanged! Example: 7.
            unplanned (Union[Unset, bool]): @Deprecated use stopStatus exclusively
            cancelled (Union[Unset, bool]): @Deprecated use stopStatus exclusively
            arrival_date_time (Union[Unset, datetime.datetime]): Arrival date/time
                ([ISO-8601](https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) UTC with time-numoffset (like '+02:00'))
                planned. Example: 2023-04-18T14:55:00+01:00.
            arrival_date_time_rt (Union[Unset, datetime.datetime]): Arrival date/time
                ([ISO-8601](https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) UTC with time-numoffset (like '+02:00'))
                in realtime (oversteers `arrivalDateTime`!).
            arrival_delay_text (Union[Unset, str]): Formatted end-user message about delay at arrival, according to SBB
                business rules.
            departure_date_time (Union[Unset, datetime.datetime]): Departure date/time
                ([ISO-8601](https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) UTC with time-numoffset (like '+02:00'))
                planned. Example: 2023-04-18T14:55:00+01:00.
            departure_date_time_rt (Union[Unset, datetime.datetime]): Departure date/time
                ([ISO-8601](https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) UTC with time-numoffset (like '+02:00'))
                in realtime (oversteers `departureDateTime`!).
            departure_delay_text (Union[Unset, str]): Realtime delay message at departure. Formatted to display for end-user
                according to SBB business rules.
            accessibility (Union[Unset, List[StopV2AccessibilityItem]]):
            accessibility_most_relevant (Union[Unset, StopV2AccessibilityMostRelevant]): The most relevant accessibility
                restriction for handicaped people out of #accessibility (according to SBB business rules). Example:
                BOARDING_ALIGHTING_SELF.
            exit_side (Union[Unset, StopV2ExitSide]): Exit side within a vehicle at a Stop (for e.g. car of train-formation)
                in relation to driving/forward direction. Example: LEFT.
            rank (Union[Unset, int]): Rank of importance based on intermediate stop priority and distance within a (partial)
                JourneyDetail. SBB KI rule based on display-info to find relevant intermediate stops to present on a visual
                stationboard (de:Perronanzeiger). Origin and destination of departure/arrival have always rank=null. Depends on
                /v2/departures or /v2/arrivals includeRank=true
            tariff_border_point (Union[Unset, bool]): true: Stop::uic represents a NOVA Tariff-BorderPoint; false: no NOVA
                TariffBorderPoint; null unknown/irrelevant
    """

    type: StopV2Type
    uic_or_id: str
    name: str
    stop_status: StopV2StopStatus
    boarding_alighting_status: StopV2BoardingAlightingStatus
    not_serviced: bool
    request_stop: bool
    arrival_platform_changed: bool
    departure_platform_changed: bool
    delay_undefined: bool
    avg_occupancy_first_class: StopV2AvgOccupancyFirstClass
    avg_occupancy_second_class: StopV2AvgOccupancySecondClass
    coordinates: Union[Unset, "CoordinatesWGS84"] = UNSET
    canton_ch: Union[Unset, str] = UNSET
    route_index: Union[Unset, int] = UNSET
    arrival_prognosis_type: Union[Unset, StopV2ArrivalPrognosisType] = UNSET
    departure_prognosis_type: Union[Unset, StopV2DeparturePrognosisType] = UNSET
    boarding: Union[Unset, bool] = UNSET
    boarding_rt: Union[Unset, bool] = UNSET
    alighting: Union[Unset, bool] = UNSET
    alighting_rt: Union[Unset, bool] = UNSET
    virtual: Union[Unset, bool] = UNSET
    arrival_track: Union[Unset, str] = UNSET
    arrival_track_rt: Union[Unset, str] = UNSET
    departure_track: Union[Unset, str] = UNSET
    departure_track_formatted: Union[Unset, str] = UNSET
    departure_track_rt: Union[Unset, str] = UNSET
    unplanned: Union[Unset, bool] = UNSET
    cancelled: Union[Unset, bool] = UNSET
    arrival_date_time: Union[Unset, datetime.datetime] = UNSET
    arrival_date_time_rt: Union[Unset, datetime.datetime] = UNSET
    arrival_delay_text: Union[Unset, str] = UNSET
    departure_date_time: Union[Unset, datetime.datetime] = UNSET
    departure_date_time_rt: Union[Unset, datetime.datetime] = UNSET
    departure_delay_text: Union[Unset, str] = UNSET
    accessibility: Union[Unset, List[StopV2AccessibilityItem]] = UNSET
    accessibility_most_relevant: Union[Unset, StopV2AccessibilityMostRelevant] = UNSET
    exit_side: Union[Unset, StopV2ExitSide] = UNSET
    rank: Union[Unset, int] = UNSET
    tariff_border_point: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        uic_or_id = self.uic_or_id
        name = self.name
        stop_status = self.stop_status.value

        boarding_alighting_status = self.boarding_alighting_status.value

        not_serviced = self.not_serviced
        request_stop = self.request_stop
        arrival_platform_changed = self.arrival_platform_changed
        departure_platform_changed = self.departure_platform_changed
        delay_undefined = self.delay_undefined
        avg_occupancy_first_class = self.avg_occupancy_first_class.value

        avg_occupancy_second_class = self.avg_occupancy_second_class.value

        coordinates: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.coordinates, Unset):
            coordinates = self.coordinates.to_dict()

        canton_ch = self.canton_ch
        route_index = self.route_index
        arrival_prognosis_type: Union[Unset, str] = UNSET
        if not isinstance(self.arrival_prognosis_type, Unset):
            arrival_prognosis_type = self.arrival_prognosis_type.value

        departure_prognosis_type: Union[Unset, str] = UNSET
        if not isinstance(self.departure_prognosis_type, Unset):
            departure_prognosis_type = self.departure_prognosis_type.value

        boarding = self.boarding
        boarding_rt = self.boarding_rt
        alighting = self.alighting
        alighting_rt = self.alighting_rt
        virtual = self.virtual
        arrival_track = self.arrival_track
        arrival_track_rt = self.arrival_track_rt
        departure_track = self.departure_track
        departure_track_formatted = self.departure_track_formatted
        departure_track_rt = self.departure_track_rt
        unplanned = self.unplanned
        cancelled = self.cancelled
        arrival_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.arrival_date_time, Unset):
            arrival_date_time = self.arrival_date_time.isoformat()

        arrival_date_time_rt: Union[Unset, str] = UNSET
        if not isinstance(self.arrival_date_time_rt, Unset):
            arrival_date_time_rt = self.arrival_date_time_rt.isoformat()

        arrival_delay_text = self.arrival_delay_text
        departure_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.departure_date_time, Unset):
            departure_date_time = self.departure_date_time.isoformat()

        departure_date_time_rt: Union[Unset, str] = UNSET
        if not isinstance(self.departure_date_time_rt, Unset):
            departure_date_time_rt = self.departure_date_time_rt.isoformat()

        departure_delay_text = self.departure_delay_text
        accessibility: Union[Unset, List[str]] = UNSET
        if not isinstance(self.accessibility, Unset):
            accessibility = []
            for accessibility_item_data in self.accessibility:
                accessibility_item = accessibility_item_data.value

                accessibility.append(accessibility_item)

        accessibility_most_relevant: Union[Unset, str] = UNSET
        if not isinstance(self.accessibility_most_relevant, Unset):
            accessibility_most_relevant = self.accessibility_most_relevant.value

        exit_side: Union[Unset, str] = UNSET
        if not isinstance(self.exit_side, Unset):
            exit_side = self.exit_side.value

        rank = self.rank
        tariff_border_point = self.tariff_border_point

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "uicOrId": uic_or_id,
                "name": name,
                "stopStatus": stop_status,
                "boardingAlightingStatus": boarding_alighting_status,
                "notServiced": not_serviced,
                "requestStop": request_stop,
                "arrivalPlatformChanged": arrival_platform_changed,
                "departurePlatformChanged": departure_platform_changed,
                "delayUndefined": delay_undefined,
                "avgOccupancyFirstClass": avg_occupancy_first_class,
                "avgOccupancySecondClass": avg_occupancy_second_class,
            }
        )
        if coordinates is not UNSET:
            field_dict["coordinates"] = coordinates
        if canton_ch is not UNSET:
            field_dict["cantonCH"] = canton_ch
        if route_index is not UNSET:
            field_dict["routeIndex"] = route_index
        if arrival_prognosis_type is not UNSET:
            field_dict["arrivalPrognosisType"] = arrival_prognosis_type
        if departure_prognosis_type is not UNSET:
            field_dict["departurePrognosisType"] = departure_prognosis_type
        if boarding is not UNSET:
            field_dict["boarding"] = boarding
        if boarding_rt is not UNSET:
            field_dict["boardingRt"] = boarding_rt
        if alighting is not UNSET:
            field_dict["alighting"] = alighting
        if alighting_rt is not UNSET:
            field_dict["alightingRt"] = alighting_rt
        if virtual is not UNSET:
            field_dict["virtual"] = virtual
        if arrival_track is not UNSET:
            field_dict["arrivalTrack"] = arrival_track
        if arrival_track_rt is not UNSET:
            field_dict["arrivalTrackRt"] = arrival_track_rt
        if departure_track is not UNSET:
            field_dict["departureTrack"] = departure_track
        if departure_track_formatted is not UNSET:
            field_dict["departureTrackFormatted"] = departure_track_formatted
        if departure_track_rt is not UNSET:
            field_dict["departureTrackRt"] = departure_track_rt
        if unplanned is not UNSET:
            field_dict["unplanned"] = unplanned
        if cancelled is not UNSET:
            field_dict["cancelled"] = cancelled
        if arrival_date_time is not UNSET:
            field_dict["arrivalDateTime"] = arrival_date_time
        if arrival_date_time_rt is not UNSET:
            field_dict["arrivalDateTimeRt"] = arrival_date_time_rt
        if arrival_delay_text is not UNSET:
            field_dict["arrivalDelayText"] = arrival_delay_text
        if departure_date_time is not UNSET:
            field_dict["departureDateTime"] = departure_date_time
        if departure_date_time_rt is not UNSET:
            field_dict["departureDateTimeRt"] = departure_date_time_rt
        if departure_delay_text is not UNSET:
            field_dict["departureDelayText"] = departure_delay_text
        if accessibility is not UNSET:
            field_dict["accessibility"] = accessibility
        if accessibility_most_relevant is not UNSET:
            field_dict["accessibilityMostRelevant"] = accessibility_most_relevant
        if exit_side is not UNSET:
            field_dict["exitSide"] = exit_side
        if rank is not UNSET:
            field_dict["rank"] = rank
        if tariff_border_point is not UNSET:
            field_dict["tariffBorderPoint"] = tariff_border_point

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.coordinates_wgs84 import CoordinatesWGS84

        d = src_dict.copy()
        type = StopV2Type(d.pop("type"))

        uic_or_id = d.pop("uicOrId")

        name = d.pop("name")

        stop_status = StopV2StopStatus(d.pop("stopStatus"))

        boarding_alighting_status = StopV2BoardingAlightingStatus(d.pop("boardingAlightingStatus"))

        not_serviced = d.pop("notServiced")

        request_stop = d.pop("requestStop")

        arrival_platform_changed = d.pop("arrivalPlatformChanged")

        departure_platform_changed = d.pop("departurePlatformChanged")

        delay_undefined = d.pop("delayUndefined")

        avg_occupancy_first_class = StopV2AvgOccupancyFirstClass(d.pop("avgOccupancyFirstClass"))

        avg_occupancy_second_class = StopV2AvgOccupancySecondClass(d.pop("avgOccupancySecondClass"))

        _coordinates = d.pop("coordinates", UNSET)
        coordinates: Union[Unset, CoordinatesWGS84]
        if isinstance(_coordinates, Unset):
            coordinates = UNSET
        else:
            coordinates = CoordinatesWGS84.from_dict(_coordinates)

        canton_ch = d.pop("cantonCH", UNSET)

        route_index = d.pop("routeIndex", UNSET)

        _arrival_prognosis_type = d.pop("arrivalPrognosisType", UNSET)
        arrival_prognosis_type: Union[Unset, StopV2ArrivalPrognosisType]
        if isinstance(_arrival_prognosis_type, Unset):
            arrival_prognosis_type = UNSET
        else:
            arrival_prognosis_type = StopV2ArrivalPrognosisType(_arrival_prognosis_type)

        _departure_prognosis_type = d.pop("departurePrognosisType", UNSET)
        departure_prognosis_type: Union[Unset, StopV2DeparturePrognosisType]
        if isinstance(_departure_prognosis_type, Unset):
            departure_prognosis_type = UNSET
        else:
            departure_prognosis_type = StopV2DeparturePrognosisType(_departure_prognosis_type)

        boarding = d.pop("boarding", UNSET)

        boarding_rt = d.pop("boardingRt", UNSET)

        alighting = d.pop("alighting", UNSET)

        alighting_rt = d.pop("alightingRt", UNSET)

        virtual = d.pop("virtual", UNSET)

        arrival_track = d.pop("arrivalTrack", UNSET)

        arrival_track_rt = d.pop("arrivalTrackRt", UNSET)

        departure_track = d.pop("departureTrack", UNSET)

        departure_track_formatted = d.pop("departureTrackFormatted", UNSET)

        departure_track_rt = d.pop("departureTrackRt", UNSET)

        unplanned = d.pop("unplanned", UNSET)

        cancelled = d.pop("cancelled", UNSET)

        _arrival_date_time = d.pop("arrivalDateTime", UNSET)
        arrival_date_time: Union[Unset, datetime.datetime]
        if isinstance(_arrival_date_time, Unset):
            arrival_date_time = UNSET
        else:
            arrival_date_time = isoparse(_arrival_date_time)

        _arrival_date_time_rt = d.pop("arrivalDateTimeRt", UNSET)
        arrival_date_time_rt: Union[Unset, datetime.datetime]
        if isinstance(_arrival_date_time_rt, Unset):
            arrival_date_time_rt = UNSET
        else:
            arrival_date_time_rt = isoparse(_arrival_date_time_rt)

        arrival_delay_text = d.pop("arrivalDelayText", UNSET)

        _departure_date_time = d.pop("departureDateTime", UNSET)
        departure_date_time: Union[Unset, datetime.datetime]
        if isinstance(_departure_date_time, Unset):
            departure_date_time = UNSET
        else:
            departure_date_time = isoparse(_departure_date_time)

        _departure_date_time_rt = d.pop("departureDateTimeRt", UNSET)
        departure_date_time_rt: Union[Unset, datetime.datetime]
        if isinstance(_departure_date_time_rt, Unset):
            departure_date_time_rt = UNSET
        else:
            departure_date_time_rt = isoparse(_departure_date_time_rt)

        departure_delay_text = d.pop("departureDelayText", UNSET)

        accessibility = []
        _accessibility = d.pop("accessibility", UNSET)
        for accessibility_item_data in _accessibility or []:
            accessibility_item = StopV2AccessibilityItem(accessibility_item_data)

            accessibility.append(accessibility_item)

        _accessibility_most_relevant = d.pop("accessibilityMostRelevant", UNSET)
        accessibility_most_relevant: Union[Unset, StopV2AccessibilityMostRelevant]
        if isinstance(_accessibility_most_relevant, Unset):
            accessibility_most_relevant = UNSET
        else:
            accessibility_most_relevant = StopV2AccessibilityMostRelevant(_accessibility_most_relevant)

        _exit_side = d.pop("exitSide", UNSET)
        exit_side: Union[Unset, StopV2ExitSide]
        if isinstance(_exit_side, Unset):
            exit_side = UNSET
        else:
            exit_side = StopV2ExitSide(_exit_side)

        rank = d.pop("rank", UNSET)

        tariff_border_point = d.pop("tariffBorderPoint", UNSET)

        stop_v2 = cls(
            type=type,
            uic_or_id=uic_or_id,
            name=name,
            stop_status=stop_status,
            boarding_alighting_status=boarding_alighting_status,
            not_serviced=not_serviced,
            request_stop=request_stop,
            arrival_platform_changed=arrival_platform_changed,
            departure_platform_changed=departure_platform_changed,
            delay_undefined=delay_undefined,
            avg_occupancy_first_class=avg_occupancy_first_class,
            avg_occupancy_second_class=avg_occupancy_second_class,
            coordinates=coordinates,
            canton_ch=canton_ch,
            route_index=route_index,
            arrival_prognosis_type=arrival_prognosis_type,
            departure_prognosis_type=departure_prognosis_type,
            boarding=boarding,
            boarding_rt=boarding_rt,
            alighting=alighting,
            alighting_rt=alighting_rt,
            virtual=virtual,
            arrival_track=arrival_track,
            arrival_track_rt=arrival_track_rt,
            departure_track=departure_track,
            departure_track_formatted=departure_track_formatted,
            departure_track_rt=departure_track_rt,
            unplanned=unplanned,
            cancelled=cancelled,
            arrival_date_time=arrival_date_time,
            arrival_date_time_rt=arrival_date_time_rt,
            arrival_delay_text=arrival_delay_text,
            departure_date_time=departure_date_time,
            departure_date_time_rt=departure_date_time_rt,
            departure_delay_text=departure_delay_text,
            accessibility=accessibility,
            accessibility_most_relevant=accessibility_most_relevant,
            exit_side=exit_side,
            rank=rank,
            tariff_border_point=tariff_border_point,
        )

        stop_v2.additional_properties = d
        return stop_v2

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
