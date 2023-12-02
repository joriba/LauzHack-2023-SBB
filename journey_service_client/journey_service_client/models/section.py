from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.car import Car


T = TypeVar("T", bound="Section")


@_attrs_define
class Section:
    """One of many Section (de:Sektor) of the platform.

    Attributes:
        name (str): Name of the section. Empty string is possible if no clear name is known. Example: A.
        cars (List['Car']):
    """

    name: str
    cars: List["Car"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        cars = []
        for cars_item_data in self.cars:
            cars_item = cars_item_data.to_dict()

            cars.append(cars_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "cars": cars,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.car import Car

        d = src_dict.copy()
        name = d.pop("name")

        cars = []
        _cars = d.pop("cars")
        for cars_item_data in _cars:
            cars_item = Car.from_dict(cars_item_data)

            cars.append(cars_item)

        section = cls(
            name=name,
            cars=cars,
        )

        section.additional_properties = d
        return section

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
