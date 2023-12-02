from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.service_journey import ServiceJourney


T = TypeVar("T", bound="DatedVehicleJourney")


@_attrs_define
class DatedVehicleJourney:
    """A particular journey of a vehicle on a particular operatingday including all modifications possibly decided by the
    control staff. Complete route of public transport service (de:Zuglauf).

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

        dated_vehicle_journey = cls(
            service_journey=service_journey,
        )

        dated_vehicle_journey.additional_properties = d
        return dated_vehicle_journey

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
