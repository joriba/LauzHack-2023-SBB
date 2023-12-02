from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="VehicleMode")


@_attrs_define
class VehicleMode:
    """A characterisation of the public transport operation according to the means of transport (aka OJP PtMode;
    Siri::VehicleMode; v580 TransportMode or de:Verkehrsmittelkategorie). Whether only `id` is given or submode as well
    depends on available data.

        Attributes:
            id (str): Mode of public transportation according to **v580 TransportMode** (see
                [de:Verkehrsmittelkategorie](https://www.allianceswisspass.ch/de/tarife-vorschriften/uebersicht/V580/Produkte-
                der-V580-FIScommun-1)) given  by [opentransportdata.swiss Transportmodes
                (de:Verkehrsmittel)](https://opentransportdata.swiss/de/dataset/vm-liste) column `EN` as
                uppercase.<br>x-extensible-enum: values see `VehicleModeEnum`. Example: TRAIN.
            name (str): Translation of related `id` (according to Accept-Language and [opentransportdata.swiss
                Transportmodes (de:Verkehrsmittel)](https://opentransportdata.swiss/de/dataset/vm-liste) language
                column).<br>(Translated according to Accept-Language.) Example: Zug.
            corporate_identity_icon (str): Icon-identifier to represent the related `id` (main mode). See [SBB Corporate-
                Identity catalog (CDN, aka FIGMA Icons)](https://www.figma.com/file/UQBd7cHKav0hr9oXYp7opJ/SBB-Icons?node-
                id=395%3A2952&t=ad26LgREBbTANSK5-1) Example: SBB_oev_b_t02.
            vehicle_sub_mode_name (Union[Unset, str]): Long, displayable submode (aka de:Gattung) related to (main) mode
                `id`. See [v580 de:Verkehrsmittelkategorien (aka Transmodel or OJP/Siri
                `VehicleMode`)](https://github.com/SchweizerischeBundesbahnen/journey-service/blob/master/TransportMode.md)
                Example: InterCity.
            vehicle_sub_mode_short_name (Union[Unset, str]): Short version of related `vehicleSubModeName`. Example: IC.
    """

    id: str
    name: str
    corporate_identity_icon: str
    vehicle_sub_mode_name: Union[Unset, str] = UNSET
    vehicle_sub_mode_short_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        corporate_identity_icon = self.corporate_identity_icon
        vehicle_sub_mode_name = self.vehicle_sub_mode_name
        vehicle_sub_mode_short_name = self.vehicle_sub_mode_short_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "corporateIdentityIcon": corporate_identity_icon,
            }
        )
        if vehicle_sub_mode_name is not UNSET:
            field_dict["vehicleSubModeName"] = vehicle_sub_mode_name
        if vehicle_sub_mode_short_name is not UNSET:
            field_dict["vehicleSubModeShortName"] = vehicle_sub_mode_short_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        corporate_identity_icon = d.pop("corporateIdentityIcon")

        vehicle_sub_mode_name = d.pop("vehicleSubModeName", UNSET)

        vehicle_sub_mode_short_name = d.pop("vehicleSubModeShortName", UNSET)

        vehicle_mode = cls(
            id=id,
            name=name,
            corporate_identity_icon=corporate_identity_icon,
            vehicle_sub_mode_name=vehicle_sub_mode_name,
            vehicle_sub_mode_short_name=vehicle_sub_mode_short_name,
        )

        vehicle_mode.additional_properties = d
        return vehicle_mode

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
