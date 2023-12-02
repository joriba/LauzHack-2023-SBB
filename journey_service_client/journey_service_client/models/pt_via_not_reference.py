from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pt_via_not_reference_status import PTViaNotReferenceStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="PTViaNotReference")


@_attrs_define
class PTViaNotReference:
    """Specificy to prevent routing by a certain `StopPlace` on a `Trip`, by means such a place should not be on the Trip
    whether as a transferring nor intermediate stop.

        Attributes:
            stop_place_id (str): StopPlace::id NOT to be passed as via. Example: 8503000.
            status (Union[Unset, PTViaNotReferenceStatus]): No pass through status.<br>x-extensible-enum:  Default:
                PTViaNotReferenceStatus.NO_PASS_THROUGH_META_STOPPLACE.
    """

    stop_place_id: str
    status: Union[Unset, PTViaNotReferenceStatus] = PTViaNotReferenceStatus.NO_PASS_THROUGH_META_STOPPLACE
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        stop_place_id = self.stop_place_id
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stopPlaceId": stop_place_id,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        stop_place_id = d.pop("stopPlaceId")

        _status = d.pop("status", UNSET)
        status: Union[Unset, PTViaNotReferenceStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = PTViaNotReferenceStatus(_status)

        pt_via_not_reference = cls(
            stop_place_id=stop_place_id,
            status=status,
        )

        pt_via_not_reference.additional_properties = d
        return pt_via_not_reference

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
