from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hysteresis import Hysteresis
    from ..models.subscription_period import SubscriptionPeriod


T = TypeVar("T", bound="TripSubscriptionRequestBody")


@_attrs_define
class TripSubscriptionRequestBody:
    """Request body.

    Attributes:
        trip_id (str): Set the Trip::id (or TripV2::reconstructionContext) to subscribe for realtime observation.
        subscription_period (Union[Unset, SubscriptionPeriod]): Period within the Trip should be observed regularly.
        hysteresis (Union[Unset, Hysteresis]): Subscriptions can be configured to only trigger notifications, if changes
            exceed a configured limit. This is done using the hysteresis property per user or subscription.
    """

    trip_id: str
    subscription_period: Union[Unset, "SubscriptionPeriod"] = UNSET
    hysteresis: Union[Unset, "Hysteresis"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        trip_id = self.trip_id
        subscription_period: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.subscription_period, Unset):
            subscription_period = self.subscription_period.to_dict()

        hysteresis: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.hysteresis, Unset):
            hysteresis = self.hysteresis.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tripId": trip_id,
            }
        )
        if subscription_period is not UNSET:
            field_dict["subscriptionPeriod"] = subscription_period
        if hysteresis is not UNSET:
            field_dict["hysteresis"] = hysteresis

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.hysteresis import Hysteresis
        from ..models.subscription_period import SubscriptionPeriod

        d = src_dict.copy()
        trip_id = d.pop("tripId")

        _subscription_period = d.pop("subscriptionPeriod", UNSET)
        subscription_period: Union[Unset, SubscriptionPeriod]
        if isinstance(_subscription_period, Unset):
            subscription_period = UNSET
        else:
            subscription_period = SubscriptionPeriod.from_dict(_subscription_period)

        _hysteresis = d.pop("hysteresis", UNSET)
        hysteresis: Union[Unset, Hysteresis]
        if isinstance(_hysteresis, Unset):
            hysteresis = UNSET
        else:
            hysteresis = Hysteresis.from_dict(_hysteresis)

        trip_subscription_request_body = cls(
            trip_id=trip_id,
            subscription_period=subscription_period,
            hysteresis=hysteresis,
        )

        trip_subscription_request_body.additional_properties = d
        return trip_subscription_request_body

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
