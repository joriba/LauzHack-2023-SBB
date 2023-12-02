from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access_end import AccessEnd


T = TypeVar("T", bound="AccessLeg")


@_attrs_define
class AccessLeg:
    """Footpath or road access to/from a StopPlace at one end:
    - and typically an Address/PointOfInterest on the other end. May occur at the beginning or end of a Trip (aka OJP
    ContinuousLeg)- or in rare cases StopPlace as well (for Meta-Station footpath like main-station to any of its bus
    edges).<br>Inherited from `Leg`.

        Attributes:
            id (str): Unique Index ordered within Trip (may be casted to Integer for local indexing). Example: 1.
            mode (str): Mode of the Leg
            type (str): **Inheritance discriminator to proper Subclass** (technical field required by [OpenApi 3
                Discriminator](https://swagger.io/docs/specification/data-models/inheritance-and-polymorphism/)) makes
                deserialization at consumer side easier.
            start (AccessEnd): Stop point on an `AccessLeg`.
            end (AccessEnd): Stop point on an `AccessLeg`.
            distance (Union[Unset, int]): Total distance for Leg (in meter).
            duration (Union[Unset, str]): [duration](https://www.w3.org/TR/xmlschema11-2/#duration)
    """

    id: str
    mode: str
    type: str
    start: "AccessEnd"
    end: "AccessEnd"
    distance: Union[Unset, int] = UNSET
    duration: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        mode = self.mode
        type = self.type
        start = self.start.to_dict()

        end = self.end.to_dict()

        distance = self.distance
        duration = self.duration

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "mode": mode,
                "type": type,
                "start": start,
                "end": end,
            }
        )
        if distance is not UNSET:
            field_dict["distance"] = distance
        if duration is not UNSET:
            field_dict["duration"] = duration

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.access_end import AccessEnd

        d = src_dict.copy()
        id = d.pop("id")

        mode = d.pop("mode")

        type = d.pop("type")

        start = AccessEnd.from_dict(d.pop("start"))

        end = AccessEnd.from_dict(d.pop("end"))

        distance = d.pop("distance", UNSET)

        duration = d.pop("duration", UNSET)

        access_leg = cls(
            id=id,
            mode=mode,
            type=type,
            start=start,
            end=end,
            distance=distance,
            duration=duration,
        )

        access_leg.additional_properties = d
        return access_leg

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
