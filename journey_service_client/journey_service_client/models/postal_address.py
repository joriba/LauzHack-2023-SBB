from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostalAddress")


@_attrs_define
class PostalAddress:
    """Postal Address (source INSA).

    Attributes:
        name (str): Main line of the address = name or company. Example: SBB AG.
        complement (Union[Unset, str]): Name's complement, typically company's service. Example: Reisezentrum.
        post_office_box (Union[Unset, str]):  Example: 1837.
        address_line_1 (Union[Unset, str]): Main address line, typically the street. Example: Bahnhofstrasse.
        house_number (Union[Unset, str]): House number completing the `addressLine1`. Example: 12.
        post_code (Union[Unset, str]): Postal code of the town Example: 8280.
        town (Union[Unset, str]): Town or city Example: Kreuzlingen.
        country_code (Union[Unset, str]): The two uppercase character of ISO 3166 code, mostly similar to lowercase IANA
            identifier (source: DiDok geographic-based _isoCountryCode_). Example: CH.
    """

    name: str
    complement: Union[Unset, str] = UNSET
    post_office_box: Union[Unset, str] = UNSET
    address_line_1: Union[Unset, str] = UNSET
    house_number: Union[Unset, str] = UNSET
    post_code: Union[Unset, str] = UNSET
    town: Union[Unset, str] = UNSET
    country_code: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        complement = self.complement
        post_office_box = self.post_office_box
        address_line_1 = self.address_line_1
        house_number = self.house_number
        post_code = self.post_code
        town = self.town
        country_code = self.country_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if complement is not UNSET:
            field_dict["complement"] = complement
        if post_office_box is not UNSET:
            field_dict["postOfficeBox"] = post_office_box
        if address_line_1 is not UNSET:
            field_dict["addressLine1"] = address_line_1
        if house_number is not UNSET:
            field_dict["houseNumber"] = house_number
        if post_code is not UNSET:
            field_dict["postCode"] = post_code
        if town is not UNSET:
            field_dict["town"] = town
        if country_code is not UNSET:
            field_dict["countryCode"] = country_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        complement = d.pop("complement", UNSET)

        post_office_box = d.pop("postOfficeBox", UNSET)

        address_line_1 = d.pop("addressLine1", UNSET)

        house_number = d.pop("houseNumber", UNSET)

        post_code = d.pop("postCode", UNSET)

        town = d.pop("town", UNSET)

        country_code = d.pop("countryCode", UNSET)

        postal_address = cls(
            name=name,
            complement=complement,
            post_office_box=post_office_box,
            address_line_1=address_line_1,
            house_number=house_number,
            post_code=post_code,
            town=town,
            country_code=country_code,
        )

        postal_address.additional_properties = d
        return postal_address

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
