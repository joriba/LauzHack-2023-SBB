from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LegendItemV3")


@_attrs_define
class LegendItemV3:
    """Provide matching legend-entry related to `TrainElement::attributes`.

    Attributes:
        id (str): Reference to related `LegendItem::text` assigned by aggregated `TrainElement::attributes` for the
            whole `CompoundTrain`. Example: FA.
        text (str): Detailed description of related `id`.<br>(Translated according to Accept-Language.) Example:
            Familienabteil.
    """

    id: str
    text: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        text = self.text

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "text": text,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        text = d.pop("text")

        legend_item_v3 = cls(
            id=id,
            text=text,
        )

        legend_item_v3.additional_properties = d
        return legend_item_v3

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
