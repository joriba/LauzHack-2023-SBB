import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="DateTimeInterval")


@_attrs_define
class DateTimeInterval:
    """Start/end date/time interval.

    Example:
        {'start': '2023-04-18T14:55:00+01:00', 'end': '2023-09-07T09:10:00+02:00', 'dailyStartingAt': '17:15',
            'dailyEndingAt': '18:05'}

    Attributes:
        start (Union[Unset, datetime.datetime]): Corresponding date/time for `ServiceJourney`. If not set, the first
            location in the reconstruction will be used that matches the location. Related to `end`.
        end (Union[Unset, datetime.datetime]): Corresponding date/time for `ServiceJourney`, related to `start`.
        daily_starting_at (Union[Unset, str]): Starting time within [start..end].
        daily_ending_at (Union[Unset, str]): Ending time within [start..end]
    """

    start: Union[Unset, datetime.datetime] = UNSET
    end: Union[Unset, datetime.datetime] = UNSET
    daily_starting_at: Union[Unset, str] = UNSET
    daily_ending_at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        start: Union[Unset, str] = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.isoformat()

        end: Union[Unset, str] = UNSET
        if not isinstance(self.end, Unset):
            end = self.end.isoformat()

        daily_starting_at = self.daily_starting_at
        daily_ending_at = self.daily_ending_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if start is not UNSET:
            field_dict["start"] = start
        if end is not UNSET:
            field_dict["end"] = end
        if daily_starting_at is not UNSET:
            field_dict["dailyStartingAt"] = daily_starting_at
        if daily_ending_at is not UNSET:
            field_dict["dailyEndingAt"] = daily_ending_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _start = d.pop("start", UNSET)
        start: Union[Unset, datetime.datetime]
        if isinstance(_start, Unset):
            start = UNSET
        else:
            start = isoparse(_start)

        _end = d.pop("end", UNSET)
        end: Union[Unset, datetime.datetime]
        if isinstance(_end, Unset):
            end = UNSET
        else:
            end = isoparse(_end)

        daily_starting_at = d.pop("dailyStartingAt", UNSET)

        daily_ending_at = d.pop("dailyEndingAt", UNSET)

        date_time_interval = cls(
            start=start,
            end=end,
            daily_starting_at=daily_starting_at,
            daily_ending_at=daily_ending_at,
        )

        date_time_interval.additional_properties = d
        return date_time_interval

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
