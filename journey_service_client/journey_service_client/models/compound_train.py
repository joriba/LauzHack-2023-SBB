from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.deck_plan import DeckPlan
    from ..models.legend_item_v3 import LegendItemV3
    from ..models.train import Train


T = TypeVar("T", bound="CompoundTrain")


@_attrs_define
class CompoundTrain:
    """A vehicle-type composed (aka composition/-formation) of a sequence of **one or more vehicle-type `Train`**. A
    `CompoundTrain` is always self-propelled (even if a Locomotive is not explicitely distinguishable).

        Attributes:
            operational_orientation (str): Type of operating direction.<br>x-extensible-enum: [LEFT, RIGHT] Example: LEFT.
            train_changes (List[str]):
            trains (List['Train']):
            legend_items (List['LegendItemV3']):
            deck_plan_assumed (Union[Unset, DeckPlan]): Plan of the build plan of vehicle-type such as a car (data quality
                might not be guaranted properly for all `TrainElement's`).
    """

    operational_orientation: str
    train_changes: List[str]
    trains: List["Train"]
    legend_items: List["LegendItemV3"]
    deck_plan_assumed: Union[Unset, "DeckPlan"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        operational_orientation = self.operational_orientation
        train_changes = self.train_changes

        trains = []
        for trains_item_data in self.trains:
            trains_item = trains_item_data.to_dict()

            trains.append(trains_item)

        legend_items = []
        for legend_items_item_data in self.legend_items:
            legend_items_item = legend_items_item_data.to_dict()

            legend_items.append(legend_items_item)

        deck_plan_assumed: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.deck_plan_assumed, Unset):
            deck_plan_assumed = self.deck_plan_assumed.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "operationalOrientation": operational_orientation,
                "trainChanges": train_changes,
                "trains": trains,
                "legendItems": legend_items,
            }
        )
        if deck_plan_assumed is not UNSET:
            field_dict["deckPlanAssumed"] = deck_plan_assumed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.deck_plan import DeckPlan
        from ..models.legend_item_v3 import LegendItemV3
        from ..models.train import Train

        d = src_dict.copy()
        operational_orientation = d.pop("operationalOrientation")

        train_changes = cast(List[str], d.pop("trainChanges"))

        trains = []
        _trains = d.pop("trains")
        for trains_item_data in _trains:
            trains_item = Train.from_dict(trains_item_data)

            trains.append(trains_item)

        legend_items = []
        _legend_items = d.pop("legendItems")
        for legend_items_item_data in _legend_items:
            legend_items_item = LegendItemV3.from_dict(legend_items_item_data)

            legend_items.append(legend_items_item)

        _deck_plan_assumed = d.pop("deckPlanAssumed", UNSET)
        deck_plan_assumed: Union[Unset, DeckPlan]
        if isinstance(_deck_plan_assumed, Unset):
            deck_plan_assumed = UNSET
        else:
            deck_plan_assumed = DeckPlan.from_dict(_deck_plan_assumed)

        compound_train = cls(
            operational_orientation=operational_orientation,
            train_changes=train_changes,
            trains=trains,
            legend_items=legend_items,
            deck_plan_assumed=deck_plan_assumed,
        )

        compound_train.additional_properties = d
        return compound_train

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
