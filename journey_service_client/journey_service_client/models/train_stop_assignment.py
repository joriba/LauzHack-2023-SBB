from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.compound_train import CompoundTrain


T = TypeVar("T", bound="TrainStopAssignment")


@_attrs_define
class TrainStopAssignment:
    """The association of a `TrainComponent` at a `ScheduledStopPoint` with a specific `StopPlace` and also possibly a
    `Quay` and `BoardingPosition`.

        Attributes:
            compound_train (CompoundTrain): A vehicle-type composed (aka composition/-formation) of a sequence of **one or
                more vehicle-type `Train`**. A `CompoundTrain` is always self-propelled (even if a Locomotive is not explicitely
                distinguishable).
    """

    compound_train: "CompoundTrain"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        compound_train = self.compound_train.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "compoundTrain": compound_train,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.compound_train import CompoundTrain

        d = src_dict.copy()
        compound_train = CompoundTrain.from_dict(d.pop("compoundTrain"))

        train_stop_assignment = cls(
            compound_train=compound_train,
        )

        train_stop_assignment.additional_properties = d
        return train_stop_assignment

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
