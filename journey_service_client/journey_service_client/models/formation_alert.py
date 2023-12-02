from typing import Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FormationAlert")


@_attrs_define
class FormationAlert:
    """Contains any Formation rt infos (such as changed wagons, ..) on PUBLIC_TRANSPORTATION LegV2. Depends on v2/trips
    parameter trainFormationType.

        Attributes:
            title (str): Title for any formation-changes (useful for sub-grouping of formationChanges).<br>(Translated
                according to Accept-Language.)
            formation_changes_at_origin (List[str]):
    """

    title: str
    formation_changes_at_origin: List[str]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        title = self.title
        formation_changes_at_origin = self.formation_changes_at_origin

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "formationChangesAtOrigin": formation_changes_at_origin,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        title = d.pop("title")

        formation_changes_at_origin = cast(List[str], d.pop("formationChangesAtOrigin"))

        formation_alert = cls(
            title=title,
            formation_changes_at_origin=formation_changes_at_origin,
        )

        formation_alert.additional_properties = d
        return formation_alert

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
