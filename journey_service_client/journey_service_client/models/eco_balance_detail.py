from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.stop_v2 import StopV2


T = TypeVar("T", bound="EcoBalanceDetail")


@_attrs_define
class EcoBalanceDetail:
    """Environmental emission coefficients occurring when generating the energy used for the vehicle during the trip.

    Attributes:
        origin (StopV2): A stop represents a specific location (typically a STATION) of a leg or a complete journey-
            detail of a transport-product (aka v3.ScheduledStopPoint, OJP StopPoint).
        destination (StopV2): A stop represents a specific location (typically a STATION) of a leg or a complete
            journey-detail of a transport-product (aka v3.ScheduledStopPoint, OJP StopPoint).
        co2 (float): CO2 emission [kg].
        co_2_in_operation (float): CO2 emission in operation [kg].
        co_2_electric_vehicle (float): CO2 emission in for electric vehicles [g].
        prime (float): PRIME emission calculated [l petrol].
        prime_in_operation (float): PRIME emission calculated [l petrol].
        particulate_matter_emission_10 (float): Particulate matter emission (PM10) in [g].
            This value includes possible particulate matter emissions occurring when generating the energy used for the
            vehicle during the trip. For example, electric cars will still have a non-zero particulate matter emission
            although the vehicle doesn't emit anything but the electric energy used by the vehicle might be generated from
            coal power plants and those created emissions during energy generation.
        particulate_matter_emission_2_5 (float): Particulate matter emission (PM2.5) in [g].
            This value includes possible particulate matter emissions occurring when generating the energy used for the
            vehicle during the trip. For example, electric cars will still have a non-zero particulate matter emission
            although the vehicle doesn't emit anything but the electric energy used by the vehicle might be generated from
            coal power plants and those created emissions during energy generation.
        nmvoc (float): NMVOC emission [g]
        nox (float): NOX emission [g]
        ubp06 (float): Environmental impact points 06
        duration (Union[Unset, str]): Overall travelling [duration](https://www.w3.org/TR/xmlschema11-2/#duration).
            Example: P1DT2H4M.
        potential_working_duration (Union[Unset, str]): Potential available travelling
            [duration](https://www.w3.org/TR/xmlschema11-2/#duration) where passenger may sit back and relax. Example:
            P1DT2H4M.
    """

    origin: "StopV2"
    destination: "StopV2"
    co2: float
    co_2_in_operation: float
    co_2_electric_vehicle: float
    prime: float
    prime_in_operation: float
    particulate_matter_emission_10: float
    particulate_matter_emission_2_5: float
    nmvoc: float
    nox: float
    ubp06: float
    duration: Union[Unset, str] = UNSET
    potential_working_duration: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        origin = self.origin.to_dict()

        destination = self.destination.to_dict()

        co2 = self.co2
        co_2_in_operation = self.co_2_in_operation
        co_2_electric_vehicle = self.co_2_electric_vehicle
        prime = self.prime
        prime_in_operation = self.prime_in_operation
        particulate_matter_emission_10 = self.particulate_matter_emission_10
        particulate_matter_emission_2_5 = self.particulate_matter_emission_2_5
        nmvoc = self.nmvoc
        nox = self.nox
        ubp06 = self.ubp06
        duration = self.duration
        potential_working_duration = self.potential_working_duration

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "origin": origin,
                "destination": destination,
                "co2": co2,
                "co2InOperation": co_2_in_operation,
                "co2ElectricVehicle": co_2_electric_vehicle,
                "prime": prime,
                "primeInOperation": prime_in_operation,
                "particulateMatterEmission10": particulate_matter_emission_10,
                "particulateMatterEmission2_5": particulate_matter_emission_2_5,
                "nmvoc": nmvoc,
                "nox": nox,
                "ubp06": ubp06,
            }
        )
        if duration is not UNSET:
            field_dict["duration"] = duration
        if potential_working_duration is not UNSET:
            field_dict["potentialWorkingDuration"] = potential_working_duration

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.stop_v2 import StopV2

        d = src_dict.copy()
        origin = StopV2.from_dict(d.pop("origin"))

        destination = StopV2.from_dict(d.pop("destination"))

        co2 = d.pop("co2")

        co_2_in_operation = d.pop("co2InOperation")

        co_2_electric_vehicle = d.pop("co2ElectricVehicle")

        prime = d.pop("prime")

        prime_in_operation = d.pop("primeInOperation")

        particulate_matter_emission_10 = d.pop("particulateMatterEmission10")

        particulate_matter_emission_2_5 = d.pop("particulateMatterEmission2_5")

        nmvoc = d.pop("nmvoc")

        nox = d.pop("nox")

        ubp06 = d.pop("ubp06")

        duration = d.pop("duration", UNSET)

        potential_working_duration = d.pop("potentialWorkingDuration", UNSET)

        eco_balance_detail = cls(
            origin=origin,
            destination=destination,
            co2=co2,
            co_2_in_operation=co_2_in_operation,
            co_2_electric_vehicle=co_2_electric_vehicle,
            prime=prime,
            prime_in_operation=prime_in_operation,
            particulate_matter_emission_10=particulate_matter_emission_10,
            particulate_matter_emission_2_5=particulate_matter_emission_2_5,
            nmvoc=nmvoc,
            nox=nox,
            ubp06=ubp06,
            duration=duration,
            potential_working_duration=potential_working_duration,
        )

        eco_balance_detail.additional_properties = d
        return eco_balance_detail

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
