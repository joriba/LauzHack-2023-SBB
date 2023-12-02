import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dated_vehicle_journey_response import DatedVehicleJourneyResponse
from ...models.get_dated_vehicle_journeys_by_vehicle_id_accept_language import (
    GetDatedVehicleJourneysByVehicleIdAcceptLanguage,
)
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    vehicle_id: str,
    *,
    date: Union[Unset, None, datetime.date] = UNSET,
    time: Union[Unset, None, str] = UNSET,
    include_intermediate_stops: Union[Unset, None, str] = "ALL",
    include_vehicle_speaker_message: Union[Unset, None, bool] = False,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[
        Unset, GetDatedVehicleJourneysByVehicleIdAcceptLanguage
    ] = GetDatedVehicleJourneysByVehicleIdAcceptLanguage.EN,
) -> Dict[str, Any]:
    headers = {}
    if not isinstance(request_id, Unset):
        headers["Request-ID"] = request_id

    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = str(accept_language)

    params: Dict[str, Any] = {}
    json_date: Union[Unset, None, str] = UNSET
    if not isinstance(date, Unset):
        json_date = date.isoformat() if date else None

    params["date"] = json_date

    params["time"] = time

    params["includeIntermediateStops"] = include_intermediate_stops

    params["includeVehicleSpeakerMessage"] = include_vehicle_speaker_message

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/v3/vehicle-journeys/by-vehicle/{vehicleId}".format(
            vehicleId=vehicle_id,
        ),
        "params": params,
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[DatedVehicleJourneyResponse, Problem]]:
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = Problem.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.OK:
        response_200 = DatedVehicleJourneyResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = Problem.from_dict(response.json())

        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[DatedVehicleJourneyResponse, Problem]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    vehicle_id: str,
    *,
    client: AuthenticatedClient,
    date: Union[Unset, None, datetime.date] = UNSET,
    time: Union[Unset, None, str] = UNSET,
    include_intermediate_stops: Union[Unset, None, str] = "ALL",
    include_vehicle_speaker_message: Union[Unset, None, bool] = False,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[
        Unset, GetDatedVehicleJourneysByVehicleIdAcceptLanguage
    ] = GetDatedVehicleJourneysByVehicleIdAcceptLanguage.EN,
) -> Response[Union[DatedVehicleJourneyResponse, Problem]]:
    """Get vehicle-journeys by car-identifier (carUIC oder BeaconID).

     Determines complete journey-details (aka de:Fahrt/Zuglauf) matching given parameters.

    Args:
        vehicle_id (str):
        date (Union[Unset, None, datetime.date]):
        time (Union[Unset, None, str]):  Example: 13:07.
        include_intermediate_stops (Union[Unset, None, str]):  Default: 'ALL'.
        include_vehicle_speaker_message (Union[Unset, None, bool]):
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetDatedVehicleJourneysByVehicleIdAcceptLanguage]):
            Default: GetDatedVehicleJourneysByVehicleIdAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DatedVehicleJourneyResponse, Problem]]
    """

    kwargs = _get_kwargs(
        vehicle_id=vehicle_id,
        date=date,
        time=time,
        include_intermediate_stops=include_intermediate_stops,
        include_vehicle_speaker_message=include_vehicle_speaker_message,
        request_id=request_id,
        accept_language=accept_language,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    vehicle_id: str,
    *,
    client: AuthenticatedClient,
    date: Union[Unset, None, datetime.date] = UNSET,
    time: Union[Unset, None, str] = UNSET,
    include_intermediate_stops: Union[Unset, None, str] = "ALL",
    include_vehicle_speaker_message: Union[Unset, None, bool] = False,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[
        Unset, GetDatedVehicleJourneysByVehicleIdAcceptLanguage
    ] = GetDatedVehicleJourneysByVehicleIdAcceptLanguage.EN,
) -> Optional[Union[DatedVehicleJourneyResponse, Problem]]:
    """Get vehicle-journeys by car-identifier (carUIC oder BeaconID).

     Determines complete journey-details (aka de:Fahrt/Zuglauf) matching given parameters.

    Args:
        vehicle_id (str):
        date (Union[Unset, None, datetime.date]):
        time (Union[Unset, None, str]):  Example: 13:07.
        include_intermediate_stops (Union[Unset, None, str]):  Default: 'ALL'.
        include_vehicle_speaker_message (Union[Unset, None, bool]):
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetDatedVehicleJourneysByVehicleIdAcceptLanguage]):
            Default: GetDatedVehicleJourneysByVehicleIdAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DatedVehicleJourneyResponse, Problem]
    """

    return sync_detailed(
        vehicle_id=vehicle_id,
        client=client,
        date=date,
        time=time,
        include_intermediate_stops=include_intermediate_stops,
        include_vehicle_speaker_message=include_vehicle_speaker_message,
        request_id=request_id,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    vehicle_id: str,
    *,
    client: AuthenticatedClient,
    date: Union[Unset, None, datetime.date] = UNSET,
    time: Union[Unset, None, str] = UNSET,
    include_intermediate_stops: Union[Unset, None, str] = "ALL",
    include_vehicle_speaker_message: Union[Unset, None, bool] = False,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[
        Unset, GetDatedVehicleJourneysByVehicleIdAcceptLanguage
    ] = GetDatedVehicleJourneysByVehicleIdAcceptLanguage.EN,
) -> Response[Union[DatedVehicleJourneyResponse, Problem]]:
    """Get vehicle-journeys by car-identifier (carUIC oder BeaconID).

     Determines complete journey-details (aka de:Fahrt/Zuglauf) matching given parameters.

    Args:
        vehicle_id (str):
        date (Union[Unset, None, datetime.date]):
        time (Union[Unset, None, str]):  Example: 13:07.
        include_intermediate_stops (Union[Unset, None, str]):  Default: 'ALL'.
        include_vehicle_speaker_message (Union[Unset, None, bool]):
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetDatedVehicleJourneysByVehicleIdAcceptLanguage]):
            Default: GetDatedVehicleJourneysByVehicleIdAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DatedVehicleJourneyResponse, Problem]]
    """

    kwargs = _get_kwargs(
        vehicle_id=vehicle_id,
        date=date,
        time=time,
        include_intermediate_stops=include_intermediate_stops,
        include_vehicle_speaker_message=include_vehicle_speaker_message,
        request_id=request_id,
        accept_language=accept_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    vehicle_id: str,
    *,
    client: AuthenticatedClient,
    date: Union[Unset, None, datetime.date] = UNSET,
    time: Union[Unset, None, str] = UNSET,
    include_intermediate_stops: Union[Unset, None, str] = "ALL",
    include_vehicle_speaker_message: Union[Unset, None, bool] = False,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[
        Unset, GetDatedVehicleJourneysByVehicleIdAcceptLanguage
    ] = GetDatedVehicleJourneysByVehicleIdAcceptLanguage.EN,
) -> Optional[Union[DatedVehicleJourneyResponse, Problem]]:
    """Get vehicle-journeys by car-identifier (carUIC oder BeaconID).

     Determines complete journey-details (aka de:Fahrt/Zuglauf) matching given parameters.

    Args:
        vehicle_id (str):
        date (Union[Unset, None, datetime.date]):
        time (Union[Unset, None, str]):  Example: 13:07.
        include_intermediate_stops (Union[Unset, None, str]):  Default: 'ALL'.
        include_vehicle_speaker_message (Union[Unset, None, bool]):
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetDatedVehicleJourneysByVehicleIdAcceptLanguage]):
            Default: GetDatedVehicleJourneysByVehicleIdAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DatedVehicleJourneyResponse, Problem]
    """

    return (
        await asyncio_detailed(
            vehicle_id=vehicle_id,
            client=client,
            date=date,
            time=time,
            include_intermediate_stops=include_intermediate_stops,
            include_vehicle_speaker_message=include_vehicle_speaker_message,
            request_id=request_id,
            accept_language=accept_language,
        )
    ).parsed
