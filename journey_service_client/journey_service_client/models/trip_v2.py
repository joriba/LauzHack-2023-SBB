from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.connection_reliability import ConnectionReliability
    from ..models.eco_balance import EcoBalance
    from ..models.leg_v2 import LegV2
    from ..models.service_days_v2 import ServiceDaysV2
    from ..models.trip_summary_v2 import TripSummaryV2


T = TypeVar("T", bound="TripV2")


@_attrs_define
class TripV2:
    """Represents a specific trip from A to B routing over [0..*] via's.

    Attributes:
        transfers (int): Number of interchanges (de:Umstiege) [greater or equal 0].
        alternative (bool): false: Planned connection; true: Realtime alternative
        valid (bool): true: Trip is still possible to ride based on the current realtime situation (related to
            TripV2::serviceDays, LegV2::reachable); false: not rideable as a 'whole' Trip' anymore.Important: if this valid
            toggles from true to false, the passenger might not be able to perform his Trip, by means re-planning options
            might occur.
        individual_change_time (bool): true: Trip is based on individual change times; false: not (default)
        legs (List['LegV2']):
        service_days (List['ServiceDaysV2']):
        reconstruction_context (Union[Unset, str]): `TripV2::reconstructionContext` or `v3.Trip::id` is a temporary
            TripContext describing a concrete rideable and priceable journey (and not to be understood as a guaranteed ID
            which might be cached forever)! Therefore proper reconstruction is not guaranteed (realtime aspects, lacking
            service-days in the future, ..)!
        duration (Union[Unset, str]): The [duration](https://www.w3.org/TR/xmlschema11-2/#duration) of the whole trip.
            The value may be null, if trip is not rideable (for e.g. cancelled). Example: P1DT2H4M.
        eco_balance (Union[Unset, EcoBalance]): Environmental coefficients to compare train and car transport.
        scroll_check_sum (Union[Unset, str]): Checksum of the trip to filter same results on client side after scroll
            requests. Example: fa02b99f_3.
        search_hint (Union[Unset, str]): A translated hint/explanation is given if Trip was not found by a direct
            (first) search. In such a case origin/destination might not match exactly to request parameters.<br>(Translated
            according to Accept-Language.) Example: Unfortunately, a connection for the desired origin and/or destination
            could not be found. We recommend the following alternative connections (please note origin/destination)..
        summary (Union[Unset, TripSummaryV2]): Most important facts of a Trip (useful for a quick overview).
        archived_connection_reliability (Union[Unset, ConnectionReliability]): Archive API Timemachine only: Validation
            of trip in the past.
        swiss_national (Union[Unset, bool]): @Deprecated IRRELEVANT not supported anymore and always false!
    """

    transfers: int
    alternative: bool
    valid: bool
    individual_change_time: bool
    legs: List["LegV2"]
    service_days: List["ServiceDaysV2"]
    reconstruction_context: Union[Unset, str] = UNSET
    duration: Union[Unset, str] = UNSET
    eco_balance: Union[Unset, "EcoBalance"] = UNSET
    scroll_check_sum: Union[Unset, str] = UNSET
    search_hint: Union[Unset, str] = UNSET
    summary: Union[Unset, "TripSummaryV2"] = UNSET
    archived_connection_reliability: Union[Unset, "ConnectionReliability"] = UNSET
    swiss_national: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        transfers = self.transfers
        alternative = self.alternative
        valid = self.valid
        individual_change_time = self.individual_change_time
        legs = []
        for legs_item_data in self.legs:
            legs_item = legs_item_data.to_dict()

            legs.append(legs_item)

        service_days = []
        for service_days_item_data in self.service_days:
            service_days_item = service_days_item_data.to_dict()

            service_days.append(service_days_item)

        reconstruction_context = self.reconstruction_context
        duration = self.duration
        eco_balance: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.eco_balance, Unset):
            eco_balance = self.eco_balance.to_dict()

        scroll_check_sum = self.scroll_check_sum
        search_hint = self.search_hint
        summary: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.summary, Unset):
            summary = self.summary.to_dict()

        archived_connection_reliability: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.archived_connection_reliability, Unset):
            archived_connection_reliability = self.archived_connection_reliability.to_dict()

        swiss_national = self.swiss_national

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "transfers": transfers,
                "alternative": alternative,
                "valid": valid,
                "individualChangeTime": individual_change_time,
                "legs": legs,
                "serviceDays": service_days,
            }
        )
        if reconstruction_context is not UNSET:
            field_dict["reconstructionContext"] = reconstruction_context
        if duration is not UNSET:
            field_dict["duration"] = duration
        if eco_balance is not UNSET:
            field_dict["ecoBalance"] = eco_balance
        if scroll_check_sum is not UNSET:
            field_dict["scrollCheckSum"] = scroll_check_sum
        if search_hint is not UNSET:
            field_dict["searchHint"] = search_hint
        if summary is not UNSET:
            field_dict["summary"] = summary
        if archived_connection_reliability is not UNSET:
            field_dict["archivedConnectionReliability"] = archived_connection_reliability
        if swiss_national is not UNSET:
            field_dict["swissNational"] = swiss_national

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.connection_reliability import ConnectionReliability
        from ..models.eco_balance import EcoBalance
        from ..models.leg_v2 import LegV2
        from ..models.service_days_v2 import ServiceDaysV2
        from ..models.trip_summary_v2 import TripSummaryV2

        d = src_dict.copy()
        transfers = d.pop("transfers")

        alternative = d.pop("alternative")

        valid = d.pop("valid")

        individual_change_time = d.pop("individualChangeTime")

        legs = []
        _legs = d.pop("legs")
        for legs_item_data in _legs:
            legs_item = LegV2.from_dict(legs_item_data)

            legs.append(legs_item)

        service_days = []
        _service_days = d.pop("serviceDays")
        for service_days_item_data in _service_days:
            service_days_item = ServiceDaysV2.from_dict(service_days_item_data)

            service_days.append(service_days_item)

        reconstruction_context = d.pop("reconstructionContext", UNSET)

        duration = d.pop("duration", UNSET)

        _eco_balance = d.pop("ecoBalance", UNSET)
        eco_balance: Union[Unset, EcoBalance]
        if isinstance(_eco_balance, Unset):
            eco_balance = UNSET
        else:
            eco_balance = EcoBalance.from_dict(_eco_balance)

        scroll_check_sum = d.pop("scrollCheckSum", UNSET)

        search_hint = d.pop("searchHint", UNSET)

        _summary = d.pop("summary", UNSET)
        summary: Union[Unset, TripSummaryV2]
        if isinstance(_summary, Unset):
            summary = UNSET
        else:
            summary = TripSummaryV2.from_dict(_summary)

        _archived_connection_reliability = d.pop("archivedConnectionReliability", UNSET)
        archived_connection_reliability: Union[Unset, ConnectionReliability]
        if isinstance(_archived_connection_reliability, Unset):
            archived_connection_reliability = UNSET
        else:
            archived_connection_reliability = ConnectionReliability.from_dict(_archived_connection_reliability)

        swiss_national = d.pop("swissNational", UNSET)

        trip_v2 = cls(
            transfers=transfers,
            alternative=alternative,
            valid=valid,
            individual_change_time=individual_change_time,
            legs=legs,
            service_days=service_days,
            reconstruction_context=reconstruction_context,
            duration=duration,
            eco_balance=eco_balance,
            scroll_check_sum=scroll_check_sum,
            search_hint=search_hint,
            summary=summary,
            archived_connection_reliability=archived_connection_reliability,
            swiss_national=swiss_national,
        )

        trip_v2.additional_properties = d
        return trip_v2

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
