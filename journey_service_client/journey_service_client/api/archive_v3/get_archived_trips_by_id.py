import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_archived_trips_by_id_accept_language import GetArchivedTripsByIdAcceptLanguage
from ...models.problem import Problem
from ...models.realtime_mode_enum import RealtimeModeEnum
from ...models.trip_response import TripResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    archive_date: datetime.date,
    id: str,
    *,
    include_summary: Union[Unset, None, bool] = False,
    include_intermediate_stops: Union[Unset, None, str] = "ALL",
    realtime_mode: Union[Unset, None, RealtimeModeEnum] = RealtimeModeEnum.REALTIME,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, GetArchivedTripsByIdAcceptLanguage] = GetArchivedTripsByIdAcceptLanguage.EN,
) -> Dict[str, Any]:
    headers = {}
    if not isinstance(request_id, Unset):
        headers["Request-ID"] = request_id

    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = str(accept_language)

    params: Dict[str, Any] = {}
    params["includeSummary"] = include_summary

    params["includeIntermediateStops"] = include_intermediate_stops

    json_realtime_mode: Union[Unset, None, str] = UNSET
    if not isinstance(realtime_mode, Unset):
        json_realtime_mode = realtime_mode.value if realtime_mode else None

    params["realtimeMode"] = json_realtime_mode

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/v3/archive/{archiveDate}/trips/{id}".format(
            archiveDate=archive_date,
            id=id,
        ),
        "params": params,
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Problem, TripResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = TripResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = Problem.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = Problem.from_dict(response.json())

        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Problem, TripResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    archive_date: datetime.date,
    id: str,
    *,
    client: AuthenticatedClient,
    include_summary: Union[Unset, None, bool] = False,
    include_intermediate_stops: Union[Unset, None, str] = "ALL",
    realtime_mode: Union[Unset, None, RealtimeModeEnum] = RealtimeModeEnum.REALTIME,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, GetArchivedTripsByIdAcceptLanguage] = GetArchivedTripsByIdAcceptLanguage.EN,
) -> Response[Union[Problem, TripResponse]]:
    """Today and past (last 60days) realtime effective archive. Get corresponding trip for a specific
    `Trip::id` in the past. However other alternative trips may result set by
    `Trip::status::isAlternative`, based on specific realtime in the past.

     Reconstruction is not always guaranteed.

    Args:
        archive_date (datetime.date):
        id (str):
        include_summary (Union[Unset, None, bool]):
        include_intermediate_stops (Union[Unset, None, str]):  Default: 'ALL'.
        realtime_mode (Union[Unset, None, RealtimeModeEnum]): <br>x-extensible-enum:
            - `REALTIME` potentially planned and RT **including non-rideable** (like cancelled)
            - `REALTIME_RIDEABLE` as `REALTIME` but **excluding non-rideable**
            - `OFF` **planned only** Default: RealtimeModeEnum.REALTIME.
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetArchivedTripsByIdAcceptLanguage]):  Default:
            GetArchivedTripsByIdAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Problem, TripResponse]]
    """

    kwargs = _get_kwargs(
        archive_date=archive_date,
        id=id,
        include_summary=include_summary,
        include_intermediate_stops=include_intermediate_stops,
        realtime_mode=realtime_mode,
        request_id=request_id,
        accept_language=accept_language,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    archive_date: datetime.date,
    id: str,
    *,
    client: AuthenticatedClient,
    include_summary: Union[Unset, None, bool] = False,
    include_intermediate_stops: Union[Unset, None, str] = "ALL",
    realtime_mode: Union[Unset, None, RealtimeModeEnum] = RealtimeModeEnum.REALTIME,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, GetArchivedTripsByIdAcceptLanguage] = GetArchivedTripsByIdAcceptLanguage.EN,
) -> Optional[Union[Problem, TripResponse]]:
    """Today and past (last 60days) realtime effective archive. Get corresponding trip for a specific
    `Trip::id` in the past. However other alternative trips may result set by
    `Trip::status::isAlternative`, based on specific realtime in the past.

     Reconstruction is not always guaranteed.

    Args:
        archive_date (datetime.date):
        id (str):
        include_summary (Union[Unset, None, bool]):
        include_intermediate_stops (Union[Unset, None, str]):  Default: 'ALL'.
        realtime_mode (Union[Unset, None, RealtimeModeEnum]): <br>x-extensible-enum:
            - `REALTIME` potentially planned and RT **including non-rideable** (like cancelled)
            - `REALTIME_RIDEABLE` as `REALTIME` but **excluding non-rideable**
            - `OFF` **planned only** Default: RealtimeModeEnum.REALTIME.
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetArchivedTripsByIdAcceptLanguage]):  Default:
            GetArchivedTripsByIdAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Problem, TripResponse]
    """

    return sync_detailed(
        archive_date=archive_date,
        id=id,
        client=client,
        include_summary=include_summary,
        include_intermediate_stops=include_intermediate_stops,
        realtime_mode=realtime_mode,
        request_id=request_id,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    archive_date: datetime.date,
    id: str,
    *,
    client: AuthenticatedClient,
    include_summary: Union[Unset, None, bool] = False,
    include_intermediate_stops: Union[Unset, None, str] = "ALL",
    realtime_mode: Union[Unset, None, RealtimeModeEnum] = RealtimeModeEnum.REALTIME,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, GetArchivedTripsByIdAcceptLanguage] = GetArchivedTripsByIdAcceptLanguage.EN,
) -> Response[Union[Problem, TripResponse]]:
    """Today and past (last 60days) realtime effective archive. Get corresponding trip for a specific
    `Trip::id` in the past. However other alternative trips may result set by
    `Trip::status::isAlternative`, based on specific realtime in the past.

     Reconstruction is not always guaranteed.

    Args:
        archive_date (datetime.date):
        id (str):
        include_summary (Union[Unset, None, bool]):
        include_intermediate_stops (Union[Unset, None, str]):  Default: 'ALL'.
        realtime_mode (Union[Unset, None, RealtimeModeEnum]): <br>x-extensible-enum:
            - `REALTIME` potentially planned and RT **including non-rideable** (like cancelled)
            - `REALTIME_RIDEABLE` as `REALTIME` but **excluding non-rideable**
            - `OFF` **planned only** Default: RealtimeModeEnum.REALTIME.
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetArchivedTripsByIdAcceptLanguage]):  Default:
            GetArchivedTripsByIdAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Problem, TripResponse]]
    """

    kwargs = _get_kwargs(
        archive_date=archive_date,
        id=id,
        include_summary=include_summary,
        include_intermediate_stops=include_intermediate_stops,
        realtime_mode=realtime_mode,
        request_id=request_id,
        accept_language=accept_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    archive_date: datetime.date,
    id: str,
    *,
    client: AuthenticatedClient,
    include_summary: Union[Unset, None, bool] = False,
    include_intermediate_stops: Union[Unset, None, str] = "ALL",
    realtime_mode: Union[Unset, None, RealtimeModeEnum] = RealtimeModeEnum.REALTIME,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, GetArchivedTripsByIdAcceptLanguage] = GetArchivedTripsByIdAcceptLanguage.EN,
) -> Optional[Union[Problem, TripResponse]]:
    """Today and past (last 60days) realtime effective archive. Get corresponding trip for a specific
    `Trip::id` in the past. However other alternative trips may result set by
    `Trip::status::isAlternative`, based on specific realtime in the past.

     Reconstruction is not always guaranteed.

    Args:
        archive_date (datetime.date):
        id (str):
        include_summary (Union[Unset, None, bool]):
        include_intermediate_stops (Union[Unset, None, str]):  Default: 'ALL'.
        realtime_mode (Union[Unset, None, RealtimeModeEnum]): <br>x-extensible-enum:
            - `REALTIME` potentially planned and RT **including non-rideable** (like cancelled)
            - `REALTIME_RIDEABLE` as `REALTIME` but **excluding non-rideable**
            - `OFF` **planned only** Default: RealtimeModeEnum.REALTIME.
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetArchivedTripsByIdAcceptLanguage]):  Default:
            GetArchivedTripsByIdAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Problem, TripResponse]
    """

    return (
        await asyncio_detailed(
            archive_date=archive_date,
            id=id,
            client=client,
            include_summary=include_summary,
            include_intermediate_stops=include_intermediate_stops,
            realtime_mode=realtime_mode,
            request_id=request_id,
            accept_language=accept_language,
        )
    ).parsed
