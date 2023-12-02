from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TripSubscriptionResponse")


@_attrs_define
class TripSubscriptionResponse:
    """Response for initial `Trip` subscription.

    Attributes:
        subscription_id (str): <Kafka-Topic-name>:<UUID>@<HCSS-TechnicalId> Example:
            CEP_CAPRE:550e8400-e29b-11d4-a716-446655440000@69644.
    """

    subscription_id: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        subscription_id = self.subscription_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subscriptionId": subscription_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        subscription_id = d.pop("subscriptionId")

        trip_subscription_response = cls(
            subscription_id=subscription_id,
        )

        trip_subscription_response.additional_properties = d
        return trip_subscription_response

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
