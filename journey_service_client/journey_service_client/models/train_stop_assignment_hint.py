from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TrainStopAssignmentHint")


@_attrs_define
class TrainStopAssignmentHint:
    """Hints which `TrainStopAssignment's` of `PTRideLeg` are potentially available for first `StopCall::departure` or last
    `StopCall::arrival`. Needs &includeTrainStopAssignments=NONE

        Attributes:
            compound_train_changes (List[str]): Known realtime changes as given by `CompoundTrain::trainChanges` (aka
                formation- or composition-changes), if any at **boarding stop** (changes at alighting are not
                contained).<br>(Translated according to Accept-Language.)
            departure_available (Union[Unset, bool]): `CompoundTrain` is currently available at the `PTRideLeg` origin stop.
            arrival_available (Union[Unset, bool]): `CompoundTrain` is currently available at the `PTRideLeg` destination
                stop.
            compound_train_changes_title (Union[Unset, str]): Related to `compoundTrainChanges`, and given only if any at
                all. Useful for sub-grouping by UIs.<br>(Translated according to Accept-Language.)
            contains_changes (Union[Unset, bool]): @Deprecated use `compoundTrainChanges` is not empty instead!
    """

    compound_train_changes: List[str]
    departure_available: Union[Unset, bool] = UNSET
    arrival_available: Union[Unset, bool] = UNSET
    compound_train_changes_title: Union[Unset, str] = UNSET
    contains_changes: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        compound_train_changes = self.compound_train_changes

        departure_available = self.departure_available
        arrival_available = self.arrival_available
        compound_train_changes_title = self.compound_train_changes_title
        contains_changes = self.contains_changes

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "compoundTrainChanges": compound_train_changes,
            }
        )
        if departure_available is not UNSET:
            field_dict["departureAvailable"] = departure_available
        if arrival_available is not UNSET:
            field_dict["arrivalAvailable"] = arrival_available
        if compound_train_changes_title is not UNSET:
            field_dict["compoundTrainChangesTitle"] = compound_train_changes_title
        if contains_changes is not UNSET:
            field_dict["containsChanges"] = contains_changes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        compound_train_changes = cast(List[str], d.pop("compoundTrainChanges"))

        departure_available = d.pop("departureAvailable", UNSET)

        arrival_available = d.pop("arrivalAvailable", UNSET)

        compound_train_changes_title = d.pop("compoundTrainChangesTitle", UNSET)

        contains_changes = d.pop("containsChanges", UNSET)

        train_stop_assignment_hint = cls(
            compound_train_changes=compound_train_changes,
            departure_available=departure_available,
            arrival_available=arrival_available,
            compound_train_changes_title=compound_train_changes_title,
            contains_changes=contains_changes,
        )

        train_stop_assignment_hint.additional_properties = d
        return train_stop_assignment_hint

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
