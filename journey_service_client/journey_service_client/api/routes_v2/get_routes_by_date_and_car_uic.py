import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_routes_by_date_and_car_uic_accept_language import GetRoutesByDateAndCarUicAcceptLanguage
from ...models.get_routes_by_date_and_car_uic_response_501 import GetRoutesByDateAndCarUicResponse501
from ...models.get_routes_by_date_and_car_uic_stop_behaviour import GetRoutesByDateAndCarUicStopBehaviour
from ...models.journey_detail import JourneyDetail
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    date: datetime.date,
    car_uic: str,
    *,
    time: Union[Unset, None, str] = UNSET,
    stop_behaviour: Union[
        Unset, None, GetRoutesByDateAndCarUicStopBehaviour
    ] = GetRoutesByDateAndCarUicStopBehaviour.REAL_BOARDING_ALIGHTING,
    accept_language: Union[Unset, GetRoutesByDateAndCarUicAcceptLanguage] = GetRoutesByDateAndCarUicAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = str(accept_language)

    if not isinstance(request_id, Unset):
        headers["Request-ID"] = request_id

    params: Dict[str, Any] = {}
    params["time"] = time

    json_stop_behaviour: Union[Unset, None, str] = UNSET
    if not isinstance(stop_behaviour, Unset):
        json_stop_behaviour = stop_behaviour.value if stop_behaviour else None

    params["stopBehaviour"] = json_stop_behaviour

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/b2c/v2/routes/{date}/{carUic}".format(
            date=date,
            carUic=car_uic,
        ),
        "params": params,
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[GetRoutesByDateAndCarUicResponse501, JourneyDetail, Problem]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = JourneyDetail.from_dict(response.json())

        return response_200
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
    if response.status_code == HTTPStatus.NOT_IMPLEMENTED:
        response_501 = GetRoutesByDateAndCarUicResponse501.from_dict(response.json())

        return response_501
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[GetRoutesByDateAndCarUicResponse501, JourneyDetail, Problem]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    date: datetime.date,
    car_uic: str,
    *,
    client: AuthenticatedClient,
    time: Union[Unset, None, str] = UNSET,
    stop_behaviour: Union[
        Unset, None, GetRoutesByDateAndCarUicStopBehaviour
    ] = GetRoutesByDateAndCarUicStopBehaviour.REAL_BOARDING_ALIGHTING,
    accept_language: Union[Unset, GetRoutesByDateAndCarUicAcceptLanguage] = GetRoutesByDateAndCarUicAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Response[Union[GetRoutesByDateAndCarUicResponse501, JourneyDetail, Problem]]:
    """@Deprecated (SWITCH to v3/vehicle-journeys/by-vehicle/{vehicleId})! Get complete journey of a
    vehicle including its stops (de: Zuglauf mit Haltestellen) by a concrete car-reference within a
    train-formation.

     The journey-detail will deliver information about the complete route of a vehicle (resp. transport-
    product such as train, bus,..).<br>The journeyReference is part of a leg or stationboard response.
    It contains a list of all stops/stations of this journey including all departure and arrival times
    (with real-time data if available) and additional information like specific attributes about
    facilities and other texts.

    Args:
        date (datetime.date):
        car_uic (str):  Example: 94.
        time (Union[Unset, None, str]):  Example: 13:07.
        stop_behaviour (Union[Unset, None, GetRoutesByDateAndCarUicStopBehaviour]):  Default:
            GetRoutesByDateAndCarUicStopBehaviour.REAL_BOARDING_ALIGHTING.
        accept_language (Union[Unset, GetRoutesByDateAndCarUicAcceptLanguage]):  Default:
            GetRoutesByDateAndCarUicAcceptLanguage.EN.
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetRoutesByDateAndCarUicResponse501, JourneyDetail, Problem]]
    """

    kwargs = _get_kwargs(
        date=date,
        car_uic=car_uic,
        time=time,
        stop_behaviour=stop_behaviour,
        accept_language=accept_language,
        request_id=request_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    date: datetime.date,
    car_uic: str,
    *,
    client: AuthenticatedClient,
    time: Union[Unset, None, str] = UNSET,
    stop_behaviour: Union[
        Unset, None, GetRoutesByDateAndCarUicStopBehaviour
    ] = GetRoutesByDateAndCarUicStopBehaviour.REAL_BOARDING_ALIGHTING,
    accept_language: Union[Unset, GetRoutesByDateAndCarUicAcceptLanguage] = GetRoutesByDateAndCarUicAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Optional[Union[GetRoutesByDateAndCarUicResponse501, JourneyDetail, Problem]]:
    """@Deprecated (SWITCH to v3/vehicle-journeys/by-vehicle/{vehicleId})! Get complete journey of a
    vehicle including its stops (de: Zuglauf mit Haltestellen) by a concrete car-reference within a
    train-formation.

     The journey-detail will deliver information about the complete route of a vehicle (resp. transport-
    product such as train, bus,..).<br>The journeyReference is part of a leg or stationboard response.
    It contains a list of all stops/stations of this journey including all departure and arrival times
    (with real-time data if available) and additional information like specific attributes about
    facilities and other texts.

    Args:
        date (datetime.date):
        car_uic (str):  Example: 94.
        time (Union[Unset, None, str]):  Example: 13:07.
        stop_behaviour (Union[Unset, None, GetRoutesByDateAndCarUicStopBehaviour]):  Default:
            GetRoutesByDateAndCarUicStopBehaviour.REAL_BOARDING_ALIGHTING.
        accept_language (Union[Unset, GetRoutesByDateAndCarUicAcceptLanguage]):  Default:
            GetRoutesByDateAndCarUicAcceptLanguage.EN.
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetRoutesByDateAndCarUicResponse501, JourneyDetail, Problem]
    """

    return sync_detailed(
        date=date,
        car_uic=car_uic,
        client=client,
        time=time,
        stop_behaviour=stop_behaviour,
        accept_language=accept_language,
        request_id=request_id,
    ).parsed


async def asyncio_detailed(
    date: datetime.date,
    car_uic: str,
    *,
    client: AuthenticatedClient,
    time: Union[Unset, None, str] = UNSET,
    stop_behaviour: Union[
        Unset, None, GetRoutesByDateAndCarUicStopBehaviour
    ] = GetRoutesByDateAndCarUicStopBehaviour.REAL_BOARDING_ALIGHTING,
    accept_language: Union[Unset, GetRoutesByDateAndCarUicAcceptLanguage] = GetRoutesByDateAndCarUicAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Response[Union[GetRoutesByDateAndCarUicResponse501, JourneyDetail, Problem]]:
    """@Deprecated (SWITCH to v3/vehicle-journeys/by-vehicle/{vehicleId})! Get complete journey of a
    vehicle including its stops (de: Zuglauf mit Haltestellen) by a concrete car-reference within a
    train-formation.

     The journey-detail will deliver information about the complete route of a vehicle (resp. transport-
    product such as train, bus,..).<br>The journeyReference is part of a leg or stationboard response.
    It contains a list of all stops/stations of this journey including all departure and arrival times
    (with real-time data if available) and additional information like specific attributes about
    facilities and other texts.

    Args:
        date (datetime.date):
        car_uic (str):  Example: 94.
        time (Union[Unset, None, str]):  Example: 13:07.
        stop_behaviour (Union[Unset, None, GetRoutesByDateAndCarUicStopBehaviour]):  Default:
            GetRoutesByDateAndCarUicStopBehaviour.REAL_BOARDING_ALIGHTING.
        accept_language (Union[Unset, GetRoutesByDateAndCarUicAcceptLanguage]):  Default:
            GetRoutesByDateAndCarUicAcceptLanguage.EN.
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetRoutesByDateAndCarUicResponse501, JourneyDetail, Problem]]
    """

    kwargs = _get_kwargs(
        date=date,
        car_uic=car_uic,
        time=time,
        stop_behaviour=stop_behaviour,
        accept_language=accept_language,
        request_id=request_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    date: datetime.date,
    car_uic: str,
    *,
    client: AuthenticatedClient,
    time: Union[Unset, None, str] = UNSET,
    stop_behaviour: Union[
        Unset, None, GetRoutesByDateAndCarUicStopBehaviour
    ] = GetRoutesByDateAndCarUicStopBehaviour.REAL_BOARDING_ALIGHTING,
    accept_language: Union[Unset, GetRoutesByDateAndCarUicAcceptLanguage] = GetRoutesByDateAndCarUicAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Optional[Union[GetRoutesByDateAndCarUicResponse501, JourneyDetail, Problem]]:
    """@Deprecated (SWITCH to v3/vehicle-journeys/by-vehicle/{vehicleId})! Get complete journey of a
    vehicle including its stops (de: Zuglauf mit Haltestellen) by a concrete car-reference within a
    train-formation.

     The journey-detail will deliver information about the complete route of a vehicle (resp. transport-
    product such as train, bus,..).<br>The journeyReference is part of a leg or stationboard response.
    It contains a list of all stops/stations of this journey including all departure and arrival times
    (with real-time data if available) and additional information like specific attributes about
    facilities and other texts.

    Args:
        date (datetime.date):
        car_uic (str):  Example: 94.
        time (Union[Unset, None, str]):  Example: 13:07.
        stop_behaviour (Union[Unset, None, GetRoutesByDateAndCarUicStopBehaviour]):  Default:
            GetRoutesByDateAndCarUicStopBehaviour.REAL_BOARDING_ALIGHTING.
        accept_language (Union[Unset, GetRoutesByDateAndCarUicAcceptLanguage]):  Default:
            GetRoutesByDateAndCarUicAcceptLanguage.EN.
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetRoutesByDateAndCarUicResponse501, JourneyDetail, Problem]
    """

    return (
        await asyncio_detailed(
            date=date,
            car_uic=car_uic,
            client=client,
            time=time,
            stop_behaviour=stop_behaviour,
            accept_language=accept_language,
            request_id=request_id,
        )
    ).parsed
