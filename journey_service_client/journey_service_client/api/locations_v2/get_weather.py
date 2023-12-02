import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_weather_accept_language import GetWeatherAcceptLanguage
from ...models.get_weather_location_type import GetWeatherLocationType
from ...models.problem import Problem
from ...models.timed_weather_forecast import TimedWeatherForecast
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    location_value: str,
    date_time: Union[Unset, None, datetime.datetime] = UNSET,
    location_type: Union[Unset, None, GetWeatherLocationType] = GetWeatherLocationType.COORDINATES,
    accept_language: Union[Unset, GetWeatherAcceptLanguage] = GetWeatherAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = str(accept_language)

    if not isinstance(request_id, Unset):
        headers["Request-ID"] = request_id

    params: Dict[str, Any] = {}
    params["locationValue"] = location_value

    json_date_time: Union[Unset, None, str] = UNSET
    if not isinstance(date_time, Unset):
        json_date_time = date_time.isoformat() if date_time else None

    params["dateTime"] = json_date_time

    json_location_type: Union[Unset, None, str] = UNSET
    if not isinstance(location_type, Unset):
        json_location_type = location_type.value if location_type else None

    params["locationType"] = json_location_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/b2c/v2/INCUBATOR/weather",
        "params": params,
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Problem, TimedWeatherForecast]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = TimedWeatherForecast.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.NOT_MODIFIED:
        response_304 = Problem.from_dict(response.json())

        return response_304
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = Problem.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = Problem.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = Problem.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = Problem.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = Problem.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Problem, TimedWeatherForecast]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    location_value: str,
    date_time: Union[Unset, None, datetime.datetime] = UNSET,
    location_type: Union[Unset, None, GetWeatherLocationType] = GetWeatherLocationType.COORDINATES,
    accept_language: Union[Unset, GetWeatherAcceptLanguage] = GetWeatherAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Response[Union[Problem, TimedWeatherForecast]]:
    """@Deprecated Will be part of /v3/trips! Get weather forecast at a Location.

     Source of data: [meteomatics](https://www.meteomatics.com/en/api/overview)

    Args:
        location_value (str):  Example: 46.948658,7.437406.
        date_time (Union[Unset, None, datetime.datetime]):  Example: 2023-04-18T14:55:00+01:00.
        location_type (Union[Unset, None, GetWeatherLocationType]):  Default:
            GetWeatherLocationType.COORDINATES.
        accept_language (Union[Unset, GetWeatherAcceptLanguage]):  Default:
            GetWeatherAcceptLanguage.EN.
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Problem, TimedWeatherForecast]]
    """

    kwargs = _get_kwargs(
        location_value=location_value,
        date_time=date_time,
        location_type=location_type,
        accept_language=accept_language,
        request_id=request_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    location_value: str,
    date_time: Union[Unset, None, datetime.datetime] = UNSET,
    location_type: Union[Unset, None, GetWeatherLocationType] = GetWeatherLocationType.COORDINATES,
    accept_language: Union[Unset, GetWeatherAcceptLanguage] = GetWeatherAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Optional[Union[Problem, TimedWeatherForecast]]:
    """@Deprecated Will be part of /v3/trips! Get weather forecast at a Location.

     Source of data: [meteomatics](https://www.meteomatics.com/en/api/overview)

    Args:
        location_value (str):  Example: 46.948658,7.437406.
        date_time (Union[Unset, None, datetime.datetime]):  Example: 2023-04-18T14:55:00+01:00.
        location_type (Union[Unset, None, GetWeatherLocationType]):  Default:
            GetWeatherLocationType.COORDINATES.
        accept_language (Union[Unset, GetWeatherAcceptLanguage]):  Default:
            GetWeatherAcceptLanguage.EN.
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Problem, TimedWeatherForecast]
    """

    return sync_detailed(
        client=client,
        location_value=location_value,
        date_time=date_time,
        location_type=location_type,
        accept_language=accept_language,
        request_id=request_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    location_value: str,
    date_time: Union[Unset, None, datetime.datetime] = UNSET,
    location_type: Union[Unset, None, GetWeatherLocationType] = GetWeatherLocationType.COORDINATES,
    accept_language: Union[Unset, GetWeatherAcceptLanguage] = GetWeatherAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Response[Union[Problem, TimedWeatherForecast]]:
    """@Deprecated Will be part of /v3/trips! Get weather forecast at a Location.

     Source of data: [meteomatics](https://www.meteomatics.com/en/api/overview)

    Args:
        location_value (str):  Example: 46.948658,7.437406.
        date_time (Union[Unset, None, datetime.datetime]):  Example: 2023-04-18T14:55:00+01:00.
        location_type (Union[Unset, None, GetWeatherLocationType]):  Default:
            GetWeatherLocationType.COORDINATES.
        accept_language (Union[Unset, GetWeatherAcceptLanguage]):  Default:
            GetWeatherAcceptLanguage.EN.
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Problem, TimedWeatherForecast]]
    """

    kwargs = _get_kwargs(
        location_value=location_value,
        date_time=date_time,
        location_type=location_type,
        accept_language=accept_language,
        request_id=request_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    location_value: str,
    date_time: Union[Unset, None, datetime.datetime] = UNSET,
    location_type: Union[Unset, None, GetWeatherLocationType] = GetWeatherLocationType.COORDINATES,
    accept_language: Union[Unset, GetWeatherAcceptLanguage] = GetWeatherAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Optional[Union[Problem, TimedWeatherForecast]]:
    """@Deprecated Will be part of /v3/trips! Get weather forecast at a Location.

     Source of data: [meteomatics](https://www.meteomatics.com/en/api/overview)

    Args:
        location_value (str):  Example: 46.948658,7.437406.
        date_time (Union[Unset, None, datetime.datetime]):  Example: 2023-04-18T14:55:00+01:00.
        location_type (Union[Unset, None, GetWeatherLocationType]):  Default:
            GetWeatherLocationType.COORDINATES.
        accept_language (Union[Unset, GetWeatherAcceptLanguage]):  Default:
            GetWeatherAcceptLanguage.EN.
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Problem, TimedWeatherForecast]
    """

    return (
        await asyncio_detailed(
            client=client,
            location_value=location_value,
            date_time=date_time,
            location_type=location_type,
            accept_language=accept_language,
            request_id=request_id,
        )
    ).parsed
