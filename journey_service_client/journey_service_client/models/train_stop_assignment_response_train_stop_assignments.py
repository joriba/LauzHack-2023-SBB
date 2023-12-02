from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.train_stop_assignment import TrainStopAssignment


T = TypeVar("T", bound="TrainStopAssignmentResponseTrainStopAssignments")


@_attrs_define
class TrainStopAssignmentResponseTrainStopAssignments:
    """Map<String (PlaceReference), `TrainStopAssignment`> each containing a `CompoundTrain` per requested stop-point. See
    v3 `PlaceReference` in [complex parameter](https://github.com/SchweizerischeBundesbahnen/journey-
    service/blob/master/JSON-Objects.md).

    """

    additional_properties: Dict[str, "TrainStopAssignment"] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pass

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.train_stop_assignment import TrainStopAssignment

        d = src_dict.copy()
        train_stop_assignment_response_train_stop_assignments = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = TrainStopAssignment.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        train_stop_assignment_response_train_stop_assignments.additional_properties = additional_properties
        return train_stop_assignment_response_train_stop_assignments

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "TrainStopAssignment":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "TrainStopAssignment") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
