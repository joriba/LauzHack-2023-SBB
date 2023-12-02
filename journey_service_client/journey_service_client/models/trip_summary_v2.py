from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.trip_summary_v2_max_occupancy_first_class import TripSummaryV2MaxOccupancyFirstClass
from ..models.trip_summary_v2_max_occupancy_second_class import TripSummaryV2MaxOccupancySecondClass
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.him_summary import HimSummary
    from ..models.stop_v2 import StopV2
    from ..models.trip_summary_v2_infos_rt import TripSummaryV2InfosRt


T = TypeVar("T", bound="TripSummaryV2")


@_attrs_define
class TripSummaryV2:
    """Most important facts of a Trip (useful for a quick overview).

    Attributes:
        origin (StopV2): A stop represents a specific location (typically a STATION) of a leg or a complete journey-
            detail of a transport-product (aka v3.ScheduledStopPoint, OJP StopPoint).
        destination (StopV2): A stop represents a specific location (typically a STATION) of a leg or a complete
            journey-detail of a transport-product (aka v3.ScheduledStopPoint, OJP StopPoint).
        origin_first_station (StopV2): A stop represents a specific location (typically a STATION) of a leg or a
            complete journey-detail of a transport-product (aka v3.ScheduledStopPoint, OJP StopPoint).
        destination_last_station (StopV2): A stop represents a specific location (typically a STATION) of a leg or a
            complete journey-detail of a transport-product (aka v3.ScheduledStopPoint, OJP StopPoint).
        transport_products (List[str]):
        max_occupancy_first_class (TripSummaryV2MaxOccupancyFirstClass): Highest occupancyAverage on any Leg::origin in
            1st class over all PTRideLeg's.
        max_occupancy_second_class (TripSummaryV2MaxOccupancySecondClass): Highest occupancy on any Leg::origin in 2nd
            class.
        cancelled (bool): de:Ausfall
        partially_cancelled (bool): de:Teilausfall
        not_serviced_stop (bool): Contains a `StopV2` which is not serviced (de:ausserordentliche Durchfahrt).
        platform_changed (bool): de:Gleisänderung
        delayed (bool): de:Verspätung
        reachable (bool): de:Anschluss gehalten
        additional_ride (bool): @Deprecated use TripV2::isAlternative
        unplanned_stop (bool): de:Zusätzlicher Halt
        unknown_delayed (bool): de:Unbestimmte Verspätung
        infos_rt (TripSummaryV2InfosRt): @Deprecated Meanwhile UI Business-Rules have changed, will not be provided by
            v3! Realtime end-user translated messages describing kinds of possible realtime changes within a Trip.
        infos_him (Union[Unset, HimSummary]): Trip overall him info.
    """

    origin: "StopV2"
    destination: "StopV2"
    origin_first_station: "StopV2"
    destination_last_station: "StopV2"
    transport_products: List[str]
    max_occupancy_first_class: TripSummaryV2MaxOccupancyFirstClass
    max_occupancy_second_class: TripSummaryV2MaxOccupancySecondClass
    cancelled: bool
    partially_cancelled: bool
    not_serviced_stop: bool
    platform_changed: bool
    delayed: bool
    reachable: bool
    additional_ride: bool
    unplanned_stop: bool
    unknown_delayed: bool
    infos_rt: "TripSummaryV2InfosRt"
    infos_him: Union[Unset, "HimSummary"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        origin = self.origin.to_dict()

        destination = self.destination.to_dict()

        origin_first_station = self.origin_first_station.to_dict()

        destination_last_station = self.destination_last_station.to_dict()

        transport_products = self.transport_products

        max_occupancy_first_class = self.max_occupancy_first_class.value

        max_occupancy_second_class = self.max_occupancy_second_class.value

        cancelled = self.cancelled
        partially_cancelled = self.partially_cancelled
        not_serviced_stop = self.not_serviced_stop
        platform_changed = self.platform_changed
        delayed = self.delayed
        reachable = self.reachable
        additional_ride = self.additional_ride
        unplanned_stop = self.unplanned_stop
        unknown_delayed = self.unknown_delayed
        infos_rt = self.infos_rt.to_dict()

        infos_him: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.infos_him, Unset):
            infos_him = self.infos_him.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "origin": origin,
                "destination": destination,
                "originFirstStation": origin_first_station,
                "destinationLastStation": destination_last_station,
                "transportProducts": transport_products,
                "maxOccupancyFirstClass": max_occupancy_first_class,
                "maxOccupancySecondClass": max_occupancy_second_class,
                "cancelled": cancelled,
                "partiallyCancelled": partially_cancelled,
                "notServicedStop": not_serviced_stop,
                "platformChanged": platform_changed,
                "delayed": delayed,
                "reachable": reachable,
                "additionalRide": additional_ride,
                "unplannedStop": unplanned_stop,
                "unknownDelayed": unknown_delayed,
                "infosRt": infos_rt,
            }
        )
        if infos_him is not UNSET:
            field_dict["infosHim"] = infos_him

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.him_summary import HimSummary
        from ..models.stop_v2 import StopV2
        from ..models.trip_summary_v2_infos_rt import TripSummaryV2InfosRt

        d = src_dict.copy()
        origin = StopV2.from_dict(d.pop("origin"))

        destination = StopV2.from_dict(d.pop("destination"))

        origin_first_station = StopV2.from_dict(d.pop("originFirstStation"))

        destination_last_station = StopV2.from_dict(d.pop("destinationLastStation"))

        transport_products = cast(List[str], d.pop("transportProducts"))

        max_occupancy_first_class = TripSummaryV2MaxOccupancyFirstClass(d.pop("maxOccupancyFirstClass"))

        max_occupancy_second_class = TripSummaryV2MaxOccupancySecondClass(d.pop("maxOccupancySecondClass"))

        cancelled = d.pop("cancelled")

        partially_cancelled = d.pop("partiallyCancelled")

        not_serviced_stop = d.pop("notServicedStop")

        platform_changed = d.pop("platformChanged")

        delayed = d.pop("delayed")

        reachable = d.pop("reachable")

        additional_ride = d.pop("additionalRide")

        unplanned_stop = d.pop("unplannedStop")

        unknown_delayed = d.pop("unknownDelayed")

        infos_rt = TripSummaryV2InfosRt.from_dict(d.pop("infosRt"))

        _infos_him = d.pop("infosHim", UNSET)
        infos_him: Union[Unset, HimSummary]
        if isinstance(_infos_him, Unset):
            infos_him = UNSET
        else:
            infos_him = HimSummary.from_dict(_infos_him)

        trip_summary_v2 = cls(
            origin=origin,
            destination=destination,
            origin_first_station=origin_first_station,
            destination_last_station=destination_last_station,
            transport_products=transport_products,
            max_occupancy_first_class=max_occupancy_first_class,
            max_occupancy_second_class=max_occupancy_second_class,
            cancelled=cancelled,
            partially_cancelled=partially_cancelled,
            not_serviced_stop=not_serviced_stop,
            platform_changed=platform_changed,
            delayed=delayed,
            reachable=reachable,
            additional_ride=additional_ride,
            unplanned_stop=unplanned_stop,
            unknown_delayed=unknown_delayed,
            infos_rt=infos_rt,
            infos_him=infos_him,
        )

        trip_summary_v2.additional_properties = d
        return trip_summary_v2

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
