from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.scheduled_stop_point_subscription import ScheduledStopPointSubscription
    from ..models.service_product_subscription import ServiceProductSubscription


T = TypeVar("T", bound="ServiceJourneySubscription")


@_attrs_define
class ServiceJourneySubscription:
    """
    Attributes:
        stop_points (List['ScheduledStopPointSubscription']):
        service_products (List['ServiceProductSubscription']):
    """

    stop_points: List["ScheduledStopPointSubscription"]
    service_products: List["ServiceProductSubscription"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        stop_points = []
        for stop_points_item_data in self.stop_points:
            stop_points_item = stop_points_item_data.to_dict()

            stop_points.append(stop_points_item)

        service_products = []
        for service_products_item_data in self.service_products:
            service_products_item = service_products_item_data.to_dict()

            service_products.append(service_products_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stopPoints": stop_points,
                "serviceProducts": service_products,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.scheduled_stop_point_subscription import ScheduledStopPointSubscription
        from ..models.service_product_subscription import ServiceProductSubscription

        d = src_dict.copy()
        stop_points = []
        _stop_points = d.pop("stopPoints")
        for stop_points_item_data in _stop_points:
            stop_points_item = ScheduledStopPointSubscription.from_dict(stop_points_item_data)

            stop_points.append(stop_points_item)

        service_products = []
        _service_products = d.pop("serviceProducts")
        for service_products_item_data in _service_products:
            service_products_item = ServiceProductSubscription.from_dict(service_products_item_data)

            service_products.append(service_products_item)

        service_journey_subscription = cls(
            stop_points=stop_points,
            service_products=service_products,
        )

        service_journey_subscription.additional_properties = d
        return service_journey_subscription

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
