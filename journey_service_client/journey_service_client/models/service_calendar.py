from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.operating_period import OperatingPeriod


T = TypeVar("T", bound="ServiceCalendar")


@_attrs_define
class ServiceCalendar:
    """Available planned journey calendar to span the whole time range covered by underlying systems for various Journey-
    Planner data.

        Attributes:
            name (str): Informational reference name.<br>(Translated according to Accept-Language.) Example: CH Fahrplan
                (SBB).
            operating_periods (List['OperatingPeriod']):
    """

    name: str
    operating_periods: List["OperatingPeriod"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        operating_periods = []
        for operating_periods_item_data in self.operating_periods:
            operating_periods_item = operating_periods_item_data.to_dict()

            operating_periods.append(operating_periods_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "operatingPeriods": operating_periods,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.operating_period import OperatingPeriod

        d = src_dict.copy()
        name = d.pop("name")

        operating_periods = []
        _operating_periods = d.pop("operatingPeriods")
        for operating_periods_item_data in _operating_periods:
            operating_periods_item = OperatingPeriod.from_dict(operating_periods_item_data)

            operating_periods.append(operating_periods_item)

        service_calendar = cls(
            name=name,
            operating_periods=operating_periods,
        )

        service_calendar.additional_properties = d
        return service_calendar

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
