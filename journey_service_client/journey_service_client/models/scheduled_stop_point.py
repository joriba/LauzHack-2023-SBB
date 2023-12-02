from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.accessibility_boarding_alighting import AccessibilityBoardingAlighting
    from ..models.stop_call import StopCall
    from ..models.stop_place import StopPlace


T = TypeVar("T", bound="ScheduledStopPoint")


@_attrs_define
class ScheduledStopPoint:
    """Passenger relevant stop-point on a `ServiceJourney`. Some properties may further by distinguished on either
    `arrival` and/or `departure StopCall` aspects.

        Attributes:
            place (StopPlace): A place (de:Haltestelle) comprising one or more areas where vehicles may stop and where
                passengers may board or leave vehicles or prepare their trip. The name is given in regional language
                only.<br>Inherited from `Place`.
            for_boarding (bool): Boarding (de:einsteigen) at a StopPlace on a PTRide;. Relates to **`departure`**,
                `stopStatus` and `accessibilityBoardingAlighting`, see [Routing-
                Basics](https://github.com/SchweizerischeBundesbahnen/journey-service/blob/master/RoutingBasics.md).
            for_alighting (bool): Alighting (de:aussteigen) at a StopPlace on a PTRide. Relates to **`arrival`**,
                `stopStatus` and `accessibilityBoardingAlighting`, see [Routing-
                Basics](https://github.com/SchweizerischeBundesbahnen/journey-service/blob/master/RoutingBasics.md).
            request_stop (bool): Passenger needs to call for a vehicle stop (aka OJP `RequestStop`, resp. de:Halt auf
                Verlangen).
            delay_undefined (bool): true: After a very long delay at either `arrival` or `departure` (also see related
                `StopCall::delayText`), according to SBB business rules. Typically blocks the whole journey or at least the
                ending part of a journey (like locomotive break at 3rd stop until the very last stop).
            occupancy_first_class (str): Occupancy in 1st class (average) at StopPlace on a PTRideLeg.<br>x-extensible-enum:
                [UNKNOWN,LOW,MEDIUM,HIGH]
            occupancy_second_class (str): Occupancy in 2nd class (average) at StopPlace on a PTRideLeg.<br>x-extensible-
                enum: [UNKNOWN,LOW,MEDIUM,HIGH]
            accessibility_boarding_alighting (Union[Unset, AccessibilityBoardingAlighting]): Hint for handicaped people at a
                StopPlace to board or alight a Vehicle on a PTRideLeg. Relates to `forBoarding` and `forAlighting`.
            stop_status (Union[Unset, str]): Status at ScheduledStopPlace on a PTRide.This is is useful when iterating from
                stop to stop getting appropriate state symbols (de:Perlenschnur), see [Routing-
                Basics](https://github.com/SchweizerischeBundesbahnen/journey-
                service/blob/master/RoutingBasics.md).<br>x-extensible-enum:
                [PLANNED,CANCELLED,BEGIN_PARTIAL_CANCELLATION,END_PARTIAL_CANCELLATION,NOT_SERVICED,UNPLANNED]
            stop_status_formatted (Union[Unset, str]): Speakable description about related `stopStatus` enum, if any.
            arrival (Union[Unset, StopCall]): Passing a `ScheduledStopPoint` on a `ServiceJourney` may have two 'views': one
                for arrival and one for departure aspects (aka OJP LegAlight::StopPoint, LegBoard::StopPoint; NeTeX Call (which
                is a VIEW on a `ScheduledStopPoint`).
            departure (Union[Unset, StopCall]): Passing a `ScheduledStopPoint` on a `ServiceJourney` may have two 'views':
                one for arrival and one for departure aspects (aka OJP LegAlight::StopPoint, LegBoard::StopPoint; NeTeX Call
                (which is a VIEW on a `ScheduledStopPoint`).
            route_index (Union[Unset, int]): Route index on this `ServiceJourney` (aka OJP order). Usually starting from 0
                or 1 and incrementing by 1. However if the route index value jumps:
                 - it is most likely that the journey was rerouted
                 - or being a virtual Stop
            exit_side (Union[Unset, str]): Exit side at this stop in direction of journey (null if unknown or irrelevant for
                e.g. in a Bus or on a Bicycle).<br>x-extensible-enum: [LEFT,RIGHT] Example: LEFT.
            rank (Union[Unset, int]): Rank of importance based on intermediate ScheduledStopPoint priority and distance
                within a (partial) ServiceJourney. SBB KI rule based on display-info to find relevant intermediate stops to
                present on a visual stationboard (de:Perronanzeiger).Origin and destination of departure/arrival have always
                rank=null. Depends on /v3/departures or /v3/arrivals includeRank=true
    """

    place: "StopPlace"
    for_boarding: bool
    for_alighting: bool
    occupancy_first_class: str
    occupancy_second_class: str
    request_stop: bool = False
    delay_undefined: bool = False
    accessibility_boarding_alighting: Union[Unset, "AccessibilityBoardingAlighting"] = UNSET
    stop_status: Union[Unset, str] = UNSET
    stop_status_formatted: Union[Unset, str] = UNSET
    arrival: Union[Unset, "StopCall"] = UNSET
    departure: Union[Unset, "StopCall"] = UNSET
    route_index: Union[Unset, int] = UNSET
    exit_side: Union[Unset, str] = UNSET
    rank: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        place = self.place.to_dict()

        for_boarding = self.for_boarding
        for_alighting = self.for_alighting
        request_stop = self.request_stop
        delay_undefined = self.delay_undefined
        occupancy_first_class = self.occupancy_first_class
        occupancy_second_class = self.occupancy_second_class
        accessibility_boarding_alighting: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.accessibility_boarding_alighting, Unset):
            accessibility_boarding_alighting = self.accessibility_boarding_alighting.to_dict()

        stop_status = self.stop_status
        stop_status_formatted = self.stop_status_formatted
        arrival: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.arrival, Unset):
            arrival = self.arrival.to_dict()

        departure: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.departure, Unset):
            departure = self.departure.to_dict()

        route_index = self.route_index
        exit_side = self.exit_side
        rank = self.rank

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "place": place,
                "forBoarding": for_boarding,
                "forAlighting": for_alighting,
                "requestStop": request_stop,
                "delayUndefined": delay_undefined,
                "occupancyFirstClass": occupancy_first_class,
                "occupancySecondClass": occupancy_second_class,
            }
        )
        if accessibility_boarding_alighting is not UNSET:
            field_dict["accessibilityBoardingAlighting"] = accessibility_boarding_alighting
        if stop_status is not UNSET:
            field_dict["stopStatus"] = stop_status
        if stop_status_formatted is not UNSET:
            field_dict["stopStatusFormatted"] = stop_status_formatted
        if arrival is not UNSET:
            field_dict["arrival"] = arrival
        if departure is not UNSET:
            field_dict["departure"] = departure
        if route_index is not UNSET:
            field_dict["routeIndex"] = route_index
        if exit_side is not UNSET:
            field_dict["exitSide"] = exit_side
        if rank is not UNSET:
            field_dict["rank"] = rank

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.accessibility_boarding_alighting import AccessibilityBoardingAlighting
        from ..models.stop_call import StopCall
        from ..models.stop_place import StopPlace

        d = src_dict.copy()
        place = StopPlace.from_dict(d.pop("place"))

        for_boarding = d.pop("forBoarding")

        for_alighting = d.pop("forAlighting")

        request_stop = d.pop("requestStop")

        delay_undefined = d.pop("delayUndefined")

        occupancy_first_class = d.pop("occupancyFirstClass")

        occupancy_second_class = d.pop("occupancySecondClass")

        _accessibility_boarding_alighting = d.pop("accessibilityBoardingAlighting", UNSET)
        accessibility_boarding_alighting: Union[Unset, AccessibilityBoardingAlighting]
        if isinstance(_accessibility_boarding_alighting, Unset):
            accessibility_boarding_alighting = UNSET
        else:
            accessibility_boarding_alighting = AccessibilityBoardingAlighting.from_dict(
                _accessibility_boarding_alighting
            )

        stop_status = d.pop("stopStatus", UNSET)

        stop_status_formatted = d.pop("stopStatusFormatted", UNSET)

        _arrival = d.pop("arrival", UNSET)
        arrival: Union[Unset, StopCall]
        if isinstance(_arrival, Unset):
            arrival = UNSET
        else:
            arrival = StopCall.from_dict(_arrival)

        _departure = d.pop("departure", UNSET)
        departure: Union[Unset, StopCall]
        if isinstance(_departure, Unset):
            departure = UNSET
        else:
            departure = StopCall.from_dict(_departure)

        route_index = d.pop("routeIndex", UNSET)

        exit_side = d.pop("exitSide", UNSET)

        rank = d.pop("rank", UNSET)

        scheduled_stop_point = cls(
            place=place,
            for_boarding=for_boarding,
            for_alighting=for_alighting,
            request_stop=request_stop,
            delay_undefined=delay_undefined,
            occupancy_first_class=occupancy_first_class,
            occupancy_second_class=occupancy_second_class,
            accessibility_boarding_alighting=accessibility_boarding_alighting,
            stop_status=stop_status,
            stop_status_formatted=stop_status_formatted,
            arrival=arrival,
            departure=departure,
            route_index=route_index,
            exit_side=exit_side,
            rank=rank,
        )

        scheduled_stop_point.additional_properties = d
        return scheduled_stop_point

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
