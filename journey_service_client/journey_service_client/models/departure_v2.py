from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.departure_v2_journey_status import DepartureV2JourneyStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.him_message_v2 import HimMessageV2
    from ..models.note import Note
    from ..models.service_days_v2 import ServiceDaysV2
    from ..models.stop_v2 import StopV2
    from ..models.transport_product_v2 import TransportProductV2


T = TypeVar("T", bound="DepartureV2")


@_attrs_define
class DepartureV2:
    """Departure resp. kind of view of JourneyDetail from a specific stop towards its direction.

    Attributes:
        journey_reference (str): Underlying system specific unique identifier representing a concrete (partial) route
            for a specific vehicle and time. Be aware this is just a temporary id and may change daily! Example:
            1|17166|0|85|18032019.
        journey_status (DepartureV2JourneyStatus): Contains the status of the journey. Example: PLANNED.
        transport_products (List['TransportProductV2']):
        origin (StopV2): A stop represents a specific location (typically a STATION) of a leg or a complete journey-
            detail of a transport-product (aka v3.ScheduledStopPoint, OJP StopPoint).
        stops (List['StopV2']):
        attributes (List['Note']):
        service_days (List['ServiceDaysV2']):
        messages (List['HimMessageV2']):
        cancelled (bool): true: Journey is `cancelled` (de:Ausfall), default=false.
        partially_cancelled (bool): true: Journey is partially cancelled (de:Teilausfall) at beginning or end,
            default=false.
        reachable (bool): true: journey is reachable (de:erreichbar)
        redirected (bool): true: journey is redirected (de:Umleitung)
        transport_product (Union[Unset, TransportProductV2]): Kind of a speaking identifier of a travelling product,
            like a concrete SBB operated train between Bern-Zürich at 14:34, for eg. 'IR 16 2177'.
            The TransportProduct relates to StopBehaviour request params, where 'ORIGIN_DESTINATION_ONLY' returns [0..1]
            transport-product (related to origin) typically without routeIndices, where other values of StopBehaviour may
            return several transport-products with given routeIndices segments.
        direction (Union[Unset, StopV2]): A stop represents a specific location (typically a STATION) of a leg or a
            complete journey-detail of a transport-product (aka v3.ScheduledStopPoint, OJP StopPoint).
        cancelled_formatted (Union[Unset, str]): If `cancelled`, enduser cancellation info.<br>(Translated according to
            Accept-Language.) Example: Ausfall.
        partially_cancelled_formatted (Union[Unset, str]): If `partiallyCancelled`, enduser info.<br>(Translated
            according to Accept-Language.) Example: Ausfall.
        redirected_formatted (Union[Unset, str]): Text intended for passengers about a planned stop being skipped,
            relates to `redirected`.<br>(Translated according to Accept-Language.) Example: This vehicle is not stopping at
            all stations..
        unplanned_stops_formatted (Union[Unset, str]): Text intended for passengers about an additional non-planned stop
            at a station.<br>(Translated according to Accept-Language.) Example: This vehicle is making exceptional stops.
            This can lead to increased travel time..
    """

    journey_reference: str
    journey_status: DepartureV2JourneyStatus
    transport_products: List["TransportProductV2"]
    origin: "StopV2"
    stops: List["StopV2"]
    attributes: List["Note"]
    service_days: List["ServiceDaysV2"]
    messages: List["HimMessageV2"]
    cancelled: bool
    partially_cancelled: bool
    reachable: bool
    redirected: bool
    transport_product: Union[Unset, "TransportProductV2"] = UNSET
    direction: Union[Unset, "StopV2"] = UNSET
    cancelled_formatted: Union[Unset, str] = UNSET
    partially_cancelled_formatted: Union[Unset, str] = UNSET
    redirected_formatted: Union[Unset, str] = UNSET
    unplanned_stops_formatted: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        journey_reference = self.journey_reference
        journey_status = self.journey_status.value

        transport_products = []
        for transport_products_item_data in self.transport_products:
            transport_products_item = transport_products_item_data.to_dict()

            transport_products.append(transport_products_item)

        origin = self.origin.to_dict()

        stops = []
        for stops_item_data in self.stops:
            stops_item = stops_item_data.to_dict()

            stops.append(stops_item)

        attributes = []
        for attributes_item_data in self.attributes:
            attributes_item = attributes_item_data.to_dict()

            attributes.append(attributes_item)

        service_days = []
        for service_days_item_data in self.service_days:
            service_days_item = service_days_item_data.to_dict()

            service_days.append(service_days_item)

        messages = []
        for messages_item_data in self.messages:
            messages_item = messages_item_data.to_dict()

            messages.append(messages_item)

        cancelled = self.cancelled
        partially_cancelled = self.partially_cancelled
        reachable = self.reachable
        redirected = self.redirected
        transport_product: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.transport_product, Unset):
            transport_product = self.transport_product.to_dict()

        direction: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.direction, Unset):
            direction = self.direction.to_dict()

        cancelled_formatted = self.cancelled_formatted
        partially_cancelled_formatted = self.partially_cancelled_formatted
        redirected_formatted = self.redirected_formatted
        unplanned_stops_formatted = self.unplanned_stops_formatted

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "journeyReference": journey_reference,
                "journeyStatus": journey_status,
                "transportProducts": transport_products,
                "origin": origin,
                "stops": stops,
                "attributes": attributes,
                "serviceDays": service_days,
                "messages": messages,
                "cancelled": cancelled,
                "partiallyCancelled": partially_cancelled,
                "reachable": reachable,
                "redirected": redirected,
            }
        )
        if transport_product is not UNSET:
            field_dict["transportProduct"] = transport_product
        if direction is not UNSET:
            field_dict["direction"] = direction
        if cancelled_formatted is not UNSET:
            field_dict["cancelledFormatted"] = cancelled_formatted
        if partially_cancelled_formatted is not UNSET:
            field_dict["partiallyCancelledFormatted"] = partially_cancelled_formatted
        if redirected_formatted is not UNSET:
            field_dict["redirectedFormatted"] = redirected_formatted
        if unplanned_stops_formatted is not UNSET:
            field_dict["unplannedStopsFormatted"] = unplanned_stops_formatted

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.him_message_v2 import HimMessageV2
        from ..models.note import Note
        from ..models.service_days_v2 import ServiceDaysV2
        from ..models.stop_v2 import StopV2
        from ..models.transport_product_v2 import TransportProductV2

        d = src_dict.copy()
        journey_reference = d.pop("journeyReference")

        journey_status = DepartureV2JourneyStatus(d.pop("journeyStatus"))

        transport_products = []
        _transport_products = d.pop("transportProducts")
        for transport_products_item_data in _transport_products:
            transport_products_item = TransportProductV2.from_dict(transport_products_item_data)

            transport_products.append(transport_products_item)

        origin = StopV2.from_dict(d.pop("origin"))

        stops = []
        _stops = d.pop("stops")
        for stops_item_data in _stops:
            stops_item = StopV2.from_dict(stops_item_data)

            stops.append(stops_item)

        attributes = []
        _attributes = d.pop("attributes")
        for attributes_item_data in _attributes:
            attributes_item = Note.from_dict(attributes_item_data)

            attributes.append(attributes_item)

        service_days = []
        _service_days = d.pop("serviceDays")
        for service_days_item_data in _service_days:
            service_days_item = ServiceDaysV2.from_dict(service_days_item_data)

            service_days.append(service_days_item)

        messages = []
        _messages = d.pop("messages")
        for messages_item_data in _messages:
            messages_item = HimMessageV2.from_dict(messages_item_data)

            messages.append(messages_item)

        cancelled = d.pop("cancelled")

        partially_cancelled = d.pop("partiallyCancelled")

        reachable = d.pop("reachable")

        redirected = d.pop("redirected")

        _transport_product = d.pop("transportProduct", UNSET)
        transport_product: Union[Unset, TransportProductV2]
        if isinstance(_transport_product, Unset):
            transport_product = UNSET
        else:
            transport_product = TransportProductV2.from_dict(_transport_product)

        _direction = d.pop("direction", UNSET)
        direction: Union[Unset, StopV2]
        if isinstance(_direction, Unset):
            direction = UNSET
        else:
            direction = StopV2.from_dict(_direction)

        cancelled_formatted = d.pop("cancelledFormatted", UNSET)

        partially_cancelled_formatted = d.pop("partiallyCancelledFormatted", UNSET)

        redirected_formatted = d.pop("redirectedFormatted", UNSET)

        unplanned_stops_formatted = d.pop("unplannedStopsFormatted", UNSET)

        departure_v2 = cls(
            journey_reference=journey_reference,
            journey_status=journey_status,
            transport_products=transport_products,
            origin=origin,
            stops=stops,
            attributes=attributes,
            service_days=service_days,
            messages=messages,
            cancelled=cancelled,
            partially_cancelled=partially_cancelled,
            reachable=reachable,
            redirected=redirected,
            transport_product=transport_product,
            direction=direction,
            cancelled_formatted=cancelled_formatted,
            partially_cancelled_formatted=partially_cancelled_formatted,
            redirected_formatted=redirected_formatted,
            unplanned_stops_formatted=unplanned_stops_formatted,
        )

        departure_v2.additional_properties = d
        return departure_v2

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
