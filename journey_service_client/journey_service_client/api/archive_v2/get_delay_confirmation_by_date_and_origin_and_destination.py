import datetime
from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_delay_confirmation_by_date_and_origin_and_destination_accept_language import (
    GetDelayConfirmationByDateAndOriginAndDestinationAcceptLanguage,
)
from ...models.get_delay_confirmation_by_date_and_origin_and_destination_response_501 import (
    GetDelayConfirmationByDateAndOriginAndDestinationResponse501,
)
from ...models.local_time import LocalTime
from ...models.problem import Problem
from ...models.trip_v2 import TripV2
from ...types import UNSET, Response, Unset


def _get_kwargs(
    archive_date: datetime.date,
    origin_uic: int,
    destination_uic: int,
    *,
    search_for_arrival: Union[Unset, None, bool] = False,
    time: Union[Unset, None, "LocalTime"] = UNSET,
    accept_language: Union[
        Unset, GetDelayConfirmationByDateAndOriginAndDestinationAcceptLanguage
    ] = GetDelayConfirmationByDateAndOriginAndDestinationAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = str(accept_language)

    if not isinstance(request_id, Unset):
        headers["Request-ID"] = request_id

    params: Dict[str, Any] = {}
    params["searchForArrival"] = search_for_arrival

    json_time: Union[Unset, None, Dict[str, Any]] = UNSET
    if not isinstance(time, Unset):
        json_time = time.to_dict() if time else None

    if not isinstance(json_time, Unset) and json_time is not None:
        params.update(json_time)

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/b2c/v2/delayConfirmation/{archiveDate}/{originUIC}/{destinationUIC}".format(
            archiveDate=archive_date,
            originUIC=origin_uic,
            destinationUIC=destination_uic,
        ),
        "params": params,
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[GetDelayConfirmationByDateAndOriginAndDestinationResponse501, List["TripV2"], Problem]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = TripV2.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = Problem.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.NOT_IMPLEMENTED:
        response_501 = GetDelayConfirmationByDateAndOriginAndDestinationResponse501.from_dict(response.json())

        return response_501
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[GetDelayConfirmationByDateAndOriginAndDestinationResponse501, List["TripV2"], Problem]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    archive_date: datetime.date,
    origin_uic: int,
    destination_uic: int,
    *,
    client: AuthenticatedClient,
    search_for_arrival: Union[Unset, None, bool] = False,
    time: Union[Unset, None, "LocalTime"] = UNSET,
    accept_language: Union[
        Unset, GetDelayConfirmationByDateAndOriginAndDestinationAcceptLanguage
    ] = GetDelayConfirmationByDateAndOriginAndDestinationAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Response[Union[GetDelayConfirmationByDateAndOriginAndDestinationResponse501, List["TripV2"], Problem]]:
    """@Deprecated use v3/archive/{archiveDate}/trips/by-origin-destination! Get one-way trips between
    origin and destination STATIONs which are delayed. Recorded today back to 5 days ago, captured at
    arrival time for **SBB, BLS, SOB, THURBO, ZB, RegionAlps and TPF**.

    Args:
        archive_date (datetime.date):
        origin_uic (int):  Example: 8507000.
        destination_uic (int):  Example: 8503000.
        search_for_arrival (Union[Unset, None, bool]):
        time (Union[Unset, None, LocalTime]): Message event period starting at time daily.
            Example: 13:07.
        accept_language (Union[Unset,
            GetDelayConfirmationByDateAndOriginAndDestinationAcceptLanguage]):  Default:
            GetDelayConfirmationByDateAndOriginAndDestinationAcceptLanguage.EN.
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetDelayConfirmationByDateAndOriginAndDestinationResponse501, List['TripV2'], Problem]]
    """

    kwargs = _get_kwargs(
        archive_date=archive_date,
        origin_uic=origin_uic,
        destination_uic=destination_uic,
        search_for_arrival=search_for_arrival,
        time=time,
        accept_language=accept_language,
        request_id=request_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    archive_date: datetime.date,
    origin_uic: int,
    destination_uic: int,
    *,
    client: AuthenticatedClient,
    search_for_arrival: Union[Unset, None, bool] = False,
    time: Union[Unset, None, "LocalTime"] = UNSET,
    accept_language: Union[
        Unset, GetDelayConfirmationByDateAndOriginAndDestinationAcceptLanguage
    ] = GetDelayConfirmationByDateAndOriginAndDestinationAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Optional[Union[GetDelayConfirmationByDateAndOriginAndDestinationResponse501, List["TripV2"], Problem]]:
    """@Deprecated use v3/archive/{archiveDate}/trips/by-origin-destination! Get one-way trips between
    origin and destination STATIONs which are delayed. Recorded today back to 5 days ago, captured at
    arrival time for **SBB, BLS, SOB, THURBO, ZB, RegionAlps and TPF**.

    Args:
        archive_date (datetime.date):
        origin_uic (int):  Example: 8507000.
        destination_uic (int):  Example: 8503000.
        search_for_arrival (Union[Unset, None, bool]):
        time (Union[Unset, None, LocalTime]): Message event period starting at time daily.
            Example: 13:07.
        accept_language (Union[Unset,
            GetDelayConfirmationByDateAndOriginAndDestinationAcceptLanguage]):  Default:
            GetDelayConfirmationByDateAndOriginAndDestinationAcceptLanguage.EN.
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetDelayConfirmationByDateAndOriginAndDestinationResponse501, List['TripV2'], Problem]
    """

    return sync_detailed(
        archive_date=archive_date,
        origin_uic=origin_uic,
        destination_uic=destination_uic,
        client=client,
        search_for_arrival=search_for_arrival,
        time=time,
        accept_language=accept_language,
        request_id=request_id,
    ).parsed


async def asyncio_detailed(
    archive_date: datetime.date,
    origin_uic: int,
    destination_uic: int,
    *,
    client: AuthenticatedClient,
    search_for_arrival: Union[Unset, None, bool] = False,
    time: Union[Unset, None, "LocalTime"] = UNSET,
    accept_language: Union[
        Unset, GetDelayConfirmationByDateAndOriginAndDestinationAcceptLanguage
    ] = GetDelayConfirmationByDateAndOriginAndDestinationAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Response[Union[GetDelayConfirmationByDateAndOriginAndDestinationResponse501, List["TripV2"], Problem]]:
    """@Deprecated use v3/archive/{archiveDate}/trips/by-origin-destination! Get one-way trips between
    origin and destination STATIONs which are delayed. Recorded today back to 5 days ago, captured at
    arrival time for **SBB, BLS, SOB, THURBO, ZB, RegionAlps and TPF**.

    Args:
        archive_date (datetime.date):
        origin_uic (int):  Example: 8507000.
        destination_uic (int):  Example: 8503000.
        search_for_arrival (Union[Unset, None, bool]):
        time (Union[Unset, None, LocalTime]): Message event period starting at time daily.
            Example: 13:07.
        accept_language (Union[Unset,
            GetDelayConfirmationByDateAndOriginAndDestinationAcceptLanguage]):  Default:
            GetDelayConfirmationByDateAndOriginAndDestinationAcceptLanguage.EN.
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetDelayConfirmationByDateAndOriginAndDestinationResponse501, List['TripV2'], Problem]]
    """

    kwargs = _get_kwargs(
        archive_date=archive_date,
        origin_uic=origin_uic,
        destination_uic=destination_uic,
        search_for_arrival=search_for_arrival,
        time=time,
        accept_language=accept_language,
        request_id=request_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    archive_date: datetime.date,
    origin_uic: int,
    destination_uic: int,
    *,
    client: AuthenticatedClient,
    search_for_arrival: Union[Unset, None, bool] = False,
    time: Union[Unset, None, "LocalTime"] = UNSET,
    accept_language: Union[
        Unset, GetDelayConfirmationByDateAndOriginAndDestinationAcceptLanguage
    ] = GetDelayConfirmationByDateAndOriginAndDestinationAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Optional[Union[GetDelayConfirmationByDateAndOriginAndDestinationResponse501, List["TripV2"], Problem]]:
    """@Deprecated use v3/archive/{archiveDate}/trips/by-origin-destination! Get one-way trips between
    origin and destination STATIONs which are delayed. Recorded today back to 5 days ago, captured at
    arrival time for **SBB, BLS, SOB, THURBO, ZB, RegionAlps and TPF**.

    Args:
        archive_date (datetime.date):
        origin_uic (int):  Example: 8507000.
        destination_uic (int):  Example: 8503000.
        search_for_arrival (Union[Unset, None, bool]):
        time (Union[Unset, None, LocalTime]): Message event period starting at time daily.
            Example: 13:07.
        accept_language (Union[Unset,
            GetDelayConfirmationByDateAndOriginAndDestinationAcceptLanguage]):  Default:
            GetDelayConfirmationByDateAndOriginAndDestinationAcceptLanguage.EN.
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetDelayConfirmationByDateAndOriginAndDestinationResponse501, List['TripV2'], Problem]
    """

    return (
        await asyncio_detailed(
            archive_date=archive_date,
            origin_uic=origin_uic,
            destination_uic=destination_uic,
            client=client,
            search_for_arrival=search_for_arrival,
            time=time,
            accept_language=accept_language,
            request_id=request_id,
        )
    ).parsed
