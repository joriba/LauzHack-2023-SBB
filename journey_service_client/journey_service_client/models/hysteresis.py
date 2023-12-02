from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Hysteresis")


@_attrs_define
class Hysteresis:
    """Subscriptions can be configured to only trigger notifications, if changes exceed a configured limit. This is done
    using the hysteresis property per user or subscription.

        Attributes:
            long_term_notification_start (Union[Unset, int]): Time in minutes before first departure time (schedule) /
                observation time for sending out first notifications during long-term observation. During this time the
                observation will be done periodically every `longTermNotificationInterval` minutes.
                - Missing values and `-1` lead to server defaults being used.
                - 0` disables the long-term observation.
                - Negative values (other than `-1`) lead to long-term observation that starts immediatly (infinite duration).
                - The observation will take place at the time of day specified as the value (abs(longTermNotificationStart)
                minutes before departure).
            long_term_notification_interval (Union[Unset, int]): Defines the interval in minutes for long-term observation.
                Observation will be done once every X minutes during the time frame specified in `longTermNotificationStart`
                - Missing values and `-1` lead to server defaults being used.
                - `0` disables the long-term observation.
            notification_start (Union[Unset, int]): Time in minutes before (schedule) departure time to start the
                observation.
    """

    long_term_notification_start: Union[Unset, int] = 0
    long_term_notification_interval: Union[Unset, int] = 0
    notification_start: Union[Unset, int] = 0
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        long_term_notification_start = self.long_term_notification_start
        long_term_notification_interval = self.long_term_notification_interval
        notification_start = self.notification_start

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if long_term_notification_start is not UNSET:
            field_dict["longTermNotificationStart"] = long_term_notification_start
        if long_term_notification_interval is not UNSET:
            field_dict["longTermNotificationInterval"] = long_term_notification_interval
        if notification_start is not UNSET:
            field_dict["notificationStart"] = notification_start

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        long_term_notification_start = d.pop("longTermNotificationStart", UNSET)

        long_term_notification_interval = d.pop("longTermNotificationInterval", UNSET)

        notification_start = d.pop("notificationStart", UNSET)

        hysteresis = cls(
            long_term_notification_start=long_term_notification_start,
            long_term_notification_interval=long_term_notification_interval,
            notification_start=notification_start,
        )

        hysteresis.additional_properties = d
        return hysteresis

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
