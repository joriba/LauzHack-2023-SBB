from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.service_journey import ServiceJourney


T = TypeVar("T", bound="Departure")


@_attrs_define
class Departure:
    """Departure view of a kind of partial `DatedVehicleJourney` from a specific stop-point towards its final destination
    or direction.

        Attributes:
            service_journey (ServiceJourney): A passenger carrying vehicle journey for one specified operation day.
    """

    service_journey: "ServiceJourney"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        service_journey = self.service_journey.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "serviceJourney": service_journey,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.service_journey import ServiceJourney

        d = src_dict.copy()
        service_journey = ServiceJourney.from_dict(d.pop("serviceJourney"))

        departure = cls(
            service_journey=service_journey,
        )

        departure.additional_properties = d
        return departure

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
