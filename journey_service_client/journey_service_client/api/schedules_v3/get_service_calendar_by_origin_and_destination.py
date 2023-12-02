from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_service_calendar_by_origin_and_destination_accept_language import (
    GetServiceCalendarByOriginAndDestinationAcceptLanguage,
)
from ...models.problem import Problem
from ...models.service_calendar_by_origin_and_destination_download_response import (
    ServiceCalendarByOriginAndDestinationDownloadResponse,
)
from ...models.service_calendar_by_origin_and_destination_request_body import (
    ServiceCalendarByOriginAndDestinationRequestBody,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    json_body: ServiceCalendarByOriginAndDestinationRequestBody,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[
        Unset, GetServiceCalendarByOriginAndDestinationAcceptLanguage
    ] = GetServiceCalendarByOriginAndDestinationAcceptLanguage.EN,
) -> Dict[str, Any]:
    headers = {}
    if not isinstance(request_id, Unset):
        headers["Request-ID"] = request_id

    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = str(accept_language)

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/v3/service-calendar/by-origin-destination",
        "json": json_json_body,
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Problem, ServiceCalendarByOriginAndDestinationDownloadResponse]]:
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = Problem.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.OK:
        response_200 = ServiceCalendarByOriginAndDestinationDownloadResponse.from_dict(response.json())

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
) -> Response[Union[Problem, ServiceCalendarByOriginAndDestinationDownloadResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: ServiceCalendarByOriginAndDestinationRequestBody,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[
        Unset, GetServiceCalendarByOriginAndDestinationAcceptLanguage
    ] = GetServiceCalendarByOriginAndDestinationAcceptLanguage.EN,
) -> Response[Union[Problem, ServiceCalendarByOriginAndDestinationDownloadResponse]]:
    """Creates a specific service-calender PDF (aka personal timetable) in the background, downloadable by
    enduser.

     See [personal timetable](https://www.sbb.ch/de/fahrplan/online-fahrplan/pdf-
    fahrplaene/persoenlicher-taschenfahrplan.html), which initiates asynchronous PDF creation in the
    background and returns reference to current state of the process:
    - if `PersonalTimetableDownloadReference::downloadUrl` is given, your **personal timetable (pdf)**
    should be downloadable by the given link
    - otherwise keep calling `v3/service-calendar/by-origin-destination/{pollId}` by given `pollId`
    until 'downloadURL' is provided (might take a few seconds).

    Args:
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetServiceCalendarByOriginAndDestinationAcceptLanguage]):
            Default: GetServiceCalendarByOriginAndDestinationAcceptLanguage.EN.
        json_body (ServiceCalendarByOriginAndDestinationRequestBody): Request parameters (POST
            body).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Problem, ServiceCalendarByOriginAndDestinationDownloadResponse]]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
        request_id=request_id,
        accept_language=accept_language,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    json_body: ServiceCalendarByOriginAndDestinationRequestBody,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[
        Unset, GetServiceCalendarByOriginAndDestinationAcceptLanguage
    ] = GetServiceCalendarByOriginAndDestinationAcceptLanguage.EN,
) -> Optional[Union[Problem, ServiceCalendarByOriginAndDestinationDownloadResponse]]:
    """Creates a specific service-calender PDF (aka personal timetable) in the background, downloadable by
    enduser.

     See [personal timetable](https://www.sbb.ch/de/fahrplan/online-fahrplan/pdf-
    fahrplaene/persoenlicher-taschenfahrplan.html), which initiates asynchronous PDF creation in the
    background and returns reference to current state of the process:
    - if `PersonalTimetableDownloadReference::downloadUrl` is given, your **personal timetable (pdf)**
    should be downloadable by the given link
    - otherwise keep calling `v3/service-calendar/by-origin-destination/{pollId}` by given `pollId`
    until 'downloadURL' is provided (might take a few seconds).

    Args:
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetServiceCalendarByOriginAndDestinationAcceptLanguage]):
            Default: GetServiceCalendarByOriginAndDestinationAcceptLanguage.EN.
        json_body (ServiceCalendarByOriginAndDestinationRequestBody): Request parameters (POST
            body).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Problem, ServiceCalendarByOriginAndDestinationDownloadResponse]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        request_id=request_id,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: ServiceCalendarByOriginAndDestinationRequestBody,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[
        Unset, GetServiceCalendarByOriginAndDestinationAcceptLanguage
    ] = GetServiceCalendarByOriginAndDestinationAcceptLanguage.EN,
) -> Response[Union[Problem, ServiceCalendarByOriginAndDestinationDownloadResponse]]:
    """Creates a specific service-calender PDF (aka personal timetable) in the background, downloadable by
    enduser.

     See [personal timetable](https://www.sbb.ch/de/fahrplan/online-fahrplan/pdf-
    fahrplaene/persoenlicher-taschenfahrplan.html), which initiates asynchronous PDF creation in the
    background and returns reference to current state of the process:
    - if `PersonalTimetableDownloadReference::downloadUrl` is given, your **personal timetable (pdf)**
    should be downloadable by the given link
    - otherwise keep calling `v3/service-calendar/by-origin-destination/{pollId}` by given `pollId`
    until 'downloadURL' is provided (might take a few seconds).

    Args:
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetServiceCalendarByOriginAndDestinationAcceptLanguage]):
            Default: GetServiceCalendarByOriginAndDestinationAcceptLanguage.EN.
        json_body (ServiceCalendarByOriginAndDestinationRequestBody): Request parameters (POST
            body).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Problem, ServiceCalendarByOriginAndDestinationDownloadResponse]]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
        request_id=request_id,
        accept_language=accept_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: ServiceCalendarByOriginAndDestinationRequestBody,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[
        Unset, GetServiceCalendarByOriginAndDestinationAcceptLanguage
    ] = GetServiceCalendarByOriginAndDestinationAcceptLanguage.EN,
) -> Optional[Union[Problem, ServiceCalendarByOriginAndDestinationDownloadResponse]]:
    """Creates a specific service-calender PDF (aka personal timetable) in the background, downloadable by
    enduser.

     See [personal timetable](https://www.sbb.ch/de/fahrplan/online-fahrplan/pdf-
    fahrplaene/persoenlicher-taschenfahrplan.html), which initiates asynchronous PDF creation in the
    background and returns reference to current state of the process:
    - if `PersonalTimetableDownloadReference::downloadUrl` is given, your **personal timetable (pdf)**
    should be downloadable by the given link
    - otherwise keep calling `v3/service-calendar/by-origin-destination/{pollId}` by given `pollId`
    until 'downloadURL' is provided (might take a few seconds).

    Args:
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetServiceCalendarByOriginAndDestinationAcceptLanguage]):
            Default: GetServiceCalendarByOriginAndDestinationAcceptLanguage.EN.
        json_body (ServiceCalendarByOriginAndDestinationRequestBody): Request parameters (POST
            body).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Problem, ServiceCalendarByOriginAndDestinationDownloadResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            request_id=request_id,
            accept_language=accept_language,
        )
    ).parsed
