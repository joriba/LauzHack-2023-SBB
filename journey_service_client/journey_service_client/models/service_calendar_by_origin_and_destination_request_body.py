import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.notice_attribute_enum import NoticeAttributeEnum
from ..models.service_calendar_by_origin_and_destination_request_body_days_in_week_item import (
    ServiceCalendarByOriginAndDestinationRequestBodyDaysInWeekItem,
)
from ..models.transport_mode_enum import TransportModeEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pt_via_reference import PTViaReference
    from ..models.trip_mobility_filter import TripMobilityFilter


T = TypeVar("T", bound="ServiceCalendarByOriginAndDestinationRequestBody")


@_attrs_define
class ServiceCalendarByOriginAndDestinationRequestBody:
    """Request parameters (POST body).

    Attributes:
        origin (str): Starting `StopPlace` of the trip at origin (departure). See v3 **PlaceReference** in [complex
            parameter](https://github.com/SchweizerischeBundesbahnen/journey-service/blob/master/JSON-Objects.md) Example:
            8503000.
        destination (str): Ending `StopPlace` of the trip at destination (arrival). See **PlaceReference** in [complex
            parameter](https://github.com/SchweizerischeBundesbahnen/journey-service/blob/master/JSON-Objects.md) Example:
            [7.435194,46.945679].
        from_date (datetime.date): Interval begin date for timetable, related to `origin` timezone. Example: 2023-01-18.
        from_time (str): Interval begin time (HH:mm), related to `fromDate`. Example: 10:15.
        to_date (datetime.date): Interval end date, related to `fromDate` and `origin`. Example: 2023-04-30.
        to_time (str): Interval end time (HH:mm), related to `toDate`. Example: 11:45.
        days_in_week (List[ServiceCalendarByOriginAndDestinationRequestBodyDaysInWeekItem]):
        mobility_filter (Union[Unset, TripMobilityFilter]): Parameters to restrict the transfer options - particularly
            for interchanging PTRideLeg's by passenger (de: Individuelles Umsteigeverhalten).
            - TripsByOriginAndDestinationPostBody: all filters supported
            - ServiceCalendarByOriginAndDestinationRequestBody: only `maxTransfers` supported yet
        vias (Union[Unset, List['PTViaReference']]):
        from_time_return (Union[Unset, str]): Interval begin time (HH:mm), related to `fromDate` and `destination`. If
            returnFrom/To are both given, returning trip timetable is generated additionally. Example: 18:00.
        to_time_return (Union[Unset, str]): Return end time (HH:mm), related to `fromTimeReturn`. Example: 20:15.
        generated_content (Union[Unset, str]): Optimize `Trip's` being printed into the PDF timetable: <br>x-extensible-
            enum: [COMPLETE,STANDARD], where:
            - COMPLETE: verbose, by means all found Trip's
            - STANDARD: only a reasonable selection of all Trip's (minimized content) Default: 'COMPLETE'.
        include_notice_attributes (Union[Unset, List[NoticeAttributeEnum]]):
        include_transport_modes (Union[Unset, List[TransportModeEnum]]):
    """

    origin: str
    destination: str
    from_date: datetime.date
    from_time: str
    to_date: datetime.date
    to_time: str
    days_in_week: List[ServiceCalendarByOriginAndDestinationRequestBodyDaysInWeekItem]
    mobility_filter: Union[Unset, "TripMobilityFilter"] = UNSET
    vias: Union[Unset, List["PTViaReference"]] = UNSET
    from_time_return: Union[Unset, str] = UNSET
    to_time_return: Union[Unset, str] = UNSET
    generated_content: Union[Unset, str] = "COMPLETE"
    include_notice_attributes: Union[Unset, List[NoticeAttributeEnum]] = UNSET
    include_transport_modes: Union[Unset, List[TransportModeEnum]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        origin = self.origin
        destination = self.destination
        from_date = self.from_date.isoformat()
        from_time = self.from_time
        to_date = self.to_date.isoformat()
        to_time = self.to_time
        days_in_week = []
        for days_in_week_item_data in self.days_in_week:
            days_in_week_item = days_in_week_item_data.value

            days_in_week.append(days_in_week_item)

        mobility_filter: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mobility_filter, Unset):
            mobility_filter = self.mobility_filter.to_dict()

        vias: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.vias, Unset):
            vias = []
            for vias_item_data in self.vias:
                vias_item = vias_item_data.to_dict()

                vias.append(vias_item)

        from_time_return = self.from_time_return
        to_time_return = self.to_time_return
        generated_content = self.generated_content
        include_notice_attributes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.include_notice_attributes, Unset):
            include_notice_attributes = []
            for include_notice_attributes_item_data in self.include_notice_attributes:
                include_notice_attributes_item = include_notice_attributes_item_data.value

                include_notice_attributes.append(include_notice_attributes_item)

        include_transport_modes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.include_transport_modes, Unset):
            include_transport_modes = []
            for include_transport_modes_item_data in self.include_transport_modes:
                include_transport_modes_item = include_transport_modes_item_data.value

                include_transport_modes.append(include_transport_modes_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "origin": origin,
                "destination": destination,
                "fromDate": from_date,
                "fromTime": from_time,
                "toDate": to_date,
                "toTime": to_time,
                "daysInWeek": days_in_week,
            }
        )
        if mobility_filter is not UNSET:
            field_dict["mobilityFilter"] = mobility_filter
        if vias is not UNSET:
            field_dict["vias"] = vias
        if from_time_return is not UNSET:
            field_dict["fromTimeReturn"] = from_time_return
        if to_time_return is not UNSET:
            field_dict["toTimeReturn"] = to_time_return
        if generated_content is not UNSET:
            field_dict["generatedContent"] = generated_content
        if include_notice_attributes is not UNSET:
            field_dict["includeNoticeAttributes"] = include_notice_attributes
        if include_transport_modes is not UNSET:
            field_dict["includeTransportModes"] = include_transport_modes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pt_via_reference import PTViaReference
        from ..models.trip_mobility_filter import TripMobilityFilter

        d = src_dict.copy()
        origin = d.pop("origin")

        destination = d.pop("destination")

        from_date = isoparse(d.pop("fromDate")).date()

        from_time = d.pop("fromTime")

        to_date = isoparse(d.pop("toDate")).date()

        to_time = d.pop("toTime")

        days_in_week = []
        _days_in_week = d.pop("daysInWeek")
        for days_in_week_item_data in _days_in_week:
            days_in_week_item = ServiceCalendarByOriginAndDestinationRequestBodyDaysInWeekItem(days_in_week_item_data)

            days_in_week.append(days_in_week_item)

        _mobility_filter = d.pop("mobilityFilter", UNSET)
        mobility_filter: Union[Unset, TripMobilityFilter]
        if isinstance(_mobility_filter, Unset):
            mobility_filter = UNSET
        else:
            mobility_filter = TripMobilityFilter.from_dict(_mobility_filter)

        vias = []
        _vias = d.pop("vias", UNSET)
        for vias_item_data in _vias or []:
            vias_item = PTViaReference.from_dict(vias_item_data)

            vias.append(vias_item)

        from_time_return = d.pop("fromTimeReturn", UNSET)

        to_time_return = d.pop("toTimeReturn", UNSET)

        generated_content = d.pop("generatedContent", UNSET)

        include_notice_attributes = []
        _include_notice_attributes = d.pop("includeNoticeAttributes", UNSET)
        for include_notice_attributes_item_data in _include_notice_attributes or []:
            include_notice_attributes_item = NoticeAttributeEnum(include_notice_attributes_item_data)

            include_notice_attributes.append(include_notice_attributes_item)

        include_transport_modes = []
        _include_transport_modes = d.pop("includeTransportModes", UNSET)
        for include_transport_modes_item_data in _include_transport_modes or []:
            include_transport_modes_item = TransportModeEnum(include_transport_modes_item_data)

            include_transport_modes.append(include_transport_modes_item)

        service_calendar_by_origin_and_destination_request_body = cls(
            origin=origin,
            destination=destination,
            from_date=from_date,
            from_time=from_time,
            to_date=to_date,
            to_time=to_time,
            days_in_week=days_in_week,
            mobility_filter=mobility_filter,
            vias=vias,
            from_time_return=from_time_return,
            to_time_return=to_time_return,
            generated_content=generated_content,
            include_notice_attributes=include_notice_attributes,
            include_transport_modes=include_transport_modes,
        )

        service_calendar_by_origin_and_destination_request_body.additional_properties = d
        return service_calendar_by_origin_and_destination_request_body

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
