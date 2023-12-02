from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.transport_product_v2_category import TransportProductV2Category
from ..models.transport_product_v2_vehicle_type import TransportProductV2VehicleType
from ..types import UNSET, Unset

T = TypeVar("T", bound="TransportProductV2")


@_attrs_define
class TransportProductV2:
    """Kind of a speaking identifier of a travelling product, like a concrete SBB operated train between Bern-Zürich at
    14:34, for eg. 'IR 16 2177'.
    The TransportProduct relates to StopBehaviour request params, where 'ORIGIN_DESTINATION_ONLY' returns [0..1]
    transport-product (related to origin) typically without routeIndices, where other values of StopBehaviour may return
    several transport-products with given routeIndices segments.

        Attributes:
            name (Union[Unset, str]): Usually displayed name for a travelling end-user. Example: IC 1 753.
            number_formatted (Union[Unset, str]): Either as number or suppressed by BR. Display by B2C enduser channels to
                not bother passengers with TU internal number. Example: 753.
            number (Union[Unset, str]): Unique per operating day (CH until 04:00) and name (where 'IC 1' can run several
                times per day in either of opposite directions). Example: 753.
            line (Union[Unset, str]): Usually referring to a specific physical route (JourneyDetail where direction is
                either way). If this value is missing, it is probably a _single-journey (de:Einzelfahrt)_. Example: 1.
            line_reference (Union[Unset, str]): External line-reference (e.g. relevant for Postauto AG), relates to `line`.
                Example: R_547_000801_0883.
            category (Union[Unset, TransportProductV2Category]): @Deprecated Use other more speaking category* properties!
                Category of transport-product (class managed by SBB Data-Mgmt). Example: INTERREGIO.
            category_code (Union[Unset, int]): @Deprecated Corresponding numeric value of category (no use unless you deal
                with Hafas directly). Example: 2.
            category_short_form (Union[Unset, str]): Short, displayable name of category. Example: IC.
            category_long_form (Union[Unset, str]): Long, displayable name of category. Example: InterCity.
            operator_name (Union[Unset, str]): Fullname of responsible operator (translatable), relates to operatorNumber.
                This value matches with [OpenTransportData.swiss GoList field
                'BEZEICHNUNG_DE'](https://opentransportdata.swiss/de/dataset/goch)<br>(Translated according to Accept-Language.)
                Example: Schweizerische Bundesbahnen SBB.
            operator_short_name (Union[Unset, str]): Abbreviation of operator (translatable), relates to operatorName. This
                value might differ from OpenTransportData.swiss abbreviation (there are 3 different versions, J-S supports
                3-digit abbreviation).<br>(Translated according to Accept-Language.) Example: SBB.
            operator_number (Union[Unset, str]): DiDok/INFO+/Plabe related operator-number (typically Integer for CH managed
                codes, however some TU's like in foreign countries might return String expressions like '80___'), relates to
                operatorName.
                NOVA does not accept trimmed numbers! Example: 000011.
            route_index_from (Union[Unset, int]): Defines the first stop/station where this product is valid. Example: 3.
            route_index_to (Union[Unset, int]): Defines the last stop/station where this product is valid. Example: 7.
            track_translation (Union[Unset, str]): Depending on a train, ship or whatever product there is specific
                terminology for its appropriate track.<br>(Translated according to Accept-Language.) Example: de:Gleis, fr:Voie.
            track_translation_short (Union[Unset, str]): Abbreviation for trackTranslation.<br>(Translated according to
                Accept-Language.) Example: de:Gl..
            vehicle_type (Union[Unset, TransportProductV2VehicleType]): v580 type (de:Gattung). SBB knows BUS, TRAMWAY
                (including METRO), BOAT, CABLEWAY (~v580) and TRAIN, other types are rather future use, see [v580
                de:Verkehrsmittelkategorien (aka Transmodel or OJP/Siri
                `VehicleMode`)](https://github.com/SchweizerischeBundesbahnen/journey-service/blob/master/TransportMode.md).
                Example: TRAIN.
            vehicle_icon_name (Union[Unset, str]): v580 type (de:Gattung) icon-name according to SBB Corporate-Identity,
                relates to `vehicleType` (see [Preview Produktion - L00 SVG Sprites - blue icons suffix for e.g. Train
                'SBB_oev_b_t02'](https://previewserver.sbb.ch/#/project/SBBCH). Example: SBB_oev_b_t02.
    """

    name: Union[Unset, str] = UNSET
    number_formatted: Union[Unset, str] = UNSET
    number: Union[Unset, str] = UNSET
    line: Union[Unset, str] = UNSET
    line_reference: Union[Unset, str] = UNSET
    category: Union[Unset, TransportProductV2Category] = UNSET
    category_code: Union[Unset, int] = UNSET
    category_short_form: Union[Unset, str] = UNSET
    category_long_form: Union[Unset, str] = UNSET
    operator_name: Union[Unset, str] = UNSET
    operator_short_name: Union[Unset, str] = UNSET
    operator_number: Union[Unset, str] = UNSET
    route_index_from: Union[Unset, int] = UNSET
    route_index_to: Union[Unset, int] = UNSET
    track_translation: Union[Unset, str] = UNSET
    track_translation_short: Union[Unset, str] = UNSET
    vehicle_type: Union[Unset, TransportProductV2VehicleType] = UNSET
    vehicle_icon_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        number_formatted = self.number_formatted
        number = self.number
        line = self.line
        line_reference = self.line_reference
        category: Union[Unset, str] = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.value

        category_code = self.category_code
        category_short_form = self.category_short_form
        category_long_form = self.category_long_form
        operator_name = self.operator_name
        operator_short_name = self.operator_short_name
        operator_number = self.operator_number
        route_index_from = self.route_index_from
        route_index_to = self.route_index_to
        track_translation = self.track_translation
        track_translation_short = self.track_translation_short
        vehicle_type: Union[Unset, str] = UNSET
        if not isinstance(self.vehicle_type, Unset):
            vehicle_type = self.vehicle_type.value

        vehicle_icon_name = self.vehicle_icon_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if number_formatted is not UNSET:
            field_dict["numberFormatted"] = number_formatted
        if number is not UNSET:
            field_dict["number"] = number
        if line is not UNSET:
            field_dict["line"] = line
        if line_reference is not UNSET:
            field_dict["lineReference"] = line_reference
        if category is not UNSET:
            field_dict["category"] = category
        if category_code is not UNSET:
            field_dict["categoryCode"] = category_code
        if category_short_form is not UNSET:
            field_dict["categoryShortForm"] = category_short_form
        if category_long_form is not UNSET:
            field_dict["categoryLongForm"] = category_long_form
        if operator_name is not UNSET:
            field_dict["operatorName"] = operator_name
        if operator_short_name is not UNSET:
            field_dict["operatorShortName"] = operator_short_name
        if operator_number is not UNSET:
            field_dict["operatorNumber"] = operator_number
        if route_index_from is not UNSET:
            field_dict["routeIndexFrom"] = route_index_from
        if route_index_to is not UNSET:
            field_dict["routeIndexTo"] = route_index_to
        if track_translation is not UNSET:
            field_dict["trackTranslation"] = track_translation
        if track_translation_short is not UNSET:
            field_dict["trackTranslationShort"] = track_translation_short
        if vehicle_type is not UNSET:
            field_dict["vehicleType"] = vehicle_type
        if vehicle_icon_name is not UNSET:
            field_dict["vehicleIconName"] = vehicle_icon_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        number_formatted = d.pop("numberFormatted", UNSET)

        number = d.pop("number", UNSET)

        line = d.pop("line", UNSET)

        line_reference = d.pop("lineReference", UNSET)

        _category = d.pop("category", UNSET)
        category: Union[Unset, TransportProductV2Category]
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = TransportProductV2Category(_category)

        category_code = d.pop("categoryCode", UNSET)

        category_short_form = d.pop("categoryShortForm", UNSET)

        category_long_form = d.pop("categoryLongForm", UNSET)

        operator_name = d.pop("operatorName", UNSET)

        operator_short_name = d.pop("operatorShortName", UNSET)

        operator_number = d.pop("operatorNumber", UNSET)

        route_index_from = d.pop("routeIndexFrom", UNSET)

        route_index_to = d.pop("routeIndexTo", UNSET)

        track_translation = d.pop("trackTranslation", UNSET)

        track_translation_short = d.pop("trackTranslationShort", UNSET)

        _vehicle_type = d.pop("vehicleType", UNSET)
        vehicle_type: Union[Unset, TransportProductV2VehicleType]
        if isinstance(_vehicle_type, Unset):
            vehicle_type = UNSET
        else:
            vehicle_type = TransportProductV2VehicleType(_vehicle_type)

        vehicle_icon_name = d.pop("vehicleIconName", UNSET)

        transport_product_v2 = cls(
            name=name,
            number_formatted=number_formatted,
            number=number,
            line=line,
            line_reference=line_reference,
            category=category,
            category_code=category_code,
            category_short_form=category_short_form,
            category_long_form=category_long_form,
            operator_name=operator_name,
            operator_short_name=operator_short_name,
            operator_number=operator_number,
            route_index_from=route_index_from,
            route_index_to=route_index_to,
            track_translation=track_translation,
            track_translation_short=track_translation_short,
            vehicle_type=vehicle_type,
            vehicle_icon_name=vehicle_icon_name,
        )

        transport_product_v2.additional_properties = d
        return transport_product_v2

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
