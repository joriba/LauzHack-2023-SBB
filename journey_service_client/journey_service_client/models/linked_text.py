from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.linked_text_arguments import LinkedTextArguments


T = TypeVar("T", bound="LinkedText")


@_attrs_define
class LinkedText:
    """Text template with optional formattable parameters. Useful to represent in UIs as clickable features like an e-Mail,
    phone or URL.<br>Usage see for e.g. [`Notice::text`](https://github.com/SchweizerischeBundesbahnen/journey-
    service/blob/master/JSON-Objects.md#linkedtext).

        Attributes:
            template (str): End-user text.<br>(Translated according to Accept-Language.)<br>If `arguments` are not empty the
                template must be formatted for end-user readability, by means arguments will be filled in or an UI may make them
                interactable (for e.g. clickable).
            arguments (LinkedTextArguments): Map(key=linkable types {EMAIL,PHONE,URL}, value=list of corresponding linkable
                values in `LinkedText::template` in ascending order of occurance).
    """

    template: str
    arguments: "LinkedTextArguments"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        template = self.template
        arguments = self.arguments.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "template": template,
                "arguments": arguments,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.linked_text_arguments import LinkedTextArguments

        d = src_dict.copy()
        template = d.pop("template")

        arguments = LinkedTextArguments.from_dict(d.pop("arguments"))

        linked_text = cls(
            template=template,
            arguments=arguments,
        )

        linked_text.additional_properties = d
        return linked_text

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
