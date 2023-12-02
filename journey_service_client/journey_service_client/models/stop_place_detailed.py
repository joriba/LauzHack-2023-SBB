from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.operator import Operator
    from ..models.point import Point
    from ..models.quay import Quay
    from ..models.tariff_zone import TariffZone
    from ..models.vehicle_mode import VehicleMode


T = TypeVar("T", bound="StopPlaceDetailed")


@_attrs_define
class StopPlaceDetailed:
    """A place (de:Haltestelle) comprising one or more areas where vehicles may stop and where passengers may board or
    leave vehicles or prepare their trip. The name is given in regional language only.<br>Inherited from
    `Place`.<br>Inherited from `Place`.

        Attributes:
            type (str): **Inheritance discriminator to proper Subclass** (technical field required by [OpenApi 3
                Discriminator](https://swagger.io/docs/specification/data-models/inheritance-and-polymorphism/)) makes
                deserialization at consumer side easier.
            id (str): Unique id referable by underlying system(s).
            name (str): Unique non-translated name of Place.
            tariff_border (bool): Boundary for fare calculation resp. whether the **stop represents a tariff border between
                Switzerland and a neighbouring country**, where _true_ is based on a NOVA Tariff-BorderPoint (and must not be
                missunderstand by [UIC borderpoints](https://uic.org/support-activities/it/article/border-points).
            tariff_zones (List['TariffZone']):
            vehicle_modes (List['VehicleMode']):
            quays (List['Quay']):
            classification (str): A classification for a StopPlace:<br>x-extensible-enum: [SIMPLE, COMPLEX, ZONED, VIRTUAL]
                as in `StopPlaceClassification`
                - `SIMPLE` just a non-grouped stop (typically for a concrete VehicleMode)
                - `COMPLEX` a grouped concrete StopPlace (typically shared among different operators like Bern)
                - `ZONED` a grouped topographically extended Stop (typically not ONE concrete StopPlace but a set of them like
                Paris)
                - `VIRTUAL` a touristic non-real edge-point like 'Bahn-2000-Strecke' (has never leader or members) Example:
                SIMPLE.
            members (List[str]): Contains members of this `StopPlace` of either type COMPLEX or ZONED, if any.
            swiss_location_id (Union[Unset, str]): Swiss location id (SLOID) from DiDok. More on [Service Points (DiDok)
                API](https://developer.sbb.ch/apis/servicepoints/documentation). Example: ch:1:sloid:16161.
            province (Union[Unset, str]): In CH this represents the 'district' name. Example: Bern-Mitteland.
            canton (Union[Unset, str]): In CH this represents the 'canton' abbreviation. Example: BE.
            country_code (Union[Unset, str]): The two uppercase character of ISO 3166 code, mostly similar to lowercase IANA
                identifier (source: DiDok geographic-based _isoCountryCode_). Example: CH.
            centroid (Union[Unset, Point]): Point in [GeoJSON](https://datatracker.ietf.org/doc/html/rfc7946) format.
            operator (Union[Unset, Operator]): A company providing public transport services (aka Carrier).
            distance_to_search_position (Union[Unset, int]): Specifies the distance in [m] to the given coordinates in
                request. (Only set for `v3/places/by-coordinates*`).
            weighting (Union[Unset, int]): The higher the traffic load/importance the higher the value, null if unknown.
                Example: 30170.
            leader (Union[Unset, str]): Pointer to `StopPlace` which acts as leader of this COMPLEX or ZONED, if so.
                Example: 198.
    """

    type: str
    id: str
    name: str
    tariff_border: bool
    tariff_zones: List["TariffZone"]
    vehicle_modes: List["VehicleMode"]
    quays: List["Quay"]
    classification: str
    members: List[str]
    swiss_location_id: Union[Unset, str] = UNSET
    province: Union[Unset, str] = UNSET
    canton: Union[Unset, str] = UNSET
    country_code: Union[Unset, str] = UNSET
    centroid: Union[Unset, "Point"] = UNSET
    operator: Union[Unset, "Operator"] = UNSET
    distance_to_search_position: Union[Unset, int] = UNSET
    weighting: Union[Unset, int] = UNSET
    leader: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        id = self.id
        name = self.name
        tariff_border = self.tariff_border
        tariff_zones = []
        for tariff_zones_item_data in self.tariff_zones:
            tariff_zones_item = tariff_zones_item_data.to_dict()

            tariff_zones.append(tariff_zones_item)

        vehicle_modes = []
        for vehicle_modes_item_data in self.vehicle_modes:
            vehicle_modes_item = vehicle_modes_item_data.to_dict()

            vehicle_modes.append(vehicle_modes_item)

        quays = []
        for quays_item_data in self.quays:
            quays_item = quays_item_data.to_dict()

            quays.append(quays_item)

        classification = self.classification
        members = self.members

        swiss_location_id = self.swiss_location_id
        province = self.province
        canton = self.canton
        country_code = self.country_code
        centroid: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.centroid, Unset):
            centroid = self.centroid.to_dict()

        operator: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.operator, Unset):
            operator = self.operator.to_dict()

        distance_to_search_position = self.distance_to_search_position
        weighting = self.weighting
        leader = self.leader

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "id": id,
                "name": name,
                "tariffBorder": tariff_border,
                "tariffZones": tariff_zones,
                "vehicleModes": vehicle_modes,
                "quays": quays,
                "classification": classification,
                "members": members,
            }
        )
        if swiss_location_id is not UNSET:
            field_dict["swissLocationId"] = swiss_location_id
        if province is not UNSET:
            field_dict["province"] = province
        if canton is not UNSET:
            field_dict["canton"] = canton
        if country_code is not UNSET:
            field_dict["countryCode"] = country_code
        if centroid is not UNSET:
            field_dict["centroid"] = centroid
        if operator is not UNSET:
            field_dict["operator"] = operator
        if distance_to_search_position is not UNSET:
            field_dict["distanceToSearchPosition"] = distance_to_search_position
        if weighting is not UNSET:
            field_dict["weighting"] = weighting
        if leader is not UNSET:
            field_dict["leader"] = leader

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.operator import Operator
        from ..models.point import Point
        from ..models.quay import Quay
        from ..models.tariff_zone import TariffZone
        from ..models.vehicle_mode import VehicleMode

        d = src_dict.copy()
        type = d.pop("type")

        id = d.pop("id")

        name = d.pop("name")

        tariff_border = d.pop("tariffBorder")

        tariff_zones = []
        _tariff_zones = d.pop("tariffZones")
        for tariff_zones_item_data in _tariff_zones:
            tariff_zones_item = TariffZone.from_dict(tariff_zones_item_data)

            tariff_zones.append(tariff_zones_item)

        vehicle_modes = []
        _vehicle_modes = d.pop("vehicleModes")
        for vehicle_modes_item_data in _vehicle_modes:
            vehicle_modes_item = VehicleMode.from_dict(vehicle_modes_item_data)

            vehicle_modes.append(vehicle_modes_item)

        quays = []
        _quays = d.pop("quays")
        for quays_item_data in _quays:
            quays_item = Quay.from_dict(quays_item_data)

            quays.append(quays_item)

        classification = d.pop("classification")

        members = cast(List[str], d.pop("members"))

        swiss_location_id = d.pop("swissLocationId", UNSET)

        province = d.pop("province", UNSET)

        canton = d.pop("canton", UNSET)

        country_code = d.pop("countryCode", UNSET)

        _centroid = d.pop("centroid", UNSET)
        centroid: Union[Unset, Point]
        if isinstance(_centroid, Unset):
            centroid = UNSET
        else:
            centroid = Point.from_dict(_centroid)

        _operator = d.pop("operator", UNSET)
        operator: Union[Unset, Operator]
        if isinstance(_operator, Unset):
            operator = UNSET
        else:
            operator = Operator.from_dict(_operator)

        distance_to_search_position = d.pop("distanceToSearchPosition", UNSET)

        weighting = d.pop("weighting", UNSET)

        leader = d.pop("leader", UNSET)

        stop_place_detailed = cls(
            type=type,
            id=id,
            name=name,
            tariff_border=tariff_border,
            tariff_zones=tariff_zones,
            vehicle_modes=vehicle_modes,
            quays=quays,
            classification=classification,
            members=members,
            swiss_location_id=swiss_location_id,
            province=province,
            canton=canton,
            country_code=country_code,
            centroid=centroid,
            operator=operator,
            distance_to_search_position=distance_to_search_position,
            weighting=weighting,
            leader=leader,
        )

        stop_place_detailed.additional_properties = d
        return stop_place_detailed

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
