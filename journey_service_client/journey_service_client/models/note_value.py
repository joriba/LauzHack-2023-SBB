from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.note_value_arguments import NoteValueArguments


T = TypeVar("T", bound="NoteValue")


@_attrs_define
class NoteValue:
    """Only set if related value has linkable data like EMAIL,PHONE,URL (which is also the sort-order) to fill in or
    annotate by UI functionality, to make args navigable for e.g. open a browser for a website. See v3 **Notice**
    (::text) in [complex parameter](https://github.com/SchweizerischeBundesbahnen/journey-service/blob/master/JSON-
    Objects.md)

        Attributes:
            template (Union[Unset, str]):
            arguments (Union[Unset, NoteValueArguments]):
    """

    template: Union[Unset, str] = UNSET
    arguments: Union[Unset, "NoteValueArguments"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        template = self.template
        arguments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.arguments, Unset):
            arguments = self.arguments.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if template is not UNSET:
            field_dict["template"] = template
        if arguments is not UNSET:
            field_dict["arguments"] = arguments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.note_value_arguments import NoteValueArguments

        d = src_dict.copy()
        template = d.pop("template", UNSET)

        _arguments = d.pop("arguments", UNSET)
        arguments: Union[Unset, NoteValueArguments]
        if isinstance(_arguments, Unset):
            arguments = UNSET
        else:
            arguments = NoteValueArguments.from_dict(_arguments)

        note_value = cls(
            template=template,
            arguments=arguments,
        )

        note_value.additional_properties = d
        return note_value

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
