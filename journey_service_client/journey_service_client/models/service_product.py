from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.operator import Operator
    from ..models.vehicle_mode import VehicleMode


T = TypeVar("T", bound="ServiceProduct")


@_attrs_define
class ServiceProduct:
    """A passenger carrying Service (phyisical public transport vehicle) provided and operated by a certain Operator
    allocated to a concrete ServiceJourney on an `OperatingDay`.<br>See SBB specific transport-modes: [v580
    de:Verkehrsmittelkategorien (aka Transmodel or OJP/Siri
    `VehicleMode`)](https://github.com/SchweizerischeBundesbahnen/journey-service/blob/master/TransportMode.md).

        Attributes:
            name (str): Product name to display to passenger, may consist of {`vehicleSubModeShortName`, `line`, `number`}.
                (Refers to Transmodel `Line::name/::id`.) Example: IC 1 753.
            vehicle_mode (VehicleMode): A characterisation of the public transport operation according to the means of
                transport (aka OJP PtMode; Siri::VehicleMode; v580 TransportMode or de:Verkehrsmittelkategorie). Whether only
                `id` is given or submode as well depends on available data.
            line (Union[Unset, str]): Usually referring to a specific commercial PT route (where direction might be either
                way), shown on vehicle displays. If this value is missing, it is probably a _single-journey (de:Einzelfahrt)_.
                (Refers to Transmodel `Line::id`.) Example: 1.
            line_id (Union[Unset, str]): External line-reference like SLNID (source INFO+) or TU specific value (for e.g.
                provided by Postauto AG), relates to `line`. Example: R_547_000801_0883.
            number (Union[Unset, str]): Unique per `OperatingDay` (CH day-change at 04:00 !) and name (where 'IC 1' can run
                several times per day in either of opposite directions). For passenger display use `numberFormatted` instead!
                (Aka Transmodel: `TrainNumber`) Example: 753.
            number_formatted (Union[Unset, str]): Either as `number` or suppressed by BR to not confuse passengers (with
                internal technical values). Example: 753.
            operator (Union[Unset, Operator]): A company providing public transport services (aka Carrier).
            route_index_from (Union[Unset, int]): Defines the first ScheduledStop::routeIndex where this product is valid on
                a Line, null if unknown. Example: 3.
            route_index_to (Union[Unset, int]): Defines the last ScheduledStop::routeIndex where this product is valid on a
                Line, null if unknown Example: 7.
    """

    name: str
    vehicle_mode: "VehicleMode"
    line: Union[Unset, str] = UNSET
    line_id: Union[Unset, str] = UNSET
    number: Union[Unset, str] = UNSET
    number_formatted: Union[Unset, str] = UNSET
    operator: Union[Unset, "Operator"] = UNSET
    route_index_from: Union[Unset, int] = UNSET
    route_index_to: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        vehicle_mode = self.vehicle_mode.to_dict()

        line = self.line
        line_id = self.line_id
        number = self.number
        number_formatted = self.number_formatted
        operator: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.operator, Unset):
            operator = self.operator.to_dict()

        route_index_from = self.route_index_from
        route_index_to = self.route_index_to

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "vehicleMode": vehicle_mode,
            }
        )
        if line is not UNSET:
            field_dict["line"] = line
        if line_id is not UNSET:
            field_dict["lineId"] = line_id
        if number is not UNSET:
            field_dict["number"] = number
        if number_formatted is not UNSET:
            field_dict["numberFormatted"] = number_formatted
        if operator is not UNSET:
            field_dict["operator"] = operator
        if route_index_from is not UNSET:
            field_dict["routeIndexFrom"] = route_index_from
        if route_index_to is not UNSET:
            field_dict["routeIndexTo"] = route_index_to

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.operator import Operator
        from ..models.vehicle_mode import VehicleMode

        d = src_dict.copy()
        name = d.pop("name")

        vehicle_mode = VehicleMode.from_dict(d.pop("vehicleMode"))

        line = d.pop("line", UNSET)

        line_id = d.pop("lineId", UNSET)

        number = d.pop("number", UNSET)

        number_formatted = d.pop("numberFormatted", UNSET)

        _operator = d.pop("operator", UNSET)
        operator: Union[Unset, Operator]
        if isinstance(_operator, Unset):
            operator = UNSET
        else:
            operator = Operator.from_dict(_operator)

        route_index_from = d.pop("routeIndexFrom", UNSET)

        route_index_to = d.pop("routeIndexTo", UNSET)

        service_product = cls(
            name=name,
            vehicle_mode=vehicle_mode,
            line=line,
            line_id=line_id,
            number=number,
            number_formatted=number_formatted,
            operator=operator,
            route_index_from=route_index_from,
            route_index_to=route_index_to,
        )

        service_product.additional_properties = d
        return service_product

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
