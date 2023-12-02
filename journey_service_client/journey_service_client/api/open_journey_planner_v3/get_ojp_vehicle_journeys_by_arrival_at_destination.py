import datetime
from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.arrival_response import ArrivalResponse
from ...models.get_ojp_vehicle_journeys_by_arrival_at_destination_accept_language import (
    GetOjpVehicleJourneysByArrivalAtDestinationAcceptLanguage,
)
from ...models.problem import Problem
from ...models.transport_mode_enum import TransportModeEnum
from ...types import UNSET, Response, Unset


def _get_kwargs(
    destination: str,
    *,
    date: Union[Unset, None, datetime.date] = UNSET,
    time: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = 20,
    include_transport_modes: Union[Unset, None, List[TransportModeEnum]] = UNSET,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[
        Unset, GetOjpVehicleJourneysByArrivalAtDestinationAcceptLanguage
    ] = GetOjpVehicleJourneysByArrivalAtDestinationAcceptLanguage.EN,
    ojp_active_instance: Union[Unset, bool] = False,
    ojp_token: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers = {}
    if not isinstance(request_id, Unset):
        headers["Request-ID"] = request_id

    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = str(accept_language)

    if not isinstance(ojp_active_instance, Unset):
        headers["OJP-Active-Instance"] = "true" if ojp_active_instance else "false"

    if not isinstance(ojp_token, Unset):
        headers["OJP-Token"] = ojp_token

    params: Dict[str, Any] = {}
    json_date: Union[Unset, None, str] = UNSET
    if not isinstance(date, Unset):
        json_date = date.isoformat() if date else None

    params["date"] = json_date

    params["time"] = time

    params["limit"] = limit

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

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/v3/INCUBATOR/ojp/vehicle-journeys/by-arrival/{destination}".format(
            destination=destination,
        ),
        "params": params,
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ArrivalResponse, Problem]]:
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = Problem.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = Problem.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.OK:
        response_200 = ArrivalResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ArrivalResponse, Problem]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    destination: str,
    *,
    client: AuthenticatedClient,
    date: Union[Unset, None, datetime.date] = UNSET,
    time: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = 20,
    include_transport_modes: Union[Unset, None, List[TransportModeEnum]] = UNSET,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[
        Unset, GetOjpVehicleJourneysByArrivalAtDestinationAcceptLanguage
    ] = GetOjpVehicleJourneysByArrivalAtDestinationAcceptLanguage.EN,
    ojp_active_instance: Union[Unset, bool] = False,
    ojp_token: Union[Unset, str] = UNSET,
) -> Response[Union[ArrivalResponse, Problem]]:
    """Get arrivals at a StopPlace.

     Determines next arrivals at a given Stop and point in time within a duration (the results always
    contain all departures running to the last minute found even if the requested maximum limit was
    overrun).

    Args:
        destination (str):  Example: 8507000.
        date (Union[Unset, None, datetime.date]):  Example: 2023-04-18.
        time (Union[Unset, None, str]):  Example: 13:07.
        limit (Union[Unset, None, int]):  Default: 20.
        include_transport_modes (Union[Unset, None, List[TransportModeEnum]]):
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetOjpVehicleJourneysByArrivalAtDestinationAcceptLanguage]):
            Default: GetOjpVehicleJourneysByArrivalAtDestinationAcceptLanguage.EN.
        ojp_active_instance (Union[Unset, bool]):
        ojp_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ArrivalResponse, Problem]]
    """

    kwargs = _get_kwargs(
        destination=destination,
        date=date,
        time=time,
        limit=limit,
        include_transport_modes=include_transport_modes,
        request_id=request_id,
        accept_language=accept_language,
        ojp_active_instance=ojp_active_instance,
        ojp_token=ojp_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    destination: str,
    *,
    client: AuthenticatedClient,
    date: Union[Unset, None, datetime.date] = UNSET,
    time: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = 20,
    include_transport_modes: Union[Unset, None, List[TransportModeEnum]] = UNSET,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[
        Unset, GetOjpVehicleJourneysByArrivalAtDestinationAcceptLanguage
    ] = GetOjpVehicleJourneysByArrivalAtDestinationAcceptLanguage.EN,
    ojp_active_instance: Union[Unset, bool] = False,
    ojp_token: Union[Unset, str] = UNSET,
) -> Optional[Union[ArrivalResponse, Problem]]:
    """Get arrivals at a StopPlace.

     Determines next arrivals at a given Stop and point in time within a duration (the results always
    contain all departures running to the last minute found even if the requested maximum limit was
    overrun).

    Args:
        destination (str):  Example: 8507000.
        date (Union[Unset, None, datetime.date]):  Example: 2023-04-18.
        time (Union[Unset, None, str]):  Example: 13:07.
        limit (Union[Unset, None, int]):  Default: 20.
        include_transport_modes (Union[Unset, None, List[TransportModeEnum]]):
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetOjpVehicleJourneysByArrivalAtDestinationAcceptLanguage]):
            Default: GetOjpVehicleJourneysByArrivalAtDestinationAcceptLanguage.EN.
        ojp_active_instance (Union[Unset, bool]):
        ojp_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ArrivalResponse, Problem]
    """

    return sync_detailed(
        destination=destination,
        client=client,
        date=date,
        time=time,
        limit=limit,
        include_transport_modes=include_transport_modes,
        request_id=request_id,
        accept_language=accept_language,
        ojp_active_instance=ojp_active_instance,
        ojp_token=ojp_token,
    ).parsed


async def asyncio_detailed(
    destination: str,
    *,
    client: AuthenticatedClient,
    date: Union[Unset, None, datetime.date] = UNSET,
    time: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = 20,
    include_transport_modes: Union[Unset, None, List[TransportModeEnum]] = UNSET,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[
        Unset, GetOjpVehicleJourneysByArrivalAtDestinationAcceptLanguage
    ] = GetOjpVehicleJourneysByArrivalAtDestinationAcceptLanguage.EN,
    ojp_active_instance: Union[Unset, bool] = False,
    ojp_token: Union[Unset, str] = UNSET,
) -> Response[Union[ArrivalResponse, Problem]]:
    """Get arrivals at a StopPlace.

     Determines next arrivals at a given Stop and point in time within a duration (the results always
    contain all departures running to the last minute found even if the requested maximum limit was
    overrun).

    Args:
        destination (str):  Example: 8507000.
        date (Union[Unset, None, datetime.date]):  Example: 2023-04-18.
        time (Union[Unset, None, str]):  Example: 13:07.
        limit (Union[Unset, None, int]):  Default: 20.
        include_transport_modes (Union[Unset, None, List[TransportModeEnum]]):
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetOjpVehicleJourneysByArrivalAtDestinationAcceptLanguage]):
            Default: GetOjpVehicleJourneysByArrivalAtDestinationAcceptLanguage.EN.
        ojp_active_instance (Union[Unset, bool]):
        ojp_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ArrivalResponse, Problem]]
    """

    kwargs = _get_kwargs(
        destination=destination,
        date=date,
        time=time,
        limit=limit,
        include_transport_modes=include_transport_modes,
        request_id=request_id,
        accept_language=accept_language,
        ojp_active_instance=ojp_active_instance,
        ojp_token=ojp_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    destination: str,
    *,
    client: AuthenticatedClient,
    date: Union[Unset, None, datetime.date] = UNSET,
    time: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = 20,
    include_transport_modes: Union[Unset, None, List[TransportModeEnum]] = UNSET,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[
        Unset, GetOjpVehicleJourneysByArrivalAtDestinationAcceptLanguage
    ] = GetOjpVehicleJourneysByArrivalAtDestinationAcceptLanguage.EN,
    ojp_active_instance: Union[Unset, bool] = False,
    ojp_token: Union[Unset, str] = UNSET,
) -> Optional[Union[ArrivalResponse, Problem]]:
    """Get arrivals at a StopPlace.

     Determines next arrivals at a given Stop and point in time within a duration (the results always
    contain all departures running to the last minute found even if the requested maximum limit was
    overrun).

    Args:
        destination (str):  Example: 8507000.
        date (Union[Unset, None, datetime.date]):  Example: 2023-04-18.
        time (Union[Unset, None, str]):  Example: 13:07.
        limit (Union[Unset, None, int]):  Default: 20.
        include_transport_modes (Union[Unset, None, List[TransportModeEnum]]):
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetOjpVehicleJourneysByArrivalAtDestinationAcceptLanguage]):
            Default: GetOjpVehicleJourneysByArrivalAtDestinationAcceptLanguage.EN.
        ojp_active_instance (Union[Unset, bool]):
        ojp_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ArrivalResponse, Problem]
    """

    return (
        await asyncio_detailed(
            destination=destination,
            client=client,
            date=date,
            time=time,
            limit=limit,
            include_transport_modes=include_transport_modes,
            request_id=request_id,
            accept_language=accept_language,
            ojp_active_instance=ojp_active_instance,
            ojp_token=ojp_token,
        )
    ).parsed
