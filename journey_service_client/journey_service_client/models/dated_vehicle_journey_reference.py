import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.scheduled_stop_point_reference import ScheduledStopPointReference


T = TypeVar("T", bound="DatedVehicleJourneyReference")


@_attrs_define
class DatedVehicleJourneyReference:
    """Reference to a `DatedVehicleJourney` (aka OJP DatedJourneyRef). See [complex JSON parameter
    **DatedVehicleJourneyReference**](https://github.com/SchweizerischeBundesbahnen/journey-service/blob/master/JSON-
    Objects.md#datedvehiclejourneyreference)

        Attributes:
            name (str): Set the complete name as returned by `ServiceProduct`, see
                [ServiceProductReference](https://github.com/SchweizerischeBundesbahnen/journey-service/blob/master/JSON-
                Objects.md#serviceproductreference) for proper format. Example: IC 1 753.
            start (Union[Unset, ScheduledStopPointReference]): ScheduledStopPoint reference to a StopPlace (PlaceReference)
                with a departure or arrival dateTime, see
                [ScheduledStopPointReference](https://github.com/SchweizerischeBundesbahnen/journey-service/blob/master/JSON-
                Objects.md#scheduledstoppointreference).
            end (Union[Unset, ScheduledStopPointReference]): ScheduledStopPoint reference to a StopPlace (PlaceReference)
                with a departure or arrival dateTime, see
                [ScheduledStopPointReference](https://github.com/SchweizerischeBundesbahnen/journey-service/blob/master/JSON-
                Objects.md#scheduledstoppointreference).
            operator_number (Union[Unset, str]): The `ServiceProduct::operator::id` for e.g. '000011' as returned by J-S.
                Example: 000011.
            operating_day (Union[Unset, datetime.date]): Operating-day of the `ServiceJourney`.
    """

    name: str
    start: Union[Unset, "ScheduledStopPointReference"] = UNSET
    end: Union[Unset, "ScheduledStopPointReference"] = UNSET
    operator_number: Union[Unset, str] = UNSET
    operating_day: Union[Unset, datetime.date] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        start: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.to_dict()

        end: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.end, Unset):
            end = self.end.to_dict()

        operator_number = self.operator_number
        operating_day: Union[Unset, str] = UNSET
        if not isinstance(self.operating_day, Unset):
            operating_day = self.operating_day.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if start is not UNSET:
            field_dict["start"] = start
        if end is not UNSET:
            field_dict["end"] = end
        if operator_number is not UNSET:
            field_dict["operatorNumber"] = operator_number
        if operating_day is not UNSET:
            field_dict["operatingDay"] = operating_day

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.scheduled_stop_point_reference import ScheduledStopPointReference

        d = src_dict.copy()
        name = d.pop("name")

        _start = d.pop("start", UNSET)
        start: Union[Unset, ScheduledStopPointReference]
        if isinstance(_start, Unset):
            start = UNSET
        else:
            start = ScheduledStopPointReference.from_dict(_start)

        _end = d.pop("end", UNSET)
        end: Union[Unset, ScheduledStopPointReference]
        if isinstance(_end, Unset):
            end = UNSET
        else:
            end = ScheduledStopPointReference.from_dict(_end)

        operator_number = d.pop("operatorNumber", UNSET)

        _operating_day = d.pop("operatingDay", UNSET)
        operating_day: Union[Unset, datetime.date]
        if isinstance(_operating_day, Unset):
            operating_day = UNSET
        else:
            operating_day = isoparse(_operating_day).date()

        dated_vehicle_journey_reference = cls(
            name=name,
            start=start,
            end=end,
            operator_number=operator_number,
            operating_day=operating_day,
        )

        dated_vehicle_journey_reference.additional_properties = d
        return dated_vehicle_journey_reference

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
