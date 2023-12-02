from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.quay_subscription import QuaySubscription


T = TypeVar("T", bound="StopCallSubscription")


@_attrs_define
class StopCallSubscription:
    """
    Attributes:
        quay_aimed (Union[Unset, QuaySubscription]):
    """

    quay_aimed: Union[Unset, "QuaySubscription"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        quay_aimed: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.quay_aimed, Unset):
            quay_aimed = self.quay_aimed.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if quay_aimed is not UNSET:
            field_dict["quayAimed"] = quay_aimed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.quay_subscription import QuaySubscription

        d = src_dict.copy()
        _quay_aimed = d.pop("quayAimed", UNSET)
        quay_aimed: Union[Unset, QuaySubscription]
        if isinstance(_quay_aimed, Unset):
            quay_aimed = UNSET
        else:
            quay_aimed = QuaySubscription.from_dict(_quay_aimed)

        stop_call_subscription = cls(
            quay_aimed=quay_aimed,
        )

        stop_call_subscription.additional_properties = d
        return stop_call_subscription

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
