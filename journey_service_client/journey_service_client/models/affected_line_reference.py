from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AffectedLineReference")


@_attrs_define
class AffectedLineReference:
    """Reference to a ServiceProduct with its id

    Example:
        {'start': '2023-04-18T14:55:00+01:00', 'end': '2023-09-07T09:10:00+02:00', 'dailyStartingAt': '17:15',
            'dailyEndingAt': '18:05'}

    Attributes:
        service_product_id (str): Internal `ServiceProduct::id`, related to `LineAffected::serviceProductId` (for e.g.
            from a previous call returning `LineAffectedResponse`). Example: L::1::IC::B2925753281::H_5_000011_::*.
        service_product_name (str): `ServiceProduct::name` line-name. See
            [ServiceProductReference](https://github.com/SchweizerischeBundesbahnen/journey-service/blob/master/JSON-
            Objects.md#serviceproductreference). Example: IC 5 1516.
    """

    service_product_id: str
    service_product_name: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        service_product_id = self.service_product_id
        service_product_name = self.service_product_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "serviceProductId": service_product_id,
                "serviceProductName": service_product_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        service_product_id = d.pop("serviceProductId")

        service_product_name = d.pop("serviceProductName")

        affected_line_reference = cls(
            service_product_id=service_product_id,
            service_product_name=service_product_name,
        )

        affected_line_reference.additional_properties = d
        return affected_line_reference

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
