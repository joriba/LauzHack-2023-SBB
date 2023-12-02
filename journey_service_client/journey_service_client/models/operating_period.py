import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="OperatingPeriod")


@_attrs_define
class OperatingPeriod:
    """A **continuous interval of time** making up a timetable frame **of 1 year**, typically starting around 2nd Sunday of
    December.

        Attributes:
            operating_days (List[datetime.date]):
            name (str): Name of attached type having this operating period, like `Trip`, `StopPlace` or `ServiceJourney`
                (just an informational value). Example: Trip.
            days_regular_formatted (Union[Unset, str]): Only set in context of a `ServiceJourney::operatingPeriods`.
                **Regular service-days a `ServiceProduct` operates** by scheduled plan within the same
                `OperatingPeriod`.<br>(Translated according to Accept-Language.) Example: täglich.
            days_irregular_formatted (Union[Unset, str]): Only set in context of a `ServiceJourney::operatingPeriods`.
                **Irregular service-days (or excpetions to regular days) a `ServiceProduct` operates** by scheduled plan within
                the same `OperatingPeriod`.<br>(Translated according to Accept-Language.) Example: nicht 24., 25. Mär, 7., 8.
                Apr.
            short_name (Union[Unset, str]): Related to `name=StopPlace` for corresponding data-poolId. Example: gabo.
            route_index_from (Union[Unset, int]): In the context of `ServiceJourney` relates to the first
                `ScheduledStop::routeIndex` where given `operatingDays` are valid, null if unknown. Example: 3.
            route_index_to (Union[Unset, int]): In the context of `ServiceJourney` relates to the last
                `ScheduledStop::routeIndex` where `operatingDays` are valid, null if unknown. Example: 7.
    """

    operating_days: List[datetime.date]
    name: str
    days_regular_formatted: Union[Unset, str] = UNSET
    days_irregular_formatted: Union[Unset, str] = UNSET
    short_name: Union[Unset, str] = UNSET
    route_index_from: Union[Unset, int] = UNSET
    route_index_to: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        operating_days = []
        for operating_days_item_data in self.operating_days:
            operating_days_item = operating_days_item_data.isoformat()
            operating_days.append(operating_days_item)

        name = self.name
        days_regular_formatted = self.days_regular_formatted
        days_irregular_formatted = self.days_irregular_formatted
        short_name = self.short_name
        route_index_from = self.route_index_from
        route_index_to = self.route_index_to

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "operatingDays": operating_days,
                "name": name,
            }
        )
        if days_regular_formatted is not UNSET:
            field_dict["daysRegularFormatted"] = days_regular_formatted
        if days_irregular_formatted is not UNSET:
            field_dict["daysIrregularFormatted"] = days_irregular_formatted
        if short_name is not UNSET:
            field_dict["shortName"] = short_name
        if route_index_from is not UNSET:
            field_dict["routeIndexFrom"] = route_index_from
        if route_index_to is not UNSET:
            field_dict["routeIndexTo"] = route_index_to

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        operating_days = []
        _operating_days = d.pop("operatingDays")
        for operating_days_item_data in _operating_days:
            operating_days_item = isoparse(operating_days_item_data).date()

            operating_days.append(operating_days_item)

        name = d.pop("name")

        days_regular_formatted = d.pop("daysRegularFormatted", UNSET)

        days_irregular_formatted = d.pop("daysIrregularFormatted", UNSET)

        short_name = d.pop("shortName", UNSET)

        route_index_from = d.pop("routeIndexFrom", UNSET)

        route_index_to = d.pop("routeIndexTo", UNSET)

        operating_period = cls(
            operating_days=operating_days,
            name=name,
            days_regular_formatted=days_regular_formatted,
            days_irregular_formatted=days_irregular_formatted,
            short_name=short_name,
            route_index_from=route_index_from,
            route_index_to=route_index_to,
        )

        operating_period.additional_properties = d
        return operating_period

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
