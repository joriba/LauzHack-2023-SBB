from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.boarding_position import BoardingPosition
    from ..models.train_element import TrainElement


T = TypeVar("T", bound="TrainComponent")


@_attrs_define
class TrainComponent:
    """An elementary component of a `Train` as an instance of a correspondent `TrainElement` on a concrete
    `ServiceJourney`, where specific values at each `ScheduledStopPoint` for this unique formation on an operation-day,
    may have its dynamic state (like section or exitSide).

        Attributes:
            occupancy (str): Occupancy prognosed on a daily basis (not a realtime fact, overall 1st and/or 2nd
                class).<br>x-extensible-enum: [LOW,MEDIUM,HIGH,UNKNOWN] Default: 'UNKNOWN'. Example: MEDIUM.
            previous_passage (bool): Determines if a passenger may pass (de: Durchgang) to the previous car within
                formation.
            next_passage (bool): Determines if a passenger may pass (de: Durchgang) to the next car within the formation.
            display_no_passage_icon (bool): true: icon for no passage should be displayed between this car and the next one
                (from left to right).
            closed (bool): true: For unknown reasons the car is not usable for passengers: false: Open or unknown.
            element (TrainElement): An elementary component of a `Train` (for e.g. a wagon/car/locomotive or in general
                'carriage') with rather permanent properties, see `TrainComponent` for its instance on a concrete journey.
            attributes_advertised (List[str]):
            label (Union[Unset, str]): Label on the `TrainElement`, typically a number visible by passenger close to the
                boarding door. Example: 7.
            restaurant_attended (Union[Unset, bool]): true: the restaurant is attended, false: the restaurant is not
                attended, null: no restaurant on this car
            boarding_position (Union[Unset, BoardingPosition]): A location within a `Quay` from which passengers may
                directly board, or onto which passengers may directly alight from a vehicle.
    """

    previous_passage: bool
    next_passage: bool
    display_no_passage_icon: bool
    closed: bool
    element: "TrainElement"
    attributes_advertised: List[str]
    occupancy: str = "UNKNOWN"
    label: Union[Unset, str] = UNSET
    restaurant_attended: Union[Unset, bool] = UNSET
    boarding_position: Union[Unset, "BoardingPosition"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        occupancy = self.occupancy
        previous_passage = self.previous_passage
        next_passage = self.next_passage
        display_no_passage_icon = self.display_no_passage_icon
        closed = self.closed
        element = self.element.to_dict()

        attributes_advertised = self.attributes_advertised

        label = self.label
        restaurant_attended = self.restaurant_attended
        boarding_position: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.boarding_position, Unset):
            boarding_position = self.boarding_position.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "occupancy": occupancy,
                "previousPassage": previous_passage,
                "nextPassage": next_passage,
                "displayNoPassageIcon": display_no_passage_icon,
                "closed": closed,
                "element": element,
                "attributesAdvertised": attributes_advertised,
            }
        )
        if label is not UNSET:
            field_dict["label"] = label
        if restaurant_attended is not UNSET:
            field_dict["restaurantAttended"] = restaurant_attended
        if boarding_position is not UNSET:
            field_dict["boardingPosition"] = boarding_position

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.boarding_position import BoardingPosition
        from ..models.train_element import TrainElement

        d = src_dict.copy()
        occupancy = d.pop("occupancy")

        previous_passage = d.pop("previousPassage")

        next_passage = d.pop("nextPassage")

        display_no_passage_icon = d.pop("displayNoPassageIcon")

        closed = d.pop("closed")

        element = TrainElement.from_dict(d.pop("element"))

        attributes_advertised = cast(List[str], d.pop("attributesAdvertised"))

        label = d.pop("label", UNSET)

        restaurant_attended = d.pop("restaurantAttended", UNSET)

        _boarding_position = d.pop("boardingPosition", UNSET)
        boarding_position: Union[Unset, BoardingPosition]
        if isinstance(_boarding_position, Unset):
            boarding_position = UNSET
        else:
            boarding_position = BoardingPosition.from_dict(_boarding_position)

        train_component = cls(
            occupancy=occupancy,
            previous_passage=previous_passage,
            next_passage=next_passage,
            display_no_passage_icon=display_no_passage_icon,
            closed=closed,
            element=element,
            attributes_advertised=attributes_advertised,
            label=label,
            restaurant_attended=restaurant_attended,
            boarding_position=boarding_position,
        )

        train_component.additional_properties = d
        return train_component

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
