from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.arrival_v3 import ArrivalV3


T = TypeVar("T", bound="ArrivalResponse")


@_attrs_define
class ArrivalResponse:
    """Contains a list of Arrival's matching the search-criterias.

    Attributes:
        arrivals (List['ArrivalV3']):
    """

    arrivals: List["ArrivalV3"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        arrivals = []
        for arrivals_item_data in self.arrivals:
            arrivals_item = arrivals_item_data.to_dict()

            arrivals.append(arrivals_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "arrivals": arrivals,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.arrival_v3 import ArrivalV3

        d = src_dict.copy()
        arrivals = []
        _arrivals = d.pop("arrivals")
        for arrivals_item_data in _arrivals:
            arrivals_item = ArrivalV3.from_dict(arrivals_item_data)

            arrivals.append(arrivals_item)

        arrival_response = cls(
            arrivals=arrivals,
        )

        arrival_response.additional_properties = d
        return arrival_response

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
