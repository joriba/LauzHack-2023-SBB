import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.forecast_element import ForecastElement
    from ..models.weather_coordinates import WeatherCoordinates


T = TypeVar("T", bound="TimedWeatherForecast")


@_attrs_define
class TimedWeatherForecast:
    """Weather forecast for a given location and time.

    Attributes:
        update_date_time (datetime.datetime): Update time of weather forecast.
        weather_coordinates (WeatherCoordinates): Coordinates for weather forecast.
        forecast (ForecastElement): Weather Forecast.
    """

    update_date_time: datetime.datetime
    weather_coordinates: "WeatherCoordinates"
    forecast: "ForecastElement"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        update_date_time = self.update_date_time.isoformat()

        weather_coordinates = self.weather_coordinates.to_dict()

        forecast = self.forecast.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "updateDateTime": update_date_time,
                "weatherCoordinates": weather_coordinates,
                "forecast": forecast,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.forecast_element import ForecastElement
        from ..models.weather_coordinates import WeatherCoordinates

        d = src_dict.copy()
        update_date_time = isoparse(d.pop("updateDateTime"))

        weather_coordinates = WeatherCoordinates.from_dict(d.pop("weatherCoordinates"))

        forecast = ForecastElement.from_dict(d.pop("forecast"))

        timed_weather_forecast = cls(
            update_date_time=update_date_time,
            weather_coordinates=weather_coordinates,
            forecast=forecast,
        )

        timed_weather_forecast.additional_properties = d
        return timed_weather_forecast

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
