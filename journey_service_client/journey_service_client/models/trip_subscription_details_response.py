from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.subscription import Subscription
    from ..models.trip_subscription import TripSubscription


T = TypeVar("T", bound="TripSubscriptionDetailsResponse")


@_attrs_define
class TripSubscriptionDetailsResponse:
    """More details about a subscribed `Trip`.

    Attributes:
        subscription (Subscription): All details about subscription (like `Trip` HCCS subscriptionId).
        trip_subscription (TripSubscription): Details about a previously subscribed `Trip` (aka HCCS
            ServiceSubscription).
        passengers_count (Union[Unset, int]): This special feature is designed for the staff of operators, and is
            available on request. With this parameter the staff is able to submit the number of affected passengers, e.g.
            for waiting for interchanges.
    """

    subscription: "Subscription"
    trip_subscription: "TripSubscription"
    passengers_count: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        subscription = self.subscription.to_dict()

        trip_subscription = self.trip_subscription.to_dict()

        passengers_count = self.passengers_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subscription": subscription,
                "tripSubscription": trip_subscription,
            }
        )
        if passengers_count is not UNSET:
            field_dict["passengersCount"] = passengers_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.subscription import Subscription
        from ..models.trip_subscription import TripSubscription

        d = src_dict.copy()
        subscription = Subscription.from_dict(d.pop("subscription"))

        trip_subscription = TripSubscription.from_dict(d.pop("tripSubscription"))

        passengers_count = d.pop("passengersCount", UNSET)

        trip_subscription_details_response = cls(
            subscription=subscription,
            trip_subscription=trip_subscription,
            passengers_count=passengers_count,
        )

        trip_subscription_details_response.additional_properties = d
        return trip_subscription_details_response

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
