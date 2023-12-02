from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.transport_mode_enum import TransportModeEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.affected_line_reference import AffectedLineReference
    from ..models.date_time_interval import DateTimeInterval
    from ..models.stop_point_interval import StopPointInterval


T = TypeVar("T", bound="AffectedJourneysRequestBody")


@_attrs_define
class AffectedJourneysRequestBody:
    """Request parameters (POST body).

    Attributes:
        stop_point_intervals (List['StopPointInterval']):
        date_time_intervals (List['DateTimeInterval']):
        affected_line_references (Union[Unset, List['AffectedLineReference']]):
        service_product_line_id (Union[Unset, str]): Matching `ServiceProduct::lineId`.
        bidirectional (Union[Unset, bool]): `ServiceJourney's` running in both directions (true) or directed (false)
            ones only. Default: True.
        include_transport_modes (Union[Unset, List[TransportModeEnum]]): Optionally restrict to a requestable set of SBB
            specific TransportMode's (aka OJP PTMode). The set is relevant for any vehicle-journey (`DatedVehicleJourney`,
            `PTRideLeg`, ..). Relates to `ServiceProduct::vehicleMode` and `::vehicleSubModes`.
            - Default: non-restricted (null or empty-list), by means all TransportMode's are searched.
            - If some choice is made, other TransportMode's are excluded implicitely.
            - To get TRAIN (VehicleMode::id) only, add:
            [HIGH_SPEED_TRAIN,INTERCITY,INTERREGIO,REGIO,URBAN_TRAIN,SPECIAL_TRAIN]
            >- Be aware that TRAMWAY also searches for METRO (not distinguished it here further!)
            - Also there is no exact possibility to distinguish more precisely between CABLEWAY_GONDOLA_CHAIRLIFT_FUNICULAR
            at search time<br><br>x-extensible-enum:
    """

    stop_point_intervals: List["StopPointInterval"]
    date_time_intervals: List["DateTimeInterval"]
    affected_line_references: Union[Unset, List["AffectedLineReference"]] = UNSET
    service_product_line_id: Union[Unset, str] = UNSET
    bidirectional: Union[Unset, bool] = True
    include_transport_modes: Union[Unset, List[TransportModeEnum]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        stop_point_intervals = []
        for stop_point_intervals_item_data in self.stop_point_intervals:
            stop_point_intervals_item = stop_point_intervals_item_data.to_dict()

            stop_point_intervals.append(stop_point_intervals_item)

        date_time_intervals = []
        for date_time_intervals_item_data in self.date_time_intervals:
            date_time_intervals_item = date_time_intervals_item_data.to_dict()

            date_time_intervals.append(date_time_intervals_item)

        affected_line_references: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.affected_line_references, Unset):
            affected_line_references = []
            for affected_line_references_item_data in self.affected_line_references:
                affected_line_references_item = affected_line_references_item_data.to_dict()

                affected_line_references.append(affected_line_references_item)

        service_product_line_id = self.service_product_line_id
        bidirectional = self.bidirectional
        include_transport_modes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.include_transport_modes, Unset):
            include_transport_modes = []
            for include_transport_modes_item_data in self.include_transport_modes:
                include_transport_modes_item = include_transport_modes_item_data.value

                include_transport_modes.append(include_transport_modes_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stopPointIntervals": stop_point_intervals,
                "dateTimeIntervals": date_time_intervals,
            }
        )
        if affected_line_references is not UNSET:
            field_dict["affectedLineReferences"] = affected_line_references
        if service_product_line_id is not UNSET:
            field_dict["serviceProductLineId"] = service_product_line_id
        if bidirectional is not UNSET:
            field_dict["bidirectional"] = bidirectional
        if include_transport_modes is not UNSET:
            field_dict["includeTransportModes"] = include_transport_modes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.affected_line_reference import AffectedLineReference
        from ..models.date_time_interval import DateTimeInterval
        from ..models.stop_point_interval import StopPointInterval

        d = src_dict.copy()
        stop_point_intervals = []
        _stop_point_intervals = d.pop("stopPointIntervals")
        for stop_point_intervals_item_data in _stop_point_intervals:
            stop_point_intervals_item = StopPointInterval.from_dict(stop_point_intervals_item_data)

            stop_point_intervals.append(stop_point_intervals_item)

        date_time_intervals = []
        _date_time_intervals = d.pop("dateTimeIntervals")
        for date_time_intervals_item_data in _date_time_intervals:
            date_time_intervals_item = DateTimeInterval.from_dict(date_time_intervals_item_data)

            date_time_intervals.append(date_time_intervals_item)

        affected_line_references = []
        _affected_line_references = d.pop("affectedLineReferences", UNSET)
        for affected_line_references_item_data in _affected_line_references or []:
            affected_line_references_item = AffectedLineReference.from_dict(affected_line_references_item_data)

            affected_line_references.append(affected_line_references_item)

        service_product_line_id = d.pop("serviceProductLineId", UNSET)

        bidirectional = d.pop("bidirectional", UNSET)

        include_transport_modes = []
        _include_transport_modes = d.pop("includeTransportModes", UNSET)
        for include_transport_modes_item_data in _include_transport_modes or []:
            include_transport_modes_item = TransportModeEnum(include_transport_modes_item_data)

            include_transport_modes.append(include_transport_modes_item)

        affected_journeys_request_body = cls(
            stop_point_intervals=stop_point_intervals,
            date_time_intervals=date_time_intervals,
            affected_line_references=affected_line_references,
            service_product_line_id=service_product_line_id,
            bidirectional=bidirectional,
            include_transport_modes=include_transport_modes,
        )

        affected_journeys_request_body.additional_properties = d
        return affected_journeys_request_body

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
