import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.scheduled_stop_point import ScheduledStopPoint
    from ..models.service_product import ServiceProduct


T = TypeVar("T", bound="ServiceJourneyAffected")


@_attrs_define
class ServiceJourneyAffected:
    """Affected `ServiceJourney`.

    Attributes:
        situation_message_ids (List[str]):
        operating_days_matched (List[datetime.date]):
        service_product (Union[Unset, ServiceProduct]): A passenger carrying Service (phyisical public transport
            vehicle) provided and operated by a certain Operator allocated to a concrete ServiceJourney on an
            `OperatingDay`.<br>See SBB specific transport-modes: [v580 de:Verkehrsmittelkategorien (aka Transmodel or
            OJP/Siri `VehicleMode`)](https://github.com/SchweizerischeBundesbahnen/journey-
            service/blob/master/TransportMode.md).
        operating_day (Union[Unset, datetime.date]): Concrete operating-day (aka service-day).
        first_stop_point (Union[Unset, ScheduledStopPoint]): Passenger relevant stop-point on a `ServiceJourney`. Some
            properties may further by distinguished on either `arrival` and/or `departure StopCall` aspects.
        last_stop_point (Union[Unset, ScheduledStopPoint]): Passenger relevant stop-point on a `ServiceJourney`. Some
            properties may further by distinguished on either `arrival` and/or `departure StopCall` aspects.
        first_match_stop_point (Union[Unset, ScheduledStopPoint]): Passenger relevant stop-point on a `ServiceJourney`.
            Some properties may further by distinguished on either `arrival` and/or `departure StopCall` aspects.
        last_match_stop_point (Union[Unset, ScheduledStopPoint]): Passenger relevant stop-point on a `ServiceJourney`.
            Some properties may further by distinguished on either `arrival` and/or `departure StopCall` aspects.
    """

    situation_message_ids: List[str]
    operating_days_matched: List[datetime.date]
    service_product: Union[Unset, "ServiceProduct"] = UNSET
    operating_day: Union[Unset, datetime.date] = UNSET
    first_stop_point: Union[Unset, "ScheduledStopPoint"] = UNSET
    last_stop_point: Union[Unset, "ScheduledStopPoint"] = UNSET
    first_match_stop_point: Union[Unset, "ScheduledStopPoint"] = UNSET
    last_match_stop_point: Union[Unset, "ScheduledStopPoint"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        situation_message_ids = self.situation_message_ids

        operating_days_matched = []
        for operating_days_matched_item_data in self.operating_days_matched:
            operating_days_matched_item = operating_days_matched_item_data.isoformat()
            operating_days_matched.append(operating_days_matched_item)

        service_product: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.service_product, Unset):
            service_product = self.service_product.to_dict()

        operating_day: Union[Unset, str] = UNSET
        if not isinstance(self.operating_day, Unset):
            operating_day = self.operating_day.isoformat()

        first_stop_point: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.first_stop_point, Unset):
            first_stop_point = self.first_stop_point.to_dict()

        last_stop_point: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.last_stop_point, Unset):
            last_stop_point = self.last_stop_point.to_dict()

        first_match_stop_point: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.first_match_stop_point, Unset):
            first_match_stop_point = self.first_match_stop_point.to_dict()

        last_match_stop_point: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.last_match_stop_point, Unset):
            last_match_stop_point = self.last_match_stop_point.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "situationMessageIds": situation_message_ids,
                "operatingDaysMatched": operating_days_matched,
            }
        )
        if service_product is not UNSET:
            field_dict["serviceProduct"] = service_product
        if operating_day is not UNSET:
            field_dict["operatingDay"] = operating_day
        if first_stop_point is not UNSET:
            field_dict["firstStopPoint"] = first_stop_point
        if last_stop_point is not UNSET:
            field_dict["lastStopPoint"] = last_stop_point
        if first_match_stop_point is not UNSET:
            field_dict["firstMatchStopPoint"] = first_match_stop_point
        if last_match_stop_point is not UNSET:
            field_dict["lastMatchStopPoint"] = last_match_stop_point

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.scheduled_stop_point import ScheduledStopPoint
        from ..models.service_product import ServiceProduct

        d = src_dict.copy()
        situation_message_ids = cast(List[str], d.pop("situationMessageIds"))

        operating_days_matched = []
        _operating_days_matched = d.pop("operatingDaysMatched")
        for operating_days_matched_item_data in _operating_days_matched:
            operating_days_matched_item = isoparse(operating_days_matched_item_data).date()

            operating_days_matched.append(operating_days_matched_item)

        _service_product = d.pop("serviceProduct", UNSET)
        service_product: Union[Unset, ServiceProduct]
        if isinstance(_service_product, Unset):
            service_product = UNSET
        else:
            service_product = ServiceProduct.from_dict(_service_product)

        _operating_day = d.pop("operatingDay", UNSET)
        operating_day: Union[Unset, datetime.date]
        if isinstance(_operating_day, Unset):
            operating_day = UNSET
        else:
            operating_day = isoparse(_operating_day).date()

        _first_stop_point = d.pop("firstStopPoint", UNSET)
        first_stop_point: Union[Unset, ScheduledStopPoint]
        if isinstance(_first_stop_point, Unset):
            first_stop_point = UNSET
        else:
            first_stop_point = ScheduledStopPoint.from_dict(_first_stop_point)

        _last_stop_point = d.pop("lastStopPoint", UNSET)
        last_stop_point: Union[Unset, ScheduledStopPoint]
        if isinstance(_last_stop_point, Unset):
            last_stop_point = UNSET
        else:
            last_stop_point = ScheduledStopPoint.from_dict(_last_stop_point)

        _first_match_stop_point = d.pop("firstMatchStopPoint", UNSET)
        first_match_stop_point: Union[Unset, ScheduledStopPoint]
        if isinstance(_first_match_stop_point, Unset):
            first_match_stop_point = UNSET
        else:
            first_match_stop_point = ScheduledStopPoint.from_dict(_first_match_stop_point)

        _last_match_stop_point = d.pop("lastMatchStopPoint", UNSET)
        last_match_stop_point: Union[Unset, ScheduledStopPoint]
        if isinstance(_last_match_stop_point, Unset):
            last_match_stop_point = UNSET
        else:
            last_match_stop_point = ScheduledStopPoint.from_dict(_last_match_stop_point)

        service_journey_affected = cls(
            situation_message_ids=situation_message_ids,
            operating_days_matched=operating_days_matched,
            service_product=service_product,
            operating_day=operating_day,
            first_stop_point=first_stop_point,
            last_stop_point=last_stop_point,
            first_match_stop_point=first_match_stop_point,
            last_match_stop_point=last_match_stop_point,
        )

        service_journey_affected.additional_properties = d
        return service_journey_affected

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
