from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.dated_vehicle_journey import DatedVehicleJourney


T = TypeVar("T", bound="DatedVehicleJourneyResponse")


@_attrs_define
class DatedVehicleJourneyResponse:
    """Contains a list of DatedVehicleJourney's matching the search-criteria.

    Attributes:
        dated_vehicle_journeys (List['DatedVehicleJourney']):
    """

    dated_vehicle_journeys: List["DatedVehicleJourney"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dated_vehicle_journeys = []
        for dated_vehicle_journeys_item_data in self.dated_vehicle_journeys:
            dated_vehicle_journeys_item = dated_vehicle_journeys_item_data.to_dict()

            dated_vehicle_journeys.append(dated_vehicle_journeys_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "datedVehicleJourneys": dated_vehicle_journeys,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dated_vehicle_journey import DatedVehicleJourney

        d = src_dict.copy()
        dated_vehicle_journeys = []
        _dated_vehicle_journeys = d.pop("datedVehicleJourneys")
        for dated_vehicle_journeys_item_data in _dated_vehicle_journeys:
            dated_vehicle_journeys_item = DatedVehicleJourney.from_dict(dated_vehicle_journeys_item_data)

            dated_vehicle_journeys.append(dated_vehicle_journeys_item)

        dated_vehicle_journey_response = cls(
            dated_vehicle_journeys=dated_vehicle_journeys,
        )

        dated_vehicle_journey_response.additional_properties = d
        return dated_vehicle_journey_response

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
