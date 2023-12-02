from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.train_component import TrainComponent


T = TypeVar("T", bound="Train")


@_attrs_define
class Train:
    """A vehicle-type composed of physical `TrainElement's` in a certain order, i.e. of wagons (aka car, coach) assembled
    together. Multiple `Train's` (aka wing-train or de:Flügelzug) may be coupled or decoupled in separate self-propelled
    units within a `CompoundTrain` on its journey.

        Attributes:
            components (List['TrainComponent']):
            label (Union[Unset, str]): Direction label, relates to `CompoundTrain::operationalOrientation`, if known. SBB
                UIs usually suppress the direction if only ONE `Train` is given in `CompoundTrain`. Example: Burgdorf.
    """

    components: List["TrainComponent"]
    label: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        components = []
        for components_item_data in self.components:
            components_item = components_item_data.to_dict()

            components.append(components_item)

        label = self.label

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "components": components,
            }
        )
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.train_component import TrainComponent

        d = src_dict.copy()
        components = []
        _components = d.pop("components")
        for components_item_data in _components:
            components_item = TrainComponent.from_dict(components_item_data)

            components.append(components_item)

        label = d.pop("label", UNSET)

        train = cls(
            components=components,
            label=label,
        )

        train.additional_properties = d
        return train

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
