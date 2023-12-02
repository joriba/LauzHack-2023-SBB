from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.point import Point


T = TypeVar("T", bound="Place")


@_attrs_define
class Place:
    """**Abstract Superclass** of concrete inherited sub-classes such as **`StopPlace`, `Address`, `PointOfInterest`**.

    Attributes:
        name (str): Unique non-translated name of Place.
        id (str): Unique id referable by underlying system(s).
        type (str): **Inheritance discriminator to proper Subclass** (technical field required by [OpenApi 3
            Discriminator](https://swagger.io/docs/specification/data-models/inheritance-and-polymorphism/)) makes
            deserialization at consumer side easier.
        distance_to_search_position (Union[Unset, int]): Specifies the distance in [m] to the given coordinates in
            request. (Only set for `v3/places/by-coordinates*`).
        canton (Union[Unset, str]): In CH this represents the 'canton' abbreviation. Example: BE.
        country_code (Union[Unset, str]): The two uppercase character of ISO 3166 code, mostly similar to lowercase IANA
            identifier (source: DiDok geographic-based _isoCountryCode_). Example: CH.
        centroid (Union[Unset, Point]): Point in [GeoJSON](https://datatracker.ietf.org/doc/html/rfc7946) format.
    """

    name: str
    id: str
    type: str
    distance_to_search_position: Union[Unset, int] = UNSET
    canton: Union[Unset, str] = UNSET
    country_code: Union[Unset, str] = UNSET
    centroid: Union[Unset, "Point"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        id = self.id
        type = self.type
        distance_to_search_position = self.distance_to_search_position
        canton = self.canton
        country_code = self.country_code
        centroid: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.centroid, Unset):
            centroid = self.centroid.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "id": id,
                "type": type,
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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.point import Point

        d = src_dict.copy()
        name = d.pop("name")

        id = d.pop("id")

        type = d.pop("type")

        distance_to_search_position = d.pop("distanceToSearchPosition", UNSET)

        canton = d.pop("canton", UNSET)

        country_code = d.pop("countryCode", UNSET)

        _centroid = d.pop("centroid", UNSET)
        centroid: Union[Unset, Point]
        if isinstance(_centroid, Unset):
            centroid = UNSET
        else:
            centroid = Point.from_dict(_centroid)

        place = cls(
            name=name,
            id=id,
            type=type,
            distance_to_search_position=distance_to_search_position,
            canton=canton,
            country_code=country_code,
            centroid=centroid,
        )

        place.additional_properties = d
        return place

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
