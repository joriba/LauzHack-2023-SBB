from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="StopPointInterval")


@_attrs_define
class StopPointInterval:
    """Start/end description of a `ServiceJourney`.

    Example:
        {'startStopPlaceId': '8503000', 'endStopPlaceId': '8507000'}

    Attributes:
        start_stop_place_id (str): Starting point of the `ServiceJourney` at origin (very first stop-point). Example:
            8503000.
        end_stop_place_id (str): Starting point of the `ServiceJourney` at destination (very last stop-point). Example:
            8507000.
    """

    start_stop_place_id: str
    end_stop_place_id: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        start_stop_place_id = self.start_stop_place_id
        end_stop_place_id = self.end_stop_place_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "startStopPlaceId": start_stop_place_id,
                "endStopPlaceId": end_stop_place_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        start_stop_place_id = d.pop("startStopPlaceId")

        end_stop_place_id = d.pop("endStopPlaceId")

        stop_point_interval = cls(
            start_stop_place_id=start_stop_place_id,
            end_stop_place_id=end_stop_place_id,
        )

        stop_point_interval.additional_properties = d
        return stop_point_interval

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
