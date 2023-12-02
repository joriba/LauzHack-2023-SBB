from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.connection_end import ConnectionEnd
    from ..models.notice import Notice


T = TypeVar("T", bound="PTConnectionLeg")


@_attrs_define
class PTConnectionLeg:
    """Passenger transfer between 2 StopPlace's (typically when the underlying router does not know how to perform the
    interchange in detail, aka OJP TransferLeg).<br>Inherited from `Leg`.

        Attributes:
            id (str): Unique Index ordered within Trip (may be casted to Integer for local indexing). Example: 1.
            mode (str): Mode of the Leg
            type (str): **Inheritance discriminator to proper Subclass** (technical field required by [OpenApi 3
                Discriminator](https://swagger.io/docs/specification/data-models/inheritance-and-polymorphism/)) makes
                deserialization at consumer side easier.
            start (ConnectionEnd): Stop point on a `PTConnectionLeg`.
            end (ConnectionEnd): Stop point on a `PTConnectionLeg`.
            notices (List['Notice']):
            distance (Union[Unset, int]): Total distance for Leg (in meter).
            duration (Union[Unset, str]): [duration](https://www.w3.org/TR/xmlschema11-2/#duration)
    """

    id: str
    mode: str
    type: str
    start: "ConnectionEnd"
    end: "ConnectionEnd"
    notices: List["Notice"]
    distance: Union[Unset, int] = UNSET
    duration: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        mode = self.mode
        type = self.type
        start = self.start.to_dict()

        end = self.end.to_dict()

        notices = []
        for notices_item_data in self.notices:
            notices_item = notices_item_data.to_dict()

            notices.append(notices_item)

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
                "notices": notices,
            }
        )
        if distance is not UNSET:
            field_dict["distance"] = distance
        if duration is not UNSET:
            field_dict["duration"] = duration

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.connection_end import ConnectionEnd
        from ..models.notice import Notice

        d = src_dict.copy()
        id = d.pop("id")

        mode = d.pop("mode")

        type = d.pop("type")

        start = ConnectionEnd.from_dict(d.pop("start"))

        end = ConnectionEnd.from_dict(d.pop("end"))

        notices = []
        _notices = d.pop("notices")
        for notices_item_data in _notices:
            notices_item = Notice.from_dict(notices_item_data)

            notices.append(notices_item)

        distance = d.pop("distance", UNSET)

        duration = d.pop("duration", UNSET)

        pt_connection_leg = cls(
            id=id,
            mode=mode,
            type=type,
            start=start,
            end=end,
            notices=notices,
            distance=distance,
            duration=duration,
        )

        pt_connection_leg.additional_properties = d
        return pt_connection_leg

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
