from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PointOfInterestCategory")


@_attrs_define
class PointOfInterestCategory:
    """Category of a Point of Interest (POI).

    Attributes:
        type (str): Type of `PointOfInterest` category (list of values see [ROKAS journey-pois API
            `Poi::category`](https://developer.sbb.ch/apis/journey-pois/documentation).<br>x-extensible-enum:  Example:
            shopping.
        name (str): Speaking name of `subtype` (or when unset of `type`).<br>(Translated according to Accept-Language.)
            Example: Bakery.
        subtype (Union[Unset, str]): Sub-category of `PointOfInterest`, related to `type` resp. main-category (list of
            values see [ROKAS journey-pois API `Poi::category`](https://developer.sbb.ch/apis/journey-pois/documentation).
            Example: bakery.
    """

    type: str
    name: str
    subtype: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        name = self.name
        subtype = self.subtype

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "name": name,
            }
        )
        if subtype is not UNSET:
            field_dict["subtype"] = subtype

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        name = d.pop("name")

        subtype = d.pop("subtype", UNSET)

        point_of_interest_category = cls(
            type=type,
            name=name,
            subtype=subtype,
        )

        point_of_interest_category.additional_properties = d
        return point_of_interest_category

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
