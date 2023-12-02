import datetime
from typing import Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="ForecastElement")


@_attrs_define
class ForecastElement:
    """Weather Forecast.

    Attributes:
        cloudiness (float): Cloudiness in percent.
        one_hour_rain_volume (float): Precipitation of rain within one hour in millimeters.
        one_hour_snow_volume (float): Precipitation of swon within one hour in millimeters.
        wind_speed (float): Wind speed in meters per second.
        temperature (float): Temperature in degrees celsius.
        humidity (float): Humidity in percent.
        descriptions (List[str]):
        wmo_weather_code (int): Weather code according to WMO standard 4677.
        date_time (datetime.datetime): Forecast time.
    """

    cloudiness: float
    one_hour_rain_volume: float
    one_hour_snow_volume: float
    wind_speed: float
    temperature: float
    humidity: float
    descriptions: List[str]
    wmo_weather_code: int
    date_time: datetime.datetime
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cloudiness = self.cloudiness
        one_hour_rain_volume = self.one_hour_rain_volume
        one_hour_snow_volume = self.one_hour_snow_volume
        wind_speed = self.wind_speed
        temperature = self.temperature
        humidity = self.humidity
        descriptions = self.descriptions

        wmo_weather_code = self.wmo_weather_code
        date_time = self.date_time.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cloudiness": cloudiness,
                "oneHourRainVolume": one_hour_rain_volume,
                "oneHourSnowVolume": one_hour_snow_volume,
                "windSpeed": wind_speed,
                "temperature": temperature,
                "humidity": humidity,
                "descriptions": descriptions,
                "wmoWeatherCode": wmo_weather_code,
                "dateTime": date_time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cloudiness = d.pop("cloudiness")

        one_hour_rain_volume = d.pop("oneHourRainVolume")

        one_hour_snow_volume = d.pop("oneHourSnowVolume")

        wind_speed = d.pop("windSpeed")

        temperature = d.pop("temperature")

        humidity = d.pop("humidity")

        descriptions = cast(List[str], d.pop("descriptions"))

        wmo_weather_code = d.pop("wmoWeatherCode")

        date_time = isoparse(d.pop("dateTime"))

        forecast_element = cls(
            cloudiness=cloudiness,
            one_hour_rain_volume=one_hour_rain_volume,
            one_hour_snow_volume=one_hour_snow_volume,
            wind_speed=wind_speed,
            temperature=temperature,
            humidity=humidity,
            descriptions=descriptions,
            wmo_weather_code=wmo_weather_code,
            date_time=date_time,
        )

        forecast_element.additional_properties = d
        return forecast_element

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
