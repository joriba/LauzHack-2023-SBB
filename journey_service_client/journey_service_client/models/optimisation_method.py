from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OptimisationMethod")


@_attrs_define
class OptimisationMethod:
    """Configure the search algorithm influencing Trip search results.

    Attributes:
        number_of_results_before (Union[Unset, int]): Indicate the minimum number of search results returned before
            related dateTime.<br>This parameter has an impact on performance and/or response volume, set wisely!
        number_of_results_after (Union[Unset, int]): Indicate the minimum number of search results returned after
            related dateTime.<br>This parameter has an impact on performance and/or response volume, set wisely! Default: 5.
    """

    number_of_results_before: Union[Unset, int] = 0
    number_of_results_after: Union[Unset, int] = 5
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        number_of_results_before = self.number_of_results_before
        number_of_results_after = self.number_of_results_after

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if number_of_results_before is not UNSET:
            field_dict["numberOfResultsBefore"] = number_of_results_before
        if number_of_results_after is not UNSET:
            field_dict["numberOfResultsAfter"] = number_of_results_after

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        number_of_results_before = d.pop("numberOfResultsBefore", UNSET)

        number_of_results_after = d.pop("numberOfResultsAfter", UNSET)

        optimisation_method = cls(
            number_of_results_before=number_of_results_before,
            number_of_results_after=number_of_results_after,
        )

        optimisation_method.additional_properties = d
        return optimisation_method

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
