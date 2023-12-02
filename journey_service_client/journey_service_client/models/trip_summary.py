from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.accessibility_boarding_alighting import AccessibilityBoardingAlighting
    from ..models.scheduled_stop_point import ScheduledStopPoint


T = TypeVar("T", bound="TripSummary")


@_attrs_define
class TripSummary:
    """Summary of most relevant aspects of the given Trip and its PTRideLeg's. (Aka OJP TripSummaryStructure.)

    Attributes:
        service_products (List[str]):
        first_stop_place (Union[Unset, ScheduledStopPoint]): Passenger relevant stop-point on a `ServiceJourney`. Some
            properties may further by distinguished on either `arrival` and/or `departure StopCall` aspects.
        last_stop_place (Union[Unset, ScheduledStopPoint]): Passenger relevant stop-point on a `ServiceJourney`. Some
            properties may further by distinguished on either `arrival` and/or `departure StopCall` aspects.
        occupancy_first_class_max (Union[Unset, str]): Highest occupancyAverage on any PTRideLeg::origin in 1st
            class.<br>x-extensible-enum: [UNKNOWN,LOW,MEDIUM,HIGH]
        occupancy_second_class_max (Union[Unset, str]): Highest occupancy on any PTRideLeg::origin in 2nd
            class.<br>x-extensible-enum: [UNKNOWN,LOW,MEDIUM,HIGH]
        boarding_alighting_accessibility (Union[Unset, str]): @Deprecated use `accessibilityBoardingAlighting` instead
            to get NO_HINT as well!<br>x-extensible-enum: [BOARDING_ALIGHTING_SELF,BOARDING_ALIGHTING_BY_CREW,BOARDING_ALIGH
            TING_BY_NOTIFICATION,BOARDING_ALIGHTING_NOT_POSSIBLE]
        accessibility_boarding_alighting (Union[Unset, AccessibilityBoardingAlighting]): Hint for handicaped people at a
            StopPlace to board or alight a Vehicle on a PTRideLeg. Relates to `forBoarding` and `forAlighting`.
    """

    service_products: List[str]
    first_stop_place: Union[Unset, "ScheduledStopPoint"] = UNSET
    last_stop_place: Union[Unset, "ScheduledStopPoint"] = UNSET
    occupancy_first_class_max: Union[Unset, str] = UNSET
    occupancy_second_class_max: Union[Unset, str] = UNSET
    boarding_alighting_accessibility: Union[Unset, str] = UNSET
    accessibility_boarding_alighting: Union[Unset, "AccessibilityBoardingAlighting"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        service_products = self.service_products

        first_stop_place: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.first_stop_place, Unset):
            first_stop_place = self.first_stop_place.to_dict()

        last_stop_place: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.last_stop_place, Unset):
            last_stop_place = self.last_stop_place.to_dict()

        occupancy_first_class_max = self.occupancy_first_class_max
        occupancy_second_class_max = self.occupancy_second_class_max
        boarding_alighting_accessibility = self.boarding_alighting_accessibility
        accessibility_boarding_alighting: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.accessibility_boarding_alighting, Unset):
            accessibility_boarding_alighting = self.accessibility_boarding_alighting.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "serviceProducts": service_products,
            }
        )
        if first_stop_place is not UNSET:
            field_dict["firstStopPlace"] = first_stop_place
        if last_stop_place is not UNSET:
            field_dict["lastStopPlace"] = last_stop_place
        if occupancy_first_class_max is not UNSET:
            field_dict["occupancyFirstClassMax"] = occupancy_first_class_max
        if occupancy_second_class_max is not UNSET:
            field_dict["occupancySecondClassMax"] = occupancy_second_class_max
        if boarding_alighting_accessibility is not UNSET:
            field_dict["boardingAlightingAccessibility"] = boarding_alighting_accessibility
        if accessibility_boarding_alighting is not UNSET:
            field_dict["accessibilityBoardingAlighting"] = accessibility_boarding_alighting

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.accessibility_boarding_alighting import AccessibilityBoardingAlighting
        from ..models.scheduled_stop_point import ScheduledStopPoint

        d = src_dict.copy()
        service_products = cast(List[str], d.pop("serviceProducts"))

        _first_stop_place = d.pop("firstStopPlace", UNSET)
        first_stop_place: Union[Unset, ScheduledStopPoint]
        if isinstance(_first_stop_place, Unset):
            first_stop_place = UNSET
        else:
            first_stop_place = ScheduledStopPoint.from_dict(_first_stop_place)

        _last_stop_place = d.pop("lastStopPlace", UNSET)
        last_stop_place: Union[Unset, ScheduledStopPoint]
        if isinstance(_last_stop_place, Unset):
            last_stop_place = UNSET
        else:
            last_stop_place = ScheduledStopPoint.from_dict(_last_stop_place)

        occupancy_first_class_max = d.pop("occupancyFirstClassMax", UNSET)

        occupancy_second_class_max = d.pop("occupancySecondClassMax", UNSET)

        boarding_alighting_accessibility = d.pop("boardingAlightingAccessibility", UNSET)

        _accessibility_boarding_alighting = d.pop("accessibilityBoardingAlighting", UNSET)
        accessibility_boarding_alighting: Union[Unset, AccessibilityBoardingAlighting]
        if isinstance(_accessibility_boarding_alighting, Unset):
            accessibility_boarding_alighting = UNSET
        else:
            accessibility_boarding_alighting = AccessibilityBoardingAlighting.from_dict(
                _accessibility_boarding_alighting
            )

        trip_summary = cls(
            service_products=service_products,
            first_stop_place=first_stop_place,
            last_stop_place=last_stop_place,
            occupancy_first_class_max=occupancy_first_class_max,
            occupancy_second_class_max=occupancy_second_class_max,
            boarding_alighting_accessibility=boarding_alighting_accessibility,
            accessibility_boarding_alighting=accessibility_boarding_alighting,
        )

        trip_summary.additional_properties = d
        return trip_summary

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
