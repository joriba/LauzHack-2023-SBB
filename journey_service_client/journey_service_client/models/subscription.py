from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hysteresis import Hysteresis


T = TypeVar("T", bound="Subscription")


@_attrs_define
class Subscription:
    """All details about subscription (like `Trip` HCCS subscriptionId).

    Attributes:
        id (str): <userId>@<HCSS-TechnicalId> Example: CEP_CAPRE:550e8400-e29b-11d4-a716-446655440000@69644.
        user_id (str): HCCS userId at subscription, resp. <Kafka-Topic-name>:<UUID>. Example:
            J_S_TOPIC_1:80376b7d-15ac-4ccf-833c-ea951115b30d.
        status (str): Subscription status like 'ACTIVE' (monitoring on), 'EXPIRED' (monitoring obsolete), ..
        external_id (Union[Unset, str]): External reference ID defined (and used) by the client.
        hysteresis (Union[Unset, Hysteresis]): Subscriptions can be configured to only trigger notifications, if changes
            exceed a configured limit. This is done using the hysteresis property per user or subscription.
    """

    id: str
    user_id: str
    status: str
    external_id: Union[Unset, str] = UNSET
    hysteresis: Union[Unset, "Hysteresis"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        user_id = self.user_id
        status = self.status
        external_id = self.external_id
        hysteresis: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.hysteresis, Unset):
            hysteresis = self.hysteresis.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "userId": user_id,
                "status": status,
            }
        )
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if hysteresis is not UNSET:
            field_dict["hysteresis"] = hysteresis

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.hysteresis import Hysteresis

        d = src_dict.copy()
        id = d.pop("id")

        user_id = d.pop("userId")

        status = d.pop("status")

        external_id = d.pop("externalId", UNSET)

        _hysteresis = d.pop("hysteresis", UNSET)
        hysteresis: Union[Unset, Hysteresis]
        if isinstance(_hysteresis, Unset):
            hysteresis = UNSET
        else:
            hysteresis = Hysteresis.from_dict(_hysteresis)

        subscription = cls(
            id=id,
            user_id=user_id,
            status=status,
            external_id=external_id,
            hysteresis=hysteresis,
        )

        subscription.additional_properties = d
        return subscription

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
