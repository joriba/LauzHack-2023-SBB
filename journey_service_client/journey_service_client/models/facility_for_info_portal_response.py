from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.equipment import Equipment
    from ..models.place_ref_by_name_with_distance import PlaceRefByNameWithDistance
    from ..models.postal_address import PostalAddress


T = TypeVar("T", bound="FacilityForInfoPortalResponse")


@_attrs_define
class FacilityForInfoPortalResponse:
    """A facility as for InfoPortal. Temporary solution before it goes to a PlaceService. Name is temporary!

    Attributes:
        postal_address (Union[Unset, PostalAddress]): Postal Address (source INSA).
        connection_hint (Union[Unset, str]):
        equipments (Union[Unset, List['Equipment']]):
        stop_places (Union[Unset, List['PlaceRefByNameWithDistance']]):
    """

    postal_address: Union[Unset, "PostalAddress"] = UNSET
    connection_hint: Union[Unset, str] = UNSET
    equipments: Union[Unset, List["Equipment"]] = UNSET
    stop_places: Union[Unset, List["PlaceRefByNameWithDistance"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        postal_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.postal_address, Unset):
            postal_address = self.postal_address.to_dict()

        connection_hint = self.connection_hint
        equipments: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.equipments, Unset):
            equipments = []
            for equipments_item_data in self.equipments:
                equipments_item = equipments_item_data.to_dict()

                equipments.append(equipments_item)

        stop_places: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.stop_places, Unset):
            stop_places = []
            for stop_places_item_data in self.stop_places:
                stop_places_item = stop_places_item_data.to_dict()

                stop_places.append(stop_places_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if postal_address is not UNSET:
            field_dict["postalAddress"] = postal_address
        if connection_hint is not UNSET:
            field_dict["connectionHint"] = connection_hint
        if equipments is not UNSET:
            field_dict["equipments"] = equipments
        if stop_places is not UNSET:
            field_dict["stopPlaces"] = stop_places

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.equipment import Equipment
        from ..models.place_ref_by_name_with_distance import PlaceRefByNameWithDistance
        from ..models.postal_address import PostalAddress

        d = src_dict.copy()
        _postal_address = d.pop("postalAddress", UNSET)
        postal_address: Union[Unset, PostalAddress]
        if isinstance(_postal_address, Unset):
            postal_address = UNSET
        else:
            postal_address = PostalAddress.from_dict(_postal_address)

        connection_hint = d.pop("connectionHint", UNSET)

        equipments = []
        _equipments = d.pop("equipments", UNSET)
        for equipments_item_data in _equipments or []:
            equipments_item = Equipment.from_dict(equipments_item_data)

            equipments.append(equipments_item)

        stop_places = []
        _stop_places = d.pop("stopPlaces", UNSET)
        for stop_places_item_data in _stop_places or []:
            stop_places_item = PlaceRefByNameWithDistance.from_dict(stop_places_item_data)

            stop_places.append(stop_places_item)

        facility_for_info_portal_response = cls(
            postal_address=postal_address,
            connection_hint=connection_hint,
            equipments=equipments,
            stop_places=stop_places,
        )

        facility_for_info_portal_response.additional_properties = d
        return facility_for_info_portal_response

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
