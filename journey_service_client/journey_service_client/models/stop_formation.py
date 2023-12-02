from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.stop_formation_leaving_direction import StopFormationLeavingDirection
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.info import Info
    from ..models.legend_item import LegendItem
    from ..models.section import Section


T = TypeVar("T", bound="StopFormation")


@_attrs_define
class StopFormation:
    """Composition of a train resp. its cars at a specific stop related to platform sections (aka Transmodel 'COMPOUND
    TRAIN' or 'TRAIN').

        Attributes:
            station_name (str): `StopV2::name` or `v3.StopPlace::name` with snapshot of concrete formation (aka Train-
                Composition) at this `ScheduledStopPoint`. Example: Zürich HB.
            sections (List['Section']):
            legend_items (List['LegendItem']):
            leaving_direction (StopFormationLeavingDirection): Direction in which the train leaves in relation to sections
                at platform. Example: LEFT.
            info (Union[Unset, Info]): Concrete realtime formation-changes.
    """

    station_name: str
    sections: List["Section"]
    legend_items: List["LegendItem"]
    leaving_direction: StopFormationLeavingDirection
    info: Union[Unset, "Info"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        station_name = self.station_name
        sections = []
        for sections_item_data in self.sections:
            sections_item = sections_item_data.to_dict()

            sections.append(sections_item)

        legend_items = []
        for legend_items_item_data in self.legend_items:
            legend_items_item = legend_items_item_data.to_dict()

            legend_items.append(legend_items_item)

        leaving_direction = self.leaving_direction.value

        info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.info, Unset):
            info = self.info.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stationName": station_name,
                "sections": sections,
                "legendItems": legend_items,
                "leavingDirection": leaving_direction,
            }
        )
        if info is not UNSET:
            field_dict["info"] = info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.info import Info
        from ..models.legend_item import LegendItem
        from ..models.section import Section

        d = src_dict.copy()
        station_name = d.pop("stationName")

        sections = []
        _sections = d.pop("sections")
        for sections_item_data in _sections:
            sections_item = Section.from_dict(sections_item_data)

            sections.append(sections_item)

        legend_items = []
        _legend_items = d.pop("legendItems")
        for legend_items_item_data in _legend_items:
            legend_items_item = LegendItem.from_dict(legend_items_item_data)

            legend_items.append(legend_items_item)

        leaving_direction = StopFormationLeavingDirection(d.pop("leavingDirection"))

        _info = d.pop("info", UNSET)
        info: Union[Unset, Info]
        if isinstance(_info, Unset):
            info = UNSET
        else:
            info = Info.from_dict(_info)

        stop_formation = cls(
            station_name=station_name,
            sections=sections,
            legend_items=legend_items,
            leaving_direction=leaving_direction,
            info=info,
        )

        stop_formation.additional_properties = d
        return stop_formation

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
