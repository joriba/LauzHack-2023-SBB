from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EcoBalance")


@_attrs_define
class EcoBalance:
    """Environmental coefficients to compare train and car transport.

    Attributes:
        co_2_train (float): CO2 emission by train [kg].
        co_2_car (float): CO2 emission by car [kg].
        prime_train (float): PRIME emission by train, calculated [l petrol].
        prime_car (float): PRIME emission by car, calculated [l petrol].
        duration_train (Union[Unset, str]): Travelling [duration](https://www.w3.org/TR/xmlschema11-2/#duration) by
            train. Example: P1DT2H4M.
        duration_car (Union[Unset, str]): Travelling [duration](https://www.w3.org/TR/xmlschema11-2/#duration) by car.
            Example: P1DT2H4M.
    """

    co_2_train: float
    co_2_car: float
    prime_train: float
    prime_car: float
    duration_train: Union[Unset, str] = UNSET
    duration_car: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        co_2_train = self.co_2_train
        co_2_car = self.co_2_car
        prime_train = self.prime_train
        prime_car = self.prime_car
        duration_train = self.duration_train
        duration_car = self.duration_car

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "co2Train": co_2_train,
                "co2Car": co_2_car,
                "primeTrain": prime_train,
                "primeCar": prime_car,
            }
        )
        if duration_train is not UNSET:
            field_dict["durationTrain"] = duration_train
        if duration_car is not UNSET:
            field_dict["durationCar"] = duration_car

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        co_2_train = d.pop("co2Train")

        co_2_car = d.pop("co2Car")

        prime_train = d.pop("primeTrain")

        prime_car = d.pop("primeCar")

        duration_train = d.pop("durationTrain", UNSET)

        duration_car = d.pop("durationCar", UNSET)

        eco_balance = cls(
            co_2_train=co_2_train,
            co_2_car=co_2_car,
            prime_train=prime_train,
            prime_car=prime_car,
            duration_train=duration_train,
            duration_car=duration_car,
        )

        eco_balance.additional_properties = d
        return eco_balance

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
