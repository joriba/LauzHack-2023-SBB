import datetime
from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.departure_response import DepartureResponse
from ...models.get_vehicle_journeys_by_departure_at_origin_accept_language import (
    GetVehicleJourneysByDepartureAtOriginAcceptLanguage,
)
from ...models.problem import Problem
from ...models.transport_mode_enum import TransportModeEnum
from ...types import UNSET, Response, Unset


def _get_kwargs(
    origin: str,
    *,
    restrict_origin: Union[Unset, None, str] = "CONCRETE_STOP",
    direction: Union[Unset, None, str] = UNSET,
    date: Union[Unset, None, datetime.date] = UNSET,
    time: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = 20,
    duration: Union[Unset, None, int] = 60,
    include_transport_modes: Union[Unset, None, List[TransportModeEnum]] = UNSET,
    include_quays: Union[Unset, None, List[str]] = UNSET,
    include_rank: Union[Unset, None, bool] = False,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[
        Unset, GetVehicleJourneysByDepartureAtOriginAcceptLanguage
    ] = GetVehicleJourneysByDepartureAtOriginAcceptLanguage.EN,
) -> Dict[str, Any]:
    headers = {}
    if not isinstance(request_id, Unset):
        headers["Request-ID"] = request_id

    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = str(accept_language)

    params: Dict[str, Any] = {}
    params["restrictOrigin"] = restrict_origin

    params["direction"] = direction

    json_date: Union[Unset, None, str] = UNSET
    if not isinstance(date, Unset):
        json_date = date.isoformat() if date else None

    params["date"] = json_date

    params["time"] = time

    params["limit"] = limit

    params["duration"] = duration

    json_include_transport_modes: Union[Unset, None, List[str]] = UNSET
    if not isinstance(include_transport_modes, Unset):
        if include_transport_modes is None:
            json_include_transport_modes = None
        else:
            json_include_transport_modes = []
            for include_transport_modes_item_data in include_transport_modes:
                include_transport_modes_item = include_transport_modes_item_data.value

                json_include_transport_modes.append(include_transport_modes_item)

    params["includeTransportModes"] = json_include_transport_modes

    json_include_quays: Union[Unset, None, List[str]] = UNSET
    if not isinstance(include_quays, Unset):
        if include_quays is None:
            json_include_quays = None
        else:
            json_include_quays = include_quays

    params["includeQuays"] = json_include_quays

    params["includeRank"] = include_rank

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/v3/vehicle-journeys/by-departure/{origin}".format(
            origin=origin,
        ),
        "params": params,
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[DepartureResponse, Problem]]:
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = Problem.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = Problem.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.OK:
        response_200 = DepartureResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[DepartureResponse, Problem]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    origin: str,
    *,
    client: AuthenticatedClient,
    restrict_origin: Union[Unset, None, str] = "CONCRETE_STOP",
    direction: Union[Unset, None, str] = UNSET,
    date: Union[Unset, None, datetime.date] = UNSET,
    time: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = 20,
    duration: Union[Unset, None, int] = 60,
    include_transport_modes: Union[Unset, None, List[TransportModeEnum]] = UNSET,
    include_quays: Union[Unset, None, List[str]] = UNSET,
    include_rank: Union[Unset, None, bool] = False,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[
        Unset, GetVehicleJourneysByDepartureAtOriginAcceptLanguage
    ] = GetVehicleJourneysByDepartureAtOriginAcceptLanguage.EN,
) -> Response[Union[DepartureResponse, Problem]]:
    """Get departures starting at a StopPlace.

     Determines next departures from a Stop and point in time within duration (the results always contain
    all departures running to the last minute found even if the requested maximum limit was overrun).

    Args:
        origin (str):  Example: 8507000.
        restrict_origin (Union[Unset, None, str]):  Default: 'CONCRETE_STOP'.
        direction (Union[Unset, None, str]):  Example: 8503000.
        date (Union[Unset, None, datetime.date]):  Example: 2023-04-18.
        time (Union[Unset, None, str]):  Example: 13:07.
        limit (Union[Unset, None, int]):  Default: 20.
        duration (Union[Unset, None, int]):  Default: 60.
        include_transport_modes (Union[Unset, None, List[TransportModeEnum]]):
        include_quays (Union[Unset, None, List[str]]):
        include_rank (Union[Unset, None, bool]):
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetVehicleJourneysByDepartureAtOriginAcceptLanguage]):
            Default: GetVehicleJourneysByDepartureAtOriginAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DepartureResponse, Problem]]
    """

    kwargs = _get_kwargs(
        origin=origin,
        restrict_origin=restrict_origin,
        direction=direction,
        date=date,
        time=time,
        limit=limit,
        duration=duration,
        include_transport_modes=include_transport_modes,
        include_quays=include_quays,
        include_rank=include_rank,
        request_id=request_id,
        accept_language=accept_language,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    origin: str,
    *,
    client: AuthenticatedClient,
    restrict_origin: Union[Unset, None, str] = "CONCRETE_STOP",
    direction: Union[Unset, None, str] = UNSET,
    date: Union[Unset, None, datetime.date] = UNSET,
    time: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = 20,
    duration: Union[Unset, None, int] = 60,
    include_transport_modes: Union[Unset, None, List[TransportModeEnum]] = UNSET,
    include_quays: Union[Unset, None, List[str]] = UNSET,
    include_rank: Union[Unset, None, bool] = False,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[
        Unset, GetVehicleJourneysByDepartureAtOriginAcceptLanguage
    ] = GetVehicleJourneysByDepartureAtOriginAcceptLanguage.EN,
) -> Optional[Union[DepartureResponse, Problem]]:
    """Get departures starting at a StopPlace.

     Determines next departures from a Stop and point in time within duration (the results always contain
    all departures running to the last minute found even if the requested maximum limit was overrun).

    Args:
        origin (str):  Example: 8507000.
        restrict_origin (Union[Unset, None, str]):  Default: 'CONCRETE_STOP'.
        direction (Union[Unset, None, str]):  Example: 8503000.
        date (Union[Unset, None, datetime.date]):  Example: 2023-04-18.
        time (Union[Unset, None, str]):  Example: 13:07.
        limit (Union[Unset, None, int]):  Default: 20.
        duration (Union[Unset, None, int]):  Default: 60.
        include_transport_modes (Union[Unset, None, List[TransportModeEnum]]):
        include_quays (Union[Unset, None, List[str]]):
        include_rank (Union[Unset, None, bool]):
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetVehicleJourneysByDepartureAtOriginAcceptLanguage]):
            Default: GetVehicleJourneysByDepartureAtOriginAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DepartureResponse, Problem]
    """

    return sync_detailed(
        origin=origin,
        client=client,
        restrict_origin=restrict_origin,
        direction=direction,
        date=date,
        time=time,
        limit=limit,
        duration=duration,
        include_transport_modes=include_transport_modes,
        include_quays=include_quays,
        include_rank=include_rank,
        request_id=request_id,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    origin: str,
    *,
    client: AuthenticatedClient,
    restrict_origin: Union[Unset, None, str] = "CONCRETE_STOP",
    direction: Union[Unset, None, str] = UNSET,
    date: Union[Unset, None, datetime.date] = UNSET,
    time: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = 20,
    duration: Union[Unset, None, int] = 60,
    include_transport_modes: Union[Unset, None, List[TransportModeEnum]] = UNSET,
    include_quays: Union[Unset, None, List[str]] = UNSET,
    include_rank: Union[Unset, None, bool] = False,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[
        Unset, GetVehicleJourneysByDepartureAtOriginAcceptLanguage
    ] = GetVehicleJourneysByDepartureAtOriginAcceptLanguage.EN,
) -> Response[Union[DepartureResponse, Problem]]:
    """Get departures starting at a StopPlace.

     Determines next departures from a Stop and point in time within duration (the results always contain
    all departures running to the last minute found even if the requested maximum limit was overrun).

    Args:
        origin (str):  Example: 8507000.
        restrict_origin (Union[Unset, None, str]):  Default: 'CONCRETE_STOP'.
        direction (Union[Unset, None, str]):  Example: 8503000.
        date (Union[Unset, None, datetime.date]):  Example: 2023-04-18.
        time (Union[Unset, None, str]):  Example: 13:07.
        limit (Union[Unset, None, int]):  Default: 20.
        duration (Union[Unset, None, int]):  Default: 60.
        include_transport_modes (Union[Unset, None, List[TransportModeEnum]]):
        include_quays (Union[Unset, None, List[str]]):
        include_rank (Union[Unset, None, bool]):
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetVehicleJourneysByDepartureAtOriginAcceptLanguage]):
            Default: GetVehicleJourneysByDepartureAtOriginAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DepartureResponse, Problem]]
    """

    kwargs = _get_kwargs(
        origin=origin,
        restrict_origin=restrict_origin,
        direction=direction,
        date=date,
        time=time,
        limit=limit,
        duration=duration,
        include_transport_modes=include_transport_modes,
        include_quays=include_quays,
        include_rank=include_rank,
        request_id=request_id,
        accept_language=accept_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    origin: str,
    *,
    client: AuthenticatedClient,
    restrict_origin: Union[Unset, None, str] = "CONCRETE_STOP",
    direction: Union[Unset, None, str] = UNSET,
    date: Union[Unset, None, datetime.date] = UNSET,
    time: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = 20,
    duration: Union[Unset, None, int] = 60,
    include_transport_modes: Union[Unset, None, List[TransportModeEnum]] = UNSET,
    include_quays: Union[Unset, None, List[str]] = UNSET,
    include_rank: Union[Unset, None, bool] = False,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[
        Unset, GetVehicleJourneysByDepartureAtOriginAcceptLanguage
    ] = GetVehicleJourneysByDepartureAtOriginAcceptLanguage.EN,
) -> Optional[Union[DepartureResponse, Problem]]:
    """Get departures starting at a StopPlace.

     Determines next departures from a Stop and point in time within duration (the results always contain
    all departures running to the last minute found even if the requested maximum limit was overrun).

    Args:
        origin (str):  Example: 8507000.
        restrict_origin (Union[Unset, None, str]):  Default: 'CONCRETE_STOP'.
        direction (Union[Unset, None, str]):  Example: 8503000.
        date (Union[Unset, None, datetime.date]):  Example: 2023-04-18.
        time (Union[Unset, None, str]):  Example: 13:07.
        limit (Union[Unset, None, int]):  Default: 20.
        duration (Union[Unset, None, int]):  Default: 60.
        include_transport_modes (Union[Unset, None, List[TransportModeEnum]]):
        include_quays (Union[Unset, None, List[str]]):
        include_rank (Union[Unset, None, bool]):
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetVehicleJourneysByDepartureAtOriginAcceptLanguage]):
            Default: GetVehicleJourneysByDepartureAtOriginAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DepartureResponse, Problem]
    """

    return (
        await asyncio_detailed(
            origin=origin,
            client=client,
            restrict_origin=restrict_origin,
            direction=direction,
            date=date,
            time=time,
            limit=limit,
            duration=duration,
            include_transport_modes=include_transport_modes,
            include_quays=include_quays,
            include_rank=include_rank,
            request_id=request_id,
            accept_language=accept_language,
        )
    ).parsed
