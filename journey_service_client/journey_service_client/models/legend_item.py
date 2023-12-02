from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LegendItem")


@_attrs_define
class LegendItem:
    """Item in the legend describing car-attributes or -codes.

    Attributes:
        id (str): Identifier if item, related to refersTo. 2 digit Note::key attribute or '-' if related to a code.
            Example: WR.
        text (str): Describing and translated legend-text.
        refers_to (str): Type of legend description, either 'TYPE' or 'CODE'. Example: TYPE.
    """

    id: str
    text: str
    refers_to: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        text = self.text
        refers_to = self.refers_to

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "text": text,
                "refersTo": refers_to,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        text = d.pop("text")

        refers_to = d.pop("refersTo")

        legend_item = cls(
            id=id,
            text=text,
            refers_to=refers_to,
        )

        legend_item.additional_properties = d
        return legend_item

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
