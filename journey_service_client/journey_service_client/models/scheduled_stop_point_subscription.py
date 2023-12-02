from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.stop_call_subscription import StopCallSubscription
    from ..models.stop_place_subscription import StopPlaceSubscription


T = TypeVar("T", bound="ScheduledStopPointSubscription")


@_attrs_define
class ScheduledStopPointSubscription:
    """
    Attributes:
        place (Union[Unset, StopPlaceSubscription]):
        arrival (Union[Unset, StopCallSubscription]):
        departure (Union[Unset, StopCallSubscription]):
    """

    place: Union[Unset, "StopPlaceSubscription"] = UNSET
    arrival: Union[Unset, "StopCallSubscription"] = UNSET
    departure: Union[Unset, "StopCallSubscription"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        place: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.place, Unset):
            place = self.place.to_dict()

        arrival: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.arrival, Unset):
            arrival = self.arrival.to_dict()

        departure: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.departure, Unset):
            departure = self.departure.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if place is not UNSET:
            field_dict["place"] = place
        if arrival is not UNSET:
            field_dict["arrival"] = arrival
        if departure is not UNSET:
            field_dict["departure"] = departure

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.stop_call_subscription import StopCallSubscription
        from ..models.stop_place_subscription import StopPlaceSubscription

        d = src_dict.copy()
        _place = d.pop("place", UNSET)
        place: Union[Unset, StopPlaceSubscription]
        if isinstance(_place, Unset):
            place = UNSET
        else:
            place = StopPlaceSubscription.from_dict(_place)

        _arrival = d.pop("arrival", UNSET)
        arrival: Union[Unset, StopCallSubscription]
        if isinstance(_arrival, Unset):
            arrival = UNSET
        else:
            arrival = StopCallSubscription.from_dict(_arrival)

        _departure = d.pop("departure", UNSET)
        departure: Union[Unset, StopCallSubscription]
        if isinstance(_departure, Unset):
            departure = UNSET
        else:
            departure = StopCallSubscription.from_dict(_departure)

        scheduled_stop_point_subscription = cls(
            place=place,
            arrival=arrival,
            departure=departure,
        )

        scheduled_stop_point_subscription.additional_properties = d
        return scheduled_stop_point_subscription

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
