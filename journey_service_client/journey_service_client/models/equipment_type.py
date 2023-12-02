from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EquipmentType")


@_attrs_define
class EquipmentType:
    """TYPE OF EQUIPMENT in Transmodel, referenced as a classification of an `Equipment`.

    Attributes:
        id (str): Id of the equipment type:<br>x-extensible-enum: [WIFI] as in `EquipmentTypeEnum`
            * `WIFI` free internet connection through Wi-Fi Example: WIFI.
        name (str): Name of the equipment type, translated.<br>(Translated according to Accept-Language.) Example: Wi-
            Fi.
        corporate_identity_icon (Union[Unset, str]): Icon-identifier to represent the equipment. See [SBB
            pictograms](https://digital.sbb.ch/de/brand_elemente/piktogramme) Example: WLAN.
    """

    id: str
    name: str
    corporate_identity_icon: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        corporate_identity_icon = self.corporate_identity_icon

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if corporate_identity_icon is not UNSET:
            field_dict["corporateIdentityIcon"] = corporate_identity_icon

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        corporate_identity_icon = d.pop("corporateIdentityIcon", UNSET)

        equipment_type = cls(
            id=id,
            name=name,
            corporate_identity_icon=corporate_identity_icon,
        )

        equipment_type.additional_properties = d
        return equipment_type

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
