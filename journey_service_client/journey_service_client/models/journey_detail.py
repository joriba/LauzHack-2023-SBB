from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.journey_detail_journey_status import JourneyDetailJourneyStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.direction_v2 import DirectionV2
    from ..models.him_message_v2 import HimMessageV2
    from ..models.note import Note
    from ..models.service_days_v2 import ServiceDaysV2
    from ..models.stop_v2 import StopV2
    from ..models.transport_product_v2 import TransportProductV2


T = TypeVar("T", bound="JourneyDetail")


@_attrs_define
class JourneyDetail:
    """Complete route (de:Zuglauf) of a transport product.

    Attributes:
        stops (List['StopV2']):
        journey_status (JourneyDetailJourneyStatus): Contains the status of the journey.
        directions (List['DirectionV2']):
        transport_products (List['TransportProductV2']):
        him_messages (List['HimMessageV2']):
        journey_reference (str): Underlying system specific unique identifier representing a concrete (partial) route
            for a specific vehicle and time. Be aware this is just a temporary id and may change daily! Example:
            1|17166|0|85|18032019.
        service_days (List['ServiceDaysV2']):
        cancelled (bool): true: Journey is `cancelled` (de:Ausfall), default=false.
        partially_cancelled (bool): true: Journey is partially cancelled (de:Teilausfall) at beginning or end,
            default=false.
        reachable (bool): Whether journey is reachable.
        redirected (bool): Whether journey is redirected.
        attributes (List['Note']):
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
        polyline_formatted (Union[Unset, str]): String list of WGS84 coordinates (optimized for min. volume and fast
            parsing.) and represents a de:Streckenverlauf. Depends on polyline=true Example:
            latitude0,longitude0|latitude1,longitude1|...
    """

    stops: List["StopV2"]
    journey_status: JourneyDetailJourneyStatus
    directions: List["DirectionV2"]
    transport_products: List["TransportProductV2"]
    him_messages: List["HimMessageV2"]
    journey_reference: str
    service_days: List["ServiceDaysV2"]
    cancelled: bool
    partially_cancelled: bool
    reachable: bool
    redirected: bool
    attributes: List["Note"]
    cancelled_formatted: Union[Unset, str] = UNSET
    partially_cancelled_formatted: Union[Unset, str] = UNSET
    redirected_formatted: Union[Unset, str] = UNSET
    unplanned_stops_formatted: Union[Unset, str] = UNSET
    polyline_formatted: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        stops = []
        for stops_item_data in self.stops:
            stops_item = stops_item_data.to_dict()

            stops.append(stops_item)

        journey_status = self.journey_status.value

        directions = []
        for directions_item_data in self.directions:
            directions_item = directions_item_data.to_dict()

            directions.append(directions_item)

        transport_products = []
        for transport_products_item_data in self.transport_products:
            transport_products_item = transport_products_item_data.to_dict()

            transport_products.append(transport_products_item)

        him_messages = []
        for him_messages_item_data in self.him_messages:
            him_messages_item = him_messages_item_data.to_dict()

            him_messages.append(him_messages_item)

        journey_reference = self.journey_reference
        service_days = []
        for service_days_item_data in self.service_days:
            service_days_item = service_days_item_data.to_dict()

            service_days.append(service_days_item)

        cancelled = self.cancelled
        partially_cancelled = self.partially_cancelled
        reachable = self.reachable
        redirected = self.redirected
        attributes = []
        for attributes_item_data in self.attributes:
            attributes_item = attributes_item_data.to_dict()

            attributes.append(attributes_item)

        cancelled_formatted = self.cancelled_formatted
        partially_cancelled_formatted = self.partially_cancelled_formatted
        redirected_formatted = self.redirected_formatted
        unplanned_stops_formatted = self.unplanned_stops_formatted
        polyline_formatted = self.polyline_formatted

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stops": stops,
                "journeyStatus": journey_status,
                "directions": directions,
                "transportProducts": transport_products,
                "himMessages": him_messages,
                "journeyReference": journey_reference,
                "serviceDays": service_days,
                "cancelled": cancelled,
                "partiallyCancelled": partially_cancelled,
                "reachable": reachable,
                "redirected": redirected,
                "attributes": attributes,
            }
        )
        if cancelled_formatted is not UNSET:
            field_dict["cancelledFormatted"] = cancelled_formatted
        if partially_cancelled_formatted is not UNSET:
            field_dict["partiallyCancelledFormatted"] = partially_cancelled_formatted
        if redirected_formatted is not UNSET:
            field_dict["redirectedFormatted"] = redirected_formatted
        if unplanned_stops_formatted is not UNSET:
            field_dict["unplannedStopsFormatted"] = unplanned_stops_formatted
        if polyline_formatted is not UNSET:
            field_dict["polylineFormatted"] = polyline_formatted

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.direction_v2 import DirectionV2
        from ..models.him_message_v2 import HimMessageV2
        from ..models.note import Note
        from ..models.service_days_v2 import ServiceDaysV2
        from ..models.stop_v2 import StopV2
        from ..models.transport_product_v2 import TransportProductV2

        d = src_dict.copy()
        stops = []
        _stops = d.pop("stops")
        for stops_item_data in _stops:
            stops_item = StopV2.from_dict(stops_item_data)

            stops.append(stops_item)

        journey_status = JourneyDetailJourneyStatus(d.pop("journeyStatus"))

        directions = []
        _directions = d.pop("directions")
        for directions_item_data in _directions:
            directions_item = DirectionV2.from_dict(directions_item_data)

            directions.append(directions_item)

        transport_products = []
        _transport_products = d.pop("transportProducts")
        for transport_products_item_data in _transport_products:
            transport_products_item = TransportProductV2.from_dict(transport_products_item_data)

            transport_products.append(transport_products_item)

        him_messages = []
        _him_messages = d.pop("himMessages")
        for him_messages_item_data in _him_messages:
            him_messages_item = HimMessageV2.from_dict(him_messages_item_data)

            him_messages.append(him_messages_item)

        journey_reference = d.pop("journeyReference")

        service_days = []
        _service_days = d.pop("serviceDays")
        for service_days_item_data in _service_days:
            service_days_item = ServiceDaysV2.from_dict(service_days_item_data)

            service_days.append(service_days_item)

        cancelled = d.pop("cancelled")

        partially_cancelled = d.pop("partiallyCancelled")

        reachable = d.pop("reachable")

        redirected = d.pop("redirected")

        attributes = []
        _attributes = d.pop("attributes")
        for attributes_item_data in _attributes:
            attributes_item = Note.from_dict(attributes_item_data)

            attributes.append(attributes_item)

        cancelled_formatted = d.pop("cancelledFormatted", UNSET)

        partially_cancelled_formatted = d.pop("partiallyCancelledFormatted", UNSET)

        redirected_formatted = d.pop("redirectedFormatted", UNSET)

        unplanned_stops_formatted = d.pop("unplannedStopsFormatted", UNSET)

        polyline_formatted = d.pop("polylineFormatted", UNSET)

        journey_detail = cls(
            stops=stops,
            journey_status=journey_status,
            directions=directions,
            transport_products=transport_products,
            him_messages=him_messages,
            journey_reference=journey_reference,
            service_days=service_days,
            cancelled=cancelled,
            partially_cancelled=partially_cancelled,
            reachable=reachable,
            redirected=redirected,
            attributes=attributes,
            cancelled_formatted=cancelled_formatted,
            partially_cancelled_formatted=partially_cancelled_formatted,
            redirected_formatted=redirected_formatted,
            unplanned_stops_formatted=unplanned_stops_formatted,
            polyline_formatted=polyline_formatted,
        )

        journey_detail.additional_properties = d
        return journey_detail

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
