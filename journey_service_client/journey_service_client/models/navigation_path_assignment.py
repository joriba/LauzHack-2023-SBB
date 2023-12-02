from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.connection import Connection


T = TypeVar("T", bound="NavigationPathAssignment")


@_attrs_define
class NavigationPathAssignment:
    """The allocation of a **navigation path** to a specific `ScheduledStopPoint` assignment, for example to indicate the
    path to be taken to make a connection.<br>Currently a **transfer-hint is given for handicaped people** at alighting
    at `PTRideLeg`s` last/alighting `ScheduledStopPoint` when transfering to next vehicle for boarding.

        Attributes:
            connection_to (Union[Unset, Connection]): The physical (spatial) possibility for a passenger to change from one
                public transport vehicle to another to continue the `Trip`, determined by two `ScheduledStopPoint's`. Different
                times may be necessary to cover the link between these points, depending on the kind of passenger.
    """

    connection_to: Union[Unset, "Connection"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        connection_to: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.connection_to, Unset):
            connection_to = self.connection_to.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if connection_to is not UNSET:
            field_dict["connectionTo"] = connection_to

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.connection import Connection

        d = src_dict.copy()
        _connection_to = d.pop("connectionTo", UNSET)
        connection_to: Union[Unset, Connection]
        if isinstance(_connection_to, Unset):
            connection_to = UNSET
        else:
            connection_to = Connection.from_dict(_connection_to)

        navigation_path_assignment = cls(
            connection_to=connection_to,
        )

        navigation_path_assignment.additional_properties = d
        return navigation_path_assignment

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
