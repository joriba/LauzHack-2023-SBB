from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Leg")


@_attrs_define
class Leg:
    """**Abstract Superclass** of concrete inherited sub-classes such as **`PTRideLeg`, `AccessLeg`, `PTConnectionLeg`,
    `AlternateModeLeg`** (aka OJP TripLeg)**, `PersonalLeg`**.

        Attributes:
            id (str): Unique Index ordered within Trip (may be casted to Integer for local indexing). Example: 1.
            mode (str): Mode of the Leg
            type (str): **Inheritance discriminator to proper Subclass** (technical field required by [OpenApi 3
                Discriminator](https://swagger.io/docs/specification/data-models/inheritance-and-polymorphism/)) makes
                deserialization at consumer side easier.
            distance (Union[Unset, int]): Total distance for Leg (in meter).
            duration (Union[Unset, str]): [duration](https://www.w3.org/TR/xmlschema11-2/#duration)
    """

    id: str
    mode: str
    type: str
    distance: Union[Unset, int] = UNSET
    duration: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        mode = self.mode
        type = self.type
        distance = self.distance
        duration = self.duration

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "mode": mode,
                "type": type,
            }
        )
        if distance is not UNSET:
            field_dict["distance"] = distance
        if duration is not UNSET:
            field_dict["duration"] = duration

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        mode = d.pop("mode")

        type = d.pop("type")

        distance = d.pop("distance", UNSET)

        duration = d.pop("duration", UNSET)

        leg = cls(
            id=id,
            mode=mode,
            type=type,
            distance=distance,
            duration=duration,
        )

        leg.additional_properties = d
        return leg

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
