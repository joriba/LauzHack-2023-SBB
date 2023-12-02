import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicationWindow")


@_attrs_define
class PublicationWindow:
    """A period during which the situation should be published.

    Attributes:
        start_date (Union[Unset, datetime.date]): Local start date of situation (related to `startTime`). Example:
            2023-04-18.
        start_time (Union[Unset, str]): Local start time of situation (related to `startDate`). Example: 14:27.
        end_date (Union[Unset, datetime.date]): Local end date of situation (related to `endTime`).
        end_time (Union[Unset, str]): Local end time of situation (related to `endDate`).
        daily_starting_at (Union[Unset, str]): Situation starting daily at time within this publication window.
        daily_duration (Union[Unset, str]): Situation [duration](https://www.w3.org/TR/xmlschema11-2/#duration) within
            this publication window. Example: PT23H59M0S.
    """

    start_date: Union[Unset, datetime.date] = UNSET
    start_time: Union[Unset, str] = UNSET
    end_date: Union[Unset, datetime.date] = UNSET
    end_time: Union[Unset, str] = UNSET
    daily_starting_at: Union[Unset, str] = UNSET
    daily_duration: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        start_time = self.start_time
        end_date: Union[Unset, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        end_time = self.end_time
        daily_starting_at = self.daily_starting_at
        daily_duration = self.daily_duration

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if daily_starting_at is not UNSET:
            field_dict["dailyStartingAt"] = daily_starting_at
        if daily_duration is not UNSET:
            field_dict["dailyDuration"] = daily_duration

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _start_date = d.pop("startDate", UNSET)
        start_date: Union[Unset, datetime.date]
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date).date()

        start_time = d.pop("startTime", UNSET)

        _end_date = d.pop("endDate", UNSET)
        end_date: Union[Unset, datetime.date]
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date).date()

        end_time = d.pop("endTime", UNSET)

        daily_starting_at = d.pop("dailyStartingAt", UNSET)

        daily_duration = d.pop("dailyDuration", UNSET)

        publication_window = cls(
            start_date=start_date,
            start_time=start_time,
            end_date=end_date,
            end_time=end_time,
            daily_starting_at=daily_starting_at,
            daily_duration=daily_duration,
        )

        publication_window.additional_properties = d
        return publication_window

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
