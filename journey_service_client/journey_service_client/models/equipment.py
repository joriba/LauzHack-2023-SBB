from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.equipment_type import EquipmentType


T = TypeVar("T", bound="Equipment")


@_attrs_define
class Equipment:
    """An equipment can be either physically installed or immaterial such as a service to travellers.

    Attributes:
        classification (EquipmentType): TYPE OF EQUIPMENT in Transmodel, referenced as a classification of an
            `Equipment`.
        id (str): Id from a technical point of view, should not be interpreted! Example: rtzwbgndjdes.
        name (Union[Unset, str]): Name of the equipment, translated if possible. Not always filled up, in contrary to
            the `classification's` name<br>(Translated according to Accept-Language.) Example: Wi-Fi, Kreuzlingen.
    """

    classification: "EquipmentType"
    id: str
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        classification = self.classification.to_dict()

        id = self.id
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "classification": classification,
                "id": id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.equipment_type import EquipmentType

        d = src_dict.copy()
        classification = EquipmentType.from_dict(d.pop("classification"))

        id = d.pop("id")

        name = d.pop("name", UNSET)

        equipment = cls(
            classification=classification,
            id=id,
            name=name,
        )

        equipment.additional_properties = d
        return equipment

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
