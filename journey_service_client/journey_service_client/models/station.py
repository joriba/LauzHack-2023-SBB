from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.station_station_type import StationStationType
from ..models.station_type import StationType
from ..models.station_vehicle_types_item import StationVehicleTypesItem
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.coordinates_wgs84 import CoordinatesWGS84
    from ..models.location_identity import LocationIdentity
    from ..models.network_zone import NetworkZone
    from ..models.perron import Perron


T = TypeVar("T", bound="Station")


@_attrs_define
class Station:
    """Station represents a LocationType::STATION (de:Haltestelle).

    Attributes:
        uic (str): Unique UIC code of station (source DiDok). Example: 8503000.
        country_code (str): Country of location (ISO 3166, 2-digits, source: DiDok organisational-based). Example: CH.
        name (str): Name of station (given in translation of local area). Example: Zürich HB.
        station_type (StationStationType): The type of the location.
            STATION represents a simple station (typically one physical location with one operator)
            STATION_COMPLEX represents a more complex station (typically with multiple operators and/or aggregated
            buildings)
            STATION_ZONED represents a set of STATION and/or STATION_COMPLEX (typically several stations in an agglomeration
            perimeter). Example: STATION_COMPLEX.
        vehicle_types (List[StationVehicleTypesItem]):
        complex_members (List['LocationIdentity']):
        zoned_members (List['LocationIdentity']):
        tracks (List[str]):
        perron_to_tracks (List['Perron']):
        type (Union[Unset, StationType]): @Deprecated use stationType.
        coordinates_wgs84 (Union[Unset, CoordinatesWGS84]): World Geodetic System 1984 (WGS 84) coordinates (latitude:
            specifies the north–south position of a point on the earth's surface; longitude: specifies the east-west
            position of a point on the earth's surface). For e.g. Bern CH (lat=46.947974,lon=7.447447).
        latitude (Union[Unset, str]): @Deprecated use `coordinatesWGS84`.
        longitude (Union[Unset, str]): @Deprecated use `coordinatesWGS84`.
        weight (Union[Unset, int]): Weight (traffic load/importance the higher the value) at station, null if unknown.
            E.g. Zürich HB has weight 30170. Example: 30170.
        complex_leader (Union[Unset, LocationIdentity]): In a group of zoned stations (relates to stationType
            STATION_ZONED) the zonedMember represents the other siblings (empty for other stationType).
        network_zones (Union[Unset, List['NetworkZone']]):
        tariff_border_point (Union[Unset, bool]): true: Stop::uic represents a NOVA TariffBorderPoint; false: no NOVA
            TariffBorderPoint; null unknown/irrelevant
    """

    uic: str
    country_code: str
    name: str
    station_type: StationStationType
    vehicle_types: List[StationVehicleTypesItem]
    complex_members: List["LocationIdentity"]
    zoned_members: List["LocationIdentity"]
    tracks: List[str]
    perron_to_tracks: List["Perron"]
    type: Union[Unset, StationType] = UNSET
    coordinates_wgs84: Union[Unset, "CoordinatesWGS84"] = UNSET
    latitude: Union[Unset, str] = UNSET
    longitude: Union[Unset, str] = UNSET
    weight: Union[Unset, int] = UNSET
    complex_leader: Union[Unset, "LocationIdentity"] = UNSET
    network_zones: Union[Unset, List["NetworkZone"]] = UNSET
    tariff_border_point: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        uic = self.uic
        country_code = self.country_code
        name = self.name
        station_type = self.station_type.value

        vehicle_types = []
        for vehicle_types_item_data in self.vehicle_types:
            vehicle_types_item = vehicle_types_item_data.value

            vehicle_types.append(vehicle_types_item)

        complex_members = []
        for complex_members_item_data in self.complex_members:
            complex_members_item = complex_members_item_data.to_dict()

            complex_members.append(complex_members_item)

        zoned_members = []
        for zoned_members_item_data in self.zoned_members:
            zoned_members_item = zoned_members_item_data.to_dict()

            zoned_members.append(zoned_members_item)

        tracks = self.tracks

        perron_to_tracks = []
        for perron_to_tracks_item_data in self.perron_to_tracks:
            perron_to_tracks_item = perron_to_tracks_item_data.to_dict()

            perron_to_tracks.append(perron_to_tracks_item)

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        coordinates_wgs84: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.coordinates_wgs84, Unset):
            coordinates_wgs84 = self.coordinates_wgs84.to_dict()

        latitude = self.latitude
        longitude = self.longitude
        weight = self.weight
        complex_leader: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.complex_leader, Unset):
            complex_leader = self.complex_leader.to_dict()

        network_zones: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.network_zones, Unset):
            network_zones = []
            for network_zones_item_data in self.network_zones:
                network_zones_item = network_zones_item_data.to_dict()

                network_zones.append(network_zones_item)

        tariff_border_point = self.tariff_border_point

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uic": uic,
                "countryCode": country_code,
                "name": name,
                "stationType": station_type,
                "vehicleTypes": vehicle_types,
                "complexMembers": complex_members,
                "zonedMembers": zoned_members,
                "tracks": tracks,
                "perronToTracks": perron_to_tracks,
            }
        )
        if type is not UNSET:
            field_dict["type"] = type
        if coordinates_wgs84 is not UNSET:
            field_dict["coordinatesWGS84"] = coordinates_wgs84
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if weight is not UNSET:
            field_dict["weight"] = weight
        if complex_leader is not UNSET:
            field_dict["complexLeader"] = complex_leader
        if network_zones is not UNSET:
            field_dict["networkZones"] = network_zones
        if tariff_border_point is not UNSET:
            field_dict["tariffBorderPoint"] = tariff_border_point

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.coordinates_wgs84 import CoordinatesWGS84
        from ..models.location_identity import LocationIdentity
        from ..models.network_zone import NetworkZone
        from ..models.perron import Perron

        d = src_dict.copy()
        uic = d.pop("uic")

        country_code = d.pop("countryCode")

        name = d.pop("name")

        station_type = StationStationType(d.pop("stationType"))

        vehicle_types = []
        _vehicle_types = d.pop("vehicleTypes")
        for vehicle_types_item_data in _vehicle_types:
            vehicle_types_item = StationVehicleTypesItem(vehicle_types_item_data)

            vehicle_types.append(vehicle_types_item)

        complex_members = []
        _complex_members = d.pop("complexMembers")
        for complex_members_item_data in _complex_members:
            complex_members_item = LocationIdentity.from_dict(complex_members_item_data)

            complex_members.append(complex_members_item)

        zoned_members = []
        _zoned_members = d.pop("zonedMembers")
        for zoned_members_item_data in _zoned_members:
            zoned_members_item = LocationIdentity.from_dict(zoned_members_item_data)

            zoned_members.append(zoned_members_item)

        tracks = cast(List[str], d.pop("tracks"))

        perron_to_tracks = []
        _perron_to_tracks = d.pop("perronToTracks")
        for perron_to_tracks_item_data in _perron_to_tracks:
            perron_to_tracks_item = Perron.from_dict(perron_to_tracks_item_data)

            perron_to_tracks.append(perron_to_tracks_item)

        _type = d.pop("type", UNSET)
        type: Union[Unset, StationType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = StationType(_type)

        _coordinates_wgs84 = d.pop("coordinatesWGS84", UNSET)
        coordinates_wgs84: Union[Unset, CoordinatesWGS84]
        if isinstance(_coordinates_wgs84, Unset):
            coordinates_wgs84 = UNSET
        else:
            coordinates_wgs84 = CoordinatesWGS84.from_dict(_coordinates_wgs84)

        latitude = d.pop("latitude", UNSET)

        longitude = d.pop("longitude", UNSET)

        weight = d.pop("weight", UNSET)

        _complex_leader = d.pop("complexLeader", UNSET)
        complex_leader: Union[Unset, LocationIdentity]
        if isinstance(_complex_leader, Unset):
            complex_leader = UNSET
        else:
            complex_leader = LocationIdentity.from_dict(_complex_leader)

        network_zones = []
        _network_zones = d.pop("networkZones", UNSET)
        for network_zones_item_data in _network_zones or []:
            network_zones_item = NetworkZone.from_dict(network_zones_item_data)

            network_zones.append(network_zones_item)

        tariff_border_point = d.pop("tariffBorderPoint", UNSET)

        station = cls(
            uic=uic,
            country_code=country_code,
            name=name,
            station_type=station_type,
            vehicle_types=vehicle_types,
            complex_members=complex_members,
            zoned_members=zoned_members,
            tracks=tracks,
            perron_to_tracks=perron_to_tracks,
            type=type,
            coordinates_wgs84=coordinates_wgs84,
            latitude=latitude,
            longitude=longitude,
            weight=weight,
            complex_leader=complex_leader,
            network_zones=network_zones,
            tariff_border_point=tariff_border_point,
        )

        station.additional_properties = d
        return station

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
