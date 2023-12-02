from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Connection")


@_attrs_define
class Connection:
    """The physical (spatial) possibility for a passenger to change from one public transport vehicle to another to
    continue the `Trip`, determined by two `ScheduledStopPoint's`. Different times may be necessary to cover the link
    between these points, depending on the kind of passenger.

        Attributes:
            mobility_restricted_traveller_duration (Union[Unset, str]): Minimal transfer
                [duration](https://www.w3.org/TR/xmlschema11-2/#duration) for a mobility impaired traveller to make transfer.
                Relates to `includeAccessibility` other than `ALL`. See `mobilityRestrictedTravellerTransferRule` for the rules
                applied to determine the time needed.
            mobility_restricted_traveller_transfer_critical (Union[Unset, bool]): Hint whether the vehicle transfer is
                critical for handicaped people, related to `mobilityRestrictedTravellerDuration`.
            mobility_restricted_traveller_transfer_rule (Union[Unset, str]): Hint for handicaped experts (such as AMO) about
                which duration rule was applied to determine minimal transfer time. Example: Fallback.
    """

    mobility_restricted_traveller_duration: Union[Unset, str] = UNSET
    mobility_restricted_traveller_transfer_critical: Union[Unset, bool] = UNSET
    mobility_restricted_traveller_transfer_rule: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mobility_restricted_traveller_duration = self.mobility_restricted_traveller_duration
        mobility_restricted_traveller_transfer_critical = self.mobility_restricted_traveller_transfer_critical
        mobility_restricted_traveller_transfer_rule = self.mobility_restricted_traveller_transfer_rule

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mobility_restricted_traveller_duration is not UNSET:
            field_dict["mobilityRestrictedTravellerDuration"] = mobility_restricted_traveller_duration
        if mobility_restricted_traveller_transfer_critical is not UNSET:
            field_dict["mobilityRestrictedTravellerTransferCritical"] = mobility_restricted_traveller_transfer_critical
        if mobility_restricted_traveller_transfer_rule is not UNSET:
            field_dict["mobilityRestrictedTravellerTransferRule"] = mobility_restricted_traveller_transfer_rule

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mobility_restricted_traveller_duration = d.pop("mobilityRestrictedTravellerDuration", UNSET)

        mobility_restricted_traveller_transfer_critical = d.pop("mobilityRestrictedTravellerTransferCritical", UNSET)

        mobility_restricted_traveller_transfer_rule = d.pop("mobilityRestrictedTravellerTransferRule", UNSET)

        connection = cls(
            mobility_restricted_traveller_duration=mobility_restricted_traveller_duration,
            mobility_restricted_traveller_transfer_critical=mobility_restricted_traveller_transfer_critical,
            mobility_restricted_traveller_transfer_rule=mobility_restricted_traveller_transfer_rule,
        )

        connection.additional_properties = d
        return connection

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
