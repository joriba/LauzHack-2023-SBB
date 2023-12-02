from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.archive_connection_reliability import ArchiveConnectionReliability
    from ..models.eco_balance import EcoBalance
    from ..models.leg import Leg
    from ..models.operating_period import OperatingPeriod
    from ..models.trip_status import TripStatus
    from ..models.trip_summary import TripSummary


T = TypeVar("T", bound="Trip")


@_attrs_define
class Trip:
    """A customer journey describing the movement of a passenger from one Place of any sort to another. A Trip may consist
    of one or more consecutive Leg's having some common characteristics.

        Attributes:
            id (str): TripContext to reconstruct this Trip.
            legs (List['Leg']):
            status (TripStatus): Realtime overall status of a `Trip` (depends on `PTRideLeg::serviceJourney` status).
            fast_transfer (bool): Relates to `TripMobilityFilter::walkSpeed`, if transfers below 100% were enforced, such
                Trip's are marked as `fastTransfer` by means passenger needs to hurry to get next vehicle because transfer time
                is lower than recommended at a StopPlace.
            transfers (int): Number of interchanges (de:Umstiege) [greater or equal 0].
            operating_periods (List['OperatingPeriod']): Operating days of 'same journey' within planned yearly operating-
                period though multiple entries are possible (for e.g. `Operator` change or different daysRegular/daysIrregular).
                Given for `Trip's` containing `PTRideLeg's`. Set includeOperatingDays for concrete
                `OperatingPeriod::operatingDays` if needed.
            duration (Union[Unset, str]): The [duration](https://www.w3.org/TR/xmlschema11-2/#duration) of the whole trip.
                The value may be null, if `Trip` is not rideable (for e.g. cancelled). Example: P1DT2H4M.
            paging_checksum (Union[Unset, str]): Checksum of the trip to filter same results on client side after scroll
                requests. Relates to `TripResponse::paginationCursor`. Example: fa02b99f_3.
            search_hint (Union[Unset, str]): A hint/explanation is given if Trip was not found by a direct (first) search.
                In such a case origin/destination might not match exactly to request parameters.<br>(Translated according to
                Accept-Language.) Example: Unfortunately, a connection for the desired origin and/or destination could not be
                found. We recommend the following alternative connections (please note origin/destination)..
            eco_balance (Union[Unset, EcoBalance]): Environmental coefficients to compare train and car transport.
            archive_connection_reliability (Union[Unset, ArchiveConnectionReliability]): Reliability of the connection or
                potential alternative connections **in the past** that will indicate the likelihood of getting the user to the
                requested destination in time (given by `Archive API /v3/archive/{archiveDate}/trips` only).
            summary (Union[Unset, TripSummary]): Summary of most relevant aspects of the given Trip and its PTRideLeg's.
                (Aka OJP TripSummaryStructure.)
    """

    id: str
    legs: List["Leg"]
    status: "TripStatus"
    fast_transfer: bool
    transfers: int
    operating_periods: List["OperatingPeriod"]
    duration: Union[Unset, str] = UNSET
    paging_checksum: Union[Unset, str] = UNSET
    search_hint: Union[Unset, str] = UNSET
    eco_balance: Union[Unset, "EcoBalance"] = UNSET
    archive_connection_reliability: Union[Unset, "ArchiveConnectionReliability"] = UNSET
    summary: Union[Unset, "TripSummary"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        legs = []
        for legs_item_data in self.legs:
            legs_item = legs_item_data.to_dict()

            legs.append(legs_item)

        status = self.status.to_dict()

        fast_transfer = self.fast_transfer
        transfers = self.transfers
        operating_periods = []
        for operating_periods_item_data in self.operating_periods:
            operating_periods_item = operating_periods_item_data.to_dict()

            operating_periods.append(operating_periods_item)

        duration = self.duration
        paging_checksum = self.paging_checksum
        search_hint = self.search_hint
        eco_balance: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.eco_balance, Unset):
            eco_balance = self.eco_balance.to_dict()

        archive_connection_reliability: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.archive_connection_reliability, Unset):
            archive_connection_reliability = self.archive_connection_reliability.to_dict()

        summary: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.summary, Unset):
            summary = self.summary.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "legs": legs,
                "status": status,
                "fastTransfer": fast_transfer,
                "transfers": transfers,
                "operatingPeriods": operating_periods,
            }
        )
        if duration is not UNSET:
            field_dict["duration"] = duration
        if paging_checksum is not UNSET:
            field_dict["pagingChecksum"] = paging_checksum
        if search_hint is not UNSET:
            field_dict["searchHint"] = search_hint
        if eco_balance is not UNSET:
            field_dict["ecoBalance"] = eco_balance
        if archive_connection_reliability is not UNSET:
            field_dict["archiveConnectionReliability"] = archive_connection_reliability
        if summary is not UNSET:
            field_dict["summary"] = summary

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.archive_connection_reliability import ArchiveConnectionReliability
        from ..models.eco_balance import EcoBalance
        from ..models.leg import Leg
        from ..models.operating_period import OperatingPeriod
        from ..models.trip_status import TripStatus
        from ..models.trip_summary import TripSummary

        d = src_dict.copy()
        id = d.pop("id")

        legs = []
        _legs = d.pop("legs")
        for legs_item_data in _legs:
            legs_item = Leg.from_dict(legs_item_data)

            legs.append(legs_item)

        status = TripStatus.from_dict(d.pop("status"))

        fast_transfer = d.pop("fastTransfer")

        transfers = d.pop("transfers")

        operating_periods = []
        _operating_periods = d.pop("operatingPeriods")
        for operating_periods_item_data in _operating_periods:
            operating_periods_item = OperatingPeriod.from_dict(operating_periods_item_data)

            operating_periods.append(operating_periods_item)

        duration = d.pop("duration", UNSET)

        paging_checksum = d.pop("pagingChecksum", UNSET)

        search_hint = d.pop("searchHint", UNSET)

        _eco_balance = d.pop("ecoBalance", UNSET)
        eco_balance: Union[Unset, EcoBalance]
        if isinstance(_eco_balance, Unset):
            eco_balance = UNSET
        else:
            eco_balance = EcoBalance.from_dict(_eco_balance)

        _archive_connection_reliability = d.pop("archiveConnectionReliability", UNSET)
        archive_connection_reliability: Union[Unset, ArchiveConnectionReliability]
        if isinstance(_archive_connection_reliability, Unset):
            archive_connection_reliability = UNSET
        else:
            archive_connection_reliability = ArchiveConnectionReliability.from_dict(_archive_connection_reliability)

        _summary = d.pop("summary", UNSET)
        summary: Union[Unset, TripSummary]
        if isinstance(_summary, Unset):
            summary = UNSET
        else:
            summary = TripSummary.from_dict(_summary)

        trip = cls(
            id=id,
            legs=legs,
            status=status,
            fast_transfer=fast_transfer,
            transfers=transfers,
            operating_periods=operating_periods,
            duration=duration,
            paging_checksum=paging_checksum,
            search_hint=search_hint,
            eco_balance=eco_balance,
            archive_connection_reliability=archive_connection_reliability,
            summary=summary,
        )

        trip.additional_properties = d
        return trip

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
