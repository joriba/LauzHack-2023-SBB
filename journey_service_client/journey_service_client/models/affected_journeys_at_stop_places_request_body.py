from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.stop_point_mode_enum import StopPointModeEnum
from ..models.transport_mode_enum import TransportModeEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.affected_line_reference import AffectedLineReference
    from ..models.date_time_interval import DateTimeInterval


T = TypeVar("T", bound="AffectedJourneysAtStopPlacesRequestBody")


@_attrs_define
class AffectedJourneysAtStopPlacesRequestBody:
    """Request parameters (POST body).

    Attributes:
        stop_place_ids (List[str]):
        date_time_intervals (List['DateTimeInterval']):
        affected_line_reference (Union[Unset, AffectedLineReference]): Reference to a ServiceProduct with its id
            Example: {'start': '2023-04-18T14:55:00+01:00', 'end': '2023-09-07T09:10:00+02:00', 'dailyStartingAt': '17:15',
            'dailyEndingAt': '18:05'}.
        service_product_line_id (Union[Unset, str]): Matching `ServiceProduct::lineId`, may represent a kind of overall
            journeys of a certain `ServiceProduct::line`, see related `affectedLineReference`.
        include_transport_modes (Union[Unset, List[TransportModeEnum]]):
        stop_point_match_mode (Union[Unset, StopPointModeEnum]): Matching mode for equivalent stop-
            points.<br>x-extensible-enum:  Example: DEFAULT.
    """

    stop_place_ids: List[str]
    date_time_intervals: List["DateTimeInterval"]
    affected_line_reference: Union[Unset, "AffectedLineReference"] = UNSET
    service_product_line_id: Union[Unset, str] = UNSET
    include_transport_modes: Union[Unset, List[TransportModeEnum]] = UNSET
    stop_point_match_mode: Union[Unset, StopPointModeEnum] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        stop_place_ids = self.stop_place_ids

        date_time_intervals = []
        for date_time_intervals_item_data in self.date_time_intervals:
            date_time_intervals_item = date_time_intervals_item_data.to_dict()

            date_time_intervals.append(date_time_intervals_item)

        affected_line_reference: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.affected_line_reference, Unset):
            affected_line_reference = self.affected_line_reference.to_dict()

        service_product_line_id = self.service_product_line_id
        include_transport_modes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.include_transport_modes, Unset):
            include_transport_modes = []
            for include_transport_modes_item_data in self.include_transport_modes:
                include_transport_modes_item = include_transport_modes_item_data.value

                include_transport_modes.append(include_transport_modes_item)

        stop_point_match_mode: Union[Unset, str] = UNSET
        if not isinstance(self.stop_point_match_mode, Unset):
            stop_point_match_mode = self.stop_point_match_mode.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stopPlaceIds": stop_place_ids,
                "dateTimeIntervals": date_time_intervals,
            }
        )
        if affected_line_reference is not UNSET:
            field_dict["affectedLineReference"] = affected_line_reference
        if service_product_line_id is not UNSET:
            field_dict["serviceProductLineId"] = service_product_line_id
        if include_transport_modes is not UNSET:
            field_dict["includeTransportModes"] = include_transport_modes
        if stop_point_match_mode is not UNSET:
            field_dict["stopPointMatchMode"] = stop_point_match_mode

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.affected_line_reference import AffectedLineReference
        from ..models.date_time_interval import DateTimeInterval

        d = src_dict.copy()
        stop_place_ids = cast(List[str], d.pop("stopPlaceIds"))

        date_time_intervals = []
        _date_time_intervals = d.pop("dateTimeIntervals")
        for date_time_intervals_item_data in _date_time_intervals:
            date_time_intervals_item = DateTimeInterval.from_dict(date_time_intervals_item_data)

            date_time_intervals.append(date_time_intervals_item)

        _affected_line_reference = d.pop("affectedLineReference", UNSET)
        affected_line_reference: Union[Unset, AffectedLineReference]
        if isinstance(_affected_line_reference, Unset):
            affected_line_reference = UNSET
        else:
            affected_line_reference = AffectedLineReference.from_dict(_affected_line_reference)

        service_product_line_id = d.pop("serviceProductLineId", UNSET)

        include_transport_modes = []
        _include_transport_modes = d.pop("includeTransportModes", UNSET)
        for include_transport_modes_item_data in _include_transport_modes or []:
            include_transport_modes_item = TransportModeEnum(include_transport_modes_item_data)

            include_transport_modes.append(include_transport_modes_item)

        _stop_point_match_mode = d.pop("stopPointMatchMode", UNSET)
        stop_point_match_mode: Union[Unset, StopPointModeEnum]
        if isinstance(_stop_point_match_mode, Unset):
            stop_point_match_mode = UNSET
        else:
            stop_point_match_mode = StopPointModeEnum(_stop_point_match_mode)

        affected_journeys_at_stop_places_request_body = cls(
            stop_place_ids=stop_place_ids,
            date_time_intervals=date_time_intervals,
            affected_line_reference=affected_line_reference,
            service_product_line_id=service_product_line_id,
            include_transport_modes=include_transport_modes,
            stop_point_match_mode=stop_point_match_mode,
        )

        affected_journeys_at_stop_places_request_body.additional_properties = d
        return affected_journeys_at_stop_places_request_body

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
