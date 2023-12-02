from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TripSubscriptionStatusResponse")


@_attrs_define
class TripSubscriptionStatusResponse:
    """Infos about the `Trip` subscription-status.

    Attributes:
        status (str): Subscription status like 'ACTIVE' (monitoring on), 'EXPIRED' (monitoring obsolete), ..
        trip_id (str): Original subscribed tripId `v3/Trip::id` (format Hafas raw reconstructionContext URL encoded but
            compatible with `/v3/trips/{id}`). Example: %C2%AC%C2%B6BAIM%C2%B6t%C2%AC%C2%B6HKI%C2%B6T%24A%3D1%40O%3DGen%C3%A
            8ve%40X%3D6142455%40Y%3D46210209%40u%3D0%40L%3D8501008%40a%3D128%40%24A%3D1%40O%3DFribourg%2FFreiburg%40X%3D7151
            045%40Y%3D46803146%40u%3D0%40L%3D8504100%40a%3D128%40%24202204081242%24202204081403%24IC+1++++%24%241%24%24%24%2
            4%C2%B6KC%C2%B6%23VE%230%23CF%23100%23CA%230%23CM%230%23SICT%231%23%C2%B6KCC%C2%B6%23VE%230%23ERG%231%23HIN%230%
            23ECK%23172122%7C172122%7C172203%7C172203%7C0%7C0%7C165%7C172093%7C1%7C-2147479534%7C0%23.
        technical_id (str): Internally generated Id trailing `Subscription::id` (useful in case of technical support).
    """

    status: str
    trip_id: str
    technical_id: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status
        trip_id = self.trip_id
        technical_id = self.technical_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "tripId": trip_id,
                "technicalId": technical_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        status = d.pop("status")

        trip_id = d.pop("tripId")

        technical_id = d.pop("technicalId")

        trip_subscription_status_response = cls(
            status=status,
            trip_id=trip_id,
            technical_id=technical_id,
        )

        trip_subscription_status_response.additional_properties = d
        return trip_subscription_status_response

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
