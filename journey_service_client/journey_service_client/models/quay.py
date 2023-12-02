from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Quay")


@_attrs_define
class Quay:
    """A `Quay` is the **place to board or alight a concrete vehicle by passengers**, aka **passenger-platform** for
    **train (de:Gleis)**, or **bus stand (de:Kante)** or **ship pier (de:Steg)**, related to a
    `ServiceProduct::vehicleMode`.

        Example:
            13

        Attributes:
            name (str): Quay name as displayed at a `StopPlace`, therefore special case like '12/13' is possible if decided
                dynamically at arrival or departure of the vehicle. Example: 12.
            id (Union[Unset, str]): Non-formal id provided by J-S, see `swissLocationId`. Example: 8507000_12.
            swiss_location_id (Union[Unset, str]): Quay SLOID, if known (within Switzerland), related to `name`.Swiss
                location id (SLOID) from DiDok. More on [Service Points (DiDok)
                API](https://developer.sbb.ch/apis/servicepoints/documentation). Depending on the context of the response, it
                might be an SLOID of the Quay itself or its departure/arrival track or even a section of a track. Example:
                ch:1:sloid:7000:55:49.
            parent_id (Union[Unset, str]): Id of the parent `Quay` (aka Transmodel `ZONE` or `STOP PLACE COMPONENT`), if
                any, modelling subzone / superzone relation. Useful to determine if 2 quays are on the same physical platform.
                Use it only for comparison, not for display, and not on long term comparison (may change over time). Only given
                for `StopPlaceDetailed`. Example: 8507000_12/13.
    """

    name: str
    id: Union[Unset, str] = UNSET
    swiss_location_id: Union[Unset, str] = UNSET
    parent_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        id = self.id
        swiss_location_id = self.swiss_location_id
        parent_id = self.parent_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if swiss_location_id is not UNSET:
            field_dict["swissLocationId"] = swiss_location_id
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        id = d.pop("id", UNSET)

        swiss_location_id = d.pop("swissLocationId", UNSET)

        parent_id = d.pop("parentId", UNSET)

        quay = cls(
            name=name,
            id=id,
            swiss_location_id=swiss_location_id,
            parent_id=parent_id,
        )

        quay.additional_properties = d
        return quay

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
