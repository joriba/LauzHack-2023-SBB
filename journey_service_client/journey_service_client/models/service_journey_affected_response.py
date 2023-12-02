from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.service_journey_affected import ServiceJourneyAffected


T = TypeVar("T", bound="ServiceJourneyAffectedResponse")


@_attrs_define
class ServiceJourneyAffectedResponse:
    """Contains a list of `ServiceJourneyAffected`'s.

    Attributes:
        service_journeys (List['ServiceJourneyAffected']):
    """

    service_journeys: List["ServiceJourneyAffected"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        service_journeys = []
        for service_journeys_item_data in self.service_journeys:
            service_journeys_item = service_journeys_item_data.to_dict()

            service_journeys.append(service_journeys_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "serviceJourneys": service_journeys,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.service_journey_affected import ServiceJourneyAffected

        d = src_dict.copy()
        service_journeys = []
        _service_journeys = d.pop("serviceJourneys")
        for service_journeys_item_data in _service_journeys:
            service_journeys_item = ServiceJourneyAffected.from_dict(service_journeys_item_data)

            service_journeys.append(service_journeys_item)

        service_journey_affected_response = cls(
            service_journeys=service_journeys,
        )

        service_journey_affected_response.additional_properties = d
        return service_journey_affected_response

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
