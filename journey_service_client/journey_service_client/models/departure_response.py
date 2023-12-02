from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.departure import Departure


T = TypeVar("T", bound="DepartureResponse")


@_attrs_define
class DepartureResponse:
    """Contains a list of Departure's matching the search-criterias.

    Attributes:
        departures (List['Departure']):
    """

    departures: List["Departure"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        departures = []
        for departures_item_data in self.departures:
            departures_item = departures_item_data.to_dict()

            departures.append(departures_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "departures": departures,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.departure import Departure

        d = src_dict.copy()
        departures = []
        _departures = d.pop("departures")
        for departures_item_data in _departures:
            departures_item = Departure.from_dict(departures_item_data)

            departures.append(departures_item)

        departure_response = cls(
            departures=departures,
        )

        departure_response.additional_properties = d
        return departure_response

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
