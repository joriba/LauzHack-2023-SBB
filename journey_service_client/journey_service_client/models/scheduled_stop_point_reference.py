import datetime
from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="ScheduledStopPointReference")


@_attrs_define
class ScheduledStopPointReference:
    """ScheduledStopPoint reference to a StopPlace (PlaceReference) with a departure or arrival dateTime, see
    [ScheduledStopPointReference](https://github.com/SchweizerischeBundesbahnen/journey-service/blob/master/JSON-
    Objects.md#scheduledstoppointreference).

        Attributes:
            stop_place_id (str): `StopPlace::id` value related to `dateTime`. Example: 8507000.
            date_time (datetime.datetime): Departure or arrival date/time
                ([ISO-8601](https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) UTC with time-numoffset (like '+02:00'))
                at `stopPlaceId`. Example: 2023-04-18T14:55:00+01:00.
    """

    stop_place_id: str
    date_time: datetime.datetime
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        stop_place_id = self.stop_place_id
        date_time = self.date_time.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stopPlaceId": stop_place_id,
                "dateTime": date_time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        stop_place_id = d.pop("stopPlaceId")

        date_time = isoparse(d.pop("dateTime"))

        scheduled_stop_point_reference = cls(
            stop_place_id=stop_place_id,
            date_time=date_time,
        )

        scheduled_stop_point_reference.additional_properties = d
        return scheduled_stop_point_reference

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
