from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.stop_formation import StopFormation


T = TypeVar("T", bound="TrainFormation")


@_attrs_define
class TrainFormation:
    """Structure containing Formations at `Leg::origin` and `Leg::destination`.

    Attributes:
        origin_formation (Union[Unset, StopFormation]): Composition of a train resp. its cars at a specific stop related
            to platform sections (aka Transmodel 'COMPOUND TRAIN' or 'TRAIN').
        destination_formation (Union[Unset, StopFormation]): Composition of a train resp. its cars at a specific stop
            related to platform sections (aka Transmodel 'COMPOUND TRAIN' or 'TRAIN').
    """

    origin_formation: Union[Unset, "StopFormation"] = UNSET
    destination_formation: Union[Unset, "StopFormation"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        origin_formation: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.origin_formation, Unset):
            origin_formation = self.origin_formation.to_dict()

        destination_formation: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.destination_formation, Unset):
            destination_formation = self.destination_formation.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if origin_formation is not UNSET:
            field_dict["originFormation"] = origin_formation
        if destination_formation is not UNSET:
            field_dict["destinationFormation"] = destination_formation

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.stop_formation import StopFormation

        d = src_dict.copy()
        _origin_formation = d.pop("originFormation", UNSET)
        origin_formation: Union[Unset, StopFormation]
        if isinstance(_origin_formation, Unset):
            origin_formation = UNSET
        else:
            origin_formation = StopFormation.from_dict(_origin_formation)

        _destination_formation = d.pop("destinationFormation", UNSET)
        destination_formation: Union[Unset, StopFormation]
        if isinstance(_destination_formation, Unset):
            destination_formation = UNSET
        else:
            destination_formation = StopFormation.from_dict(_destination_formation)

        train_formation = cls(
            origin_formation=origin_formation,
            destination_formation=destination_formation,
        )

        train_formation.additional_properties = d
        return train_formation

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
