from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.connection_reliability_alternative import ConnectionReliabilityAlternative
from ..models.connection_reliability_original import ConnectionReliabilityOriginal
from ..types import UNSET, Unset

T = TypeVar("T", bound="ConnectionReliability")


@_attrs_define
class ConnectionReliability:
    """Archive API Timemachine only: Validation of trip in the past.

    Attributes:
        original (Union[Unset, ConnectionReliabilityOriginal]):
        alternative (Union[Unset, ConnectionReliabilityAlternative]):
    """

    original: Union[Unset, ConnectionReliabilityOriginal] = UNSET
    alternative: Union[Unset, ConnectionReliabilityAlternative] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        original: Union[Unset, str] = UNSET
        if not isinstance(self.original, Unset):
            original = self.original.value

        alternative: Union[Unset, str] = UNSET
        if not isinstance(self.alternative, Unset):
            alternative = self.alternative.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if original is not UNSET:
            field_dict["original"] = original
        if alternative is not UNSET:
            field_dict["alternative"] = alternative

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _original = d.pop("original", UNSET)
        original: Union[Unset, ConnectionReliabilityOriginal]
        if isinstance(_original, Unset):
            original = UNSET
        else:
            original = ConnectionReliabilityOriginal(_original)

        _alternative = d.pop("alternative", UNSET)
        alternative: Union[Unset, ConnectionReliabilityAlternative]
        if isinstance(_alternative, Unset):
            alternative = UNSET
        else:
            alternative = ConnectionReliabilityAlternative(_alternative)

        connection_reliability = cls(
            original=original,
            alternative=alternative,
        )

        connection_reliability.additional_properties = d
        return connection_reliability

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
