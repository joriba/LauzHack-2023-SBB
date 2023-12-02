from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pt_via_reference_status import PTViaReferenceStatus
from ..models.transport_mode_enum import TransportModeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PTViaReference")


@_attrs_define
class PTViaReference:
    """Specification and behaviour of via StopPlace (aka OJP TripViaStructure).
    - TripsByOriginAndDestinationPostBody: all filters supported
    - ServiceCalendarByOriginAndDestinationRequestBody: only `stopPlaceId` and `transportModes` supported yet

        Attributes:
            stop_place_id (str): `StopPlace::id` to be passed as via. Example: 8507000.
            status (Union[Unset, PTViaReferenceStatus]): Boarding/alighting-status at via `StopPlace`.<br>x-extensible-enum:
                Default: PTViaReferenceStatus.BOARDING_ALIGHTING_NECESSARY.
            transport_modes (Union[Unset, List[TransportModeEnum]]): The modes are relevant until the next Via. Optionally
                restrict to a requestable set of SBB specific TransportMode's (aka OJP PTMode). The set is relevant for any
                vehicle-journey (`DatedVehicleJourney`, `PTRideLeg`, ..). Relates to `ServiceProduct::vehicleMode` and
                `::vehicleSubModes`.
                - Default: non-restricted (null or empty-list), by means all TransportMode's are searched.
                - If some choice is made, other TransportMode's are excluded implicitely.
                - To get TRAIN (VehicleMode::id) only, add:
                [HIGH_SPEED_TRAIN,INTERCITY,INTERREGIO,REGIO,URBAN_TRAIN,SPECIAL_TRAIN]
                >- Be aware that TRAMWAY also searches for METRO (not distinguished it here further!)
                - Also there is no exact possibility to distinguish more precisely between CABLEWAY_GONDOLA_CHAIRLIFT_FUNICULAR
                at search time<br><br>x-extensible-enum:
            waittime (Union[Unset, int]): Minimum waiting time to be spent at via StopPlace [min.]. Some additional minutes
                might be added by underlying router (aka OJP dwellTime).
            direct (Union[Unset, bool]): true: Via section has to be direct (relates to ChangeBehaviour::maxChanges); false:
                might be direct or not.
            couchette (Union[Unset, bool]): true: Via section should include couchette Car.
            sleeping_car (Union[Unset, bool]): true: Via section should include sleeping car.
    """

    stop_place_id: str
    status: Union[Unset, PTViaReferenceStatus] = PTViaReferenceStatus.BOARDING_ALIGHTING_NECESSARY
    transport_modes: Union[Unset, List[TransportModeEnum]] = UNSET
    waittime: Union[Unset, int] = UNSET
    direct: Union[Unset, bool] = False
    couchette: Union[Unset, bool] = False
    sleeping_car: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        stop_place_id = self.stop_place_id
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        transport_modes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.transport_modes, Unset):
            transport_modes = []
            for transport_modes_item_data in self.transport_modes:
                transport_modes_item = transport_modes_item_data.value

                transport_modes.append(transport_modes_item)

        waittime = self.waittime
        direct = self.direct
        couchette = self.couchette
        sleeping_car = self.sleeping_car

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stopPlaceId": stop_place_id,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status
        if transport_modes is not UNSET:
            field_dict["transportModes"] = transport_modes
        if waittime is not UNSET:
            field_dict["waittime"] = waittime
        if direct is not UNSET:
            field_dict["direct"] = direct
        if couchette is not UNSET:
            field_dict["couchette"] = couchette
        if sleeping_car is not UNSET:
            field_dict["sleepingCar"] = sleeping_car

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        stop_place_id = d.pop("stopPlaceId")

        _status = d.pop("status", UNSET)
        status: Union[Unset, PTViaReferenceStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = PTViaReferenceStatus(_status)

        transport_modes = []
        _transport_modes = d.pop("transportModes", UNSET)
        for transport_modes_item_data in _transport_modes or []:
            transport_modes_item = TransportModeEnum(transport_modes_item_data)

            transport_modes.append(transport_modes_item)

        waittime = d.pop("waittime", UNSET)

        direct = d.pop("direct", UNSET)

        couchette = d.pop("couchette", UNSET)

        sleeping_car = d.pop("sleepingCar", UNSET)

        pt_via_reference = cls(
            stop_place_id=stop_place_id,
            status=status,
            transport_modes=transport_modes,
            waittime=waittime,
            direct=direct,
            couchette=couchette,
            sleeping_car=sleeping_car,
        )

        pt_via_reference.additional_properties = d
        return pt_via_reference

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
