from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.station import Station


T = TypeVar("T", bound="StationsPage")


@_attrs_define
class StationsPage:
    """Paged subset of all STATIONs according to its page-index.

    Attributes:
        stations (List['Station']):
        next_page_available (bool): True if there is a succeeding page of station-entries.
    """

    stations: List["Station"]
    next_page_available: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        stations = []
        for stations_item_data in self.stations:
            stations_item = stations_item_data.to_dict()

            stations.append(stations_item)

        next_page_available = self.next_page_available

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stations": stations,
                "nextPageAvailable": next_page_available,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.station import Station

        d = src_dict.copy()
        stations = []
        _stations = d.pop("stations")
        for stations_item_data in _stations:
            stations_item = Station.from_dict(stations_item_data)

            stations.append(stations_item)

        next_page_available = d.pop("nextPageAvailable")

        stations_page = cls(
            stations=stations,
            next_page_available=next_page_available,
        )

        stations_page.additional_properties = d
        return stations_page

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
