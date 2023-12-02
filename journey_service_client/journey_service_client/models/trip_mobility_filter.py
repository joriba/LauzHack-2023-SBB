from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TripMobilityFilter")


@_attrs_define
class TripMobilityFilter:
    """Parameters to restrict the transfer options - particularly for interchanging PTRideLeg's by passenger (de:
    Individuelles Umsteigeverhalten).
    - TripsByOriginAndDestinationPostBody: all filters supported
    - ServiceCalendarByOriginAndDestinationRequestBody: only `maxTransfers` supported yet

        Attributes:
            max_transfers (Union[Unset, int]): Max. number of Vehicle changes. The parameter is relevant between origin and
                destination or between origin and ptVias[0] if any among all PTRideLeg's. Default: 11.
            walk_speed (Union[Unset, int]): Walking speed when changing Vehicles: 100% means default speed, 200% doubles it
                and below 100% will reduce changing time below SBB recommendation.
                - If the calculation does not result in full minutes, it is rounded using 'round half up' method.
                - See `Trip::fastTransfer` for time risky changes. Default: 100.
            additional_transfer_time (Union[Unset, int]): Additional time [in min.] on top of default transfer time when
                changing Vehicle's.
            min_transfer_time (Union[Unset, int]): Minimum change time [in min.] when changing transport-products. There is
                no constant default, depends on SBB defined changing time at specific STATION.
            max_transfer_time (Union[Unset, int]): Maximum change time at stop in minutes. In realtimeMode=FULL only planned
                time is considered (by means not guaranteed if dateTimeRt is given).
    """

    max_transfers: Union[Unset, int] = 11
    walk_speed: Union[Unset, int] = 100
    additional_transfer_time: Union[Unset, int] = 0
    min_transfer_time: Union[Unset, int] = UNSET
    max_transfer_time: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        max_transfers = self.max_transfers
        walk_speed = self.walk_speed
        additional_transfer_time = self.additional_transfer_time
        min_transfer_time = self.min_transfer_time
        max_transfer_time = self.max_transfer_time

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_transfers is not UNSET:
            field_dict["maxTransfers"] = max_transfers
        if walk_speed is not UNSET:
            field_dict["walkSpeed"] = walk_speed
        if additional_transfer_time is not UNSET:
            field_dict["additionalTransferTime"] = additional_transfer_time
        if min_transfer_time is not UNSET:
            field_dict["minTransferTime"] = min_transfer_time
        if max_transfer_time is not UNSET:
            field_dict["maxTransferTime"] = max_transfer_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        max_transfers = d.pop("maxTransfers", UNSET)

        walk_speed = d.pop("walkSpeed", UNSET)

        additional_transfer_time = d.pop("additionalTransferTime", UNSET)

        min_transfer_time = d.pop("minTransferTime", UNSET)

        max_transfer_time = d.pop("maxTransferTime", UNSET)

        trip_mobility_filter = cls(
            max_transfers=max_transfers,
            walk_speed=walk_speed,
            additional_transfer_time=additional_transfer_time,
            min_transfer_time=min_transfer_time,
            max_transfer_time=max_transfer_time,
        )

        trip_mobility_filter.additional_properties = d
        return trip_mobility_filter

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
