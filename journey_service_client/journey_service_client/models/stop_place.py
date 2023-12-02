from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.links import Links
    from ..models.point import Point
    from ..models.vehicle_mode import VehicleMode


T = TypeVar("T", bound="StopPlace")


@_attrs_define
class StopPlace:
    """A place (de:Haltestelle) comprising one or more areas where vehicles may stop and where passengers may board or
    leave vehicles or prepare their trip. The name is given in regional language only.<br>Inherited from `Place`.

        Attributes:
            name (str): Unique non-translated name of Place.
            id (str): Unique id referable by underlying system(s).
            type (str): **Inheritance discriminator to proper Subclass** (technical field required by [OpenApi 3
                Discriminator](https://swagger.io/docs/specification/data-models/inheritance-and-polymorphism/)) makes
                deserialization at consumer side easier.
            tariff_border (bool): Boundary for fare calculation resp. whether the **stop represents a tariff border between
                Switzerland and a neighbouring country**, where _true_ is based on a NOVA Tariff-BorderPoint (and must not be
                missunderstand by [UIC borderpoints](https://uic.org/support-activities/it/article/border-points).
            vehicle_modes (List['VehicleMode']):
            distance_to_search_position (Union[Unset, int]): Specifies the distance in [m] to the given coordinates in
                request. (Only set for `v3/places/by-coordinates*`).
            canton (Union[Unset, str]): In CH this represents the 'canton' abbreviation. Example: BE.
            country_code (Union[Unset, str]): The two uppercase character of ISO 3166 code, mostly similar to lowercase IANA
                identifier (source: DiDok geographic-based _isoCountryCode_). Example: CH.
            centroid (Union[Unset, Point]): Point in [GeoJSON](https://datatracker.ietf.org/doc/html/rfc7946) format.
            weighting (Union[Unset, int]): The higher the traffic load/importance the higher the value, null if unknown.
                Example: 30170.
            links (Union[Unset, Links]): List of links as per [HATEOAS](https://en.wikipedia.org/wiki/HATEOAS) principle.
    """

    name: str
    id: str
    type: str
    tariff_border: bool
    vehicle_modes: List["VehicleMode"]
    distance_to_search_position: Union[Unset, int] = UNSET
    canton: Union[Unset, str] = UNSET
    country_code: Union[Unset, str] = UNSET
    centroid: Union[Unset, "Point"] = UNSET
    weighting: Union[Unset, int] = UNSET
    links: Union[Unset, "Links"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        id = self.id
        type = self.type
        tariff_border = self.tariff_border
        vehicle_modes = []
        for vehicle_modes_item_data in self.vehicle_modes:
            vehicle_modes_item = vehicle_modes_item_data.to_dict()

            vehicle_modes.append(vehicle_modes_item)

        distance_to_search_position = self.distance_to_search_position
        canton = self.canton
        country_code = self.country_code
        centroid: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.centroid, Unset):
            centroid = self.centroid.to_dict()

        weighting = self.weighting
        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "id": id,
                "type": type,
                "tariffBorder": tariff_border,
                "vehicleModes": vehicle_modes,
            }
        )
        if distance_to_search_position is not UNSET:
            field_dict["distanceToSearchPosition"] = distance_to_search_position
        if canton is not UNSET:
            field_dict["canton"] = canton
        if country_code is not UNSET:
            field_dict["countryCode"] = country_code
        if centroid is not UNSET:
            field_dict["centroid"] = centroid
        if weighting is not UNSET:
            field_dict["weighting"] = weighting
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.links import Links
        from ..models.point import Point
        from ..models.vehicle_mode import VehicleMode

        d = src_dict.copy()
        name = d.pop("name")

        id = d.pop("id")

        type = d.pop("type")

        tariff_border = d.pop("tariffBorder")

        vehicle_modes = []
        _vehicle_modes = d.pop("vehicleModes")
        for vehicle_modes_item_data in _vehicle_modes:
            vehicle_modes_item = VehicleMode.from_dict(vehicle_modes_item_data)

            vehicle_modes.append(vehicle_modes_item)

        distance_to_search_position = d.pop("distanceToSearchPosition", UNSET)

        canton = d.pop("canton", UNSET)

        country_code = d.pop("countryCode", UNSET)

        _centroid = d.pop("centroid", UNSET)
        centroid: Union[Unset, Point]
        if isinstance(_centroid, Unset):
            centroid = UNSET
        else:
            centroid = Point.from_dict(_centroid)

        weighting = d.pop("weighting", UNSET)

        _links = d.pop("links", UNSET)
        links: Union[Unset, Links]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = Links.from_dict(_links)

        stop_place = cls(
            name=name,
            id=id,
            type=type,
            tariff_border=tariff_border,
            vehicle_modes=vehicle_modes,
            distance_to_search_position=distance_to_search_position,
            canton=canton,
            country_code=country_code,
            centroid=centroid,
            weighting=weighting,
            links=links,
        )

        stop_place.additional_properties = d
        return stop_place

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
