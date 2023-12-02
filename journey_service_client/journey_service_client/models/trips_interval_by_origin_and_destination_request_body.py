import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.accessibility_enum import AccessibilityEnum
from ..models.alternate_match_enum import AlternateMatchEnum
from ..models.notice_attribute_enum import NoticeAttributeEnum
from ..models.occupancy_average_enum import OccupancyAverageEnum
from ..models.realtime_mode_enum import RealtimeModeEnum
from ..models.transport_mode_enum import TransportModeEnum
from ..models.trips_interval_by_origin_and_destination_request_body_include_intermediate_stops import (
    TripsIntervalByOriginAndDestinationRequestBodyIncludeIntermediateStops,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pt_via_no_change_at_reference import PTViaNoChangeAtReference
    from ..models.pt_via_not_reference import PTViaNotReference
    from ..models.pt_via_reference import PTViaReference
    from ..models.trip_mobility_filter import TripMobilityFilter


T = TypeVar("T", bound="TripsIntervalByOriginAndDestinationRequestBody")


@_attrs_define
class TripsIntervalByOriginAndDestinationRequestBody:
    """Request parameters (POST body).

    Attributes:
        origin (str): Starting point of the trip at origin (departure). See v3 **PlaceReference** as `StopPlace` only in
            [complex parameter](https://github.com/SchweizerischeBundesbahnen/journey-service/blob/master/JSON-Objects.md)
            Example: 8503000.
        destination (str): Ending point of the trip at destination (arrival). See **PlaceReference** as `StopPlace` only
            in [complex parameter](https://github.com/SchweizerischeBundesbahnen/journey-service/blob/master/JSON-
            Objects.md) Example: [7.435194,46.945679].
        date (Union[Unset, datetime.date]): (Local) date at either origin related to `time`, defaults to TODAY. Example:
            2023-04-18.
        time (Union[Unset, str]): Local time at either origin related to `date`, defaults to NOW (seconds will be
            ignored). Example: 13:07.
        occupancy_average (Union[Unset, OccupancyAverageEnum]): Find trips with average occupancy (or better, by means
            emptier) per passenger-class in Public Transportation vehicle.<br>x-extensible-enum:  Default:
            OccupancyAverageEnum.ALL.
        mobility_filter (Union[Unset, TripMobilityFilter]): Parameters to restrict the transfer options - particularly
            for interchanging PTRideLeg's by passenger (de: Individuelles Umsteigeverhalten).
            - TripsByOriginAndDestinationPostBody: all filters supported
            - ServiceCalendarByOriginAndDestinationRequestBody: only `maxTransfers` supported yet
        vias (Union[Unset, List['PTViaReference']]):
        vias_not (Union[Unset, List['PTViaNotReference']]):
        vias_no_transfer (Union[Unset, List['PTViaNoChangeAtReference']]):
        realtime_mode (Union[Unset, RealtimeModeEnum]): <br>x-extensible-enum:
            - `REALTIME` potentially planned and RT **including non-rideable** (like cancelled)
            - `REALTIME_RIDEABLE` as `REALTIME` but **excluding non-rideable**
            - `OFF` **planned only** Default: RealtimeModeEnum.REALTIME.
        paging_cursor (Union[Unset, str]): Based on a returned `TripResponse::pagingCursor`, `previous` or `next`
            connections **reusing the very same search-parameters** can be retrieved by scrolling pagination mechanisme, see
            `Trip::pagingChecksum`).
        limit (Union[Unset, int]): Maximum number of results to be returned, related to parameter `duration` and may
            reduce or expand `limit` settings. Default: 20.
        duration (Union[Unset, int]): Interval duration [min.] (0..1439) to consider. Relates to parameter `limit`,
            which will limit results within the duration. Default: 60.
        include_accessibility (Union[Unset, AccessibilityEnum]): Accessibility (de:BFR/BAIM) for better handicap support
            using vehicles. If available relevant on first (boarding) and last (alighting) ScheduledStopPoint per PTRideLeg.
            Impacts `ScheduledStopPoint::accessibilityBoardingAlighting`.<br>x-extensible-enum:  see enum
            values.<br>`ServiceJourney::notices` will get an entry of `type=INFO, key=RN` if available, its `Notice::value`
            is relevant for Postauto AG (PAG) operations-reference. Default: AccessibilityEnum.ALL.
        include_alternate_match (Union[Unset, AlternateMatchEnum]): Post-filter to adjust cancelled/alternate 1:1 Trip
            cases per response (de:Ausfall/Ersatz) according to SBB BR, where other Trip's remain as is.<br>x-extensible-
            enum:
            - IRRELEVANT: no adaption
            - BOTH: as IRRELEVANT but some Note's will be cloned from cancelled to 1:1 alternate Trip
            - ALTERNATE_ONLY: suppresses cancelled 1:1 Trip's if matched with alternates
            - CANCELLED_ONLY: suppress exactly matching 1:1 alternates Default: AlternateMatchEnum.IRRELEVANT.
        include_notice_attributes (Union[Unset, List[NoticeAttributeEnum]]):
        include_transport_modes (Union[Unset, List[TransportModeEnum]]):
        include_summary (Union[Unset, bool]): Create some summary facts about each Trip (useful for UI
            overviews).<br>This parameter has an impact on performance and/or response volume, set wisely!
        include_intermediate_stops (Union[Unset,
            TripsIntervalByOriginAndDestinationRequestBodyIncludeIntermediateStops]): Whether the `PTRideLeg's` should
            include intermediate stops (between the passenger's board and alight in
            `ServiceJourney::stopPoints`).<br>x-extensible-enum:  [ALL,NONE,BOARDING_ALIGHTING] where ALL is
            BOARDING_ALIGHTING plus virtual stops. Default:
            TripsIntervalByOriginAndDestinationRequestBodyIncludeIntermediateStops.ALL.
    """

    origin: str
    destination: str
    date: Union[Unset, datetime.date] = UNSET
    time: Union[Unset, str] = UNSET
    occupancy_average: Union[Unset, OccupancyAverageEnum] = OccupancyAverageEnum.ALL
    mobility_filter: Union[Unset, "TripMobilityFilter"] = UNSET
    vias: Union[Unset, List["PTViaReference"]] = UNSET
    vias_not: Union[Unset, List["PTViaNotReference"]] = UNSET
    vias_no_transfer: Union[Unset, List["PTViaNoChangeAtReference"]] = UNSET
    realtime_mode: Union[Unset, RealtimeModeEnum] = RealtimeModeEnum.REALTIME
    paging_cursor: Union[Unset, str] = UNSET
    limit: Union[Unset, int] = 20
    duration: Union[Unset, int] = 60
    include_accessibility: Union[Unset, AccessibilityEnum] = AccessibilityEnum.ALL
    include_alternate_match: Union[Unset, AlternateMatchEnum] = AlternateMatchEnum.IRRELEVANT
    include_notice_attributes: Union[Unset, List[NoticeAttributeEnum]] = UNSET
    include_transport_modes: Union[Unset, List[TransportModeEnum]] = UNSET
    include_summary: Union[Unset, bool] = False
    include_intermediate_stops: Union[
        Unset, TripsIntervalByOriginAndDestinationRequestBodyIncludeIntermediateStops
    ] = TripsIntervalByOriginAndDestinationRequestBodyIncludeIntermediateStops.ALL
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        origin = self.origin
        destination = self.destination
        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        time = self.time
        occupancy_average: Union[Unset, str] = UNSET
        if not isinstance(self.occupancy_average, Unset):
            occupancy_average = self.occupancy_average.value

        mobility_filter: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mobility_filter, Unset):
            mobility_filter = self.mobility_filter.to_dict()

        vias: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.vias, Unset):
            vias = []
            for vias_item_data in self.vias:
                vias_item = vias_item_data.to_dict()

                vias.append(vias_item)

        vias_not: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.vias_not, Unset):
            vias_not = []
            for vias_not_item_data in self.vias_not:
                vias_not_item = vias_not_item_data.to_dict()

                vias_not.append(vias_not_item)

        vias_no_transfer: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.vias_no_transfer, Unset):
            vias_no_transfer = []
            for vias_no_transfer_item_data in self.vias_no_transfer:
                vias_no_transfer_item = vias_no_transfer_item_data.to_dict()

                vias_no_transfer.append(vias_no_transfer_item)

        realtime_mode: Union[Unset, str] = UNSET
        if not isinstance(self.realtime_mode, Unset):
            realtime_mode = self.realtime_mode.value

        paging_cursor = self.paging_cursor
        limit = self.limit
        duration = self.duration
        include_accessibility: Union[Unset, str] = UNSET
        if not isinstance(self.include_accessibility, Unset):
            include_accessibility = self.include_accessibility.value

        include_alternate_match: Union[Unset, str] = UNSET
        if not isinstance(self.include_alternate_match, Unset):
            include_alternate_match = self.include_alternate_match.value

        include_notice_attributes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.include_notice_attributes, Unset):
            include_notice_attributes = []
            for include_notice_attributes_item_data in self.include_notice_attributes:
                include_notice_attributes_item = include_notice_attributes_item_data.value

                include_notice_attributes.append(include_notice_attributes_item)

        include_transport_modes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.include_transport_modes, Unset):
            include_transport_modes = []
            for include_transport_modes_item_data in self.include_transport_modes:
                include_transport_modes_item = include_transport_modes_item_data.value

                include_transport_modes.append(include_transport_modes_item)

        include_summary = self.include_summary
        include_intermediate_stops: Union[Unset, str] = UNSET
        if not isinstance(self.include_intermediate_stops, Unset):
            include_intermediate_stops = self.include_intermediate_stops.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "origin": origin,
                "destination": destination,
            }
        )
        if date is not UNSET:
            field_dict["date"] = date
        if time is not UNSET:
            field_dict["time"] = time
        if occupancy_average is not UNSET:
            field_dict["occupancyAverage"] = occupancy_average
        if mobility_filter is not UNSET:
            field_dict["mobilityFilter"] = mobility_filter
        if vias is not UNSET:
            field_dict["vias"] = vias
        if vias_not is not UNSET:
            field_dict["viasNot"] = vias_not
        if vias_no_transfer is not UNSET:
            field_dict["viasNoTransfer"] = vias_no_transfer
        if realtime_mode is not UNSET:
            field_dict["realtimeMode"] = realtime_mode
        if paging_cursor is not UNSET:
            field_dict["pagingCursor"] = paging_cursor
        if limit is not UNSET:
            field_dict["limit"] = limit
        if duration is not UNSET:
            field_dict["duration"] = duration
        if include_accessibility is not UNSET:
            field_dict["includeAccessibility"] = include_accessibility
        if include_alternate_match is not UNSET:
            field_dict["includeAlternateMatch"] = include_alternate_match
        if include_notice_attributes is not UNSET:
            field_dict["includeNoticeAttributes"] = include_notice_attributes
        if include_transport_modes is not UNSET:
            field_dict["includeTransportModes"] = include_transport_modes
        if include_summary is not UNSET:
            field_dict["includeSummary"] = include_summary
        if include_intermediate_stops is not UNSET:
            field_dict["includeIntermediateStops"] = include_intermediate_stops

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pt_via_no_change_at_reference import PTViaNoChangeAtReference
        from ..models.pt_via_not_reference import PTViaNotReference
        from ..models.pt_via_reference import PTViaReference
        from ..models.trip_mobility_filter import TripMobilityFilter

        d = src_dict.copy()
        origin = d.pop("origin")

        destination = d.pop("destination")

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.date]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()

        time = d.pop("time", UNSET)

        _occupancy_average = d.pop("occupancyAverage", UNSET)
        occupancy_average: Union[Unset, OccupancyAverageEnum]
        if isinstance(_occupancy_average, Unset):
            occupancy_average = UNSET
        else:
            occupancy_average = OccupancyAverageEnum(_occupancy_average)

        _mobility_filter = d.pop("mobilityFilter", UNSET)
        mobility_filter: Union[Unset, TripMobilityFilter]
        if isinstance(_mobility_filter, Unset):
            mobility_filter = UNSET
        else:
            mobility_filter = TripMobilityFilter.from_dict(_mobility_filter)

        vias = []
        _vias = d.pop("vias", UNSET)
        for vias_item_data in _vias or []:
            vias_item = PTViaReference.from_dict(vias_item_data)

            vias.append(vias_item)

        vias_not = []
        _vias_not = d.pop("viasNot", UNSET)
        for vias_not_item_data in _vias_not or []:
            vias_not_item = PTViaNotReference.from_dict(vias_not_item_data)

            vias_not.append(vias_not_item)

        vias_no_transfer = []
        _vias_no_transfer = d.pop("viasNoTransfer", UNSET)
        for vias_no_transfer_item_data in _vias_no_transfer or []:
            vias_no_transfer_item = PTViaNoChangeAtReference.from_dict(vias_no_transfer_item_data)

            vias_no_transfer.append(vias_no_transfer_item)

        _realtime_mode = d.pop("realtimeMode", UNSET)
        realtime_mode: Union[Unset, RealtimeModeEnum]
        if isinstance(_realtime_mode, Unset):
            realtime_mode = UNSET
        else:
            realtime_mode = RealtimeModeEnum(_realtime_mode)

        paging_cursor = d.pop("pagingCursor", UNSET)

        limit = d.pop("limit", UNSET)

        duration = d.pop("duration", UNSET)

        _include_accessibility = d.pop("includeAccessibility", UNSET)
        include_accessibility: Union[Unset, AccessibilityEnum]
        if isinstance(_include_accessibility, Unset):
            include_accessibility = UNSET
        else:
            include_accessibility = AccessibilityEnum(_include_accessibility)

        _include_alternate_match = d.pop("includeAlternateMatch", UNSET)
        include_alternate_match: Union[Unset, AlternateMatchEnum]
        if isinstance(_include_alternate_match, Unset):
            include_alternate_match = UNSET
        else:
            include_alternate_match = AlternateMatchEnum(_include_alternate_match)

        include_notice_attributes = []
        _include_notice_attributes = d.pop("includeNoticeAttributes", UNSET)
        for include_notice_attributes_item_data in _include_notice_attributes or []:
            include_notice_attributes_item = NoticeAttributeEnum(include_notice_attributes_item_data)

            include_notice_attributes.append(include_notice_attributes_item)

        include_transport_modes = []
        _include_transport_modes = d.pop("includeTransportModes", UNSET)
        for include_transport_modes_item_data in _include_transport_modes or []:
            include_transport_modes_item = TransportModeEnum(include_transport_modes_item_data)

            include_transport_modes.append(include_transport_modes_item)

        include_summary = d.pop("includeSummary", UNSET)

        _include_intermediate_stops = d.pop("includeIntermediateStops", UNSET)
        include_intermediate_stops: Union[Unset, TripsIntervalByOriginAndDestinationRequestBodyIncludeIntermediateStops]
        if isinstance(_include_intermediate_stops, Unset):
            include_intermediate_stops = UNSET
        else:
            include_intermediate_stops = TripsIntervalByOriginAndDestinationRequestBodyIncludeIntermediateStops(
                _include_intermediate_stops
            )

        trips_interval_by_origin_and_destination_request_body = cls(
            origin=origin,
            destination=destination,
            date=date,
            time=time,
            occupancy_average=occupancy_average,
            mobility_filter=mobility_filter,
            vias=vias,
            vias_not=vias_not,
            vias_no_transfer=vias_no_transfer,
            realtime_mode=realtime_mode,
            paging_cursor=paging_cursor,
            limit=limit,
            duration=duration,
            include_accessibility=include_accessibility,
            include_alternate_match=include_alternate_match,
            include_notice_attributes=include_notice_attributes,
            include_transport_modes=include_transport_modes,
            include_summary=include_summary,
            include_intermediate_stops=include_intermediate_stops,
        )

        trips_interval_by_origin_and_destination_request_body.additional_properties = d
        return trips_interval_by_origin_and_destination_request_body

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
