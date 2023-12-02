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
from ..models.train_stop_assignments_enum import TrainStopAssignmentsEnum
from ..models.transport_mode_enum import TransportModeEnum
from ..models.trips_by_origin_and_destination_request_body_include_ecology_comparison import (
    TripsByOriginAndDestinationRequestBodyIncludeEcologyComparison,
)
from ..models.trips_by_origin_and_destination_request_body_include_intermediate_stops import (
    TripsByOriginAndDestinationRequestBodyIncludeIntermediateStops,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dated_vehicle_journey_reference import DatedVehicleJourneyReference
    from ..models.optimisation_method import OptimisationMethod
    from ..models.pt_via_no_change_at_reference import PTViaNoChangeAtReference
    from ..models.pt_via_not_reference import PTViaNotReference
    from ..models.pt_via_reference import PTViaReference
    from ..models.trip_mobility_filter import TripMobilityFilter


T = TypeVar("T", bound="TripsByOriginAndDestinationRequestBody")


@_attrs_define
class TripsByOriginAndDestinationRequestBody:
    """Request parameters (POST body). OJP passive instance requires Stop UIC like '850700' whereas active instance
    enforces 'OJP:STOP:SBB:8507000|Bern'.

        Attributes:
            origin (str): Starting point of the trip at origin (departure). See v3 **PlaceReference** in [complex
                parameter](https://github.com/SchweizerischeBundesbahnen/journey-service/blob/master/JSON-Objects.md) Example:
                8503000.
            destination (str): Ending point of the trip at destination (arrival). See **PlaceReference** in [complex
                parameter](https://github.com/SchweizerischeBundesbahnen/journey-service/blob/master/JSON-Objects.md) Example:
                [7.435194,46.945679].
            origin_radius (Union[Unset, int]): Tolerated walk distance (radius [m]) at `Place` origin (departure). Default
                is 1500 Example: 800.
            destination_radius (Union[Unset, int]): Tolerated walk distance (radius [m]) at `Place` destination (arrival).
                Default is 1500 Example: 1500.
            for_arrival (Union[Unset, bool]): Search for arriving (true) or departing (false) trips.
            date (Union[Unset, datetime.date]): (Local) date at either origin (`forArrival`=false) or destination
                (`forArrival`=true) related to `time`, defaults to TODAY. Example: 2023-04-18.
            time (Union[Unset, str]): Local time at either origin (`forArrival`=false) or destination (`forArrival`=true)
                related to `date`, defaults to NOW (seconds will be ignored). Example: 13:07.
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
            optimisation_method (Union[Unset, OptimisationMethod]): Configure the search algorithm influencing Trip search
                results.
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
            include_economic (Union[Unset, bool]): Consider additional connections by Bus or S-Bahn leading to destination
                as well (de:'Zusätzliche Alternativverbindungen', 'Mehrdimensionale Suche', 'Preiswerte Suche').<br>This
                parameter has an impact on performance and/or response volume, set wisely!
            include_unsharp (Union[Unset, bool]): Consider alternative stations origin/destination (de: Erweiterte Anzeige).
            include_earlier (Union[Unset, bool]): Consider earlier leaving connections, even if arrival is later.
            include_ecology_comparison (Union[Unset, TripsByOriginAndDestinationRequestBodyIncludeEcologyComparison]):
                Create Trip::EcoBalance (C02, ..) per Trip. DEFAULT is based on SBB default car eco-params.<br>x-extensible-
                enum:  Default: TripsByOriginAndDestinationRequestBodyIncludeEcologyComparison.NONE.
            include_transport_modes (Union[Unset, List[TransportModeEnum]]):
            include_operating_days (Union[Unset, bool]): `Trip::operatingPeriods` will always be returned if it is a
                **repeatable planned Trip over the period**. To enforce concrete planned dates in
                `OperatingPeriod::operatingDays`set `includeOperatingDays=true` (PTRideLeg::serviceJourney::operationPeriods
                will remain empty, because whole Trip is of interest).<br>This parameter has an impact on performance and/or
                response volume, set wisely!
            include_route_projection (Union[Unset, bool]): With or without a plottable polyline for each vehicle-journey (if
                available).<br>This parameter has an impact on performance and/or response volume, set wisely!
            include_group_reservation (Union[Unset, str]): Relates to `PTRideLeg::groupReservationStatus`. Include the
                status for group-reservation possibilities (source CAPRE).<br>Format 'x:y' which means to check reservation
                status for number of x passenger in first class and y passengers in second class.<br>Needs specific GRANT
                rights, do not specify unless you have them!<br>This parameter has an impact on performance and/or response
                volume, set wisely! `ServiceJourney::notices` will get an entry of `type=INFO, key=RN` if available, its
                `Notice::value` is relevant for Postauto AG (PAG) operations-reference. Example: 5:7.
            include_summary (Union[Unset, bool]): Create some summary facts about each Trip (useful for UI
                overviews).<br>This parameter has an impact on performance and/or response volume, set wisely!
            include_intermediate_stops (Union[Unset, TripsByOriginAndDestinationRequestBodyIncludeIntermediateStops]):
                Whether the `PTRideLeg's` should include intermediate stops (between the passenger's board and alight in
                `ServiceJourney::stopPoints`).<br>x-extensible-enum:  [ALL,NONE,BOARDING_ALIGHTING] where ALL is
                BOARDING_ALIGHTING plus virtual stops. Default:
                TripsByOriginAndDestinationRequestBodyIncludeIntermediateStops.ALL.
            include_train_stop_assignments (Union[Unset, TrainStopAssignmentsEnum]): Whether `PTRideLeg's` should include
                `CompoundTrain's`(aka formation, composition). However, `CompoundTrain's` at any `ScheduledStopPoint` on the
                `ServiceJourney` may be loaded separately by `/v3/vehicle-journeys/by-stoppoints`.
                Possible values:
                - NONE none at all, though a `PTRideLeg::trainStopAssignmentHint` is always given.
                - ORIGIN  `TrainStopAssignment's` are added to first (departure) `ScheduledStopPoint` of each `PTRideLeg`
                - ORIGIN_DESTINATION `TrainStopAssignment's` are added to first (departure) and last (arrival)
                `ScheduledStopPoint` of each `PTRideLeg` having a `TrainStopAssignment` resp. a `CompoundTrain`. Default:
                TrainStopAssignmentsEnum.NONE.
            exclude_dated_vehicle_journeys (Union[Unset, List['DatedVehicleJourneyReference']]):
            exclude_footpath_at_origin_and_destination (Union[Unset, bool]): In case of `StopPlace` to `StopPlace` at origin
                and/or destination set true to prevent `AccessLeg's` at beginning or end.
    """

    origin: str
    destination: str
    origin_radius: Union[Unset, int] = UNSET
    destination_radius: Union[Unset, int] = UNSET
    for_arrival: Union[Unset, bool] = False
    date: Union[Unset, datetime.date] = UNSET
    time: Union[Unset, str] = UNSET
    occupancy_average: Union[Unset, OccupancyAverageEnum] = OccupancyAverageEnum.ALL
    mobility_filter: Union[Unset, "TripMobilityFilter"] = UNSET
    vias: Union[Unset, List["PTViaReference"]] = UNSET
    vias_not: Union[Unset, List["PTViaNotReference"]] = UNSET
    vias_no_transfer: Union[Unset, List["PTViaNoChangeAtReference"]] = UNSET
    realtime_mode: Union[Unset, RealtimeModeEnum] = RealtimeModeEnum.REALTIME
    paging_cursor: Union[Unset, str] = UNSET
    optimisation_method: Union[Unset, "OptimisationMethod"] = UNSET
    include_accessibility: Union[Unset, AccessibilityEnum] = AccessibilityEnum.ALL
    include_alternate_match: Union[Unset, AlternateMatchEnum] = AlternateMatchEnum.IRRELEVANT
    include_notice_attributes: Union[Unset, List[NoticeAttributeEnum]] = UNSET
    include_economic: Union[Unset, bool] = False
    include_unsharp: Union[Unset, bool] = False
    include_earlier: Union[Unset, bool] = False
    include_ecology_comparison: Union[
        Unset, TripsByOriginAndDestinationRequestBodyIncludeEcologyComparison
    ] = TripsByOriginAndDestinationRequestBodyIncludeEcologyComparison.NONE
    include_transport_modes: Union[Unset, List[TransportModeEnum]] = UNSET
    include_operating_days: Union[Unset, bool] = False
    include_route_projection: Union[Unset, bool] = False
    include_group_reservation: Union[Unset, str] = UNSET
    include_summary: Union[Unset, bool] = False
    include_intermediate_stops: Union[
        Unset, TripsByOriginAndDestinationRequestBodyIncludeIntermediateStops
    ] = TripsByOriginAndDestinationRequestBodyIncludeIntermediateStops.ALL
    include_train_stop_assignments: Union[Unset, TrainStopAssignmentsEnum] = TrainStopAssignmentsEnum.NONE
    exclude_dated_vehicle_journeys: Union[Unset, List["DatedVehicleJourneyReference"]] = UNSET
    exclude_footpath_at_origin_and_destination: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        origin = self.origin
        destination = self.destination
        origin_radius = self.origin_radius
        destination_radius = self.destination_radius
        for_arrival = self.for_arrival
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
        optimisation_method: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.optimisation_method, Unset):
            optimisation_method = self.optimisation_method.to_dict()

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

        include_economic = self.include_economic
        include_unsharp = self.include_unsharp
        include_earlier = self.include_earlier
        include_ecology_comparison: Union[Unset, str] = UNSET
        if not isinstance(self.include_ecology_comparison, Unset):
            include_ecology_comparison = self.include_ecology_comparison.value

        include_transport_modes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.include_transport_modes, Unset):
            include_transport_modes = []
            for include_transport_modes_item_data in self.include_transport_modes:
                include_transport_modes_item = include_transport_modes_item_data.value

                include_transport_modes.append(include_transport_modes_item)

        include_operating_days = self.include_operating_days
        include_route_projection = self.include_route_projection
        include_group_reservation = self.include_group_reservation
        include_summary = self.include_summary
        include_intermediate_stops: Union[Unset, str] = UNSET
        if not isinstance(self.include_intermediate_stops, Unset):
            include_intermediate_stops = self.include_intermediate_stops.value

        include_train_stop_assignments: Union[Unset, str] = UNSET
        if not isinstance(self.include_train_stop_assignments, Unset):
            include_train_stop_assignments = self.include_train_stop_assignments.value

        exclude_dated_vehicle_journeys: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.exclude_dated_vehicle_journeys, Unset):
            exclude_dated_vehicle_journeys = []
            for exclude_dated_vehicle_journeys_item_data in self.exclude_dated_vehicle_journeys:
                exclude_dated_vehicle_journeys_item = exclude_dated_vehicle_journeys_item_data.to_dict()

                exclude_dated_vehicle_journeys.append(exclude_dated_vehicle_journeys_item)

        exclude_footpath_at_origin_and_destination = self.exclude_footpath_at_origin_and_destination

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "origin": origin,
                "destination": destination,
            }
        )
        if origin_radius is not UNSET:
            field_dict["originRadius"] = origin_radius
        if destination_radius is not UNSET:
            field_dict["destinationRadius"] = destination_radius
        if for_arrival is not UNSET:
            field_dict["forArrival"] = for_arrival
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
        if optimisation_method is not UNSET:
            field_dict["optimisationMethod"] = optimisation_method
        if include_accessibility is not UNSET:
            field_dict["includeAccessibility"] = include_accessibility
        if include_alternate_match is not UNSET:
            field_dict["includeAlternateMatch"] = include_alternate_match
        if include_notice_attributes is not UNSET:
            field_dict["includeNoticeAttributes"] = include_notice_attributes
        if include_economic is not UNSET:
            field_dict["includeEconomic"] = include_economic
        if include_unsharp is not UNSET:
            field_dict["includeUnsharp"] = include_unsharp
        if include_earlier is not UNSET:
            field_dict["includeEarlier"] = include_earlier
        if include_ecology_comparison is not UNSET:
            field_dict["includeEcologyComparison"] = include_ecology_comparison
        if include_transport_modes is not UNSET:
            field_dict["includeTransportModes"] = include_transport_modes
        if include_operating_days is not UNSET:
            field_dict["includeOperatingDays"] = include_operating_days
        if include_route_projection is not UNSET:
            field_dict["includeRouteProjection"] = include_route_projection
        if include_group_reservation is not UNSET:
            field_dict["includeGroupReservation"] = include_group_reservation
        if include_summary is not UNSET:
            field_dict["includeSummary"] = include_summary
        if include_intermediate_stops is not UNSET:
            field_dict["includeIntermediateStops"] = include_intermediate_stops
        if include_train_stop_assignments is not UNSET:
            field_dict["includeTrainStopAssignments"] = include_train_stop_assignments
        if exclude_dated_vehicle_journeys is not UNSET:
            field_dict["excludeDatedVehicleJourneys"] = exclude_dated_vehicle_journeys
        if exclude_footpath_at_origin_and_destination is not UNSET:
            field_dict["excludeFootpathAtOriginAndDestination"] = exclude_footpath_at_origin_and_destination

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dated_vehicle_journey_reference import DatedVehicleJourneyReference
        from ..models.optimisation_method import OptimisationMethod
        from ..models.pt_via_no_change_at_reference import PTViaNoChangeAtReference
        from ..models.pt_via_not_reference import PTViaNotReference
        from ..models.pt_via_reference import PTViaReference
        from ..models.trip_mobility_filter import TripMobilityFilter

        d = src_dict.copy()
        origin = d.pop("origin")

        destination = d.pop("destination")

        origin_radius = d.pop("originRadius", UNSET)

        destination_radius = d.pop("destinationRadius", UNSET)

        for_arrival = d.pop("forArrival", UNSET)

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

        _optimisation_method = d.pop("optimisationMethod", UNSET)
        optimisation_method: Union[Unset, OptimisationMethod]
        if isinstance(_optimisation_method, Unset):
            optimisation_method = UNSET
        else:
            optimisation_method = OptimisationMethod.from_dict(_optimisation_method)

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

        include_economic = d.pop("includeEconomic", UNSET)

        include_unsharp = d.pop("includeUnsharp", UNSET)

        include_earlier = d.pop("includeEarlier", UNSET)

        _include_ecology_comparison = d.pop("includeEcologyComparison", UNSET)
        include_ecology_comparison: Union[Unset, TripsByOriginAndDestinationRequestBodyIncludeEcologyComparison]
        if isinstance(_include_ecology_comparison, Unset):
            include_ecology_comparison = UNSET
        else:
            include_ecology_comparison = TripsByOriginAndDestinationRequestBodyIncludeEcologyComparison(
                _include_ecology_comparison
            )

        include_transport_modes = []
        _include_transport_modes = d.pop("includeTransportModes", UNSET)
        for include_transport_modes_item_data in _include_transport_modes or []:
            include_transport_modes_item = TransportModeEnum(include_transport_modes_item_data)

            include_transport_modes.append(include_transport_modes_item)

        include_operating_days = d.pop("includeOperatingDays", UNSET)

        include_route_projection = d.pop("includeRouteProjection", UNSET)

        include_group_reservation = d.pop("includeGroupReservation", UNSET)

        include_summary = d.pop("includeSummary", UNSET)

        _include_intermediate_stops = d.pop("includeIntermediateStops", UNSET)
        include_intermediate_stops: Union[Unset, TripsByOriginAndDestinationRequestBodyIncludeIntermediateStops]
        if isinstance(_include_intermediate_stops, Unset):
            include_intermediate_stops = UNSET
        else:
            include_intermediate_stops = TripsByOriginAndDestinationRequestBodyIncludeIntermediateStops(
                _include_intermediate_stops
            )

        _include_train_stop_assignments = d.pop("includeTrainStopAssignments", UNSET)
        include_train_stop_assignments: Union[Unset, TrainStopAssignmentsEnum]
        if isinstance(_include_train_stop_assignments, Unset):
            include_train_stop_assignments = UNSET
        else:
            include_train_stop_assignments = TrainStopAssignmentsEnum(_include_train_stop_assignments)

        exclude_dated_vehicle_journeys = []
        _exclude_dated_vehicle_journeys = d.pop("excludeDatedVehicleJourneys", UNSET)
        for exclude_dated_vehicle_journeys_item_data in _exclude_dated_vehicle_journeys or []:
            exclude_dated_vehicle_journeys_item = DatedVehicleJourneyReference.from_dict(
                exclude_dated_vehicle_journeys_item_data
            )

            exclude_dated_vehicle_journeys.append(exclude_dated_vehicle_journeys_item)

        exclude_footpath_at_origin_and_destination = d.pop("excludeFootpathAtOriginAndDestination", UNSET)

        trips_by_origin_and_destination_request_body = cls(
            origin=origin,
            destination=destination,
            origin_radius=origin_radius,
            destination_radius=destination_radius,
            for_arrival=for_arrival,
            date=date,
            time=time,
            occupancy_average=occupancy_average,
            mobility_filter=mobility_filter,
            vias=vias,
            vias_not=vias_not,
            vias_no_transfer=vias_no_transfer,
            realtime_mode=realtime_mode,
            paging_cursor=paging_cursor,
            optimisation_method=optimisation_method,
            include_accessibility=include_accessibility,
            include_alternate_match=include_alternate_match,
            include_notice_attributes=include_notice_attributes,
            include_economic=include_economic,
            include_unsharp=include_unsharp,
            include_earlier=include_earlier,
            include_ecology_comparison=include_ecology_comparison,
            include_transport_modes=include_transport_modes,
            include_operating_days=include_operating_days,
            include_route_projection=include_route_projection,
            include_group_reservation=include_group_reservation,
            include_summary=include_summary,
            include_intermediate_stops=include_intermediate_stops,
            include_train_stop_assignments=include_train_stop_assignments,
            exclude_dated_vehicle_journeys=exclude_dated_vehicle_journeys,
            exclude_footpath_at_origin_and_destination=exclude_footpath_at_origin_and_destination,
        )

        trips_by_origin_and_destination_request_body.additional_properties = d
        return trips_by_origin_and_destination_request_body

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
