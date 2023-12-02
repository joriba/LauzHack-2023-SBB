from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.train_stop_assignment_response_train_stop_assignments import (
        TrainStopAssignmentResponseTrainStopAssignments,
    )


T = TypeVar("T", bound="TrainStopAssignmentResponse")


@_attrs_define
class TrainStopAssignmentResponse:
    """Contains a list of `TrainStopAssignment's`, matching the given stops, if known.

    Attributes:
        train_stop_assignments (TrainStopAssignmentResponseTrainStopAssignments): Map<String (PlaceReference),
            `TrainStopAssignment`> each containing a `CompoundTrain` per requested stop-point. See v3 `PlaceReference` in
            [complex parameter](https://github.com/SchweizerischeBundesbahnen/journey-service/blob/master/JSON-Objects.md).
    """

    train_stop_assignments: "TrainStopAssignmentResponseTrainStopAssignments"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        train_stop_assignments = self.train_stop_assignments.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "trainStopAssignments": train_stop_assignments,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.train_stop_assignment_response_train_stop_assignments import (
            TrainStopAssignmentResponseTrainStopAssignments,
        )

        d = src_dict.copy()
        train_stop_assignments = TrainStopAssignmentResponseTrainStopAssignments.from_dict(
            d.pop("trainStopAssignments")
        )

        train_stop_assignment_response = cls(
            train_stop_assignments=train_stop_assignments,
        )

        train_stop_assignment_response.additional_properties = d
        return train_stop_assignment_response

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
