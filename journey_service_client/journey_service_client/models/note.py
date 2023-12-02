from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.note_value import NoteValue


T = TypeVar("T", bound="Note")


@_attrs_define
class Note:
    """Some objects have additional notes (like car-attributes, customer-infos, ..).

    Attributes:
        key (str): An identifier of this note (two letter combination further identifying the #value of the note).
        priority (int): A lower priority value means a higher importance (default=100).
        value (Union[Unset, str]): Speaking fully formatted value relating to key. <br>(Translated according to Accept-
            Language.)
        route_index_from (Union[Unset, int]): Relates to Stop::routeIndex where this note is valid from.
        route_index_to (Union[Unset, int]): Relates to Stop::routeIndex where this note is valid to.
        value_formattable (Union[Unset, NoteValue]): Only set if related value has linkable data like EMAIL,PHONE,URL
            (which is also the sort-order) to fill in or annotate by UI functionality, to make args navigable for e.g. open
            a browser for a website. See v3 **Notice** (::text) in [complex
            parameter](https://github.com/SchweizerischeBundesbahnen/journey-service/blob/master/JSON-Objects.md)
    """

    key: str
    priority: int
    value: Union[Unset, str] = UNSET
    route_index_from: Union[Unset, int] = UNSET
    route_index_to: Union[Unset, int] = UNSET
    value_formattable: Union[Unset, "NoteValue"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key = self.key
        priority = self.priority
        value = self.value
        route_index_from = self.route_index_from
        route_index_to = self.route_index_to
        value_formattable: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.value_formattable, Unset):
            value_formattable = self.value_formattable.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "priority": priority,
            }
        )
        if value is not UNSET:
            field_dict["value"] = value
        if route_index_from is not UNSET:
            field_dict["routeIndexFrom"] = route_index_from
        if route_index_to is not UNSET:
            field_dict["routeIndexTo"] = route_index_to
        if value_formattable is not UNSET:
            field_dict["valueFormattable"] = value_formattable

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.note_value import NoteValue

        d = src_dict.copy()
        key = d.pop("key")

        priority = d.pop("priority")

        value = d.pop("value", UNSET)

        route_index_from = d.pop("routeIndexFrom", UNSET)

        route_index_to = d.pop("routeIndexTo", UNSET)

        _value_formattable = d.pop("valueFormattable", UNSET)
        value_formattable: Union[Unset, NoteValue]
        if isinstance(_value_formattable, Unset):
            value_formattable = UNSET
        else:
            value_formattable = NoteValue.from_dict(_value_formattable)

        note = cls(
            key=key,
            priority=priority,
            value=value,
            route_index_from=route_index_from,
            route_index_to=route_index_to,
            value_formattable=value_formattable,
        )

        note.additional_properties = d
        return note

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
