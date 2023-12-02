from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.leg_v2_formation_hint import LegV2FormationHint
from ..models.leg_v2_group_reservation_status import LegV2GroupReservationStatus
from ..models.leg_v2_journey_status import LegV2JourneyStatus
from ..models.leg_v2_type import LegV2Type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.formation_alert import FormationAlert
    from ..models.him_message_v2 import HimMessageV2
    from ..models.note import Note
    from ..models.pagination_cursor import PaginationCursor
    from ..models.service_days_v2 import ServiceDaysV2
    from ..models.stop_v2 import StopV2
    from ..models.transport_product_v2 import TransportProductV2


T = TypeVar("T", bound="LegV2")


@_attrs_define
class LegV2:
    """A trip consists of [1..*] legs, where a leg represents a part of the travelling route (for e.g. from A to B) with
    the same type of transportation (typically by public transportation or by foot).

        Attributes:
            type (LegV2Type): Type of leg indicates what kind of transportation is implicated (supported by SBB:
                PUBLIC_JOURNEY, FOOTPATH, TRANSFER, CAR_ROUTE).
            stops (List['StopV2']):
            transport_products (List['TransportProductV2']):
            service_days (List['ServiceDaysV2']):
            duration (str): The [duration](https://www.w3.org/TR/xmlschema11-2/#duration) leg::origin to leg::destination in
                realtime. If a Leg is not rideable (for e.g. cancelled), the value may be ZERO. Example: P1DT2H4M.
            messages (List['HimMessageV2']):
            cancelled (bool): true: Journey is `cancelled` (de:Ausfall), default=false.
            partially_cancelled (bool): true: Journey is partially cancelled (de:Teilausfall) at beginning or end,
                default=false.
            reachable (bool): true: transport-product change from Leg to Leg is reachable (de: Anschluss kann gehalten
                werden, see TripV2::valid); false: de:nicht mehr erreichbare Fahrt
            redirected (bool): true: journey is redirected
            attributes (List['Note']):
            infos (List['Note']):
            index (int): Leg's are ordered within its Trip riding sequence starting from 0 and incrementing by 1.
            distance (Union[Unset, int]): Distance for this leg in meter.
            direction (Union[Unset, str]): Direction information correlating to Vehicle or Perron display. Typically the
                last stop-point of the associated line, though for operational or commercial reasons, the direction can also be
                a stop-over if the passengers are to be published a destination that makes sense in relation to their place of
                departure.
            journey_status (Union[Unset, LegV2JourneyStatus]): @Deprecated Contains the status of the journey. Given for
                LegType.PUBLIC_JOURNEY only.
            journey_reference (Union[Unset, str]): Underlying system specific unique identifier representing a concrete
                (partial) route for a specific vehicle and time. Be aware this is just a temporary id and may change daily!
                (Required for LegType.PUBLIC_JOURNEY.) Example: 1|17166|0|85|18032019.
            cancelled_formatted (Union[Unset, str]): If `cancelled`, enduser cancellation info.<br>(Translated according to
                Accept-Language.) Example: Ausfall.
            partially_cancelled_formatted (Union[Unset, str]): If `partiallyCancelled`, enduser info.<br>(Translated
                according to Accept-Language.) Example: Ausfall.
            reachable_formatted (Union[Unset, str]): Transport-product change from Leg to Leg info according to SBB business
                rules. Relates to reachable.<br>(Translated according to Accept-Language.) Example: Your connecting train will
                be waiting, please change trains immediately..
            redirected_formatted (Union[Unset, str]): Text intended for passengers about a planned stop being skipped,
                relates to `redirected`.<br>(Translated according to Accept-Language.) Example: This vehicle is not stopping at
                all stations..
            unplanned_stops_formatted (Union[Unset, str]): Text intended for passengers about an additional non-planned stop
                at a station.<br>(Translated according to Accept-Language.) Example: This vehicle is making exceptional stops.
                This can lead to increased travel time..
            formation_hint (Union[Unset, LegV2FormationHint]): Just a hint whether a Formation is available for this Leg.
                Set trainFormationType=ORIGIN_DESTINATION to force this info and call v2/trips/trainFormation afterwards only if
                flags signal availability of a formation to reduce unnecessary requests.
            formation_alert (Union[Unset, FormationAlert]): Contains any Formation rt infos (such as changed wagons, ..) on
                PUBLIC_TRANSPORTATION LegV2. Depends on v2/trips parameter trainFormationType.
            polyline_formatted (Union[Unset, str]): String list of WGS84 coordinates in `latitude,longitude|..` pairs' (J-S
                v2 proprietary representation and vice versa to GeoJSON lon/lat order!!!) and represents a de:Streckenverlauf.
                Depends on polyline=true. Example: 46.44,7.99|47.234,7.956|...
            delayed_formatted (Union[Unset, str]): Enduser text, saying whether there is a delay on Leg (referring to
                first/last Stop).<br>(Translated according to Accept-Language.) Example: Delay.
            platform_changed_formatted (Union[Unset, str]): Enduser text, saying whether there is a platform change on Leg
                (referring to first and/or last Stop on leg), which indicates the passengers to check carefully at
                boarding/alighting.<br>(Translated according to Accept-Language.) Example: Gleisänderung.
            group_reservation_status (Union[Unset, LegV2GroupReservationStatus]): Denotes if reservations are possible for
                groups on this specific trip. Set only if enforced by related param `includeGroupReservation`.
            pagination_cursor (Union[Unset, PaginationCursor]): Pagination-cursor for next/previous of the same. By means in
                a Trip context earlier/later.
    """

    type: LegV2Type
    stops: List["StopV2"]
    transport_products: List["TransportProductV2"]
    service_days: List["ServiceDaysV2"]
    duration: str
    messages: List["HimMessageV2"]
    cancelled: bool
    partially_cancelled: bool
    reachable: bool
    redirected: bool
    attributes: List["Note"]
    infos: List["Note"]
    index: int
    distance: Union[Unset, int] = UNSET
    direction: Union[Unset, str] = UNSET
    journey_status: Union[Unset, LegV2JourneyStatus] = UNSET
    journey_reference: Union[Unset, str] = UNSET
    cancelled_formatted: Union[Unset, str] = UNSET
    partially_cancelled_formatted: Union[Unset, str] = UNSET
    reachable_formatted: Union[Unset, str] = UNSET
    redirected_formatted: Union[Unset, str] = UNSET
    unplanned_stops_formatted: Union[Unset, str] = UNSET
    formation_hint: Union[Unset, LegV2FormationHint] = UNSET
    formation_alert: Union[Unset, "FormationAlert"] = UNSET
    polyline_formatted: Union[Unset, str] = UNSET
    delayed_formatted: Union[Unset, str] = UNSET
    platform_changed_formatted: Union[Unset, str] = UNSET
    group_reservation_status: Union[Unset, LegV2GroupReservationStatus] = UNSET
    pagination_cursor: Union[Unset, "PaginationCursor"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        stops = []
        for stops_item_data in self.stops:
            stops_item = stops_item_data.to_dict()

            stops.append(stops_item)

        transport_products = []
        for transport_products_item_data in self.transport_products:
            transport_products_item = transport_products_item_data.to_dict()

            transport_products.append(transport_products_item)

        service_days = []
        for service_days_item_data in self.service_days:
            service_days_item = service_days_item_data.to_dict()

            service_days.append(service_days_item)

        duration = self.duration
        messages = []
        for messages_item_data in self.messages:
            messages_item = messages_item_data.to_dict()

            messages.append(messages_item)

        cancelled = self.cancelled
        partially_cancelled = self.partially_cancelled
        reachable = self.reachable
        redirected = self.redirected
        attributes = []
        for attributes_item_data in self.attributes:
            attributes_item = attributes_item_data.to_dict()

            attributes.append(attributes_item)

        infos = []
        for infos_item_data in self.infos:
            infos_item = infos_item_data.to_dict()

            infos.append(infos_item)

        index = self.index
        distance = self.distance
        direction = self.direction
        journey_status: Union[Unset, str] = UNSET
        if not isinstance(self.journey_status, Unset):
            journey_status = self.journey_status.value

        journey_reference = self.journey_reference
        cancelled_formatted = self.cancelled_formatted
        partially_cancelled_formatted = self.partially_cancelled_formatted
        reachable_formatted = self.reachable_formatted
        redirected_formatted = self.redirected_formatted
        unplanned_stops_formatted = self.unplanned_stops_formatted
        formation_hint: Union[Unset, str] = UNSET
        if not isinstance(self.formation_hint, Unset):
            formation_hint = self.formation_hint.value

        formation_alert: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.formation_alert, Unset):
            formation_alert = self.formation_alert.to_dict()

        polyline_formatted = self.polyline_formatted
        delayed_formatted = self.delayed_formatted
        platform_changed_formatted = self.platform_changed_formatted
        group_reservation_status: Union[Unset, str] = UNSET
        if not isinstance(self.group_reservation_status, Unset):
            group_reservation_status = self.group_reservation_status.value

        pagination_cursor: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pagination_cursor, Unset):
            pagination_cursor = self.pagination_cursor.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "stops": stops,
                "transportProducts": transport_products,
                "serviceDays": service_days,
                "duration": duration,
                "messages": messages,
                "cancelled": cancelled,
                "partiallyCancelled": partially_cancelled,
                "reachable": reachable,
                "redirected": redirected,
                "attributes": attributes,
                "infos": infos,
                "index": index,
            }
        )
        if distance is not UNSET:
            field_dict["distance"] = distance
        if direction is not UNSET:
            field_dict["direction"] = direction
        if journey_status is not UNSET:
            field_dict["journeyStatus"] = journey_status
        if journey_reference is not UNSET:
            field_dict["journeyReference"] = journey_reference
        if cancelled_formatted is not UNSET:
            field_dict["cancelledFormatted"] = cancelled_formatted
        if partially_cancelled_formatted is not UNSET:
            field_dict["partiallyCancelledFormatted"] = partially_cancelled_formatted
        if reachable_formatted is not UNSET:
            field_dict["reachableFormatted"] = reachable_formatted
        if redirected_formatted is not UNSET:
            field_dict["redirectedFormatted"] = redirected_formatted
        if unplanned_stops_formatted is not UNSET:
            field_dict["unplannedStopsFormatted"] = unplanned_stops_formatted
        if formation_hint is not UNSET:
            field_dict["formationHint"] = formation_hint
        if formation_alert is not UNSET:
            field_dict["formationAlert"] = formation_alert
        if polyline_formatted is not UNSET:
            field_dict["polylineFormatted"] = polyline_formatted
        if delayed_formatted is not UNSET:
            field_dict["delayedFormatted"] = delayed_formatted
        if platform_changed_formatted is not UNSET:
            field_dict["platformChangedFormatted"] = platform_changed_formatted
        if group_reservation_status is not UNSET:
            field_dict["groupReservationStatus"] = group_reservation_status
        if pagination_cursor is not UNSET:
            field_dict["paginationCursor"] = pagination_cursor

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.formation_alert import FormationAlert
        from ..models.him_message_v2 import HimMessageV2
        from ..models.note import Note
        from ..models.pagination_cursor import PaginationCursor
        from ..models.service_days_v2 import ServiceDaysV2
        from ..models.stop_v2 import StopV2
        from ..models.transport_product_v2 import TransportProductV2

        d = src_dict.copy()
        type = LegV2Type(d.pop("type"))

        stops = []
        _stops = d.pop("stops")
        for stops_item_data in _stops:
            stops_item = StopV2.from_dict(stops_item_data)

            stops.append(stops_item)

        transport_products = []
        _transport_products = d.pop("transportProducts")
        for transport_products_item_data in _transport_products:
            transport_products_item = TransportProductV2.from_dict(transport_products_item_data)

            transport_products.append(transport_products_item)

        service_days = []
        _service_days = d.pop("serviceDays")
        for service_days_item_data in _service_days:
            service_days_item = ServiceDaysV2.from_dict(service_days_item_data)

            service_days.append(service_days_item)

        duration = d.pop("duration")

        messages = []
        _messages = d.pop("messages")
        for messages_item_data in _messages:
            messages_item = HimMessageV2.from_dict(messages_item_data)

            messages.append(messages_item)

        cancelled = d.pop("cancelled")

        partially_cancelled = d.pop("partiallyCancelled")

        reachable = d.pop("reachable")

        redirected = d.pop("redirected")

        attributes = []
        _attributes = d.pop("attributes")
        for attributes_item_data in _attributes:
            attributes_item = Note.from_dict(attributes_item_data)

            attributes.append(attributes_item)

        infos = []
        _infos = d.pop("infos")
        for infos_item_data in _infos:
            infos_item = Note.from_dict(infos_item_data)

            infos.append(infos_item)

        index = d.pop("index")

        distance = d.pop("distance", UNSET)

        direction = d.pop("direction", UNSET)

        _journey_status = d.pop("journeyStatus", UNSET)
        journey_status: Union[Unset, LegV2JourneyStatus]
        if isinstance(_journey_status, Unset):
            journey_status = UNSET
        else:
            journey_status = LegV2JourneyStatus(_journey_status)

        journey_reference = d.pop("journeyReference", UNSET)

        cancelled_formatted = d.pop("cancelledFormatted", UNSET)

        partially_cancelled_formatted = d.pop("partiallyCancelledFormatted", UNSET)

        reachable_formatted = d.pop("reachableFormatted", UNSET)

        redirected_formatted = d.pop("redirectedFormatted", UNSET)

        unplanned_stops_formatted = d.pop("unplannedStopsFormatted", UNSET)

        _formation_hint = d.pop("formationHint", UNSET)
        formation_hint: Union[Unset, LegV2FormationHint]
        if isinstance(_formation_hint, Unset):
            formation_hint = UNSET
        else:
            formation_hint = LegV2FormationHint(_formation_hint)

        _formation_alert = d.pop("formationAlert", UNSET)
        formation_alert: Union[Unset, FormationAlert]
        if isinstance(_formation_alert, Unset):
            formation_alert = UNSET
        else:
            formation_alert = FormationAlert.from_dict(_formation_alert)

        polyline_formatted = d.pop("polylineFormatted", UNSET)

        delayed_formatted = d.pop("delayedFormatted", UNSET)

        platform_changed_formatted = d.pop("platformChangedFormatted", UNSET)

        _group_reservation_status = d.pop("groupReservationStatus", UNSET)
        group_reservation_status: Union[Unset, LegV2GroupReservationStatus]
        if isinstance(_group_reservation_status, Unset):
            group_reservation_status = UNSET
        else:
            group_reservation_status = LegV2GroupReservationStatus(_group_reservation_status)

        _pagination_cursor = d.pop("paginationCursor", UNSET)
        pagination_cursor: Union[Unset, PaginationCursor]
        if isinstance(_pagination_cursor, Unset):
            pagination_cursor = UNSET
        else:
            pagination_cursor = PaginationCursor.from_dict(_pagination_cursor)

        leg_v2 = cls(
            type=type,
            stops=stops,
            transport_products=transport_products,
            service_days=service_days,
            duration=duration,
            messages=messages,
            cancelled=cancelled,
            partially_cancelled=partially_cancelled,
            reachable=reachable,
            redirected=redirected,
            attributes=attributes,
            infos=infos,
            index=index,
            distance=distance,
            direction=direction,
            journey_status=journey_status,
            journey_reference=journey_reference,
            cancelled_formatted=cancelled_formatted,
            partially_cancelled_formatted=partially_cancelled_formatted,
            reachable_formatted=reachable_formatted,
            redirected_formatted=redirected_formatted,
            unplanned_stops_formatted=unplanned_stops_formatted,
            formation_hint=formation_hint,
            formation_alert=formation_alert,
            polyline_formatted=polyline_formatted,
            delayed_formatted=delayed_formatted,
            platform_changed_formatted=platform_changed_formatted,
            group_reservation_status=group_reservation_status,
            pagination_cursor=pagination_cursor,
        )

        leg_v2.additional_properties = d
        return leg_v2

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
