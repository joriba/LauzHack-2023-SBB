import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.him_message_v2_category import HimMessageV2Category
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.local_time import LocalTime
    from ..models.message_channel_type import MessageChannelType
    from ..models.message_edge import MessageEdge
    from ..models.message_region import MessageRegion
    from ..models.service_days_v2 import ServiceDaysV2
    from ..models.stop_v2 import StopV2
    from ..models.transport_product_v2 import TransportProductV2


T = TypeVar("T", bound="HimMessageV2")


@_attrs_define
class HimMessageV2:
    """A disruption (for e.g. an incident or a deviation (aka de:Störungs-, Ereignismeldung)) affecting planned PT
    `TransportProductV2` in certain edges and/or regions.

        Attributes:
            id (str): Identity of message (aka HIM id). Example: x944292.
            priority (int): Priority rank (the smaller the higher): low = 80, medium = 60, high = 40, de:Grossereignis = 20
                Example: 80.
            formatted_header (str): Heading of message formatted according to SBB business rule: affectedProducts, from/to,
                head, lead
            formatted_footer (str): Complete Footer/text of message formatted according to SBB business rule (HTML tags like
                BR(eak) are possible). Scoped for browser based UIs.
            formatted_footer_short (str): Short Footer/text of message formatted according to SBB business rule (HTML tags
                like BR(eak) are possible). Scoped for App UIs.
            channels (List['MessageChannelType']):
            edges (List['MessageEdge']):
            regions (List['MessageRegion']):
            category (Union[Unset, HimMessageV2Category]): Represents disruption type for HIM messages. Example:
                DISTURBANCE.
            valid_from_stop (Union[Unset, StopV2]): A stop represents a specific location (typically a STATION) of a leg or
                a complete journey-detail of a transport-product (aka v3.ScheduledStopPoint, OJP StopPoint).
            valid_from_stop_name (Union[Unset, str]): @Deprecated use validFromStop::name
            valid_to_stop (Union[Unset, StopV2]): A stop represents a specific location (typically a STATION) of a leg or a
                complete journey-detail of a transport-product (aka v3.ScheduledStopPoint, OJP StopPoint).
            valid_to_stop_name (Union[Unset, str]): @Deprecated use validToStop::name
            route_index_from (Union[Unset, int]): @Deprecated Use `validFromStop::routeIndex` instead. First stop/station
                where this message is valid. See the Stops list in the JourneyDetail response for this leg to get more details
                about this stop/station.
            route_index_to (Union[Unset, int]): @Deprecated Use `validToStop::routeIndex` instead. Last stop/station where
                this message is valid. See the Stops list in the JourneyDetail response for this leg to get more details about
                this stop/station.
            start_time (Union[Unset, LocalTime]): Message event period starting at time daily. Example: 13:07.
            start_date (Union[Unset, datetime.date]): Start date of event (related to `startTime`).
            end_time (Union[Unset, LocalTime]): Message event period starting at time daily. Example: 13:07.
            end_date (Union[Unset, datetime.date]): End date of event (related to `endTime`).
            start_text (Union[Unset, str]): @Deprecated Descriptive text for start of event period.
            end_text (Union[Unset, str]): @Deprecated Descriptive text for end of event period.
            daily_starting_at (Union[Unset, LocalTime]): Message event period starting at time daily. Example: 13:07.
            daily_duration (Union[Unset, str]): Message event period
                [duration](https://www.w3.org/TR/xmlschema11-2/#duration) starting at dailyStartingAt for dailyDuration amount
                of time. Example: P1DT2H4M.
            service_days (Union[Unset, ServiceDaysV2]): Service-period of a transport-product in regular schedule. Given for
                a yearly journey-planning period (see /info).
            transport_products (Union[Unset, List['TransportProductV2']]):
    """

    id: str
    priority: int
    formatted_header: str
    formatted_footer: str
    formatted_footer_short: str
    channels: List["MessageChannelType"]
    edges: List["MessageEdge"]
    regions: List["MessageRegion"]
    category: Union[Unset, HimMessageV2Category] = UNSET
    valid_from_stop: Union[Unset, "StopV2"] = UNSET
    valid_from_stop_name: Union[Unset, str] = UNSET
    valid_to_stop: Union[Unset, "StopV2"] = UNSET
    valid_to_stop_name: Union[Unset, str] = UNSET
    route_index_from: Union[Unset, int] = UNSET
    route_index_to: Union[Unset, int] = UNSET
    start_time: Union[Unset, "LocalTime"] = UNSET
    start_date: Union[Unset, datetime.date] = UNSET
    end_time: Union[Unset, "LocalTime"] = UNSET
    end_date: Union[Unset, datetime.date] = UNSET
    start_text: Union[Unset, str] = UNSET
    end_text: Union[Unset, str] = UNSET
    daily_starting_at: Union[Unset, "LocalTime"] = UNSET
    daily_duration: Union[Unset, str] = UNSET
    service_days: Union[Unset, "ServiceDaysV2"] = UNSET
    transport_products: Union[Unset, List["TransportProductV2"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        priority = self.priority
        formatted_header = self.formatted_header
        formatted_footer = self.formatted_footer
        formatted_footer_short = self.formatted_footer_short
        channels = []
        for channels_item_data in self.channels:
            channels_item = channels_item_data.to_dict()

            channels.append(channels_item)

        edges = []
        for edges_item_data in self.edges:
            edges_item = edges_item_data.to_dict()

            edges.append(edges_item)

        regions = []
        for regions_item_data in self.regions:
            regions_item = regions_item_data.to_dict()

            regions.append(regions_item)

        category: Union[Unset, str] = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.value

        valid_from_stop: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.valid_from_stop, Unset):
            valid_from_stop = self.valid_from_stop.to_dict()

        valid_from_stop_name = self.valid_from_stop_name
        valid_to_stop: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.valid_to_stop, Unset):
            valid_to_stop = self.valid_to_stop.to_dict()

        valid_to_stop_name = self.valid_to_stop_name
        route_index_from = self.route_index_from
        route_index_to = self.route_index_to
        start_time: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.to_dict()

        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        end_time: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.end_time, Unset):
            end_time = self.end_time.to_dict()

        end_date: Union[Unset, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        start_text = self.start_text
        end_text = self.end_text
        daily_starting_at: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.daily_starting_at, Unset):
            daily_starting_at = self.daily_starting_at.to_dict()

        daily_duration = self.daily_duration
        service_days: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.service_days, Unset):
            service_days = self.service_days.to_dict()

        transport_products: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.transport_products, Unset):
            transport_products = []
            for transport_products_item_data in self.transport_products:
                transport_products_item = transport_products_item_data.to_dict()

                transport_products.append(transport_products_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "priority": priority,
                "formattedHeader": formatted_header,
                "formattedFooter": formatted_footer,
                "formattedFooterShort": formatted_footer_short,
                "channels": channels,
                "edges": edges,
                "regions": regions,
            }
        )
        if category is not UNSET:
            field_dict["category"] = category
        if valid_from_stop is not UNSET:
            field_dict["validFromStop"] = valid_from_stop
        if valid_from_stop_name is not UNSET:
            field_dict["validFromStopName"] = valid_from_stop_name
        if valid_to_stop is not UNSET:
            field_dict["validToStop"] = valid_to_stop
        if valid_to_stop_name is not UNSET:
            field_dict["validToStopName"] = valid_to_stop_name
        if route_index_from is not UNSET:
            field_dict["routeIndexFrom"] = route_index_from
        if route_index_to is not UNSET:
            field_dict["routeIndexTo"] = route_index_to
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if start_text is not UNSET:
            field_dict["startText"] = start_text
        if end_text is not UNSET:
            field_dict["endText"] = end_text
        if daily_starting_at is not UNSET:
            field_dict["dailyStartingAt"] = daily_starting_at
        if daily_duration is not UNSET:
            field_dict["dailyDuration"] = daily_duration
        if service_days is not UNSET:
            field_dict["serviceDays"] = service_days
        if transport_products is not UNSET:
            field_dict["transportProducts"] = transport_products

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.local_time import LocalTime
        from ..models.message_channel_type import MessageChannelType
        from ..models.message_edge import MessageEdge
        from ..models.message_region import MessageRegion
        from ..models.service_days_v2 import ServiceDaysV2
        from ..models.stop_v2 import StopV2
        from ..models.transport_product_v2 import TransportProductV2

        d = src_dict.copy()
        id = d.pop("id")

        priority = d.pop("priority")

        formatted_header = d.pop("formattedHeader")

        formatted_footer = d.pop("formattedFooter")

        formatted_footer_short = d.pop("formattedFooterShort")

        channels = []
        _channels = d.pop("channels")
        for channels_item_data in _channels:
            channels_item = MessageChannelType.from_dict(channels_item_data)

            channels.append(channels_item)

        edges = []
        _edges = d.pop("edges")
        for edges_item_data in _edges:
            edges_item = MessageEdge.from_dict(edges_item_data)

            edges.append(edges_item)

        regions = []
        _regions = d.pop("regions")
        for regions_item_data in _regions:
            regions_item = MessageRegion.from_dict(regions_item_data)

            regions.append(regions_item)

        _category = d.pop("category", UNSET)
        category: Union[Unset, HimMessageV2Category]
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = HimMessageV2Category(_category)

        _valid_from_stop = d.pop("validFromStop", UNSET)
        valid_from_stop: Union[Unset, StopV2]
        if isinstance(_valid_from_stop, Unset):
            valid_from_stop = UNSET
        else:
            valid_from_stop = StopV2.from_dict(_valid_from_stop)

        valid_from_stop_name = d.pop("validFromStopName", UNSET)

        _valid_to_stop = d.pop("validToStop", UNSET)
        valid_to_stop: Union[Unset, StopV2]
        if isinstance(_valid_to_stop, Unset):
            valid_to_stop = UNSET
        else:
            valid_to_stop = StopV2.from_dict(_valid_to_stop)

        valid_to_stop_name = d.pop("validToStopName", UNSET)

        route_index_from = d.pop("routeIndexFrom", UNSET)

        route_index_to = d.pop("routeIndexTo", UNSET)

        _start_time = d.pop("startTime", UNSET)
        start_time: Union[Unset, LocalTime]
        if isinstance(_start_time, Unset):
            start_time = UNSET
        else:
            start_time = LocalTime.from_dict(_start_time)

        _start_date = d.pop("startDate", UNSET)
        start_date: Union[Unset, datetime.date]
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date).date()

        _end_time = d.pop("endTime", UNSET)
        end_time: Union[Unset, LocalTime]
        if isinstance(_end_time, Unset):
            end_time = UNSET
        else:
            end_time = LocalTime.from_dict(_end_time)

        _end_date = d.pop("endDate", UNSET)
        end_date: Union[Unset, datetime.date]
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date).date()

        start_text = d.pop("startText", UNSET)

        end_text = d.pop("endText", UNSET)

        _daily_starting_at = d.pop("dailyStartingAt", UNSET)
        daily_starting_at: Union[Unset, LocalTime]
        if isinstance(_daily_starting_at, Unset):
            daily_starting_at = UNSET
        else:
            daily_starting_at = LocalTime.from_dict(_daily_starting_at)

        daily_duration = d.pop("dailyDuration", UNSET)

        _service_days = d.pop("serviceDays", UNSET)
        service_days: Union[Unset, ServiceDaysV2]
        if isinstance(_service_days, Unset):
            service_days = UNSET
        else:
            service_days = ServiceDaysV2.from_dict(_service_days)

        transport_products = []
        _transport_products = d.pop("transportProducts", UNSET)
        for transport_products_item_data in _transport_products or []:
            transport_products_item = TransportProductV2.from_dict(transport_products_item_data)

            transport_products.append(transport_products_item)

        him_message_v2 = cls(
            id=id,
            priority=priority,
            formatted_header=formatted_header,
            formatted_footer=formatted_footer,
            formatted_footer_short=formatted_footer_short,
            channels=channels,
            edges=edges,
            regions=regions,
            category=category,
            valid_from_stop=valid_from_stop,
            valid_from_stop_name=valid_from_stop_name,
            valid_to_stop=valid_to_stop,
            valid_to_stop_name=valid_to_stop_name,
            route_index_from=route_index_from,
            route_index_to=route_index_to,
            start_time=start_time,
            start_date=start_date,
            end_time=end_time,
            end_date=end_date,
            start_text=start_text,
            end_text=end_text,
            daily_starting_at=daily_starting_at,
            daily_duration=daily_duration,
            service_days=service_days,
            transport_products=transport_products,
        )

        him_message_v2.additional_properties = d
        return him_message_v2

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
