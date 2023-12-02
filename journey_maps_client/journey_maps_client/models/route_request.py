from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.mot import Mot
from ..types import UNSET, Unset

T = TypeVar("T", bound="RouteRequest")


@_attrs_define
class RouteRequest:
    """
    Attributes:
        calculate_midpoint (Union[Unset, bool]):
        from_station_id (Union[Unset, int]):
        generalization (Union[Unset, bool]):
        mot (Union[Unset, Mot]):
        route_identifier (Union[Unset, str]):
        to_station_id (Union[Unset, int]):
        via (Union[Unset, str]):
    """

    calculate_midpoint: Union[Unset, bool] = UNSET
    from_station_id: Union[Unset, int] = UNSET
    generalization: Union[Unset, bool] = UNSET
    mot: Union[Unset, Mot] = UNSET
    route_identifier: Union[Unset, str] = UNSET
    to_station_id: Union[Unset, int] = UNSET
    via: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        calculate_midpoint = self.calculate_midpoint
        from_station_id = self.from_station_id
        generalization = self.generalization
        mot: Union[Unset, str] = UNSET
        if not isinstance(self.mot, Unset):
            mot = self.mot.value

        route_identifier = self.route_identifier
        to_station_id = self.to_station_id
        via = self.via

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if calculate_midpoint is not UNSET:
            field_dict["calculateMidpoint"] = calculate_midpoint
        if from_station_id is not UNSET:
            field_dict["fromStationId"] = from_station_id
        if generalization is not UNSET:
            field_dict["generalization"] = generalization
        if mot is not UNSET:
            field_dict["mot"] = mot
        if route_identifier is not UNSET:
            field_dict["routeIdentifier"] = route_identifier
        if to_station_id is not UNSET:
            field_dict["toStationId"] = to_station_id
        if via is not UNSET:
            field_dict["via"] = via

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        calculate_midpoint = d.pop("calculateMidpoint", UNSET)

        from_station_id = d.pop("fromStationId", UNSET)

        generalization = d.pop("generalization", UNSET)

        _mot = d.pop("mot", UNSET)
        mot: Union[Unset, Mot]
        if isinstance(_mot, Unset):
            mot = UNSET
        else:
            mot = Mot(_mot)

        route_identifier = d.pop("routeIdentifier", UNSET)

        to_station_id = d.pop("toStationId", UNSET)

        via = d.pop("via", UNSET)

        route_request = cls(
            calculate_midpoint=calculate_midpoint,
            from_station_id=from_station_id,
            generalization=generalization,
            mot=mot,
            route_identifier=route_identifier,
            to_station_id=to_station_id,
            via=via,
        )

        route_request.additional_properties = d
        return route_request

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
