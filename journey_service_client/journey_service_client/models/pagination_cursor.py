from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PaginationCursor")


@_attrs_define
class PaginationCursor:
    """Pagination-cursor for next/previous of the same. By means in a Trip context earlier/later.

    Attributes:
        previous (Union[Unset, str]): Previous-context.
        next_ (Union[Unset, str]): Next-context.
    """

    previous: Union[Unset, str] = UNSET
    next_: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        previous = self.previous
        next_ = self.next_

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if previous is not UNSET:
            field_dict["previous"] = previous
        if next_ is not UNSET:
            field_dict["next"] = next_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        previous = d.pop("previous", UNSET)

        next_ = d.pop("next", UNSET)

        pagination_cursor = cls(
            previous=previous,
            next_=next_,
        )

        pagination_cursor.additional_properties = d
        return pagination_cursor

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
