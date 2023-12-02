from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="NetworkZone")


@_attrs_define
class NetworkZone:
    """NOVA Tariff-group (source 'VERBUNDLISTE.CSV').

    Attributes:
        name (str): Name of Network (de:Verbund). Example: Léman Pass.
        code (int): The zoneCode of NetworkZone. Example: 10.
        plan (str): Zone plan of tariff zone. Example: Léman Pass Abo & Billett.
        owner_name (str): Owner name of tariff zone. (NOVA: 'ZONENOWNER) Example: Léman Pass.
        owner_code (int): Zone owner code of tariff zone. Example: 419.
    """

    name: str
    code: int
    plan: str
    owner_name: str
    owner_code: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        code = self.code
        plan = self.plan
        owner_name = self.owner_name
        owner_code = self.owner_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "code": code,
                "plan": plan,
                "ownerName": owner_name,
                "ownerCode": owner_code,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        code = d.pop("code")

        plan = d.pop("plan")

        owner_name = d.pop("ownerName")

        owner_code = d.pop("ownerCode")

        network_zone = cls(
            name=name,
            code=code,
            plan=plan,
            owner_name=owner_name,
            owner_code=owner_code,
        )

        network_zone.additional_properties = d
        return network_zone

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
