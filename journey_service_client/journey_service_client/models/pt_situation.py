from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pt_situation_affected_scope import PTSituationAffectedScope
    from ..models.pt_situation_message import PTSituationMessage


T = TypeVar("T", bound="PTSituation")


@_attrs_define
class PTSituation:
    """A disruption (fort e.g. an incident or a deviation (aka de:Störungs-, Ereignismeldung)) affecting planned PT
    `ServiceProduct's` in certain edges and/or regions.

        Attributes:
            broadcast_messages (List['PTSituationMessage']):
            cause (Union[Unset, str]): A classification of what caused the situation (aka HIM category), values see
                `SituationCauseEnum`.<br>x-extensible-enum:  Example: DISTURBANCE.
            affected_scope (Union[Unset, PTSituationAffectedScope]): An extent directly involved in the PT situation such as
                a set of `ServiceJourney` or `StopPlace`.
    """

    broadcast_messages: List["PTSituationMessage"]
    cause: Union[Unset, str] = UNSET
    affected_scope: Union[Unset, "PTSituationAffectedScope"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        broadcast_messages = []
        for broadcast_messages_item_data in self.broadcast_messages:
            broadcast_messages_item = broadcast_messages_item_data.to_dict()

            broadcast_messages.append(broadcast_messages_item)

        cause = self.cause
        affected_scope: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.affected_scope, Unset):
            affected_scope = self.affected_scope.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "broadcastMessages": broadcast_messages,
            }
        )
        if cause is not UNSET:
            field_dict["cause"] = cause
        if affected_scope is not UNSET:
            field_dict["affectedScope"] = affected_scope

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pt_situation_affected_scope import PTSituationAffectedScope
        from ..models.pt_situation_message import PTSituationMessage

        d = src_dict.copy()
        broadcast_messages = []
        _broadcast_messages = d.pop("broadcastMessages")
        for broadcast_messages_item_data in _broadcast_messages:
            broadcast_messages_item = PTSituationMessage.from_dict(broadcast_messages_item_data)

            broadcast_messages.append(broadcast_messages_item)

        cause = d.pop("cause", UNSET)

        _affected_scope = d.pop("affectedScope", UNSET)
        affected_scope: Union[Unset, PTSituationAffectedScope]
        if isinstance(_affected_scope, Unset):
            affected_scope = UNSET
        else:
            affected_scope = PTSituationAffectedScope.from_dict(_affected_scope)

        pt_situation = cls(
            broadcast_messages=broadcast_messages,
            cause=cause,
            affected_scope=affected_scope,
        )

        pt_situation.additional_properties = d
        return pt_situation

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
