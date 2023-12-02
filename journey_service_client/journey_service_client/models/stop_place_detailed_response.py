from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.stop_place_detailed import StopPlaceDetailed


T = TypeVar("T", bound="StopPlaceDetailedResponse")


@_attrs_define
class StopPlaceDetailedResponse:
    """Response containing matching `StopPlaceDetailed`, which are `StopPlace`s with further details (see
    `StopPlace::links::detail`).

        Attributes:
            stop_places (List['StopPlaceDetailed']):
    """

    stop_places: List["StopPlaceDetailed"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        stop_places = []
        for stop_places_item_data in self.stop_places:
            stop_places_item = stop_places_item_data.to_dict()

            stop_places.append(stop_places_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stopPlaces": stop_places,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.stop_place_detailed import StopPlaceDetailed

        d = src_dict.copy()
        stop_places = []
        _stop_places = d.pop("stopPlaces")
        for stop_places_item_data in _stop_places:
            stop_places_item = StopPlaceDetailed.from_dict(stop_places_item_data)

            stop_places.append(stop_places_item)

        stop_place_detailed_response = cls(
            stop_places=stop_places,
        )

        stop_place_detailed_response.additional_properties = d
        return stop_place_detailed_response

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
