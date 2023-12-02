from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pagination_cursor import PaginationCursor
    from ..models.trip import Trip


T = TypeVar("T", bound="TripResponse")


@_attrs_define
class TripResponse:
    """Contains a list of Trip's matching the search-criteria.

    Attributes:
        trips (List['Trip']):
        pagination_cursor (Union[Unset, PaginationCursor]): Pagination-cursor for next/previous of the same. By means in
            a Trip context earlier/later.
        service_product_adapted (Union[Unset, bool]): Set for `v3/trips/{id}` only, otherwise set to null because
            irrelevant. **100% correctness cannot be guaranteed if `TripResponse::serviceProductAdapted` is true, do
            validate found `Trip` whether it might be what you are looking for!**
            - If request parameter `retryFuzzy`=true and direct resolving of `Trip::id` failed and `ServiceProduct::number`
            tolerant re-search found an alternate match, this flag will be true.
            - Otherwise if `retryFuzzy`=false or resolved initially by `id` this flag will be false.
    """

    trips: List["Trip"]
    pagination_cursor: Union[Unset, "PaginationCursor"] = UNSET
    service_product_adapted: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        trips = []
        for trips_item_data in self.trips:
            trips_item = trips_item_data.to_dict()

            trips.append(trips_item)

        pagination_cursor: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pagination_cursor, Unset):
            pagination_cursor = self.pagination_cursor.to_dict()

        service_product_adapted = self.service_product_adapted

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "trips": trips,
            }
        )
        if pagination_cursor is not UNSET:
            field_dict["paginationCursor"] = pagination_cursor
        if service_product_adapted is not UNSET:
            field_dict["serviceProductAdapted"] = service_product_adapted

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pagination_cursor import PaginationCursor
        from ..models.trip import Trip

        d = src_dict.copy()
        trips = []
        _trips = d.pop("trips")
        for trips_item_data in _trips:
            trips_item = Trip.from_dict(trips_item_data)

            trips.append(trips_item)

        _pagination_cursor = d.pop("paginationCursor", UNSET)
        pagination_cursor: Union[Unset, PaginationCursor]
        if isinstance(_pagination_cursor, Unset):
            pagination_cursor = UNSET
        else:
            pagination_cursor = PaginationCursor.from_dict(_pagination_cursor)

        service_product_adapted = d.pop("serviceProductAdapted", UNSET)

        trip_response = cls(
            trips=trips,
            pagination_cursor=pagination_cursor,
            service_product_adapted=service_product_adapted,
        )

        trip_response.additional_properties = d
        return trip_response

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
