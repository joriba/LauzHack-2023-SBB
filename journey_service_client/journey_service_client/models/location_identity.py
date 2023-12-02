from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.location_identity_type import LocationIdentityType
from ..types import UNSET, Unset

T = TypeVar("T", bound="LocationIdentity")


@_attrs_define
class LocationIdentity:
    """In a group of zoned stations (relates to stationType STATION_ZONED) the zonedMember represents the other siblings
    (empty for other stationType).

        Attributes:
            value (str):
            type (Union[Unset, LocationIdentityType]):
    """

    value: str
    type: Union[Unset, LocationIdentityType] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        value = self.value
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
            }
        )
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        value = d.pop("value")

        _type = d.pop("type", UNSET)
        type: Union[Unset, LocationIdentityType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = LocationIdentityType(_type)

        location_identity = cls(
            value=value,
            type=type,
        )

        location_identity.additional_properties = d
        return location_identity

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
