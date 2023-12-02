from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.audience_enum import AudienceEnum
from ..models.equipment_type_enum import EquipmentTypeEnum
from ..models.group_reservation_status_enum import GroupReservationStatusEnum
from ..models.stop_place_classification import StopPlaceClassification
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access_leg import AccessLeg
    from ..models.leg import Leg
    from ..models.place import Place
    from ..models.point_of_interest import PointOfInterest
    from ..models.pt_connection_leg import PTConnectionLeg
    from ..models.pt_ride_leg import PTRideLeg


T = TypeVar("T", bound="InheritanceResponse")


@_attrs_define
class InheritanceResponse:
    """OpenApi patch to enforce generation of all dummy-property classes.

    Attributes:
        dummy_address (Union[Unset, Place]): **Abstract Superclass** of concrete inherited sub-classes such as
            **`StopPlace`, `Address`, `PointOfInterest`**.
        dummy_point_of_interest (Union[Unset, PointOfInterest]): Point of Interest (POI), such as a Museum (source:
            [ROKAS POI-Service `Poi`](https://developer.sbb.ch/apis/journey-pois/information).<br>Inherited from `Place`.
        dummy_pt_ride_leg (Union[Unset, PTRideLeg]): Public-Transportation Leg (aka OJP TimedLeg).<br>Inherited from
            `Leg`.
        dummy_access_leg (Union[Unset, AccessLeg]): Footpath or road access to/from a StopPlace at one end:
            - and typically an Address/PointOfInterest on the other end. May occur at the beginning or end of a Trip (aka
            OJP ContinuousLeg)- or in rare cases StopPlace as well (for Meta-Station footpath like main-station to any of
            its bus edges).<br>Inherited from `Leg`.
        dummy_pt_connection_leg (Union[Unset, PTConnectionLeg]): Passenger transfer between 2 StopPlace's (typically
            when the underlying router does not know how to perform the interchange in detail, aka OJP
            TransferLeg).<br>Inherited from `Leg`.
        dummy_alternative_mode_leg (Union[Unset, Leg]): **Abstract Superclass** of concrete inherited sub-classes such
            as **`PTRideLeg`, `AccessLeg`, `PTConnectionLeg`, `AlternateModeLeg`** (aka OJP TripLeg)**, `PersonalLeg`**.
        dummy_personal_leg (Union[Unset, Leg]): **Abstract Superclass** of concrete inherited sub-classes such as
            **`PTRideLeg`, `AccessLeg`, `PTConnectionLeg`, `AlternateModeLeg`** (aka OJP TripLeg)**, `PersonalLeg`**.
        dummy_audience_enum (Union[Unset, AudienceEnum]): Enum whose values can be extended, thus default case should be
            foreseen wenn parsing the response (in Java, avoid `valueOf`, prefer `switch` with the value's name and define a
            default). You may become unexpected values if your client is out-of-sync.  Default: AudienceEnum.B2C_TEXT.
        dummy_group_reservation_status_enum (Union[Unset, GroupReservationStatusEnum]): Enum whose values can be
            extended, thus default case should be foreseen wenn parsing the response (in Java, avoid `valueOf`, prefer
            `switch` with the value's name and define a default). You may become unexpected values if your client is out-of-
            sync.
        dummy_stop_place_classification (Union[Unset, StopPlaceClassification]): Enum whose values can be extended, thus
            default case should be foreseen wenn parsing the response (in Java, avoid `valueOf`, prefer `switch` with the
            value's name and define a default). You may become unexpected values if your client is out-of-sync. Meaning of
            each value is explained in `StopPlaceDetailed::classification`
        dummy_equipment_type_enum (Union[Unset, EquipmentTypeEnum]): Values described in `EquipmentType::id`. Enum whose
            values can be extended, thus default case should be foreseen wenn parsing the response (in Java, avoid
            `valueOf`, prefer `switch` with the value's name and define a default). You may become unexpected values if your
            client is out-of-sync.
    """

    dummy_address: Union[Unset, "Place"] = UNSET
    dummy_point_of_interest: Union[Unset, "PointOfInterest"] = UNSET
    dummy_pt_ride_leg: Union[Unset, "PTRideLeg"] = UNSET
    dummy_access_leg: Union[Unset, "AccessLeg"] = UNSET
    dummy_pt_connection_leg: Union[Unset, "PTConnectionLeg"] = UNSET
    dummy_alternative_mode_leg: Union[Unset, "Leg"] = UNSET
    dummy_personal_leg: Union[Unset, "Leg"] = UNSET
    dummy_audience_enum: Union[Unset, AudienceEnum] = AudienceEnum.B2C_TEXT
    dummy_group_reservation_status_enum: Union[Unset, GroupReservationStatusEnum] = UNSET
    dummy_stop_place_classification: Union[Unset, StopPlaceClassification] = UNSET
    dummy_equipment_type_enum: Union[Unset, EquipmentTypeEnum] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dummy_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dummy_address, Unset):
            dummy_address = self.dummy_address.to_dict()

        dummy_point_of_interest: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dummy_point_of_interest, Unset):
            dummy_point_of_interest = self.dummy_point_of_interest.to_dict()

        dummy_pt_ride_leg: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dummy_pt_ride_leg, Unset):
            dummy_pt_ride_leg = self.dummy_pt_ride_leg.to_dict()

        dummy_access_leg: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dummy_access_leg, Unset):
            dummy_access_leg = self.dummy_access_leg.to_dict()

        dummy_pt_connection_leg: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dummy_pt_connection_leg, Unset):
            dummy_pt_connection_leg = self.dummy_pt_connection_leg.to_dict()

        dummy_alternative_mode_leg: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dummy_alternative_mode_leg, Unset):
            dummy_alternative_mode_leg = self.dummy_alternative_mode_leg.to_dict()

        dummy_personal_leg: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dummy_personal_leg, Unset):
            dummy_personal_leg = self.dummy_personal_leg.to_dict()

        dummy_audience_enum: Union[Unset, str] = UNSET
        if not isinstance(self.dummy_audience_enum, Unset):
            dummy_audience_enum = self.dummy_audience_enum.value

        dummy_group_reservation_status_enum: Union[Unset, str] = UNSET
        if not isinstance(self.dummy_group_reservation_status_enum, Unset):
            dummy_group_reservation_status_enum = self.dummy_group_reservation_status_enum.value

        dummy_stop_place_classification: Union[Unset, str] = UNSET
        if not isinstance(self.dummy_stop_place_classification, Unset):
            dummy_stop_place_classification = self.dummy_stop_place_classification.value

        dummy_equipment_type_enum: Union[Unset, str] = UNSET
        if not isinstance(self.dummy_equipment_type_enum, Unset):
            dummy_equipment_type_enum = self.dummy_equipment_type_enum.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dummy_address is not UNSET:
            field_dict["dummyAddress"] = dummy_address
        if dummy_point_of_interest is not UNSET:
            field_dict["dummyPointOfInterest"] = dummy_point_of_interest
        if dummy_pt_ride_leg is not UNSET:
            field_dict["dummyPTRideLeg"] = dummy_pt_ride_leg
        if dummy_access_leg is not UNSET:
            field_dict["dummyAccessLeg"] = dummy_access_leg
        if dummy_pt_connection_leg is not UNSET:
            field_dict["dummyPTConnectionLeg"] = dummy_pt_connection_leg
        if dummy_alternative_mode_leg is not UNSET:
            field_dict["dummyAlternativeModeLeg"] = dummy_alternative_mode_leg
        if dummy_personal_leg is not UNSET:
            field_dict["dummyPersonalLeg"] = dummy_personal_leg
        if dummy_audience_enum is not UNSET:
            field_dict["dummyAudienceEnum"] = dummy_audience_enum
        if dummy_group_reservation_status_enum is not UNSET:
            field_dict["dummyGroupReservationStatusEnum"] = dummy_group_reservation_status_enum
        if dummy_stop_place_classification is not UNSET:
            field_dict["dummyStopPlaceClassification"] = dummy_stop_place_classification
        if dummy_equipment_type_enum is not UNSET:
            field_dict["dummyEquipmentTypeEnum"] = dummy_equipment_type_enum

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.access_leg import AccessLeg
        from ..models.leg import Leg
        from ..models.place import Place
        from ..models.point_of_interest import PointOfInterest
        from ..models.pt_connection_leg import PTConnectionLeg
        from ..models.pt_ride_leg import PTRideLeg

        d = src_dict.copy()
        _dummy_address = d.pop("dummyAddress", UNSET)
        dummy_address: Union[Unset, Place]
        if isinstance(_dummy_address, Unset):
            dummy_address = UNSET
        else:
            dummy_address = Place.from_dict(_dummy_address)

        _dummy_point_of_interest = d.pop("dummyPointOfInterest", UNSET)
        dummy_point_of_interest: Union[Unset, PointOfInterest]
        if isinstance(_dummy_point_of_interest, Unset):
            dummy_point_of_interest = UNSET
        else:
            dummy_point_of_interest = PointOfInterest.from_dict(_dummy_point_of_interest)

        _dummy_pt_ride_leg = d.pop("dummyPTRideLeg", UNSET)
        dummy_pt_ride_leg: Union[Unset, PTRideLeg]
        if isinstance(_dummy_pt_ride_leg, Unset):
            dummy_pt_ride_leg = UNSET
        else:
            dummy_pt_ride_leg = PTRideLeg.from_dict(_dummy_pt_ride_leg)

        _dummy_access_leg = d.pop("dummyAccessLeg", UNSET)
        dummy_access_leg: Union[Unset, AccessLeg]
        if isinstance(_dummy_access_leg, Unset):
            dummy_access_leg = UNSET
        else:
            dummy_access_leg = AccessLeg.from_dict(_dummy_access_leg)

        _dummy_pt_connection_leg = d.pop("dummyPTConnectionLeg", UNSET)
        dummy_pt_connection_leg: Union[Unset, PTConnectionLeg]
        if isinstance(_dummy_pt_connection_leg, Unset):
            dummy_pt_connection_leg = UNSET
        else:
            dummy_pt_connection_leg = PTConnectionLeg.from_dict(_dummy_pt_connection_leg)

        _dummy_alternative_mode_leg = d.pop("dummyAlternativeModeLeg", UNSET)
        dummy_alternative_mode_leg: Union[Unset, Leg]
        if isinstance(_dummy_alternative_mode_leg, Unset):
            dummy_alternative_mode_leg = UNSET
        else:
            dummy_alternative_mode_leg = Leg.from_dict(_dummy_alternative_mode_leg)

        _dummy_personal_leg = d.pop("dummyPersonalLeg", UNSET)
        dummy_personal_leg: Union[Unset, Leg]
        if isinstance(_dummy_personal_leg, Unset):
            dummy_personal_leg = UNSET
        else:
            dummy_personal_leg = Leg.from_dict(_dummy_personal_leg)

        _dummy_audience_enum = d.pop("dummyAudienceEnum", UNSET)
        dummy_audience_enum: Union[Unset, AudienceEnum]
        if isinstance(_dummy_audience_enum, Unset):
            dummy_audience_enum = UNSET
        else:
            dummy_audience_enum = AudienceEnum(_dummy_audience_enum)

        _dummy_group_reservation_status_enum = d.pop("dummyGroupReservationStatusEnum", UNSET)
        dummy_group_reservation_status_enum: Union[Unset, GroupReservationStatusEnum]
        if isinstance(_dummy_group_reservation_status_enum, Unset):
            dummy_group_reservation_status_enum = UNSET
        else:
            dummy_group_reservation_status_enum = GroupReservationStatusEnum(_dummy_group_reservation_status_enum)

        _dummy_stop_place_classification = d.pop("dummyStopPlaceClassification", UNSET)
        dummy_stop_place_classification: Union[Unset, StopPlaceClassification]
        if isinstance(_dummy_stop_place_classification, Unset):
            dummy_stop_place_classification = UNSET
        else:
            dummy_stop_place_classification = StopPlaceClassification(_dummy_stop_place_classification)

        _dummy_equipment_type_enum = d.pop("dummyEquipmentTypeEnum", UNSET)
        dummy_equipment_type_enum: Union[Unset, EquipmentTypeEnum]
        if isinstance(_dummy_equipment_type_enum, Unset):
            dummy_equipment_type_enum = UNSET
        else:
            dummy_equipment_type_enum = EquipmentTypeEnum(_dummy_equipment_type_enum)

        inheritance_response = cls(
            dummy_address=dummy_address,
            dummy_point_of_interest=dummy_point_of_interest,
            dummy_pt_ride_leg=dummy_pt_ride_leg,
            dummy_access_leg=dummy_access_leg,
            dummy_pt_connection_leg=dummy_pt_connection_leg,
            dummy_alternative_mode_leg=dummy_alternative_mode_leg,
            dummy_personal_leg=dummy_personal_leg,
            dummy_audience_enum=dummy_audience_enum,
            dummy_group_reservation_status_enum=dummy_group_reservation_status_enum,
            dummy_stop_place_classification=dummy_stop_place_classification,
            dummy_equipment_type_enum=dummy_equipment_type_enum,
        )

        inheritance_response.additional_properties = d
        return inheritance_response

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
