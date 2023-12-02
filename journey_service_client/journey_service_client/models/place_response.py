from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.place import Place


T = TypeVar("T", bound="PlaceResponse")


@_attrs_define
class PlaceResponse:
    """Response container of a Place-request.

    Attributes:
        places (List['Place']):
    """

    places: List["Place"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        places = []
        for places_item_data in self.places:
            places_item = places_item_data.to_dict()

            places.append(places_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "places": places,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.place import Place

        d = src_dict.copy()
        places = []
        _places = d.pop("places")
        for places_item_data in _places:
            places_item = Place.from_dict(places_item_data)

            places.append(places_item)

        place_response = cls(
            places=places,
        )

        place_response.additional_properties = d
        return place_response

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
