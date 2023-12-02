from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.deck_plan import DeckPlan


T = TypeVar("T", bound="TrainElement")


@_attrs_define
class TrainElement:
    """An elementary component of a `Train` (for e.g. a wagon/car/locomotive or in general 'carriage') with rather
    permanent properties, see `TrainComponent` for its instance on a concrete journey.

        Attributes:
            attributes (List[str]):
            id (Union[Unset, str]): Aka car-UIC, which is potentially mapped to beacons installed. `/v3/vehicles/by-
                vehicle/{vehicleId}` may detect a `Train` composing a `TrainElement` (mainly for SBB operated `VehicleMode`
                TRAIN) is on its way within a certain `ServiceJourney` (null means not present). Example: 938525010246.
            type (Union[Unset, str]): Type of car (where a 'CAR' may be self-propelled in case of a combined passenger-
                car/locomotive (de:Triebwagen)): <br>x-extensible-enum:  ['FA','WR','CC','WL','CAR','LOC','UNKNOWN']
            passenger_class (Union[Unset, str]): Passenger-class ('1' or '2') of the car, if known.<br>x-extensible-enum:
            deck_plan (Union[Unset, DeckPlan]): Plan of the build plan of vehicle-type such as a car (data quality might not
                be guaranted properly for all `TrainElement's`).
    """

    attributes: List[str]
    id: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    passenger_class: Union[Unset, str] = UNSET
    deck_plan: Union[Unset, "DeckPlan"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attributes = self.attributes

        id = self.id
        type = self.type
        passenger_class = self.passenger_class
        deck_plan: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.deck_plan, Unset):
            deck_plan = self.deck_plan.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attributes": attributes,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["type"] = type
        if passenger_class is not UNSET:
            field_dict["passengerClass"] = passenger_class
        if deck_plan is not UNSET:
            field_dict["deckPlan"] = deck_plan

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.deck_plan import DeckPlan

        d = src_dict.copy()
        attributes = cast(List[str], d.pop("attributes"))

        id = d.pop("id", UNSET)

        type = d.pop("type", UNSET)

        passenger_class = d.pop("passengerClass", UNSET)

        _deck_plan = d.pop("deckPlan", UNSET)
        deck_plan: Union[Unset, DeckPlan]
        if isinstance(_deck_plan, Unset):
            deck_plan = UNSET
        else:
            deck_plan = DeckPlan.from_dict(_deck_plan)

        train_element = cls(
            attributes=attributes,
            id=id,
            type=type,
            passenger_class=passenger_class,
            deck_plan=deck_plan,
        )

        train_element.additional_properties = d
        return train_element

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
