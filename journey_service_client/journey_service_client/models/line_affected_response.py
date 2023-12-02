from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.line_affected import LineAffected


T = TypeVar("T", bound="LineAffectedResponse")


@_attrs_define
class LineAffectedResponse:
    """Contains a list of `LineAffected`'s matching the search-criteria.

    Attributes:
        lines_affected (List['LineAffected']):
    """

    lines_affected: List["LineAffected"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        lines_affected = []
        for lines_affected_item_data in self.lines_affected:
            lines_affected_item = lines_affected_item_data.to_dict()

            lines_affected.append(lines_affected_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "linesAffected": lines_affected,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.line_affected import LineAffected

        d = src_dict.copy()
        lines_affected = []
        _lines_affected = d.pop("linesAffected")
        for lines_affected_item_data in _lines_affected:
            lines_affected_item = LineAffected.from_dict(lines_affected_item_data)

            lines_affected.append(lines_affected_item)

        line_affected_response = cls(
            lines_affected=lines_affected,
        )

        line_affected_response.additional_properties = d
        return line_affected_response

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
