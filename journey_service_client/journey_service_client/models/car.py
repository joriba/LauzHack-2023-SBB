from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.car_class import CarClass
from ..models.car_occupancy import CarOccupancy
from ..models.car_type import CarType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Car")


@_attrs_define
class Car:
    """Single wagon of a transport-product (aka Transmodel 'TRAIN ELEMENT').

    Attributes:
        type (CarType): Type of the car in the formation (e.g. Locomotive, Restaurant or Couchette).<br>x-extensible-
            enum:
        occupancy (CarOccupancy): Prognosed occupancy of the car (overall 1st and/or 2nd class).<br>x-extensible-enum:
            [UNKNOWN,LOW,MEDIUM,HIGH]
        attributes (List[str]):
        closed (bool): true: For unknown reasons the car is not usable for passengers: false: Open or unknown.
        unattended (bool): true: the restaurant is not attend and therefore not open. The car is still usable for
            passengers, false: restaurant is open
        previous_passage (bool): Determines if a passenger may pass (de: Durchgang) to the previous car within
            formation.
        next_passage (bool): Determines if a passenger may pass (de: Durchgang) to the next car within the formation.
        display_no_passage (bool): true: icon for no passage should be displayed between this car and the next one (from
            left to right)
        number (Union[Unset, str]): Number of the car within a formation (this number can be seen by passengers on a car
            for e.g. next to the door).
        car_uic (Union[Unset, str]): The carUic of the car. With this information you can calculate with the carUic from
            a beacon, where you are inside a trainformation. This information is not always present (null means not
            present).
        class_ (Union[Unset, CarClass]): Passenger class (first or second) of the car.<br>x-extensible-enum:
        destination (Union[Unset, str]): Each `Car::destination` with a value (set once per **TrainGroup** on the
            leading car) represents a distinguished set of cars going to the very same direction. If no destination is set,
            by means all `Car's` belong to the same Traingroup and therefore have the same direction (destination is omitted
            by SBB Business Rule). If given (more than once), the formation represents a wing-train (de:Flügelzug) where
            each Traingroup is heading to a different direction.
        model_type (Union[Unset, str]): Specific parameter from Ceres which describes vehicle's of a train-formation
            (aka de: zbpType, FahrzeugType gemäss Zugbildungsplan (ZBP), s. [CERES
            Glossar](https://confluence.sbb.ch/pages/viewpage.action?spaceKey=CAROS&title=CERES+Glossar) Example:
            RABDe(ICN).
    """

    type: CarType
    occupancy: CarOccupancy
    attributes: List[str]
    closed: bool
    unattended: bool
    previous_passage: bool
    next_passage: bool
    display_no_passage: bool
    number: Union[Unset, str] = UNSET
    car_uic: Union[Unset, str] = UNSET
    class_: Union[Unset, CarClass] = UNSET
    destination: Union[Unset, str] = UNSET
    model_type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        occupancy = self.occupancy.value

        attributes = self.attributes

        closed = self.closed
        unattended = self.unattended
        previous_passage = self.previous_passage
        next_passage = self.next_passage
        display_no_passage = self.display_no_passage
        number = self.number
        car_uic = self.car_uic
        class_: Union[Unset, str] = UNSET
        if not isinstance(self.class_, Unset):
            class_ = self.class_.value

        destination = self.destination
        model_type = self.model_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "occupancy": occupancy,
                "attributes": attributes,
                "closed": closed,
                "unattended": unattended,
                "previousPassage": previous_passage,
                "nextPassage": next_passage,
                "displayNoPassage": display_no_passage,
            }
        )
        if number is not UNSET:
            field_dict["number"] = number
        if car_uic is not UNSET:
            field_dict["carUic"] = car_uic
        if class_ is not UNSET:
            field_dict["class"] = class_
        if destination is not UNSET:
            field_dict["destination"] = destination
        if model_type is not UNSET:
            field_dict["modelType"] = model_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = CarType(d.pop("type"))

        occupancy = CarOccupancy(d.pop("occupancy"))

        attributes = cast(List[str], d.pop("attributes"))

        closed = d.pop("closed")

        unattended = d.pop("unattended")

        previous_passage = d.pop("previousPassage")

        next_passage = d.pop("nextPassage")

        display_no_passage = d.pop("displayNoPassage")

        number = d.pop("number", UNSET)

        car_uic = d.pop("carUic", UNSET)

        _class_ = d.pop("class", UNSET)
        class_: Union[Unset, CarClass]
        if isinstance(_class_, Unset):
            class_ = UNSET
        else:
            class_ = CarClass(_class_)

        destination = d.pop("destination", UNSET)

        model_type = d.pop("modelType", UNSET)

        car = cls(
            type=type,
            occupancy=occupancy,
            attributes=attributes,
            closed=closed,
            unattended=unattended,
            previous_passage=previous_passage,
            next_passage=next_passage,
            display_no_passage=display_no_passage,
            number=number,
            car_uic=car_uic,
            class_=class_,
            destination=destination,
            model_type=model_type,
        )

        car.additional_properties = d
        return car

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
