import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.place import Place


T = TypeVar("T", bound="AccessEnd")


@_attrs_define
class AccessEnd:
    """Stop point on an `AccessLeg`.

    Attributes:
        place (Place): **Abstract Superclass** of concrete inherited sub-classes such as **`StopPlace`, `Address`,
            `PointOfInterest`**.
        time_aimed (datetime.datetime): Date/time ([ISO-8601](https://datatracker.ietf.org/doc/html/rfc3339#section-5.6)
            UTC with time-numoffset (like '+02:00')) planned, relates to `AccessLeg::start/::end` whether departure or
            arrival time. Example: 2023-04-18T14:55:00+01:00.
    """

    place: "Place"
    time_aimed: datetime.datetime
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        place = self.place.to_dict()

        time_aimed = self.time_aimed.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "place": place,
                "timeAimed": time_aimed,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.place import Place

        d = src_dict.copy()
        place = Place.from_dict(d.pop("place"))

        time_aimed = isoparse(d.pop("timeAimed"))

        access_end = cls(
            place=place,
            time_aimed=time_aimed,
        )

        access_end.additional_properties = d
        return access_end

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
