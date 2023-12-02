from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pt_via_no_change_at_reference_status import PTViaNoChangeAtReferenceStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="PTViaNoChangeAtReference")


@_attrs_define
class PTViaNoChangeAtReference:
    """Specificy to prevent transferring Vehicle's at certain `StopPlace` on `Trip`. Can be useful to avoid certain places
    (for e.g. not handicap capable enough).

        Attributes:
            stop_place_id (str): StopPlace::id where Vehicle must NOT be changed. Example: 8506000.
            status (Union[Unset, PTViaNoChangeAtReferenceStatus]): Status to force transfer-behaviour at a `StopPlace`
                (whether a StopPlace is meta is defined by SBB Data-Management).<br>x-extensible-enum:  Default:
                PTViaNoChangeAtReferenceStatus.NO_TRANSFER_META_STOPPLACE.
    """

    stop_place_id: str
    status: Union[Unset, PTViaNoChangeAtReferenceStatus] = PTViaNoChangeAtReferenceStatus.NO_TRANSFER_META_STOPPLACE
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
        status: Union[Unset, PTViaNoChangeAtReferenceStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = PTViaNoChangeAtReferenceStatus(_status)

        pt_via_no_change_at_reference = cls(
            stop_place_id=stop_place_id,
            status=status,
        )

        pt_via_no_change_at_reference.additional_properties = d
        return pt_via_no_change_at_reference

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
