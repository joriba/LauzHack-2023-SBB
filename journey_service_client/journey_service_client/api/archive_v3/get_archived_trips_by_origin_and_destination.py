import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_archived_trips_by_origin_and_destination_accept_language import (
    GetArchivedTripsByOriginAndDestinationAcceptLanguage,
)
from ...models.problem import Problem
from ...models.trip_response import TripResponse
from ...models.trips_by_origin_and_destination_request_body import TripsByOriginAndDestinationRequestBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    archive_date: datetime.date,
    *,
    json_body: TripsByOriginAndDestinationRequestBody,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[
        Unset, GetArchivedTripsByOriginAndDestinationAcceptLanguage
    ] = GetArchivedTripsByOriginAndDestinationAcceptLanguage.EN,
) -> Dict[str, Any]:
    headers = {}
    if not isinstance(request_id, Unset):
        headers["Request-ID"] = request_id

    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = str(accept_language)

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/v3/archive/{archiveDate}/trips/by-origin-destination".format(
            archiveDate=archive_date,
        ),
        "json": json_json_body,
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
    *,
    client: AuthenticatedClient,
    json_body: TripsByOriginAndDestinationRequestBody,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[
        Unset, GetArchivedTripsByOriginAndDestinationAcceptLanguage
    ] = GetArchivedTripsByOriginAndDestinationAcceptLanguage.EN,
) -> Response[Union[Problem, TripResponse]]:
    """{Idempotent: GET with body payload} Today and past (last 60days) realtime effective archive. Get
    one-way trips between given origin and destination locations based on archived trips in the past.
    API behaves like /trips with additional properties. **Some attributes of `v3/trips` are not
    supported yet**: viasNot, viasNoTransfer, optimisationMethod, includeAlternateMatch,
    includeNoticeAttributes, includeEconomic, includeUnsharp, includeEarlier, includeEcologyComparison,
    includeOperatingDays, includeRouteProjection, includeGroupReservation, excludeDatedVehicleJourneys,
    excludeFootpathAtOriginAndDestination

     This API may be used to validate delays, for e.g. requested by PARE.

    Args:
        archive_date (datetime.date):
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetArchivedTripsByOriginAndDestinationAcceptLanguage]):
            Default: GetArchivedTripsByOriginAndDestinationAcceptLanguage.EN.
        json_body (TripsByOriginAndDestinationRequestBody): Request parameters (POST body). OJP
            passive instance requires Stop UIC like '850700' whereas active instance enforces
            'OJP:STOP:SBB:8507000|Bern'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Problem, TripResponse]]
    """

    kwargs = _get_kwargs(
        archive_date=archive_date,
        json_body=json_body,
        request_id=request_id,
        accept_language=accept_language,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    archive_date: datetime.date,
    *,
    client: AuthenticatedClient,
    json_body: TripsByOriginAndDestinationRequestBody,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[
        Unset, GetArchivedTripsByOriginAndDestinationAcceptLanguage
    ] = GetArchivedTripsByOriginAndDestinationAcceptLanguage.EN,
) -> Optional[Union[Problem, TripResponse]]:
    """{Idempotent: GET with body payload} Today and past (last 60days) realtime effective archive. Get
    one-way trips between given origin and destination locations based on archived trips in the past.
    API behaves like /trips with additional properties. **Some attributes of `v3/trips` are not
    supported yet**: viasNot, viasNoTransfer, optimisationMethod, includeAlternateMatch,
    includeNoticeAttributes, includeEconomic, includeUnsharp, includeEarlier, includeEcologyComparison,
    includeOperatingDays, includeRouteProjection, includeGroupReservation, excludeDatedVehicleJourneys,
    excludeFootpathAtOriginAndDestination

     This API may be used to validate delays, for e.g. requested by PARE.

    Args:
        archive_date (datetime.date):
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetArchivedTripsByOriginAndDestinationAcceptLanguage]):
            Default: GetArchivedTripsByOriginAndDestinationAcceptLanguage.EN.
        json_body (TripsByOriginAndDestinationRequestBody): Request parameters (POST body). OJP
            passive instance requires Stop UIC like '850700' whereas active instance enforces
            'OJP:STOP:SBB:8507000|Bern'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Problem, TripResponse]
    """

    return sync_detailed(
        archive_date=archive_date,
        client=client,
        json_body=json_body,
        request_id=request_id,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    archive_date: datetime.date,
    *,
    client: AuthenticatedClient,
    json_body: TripsByOriginAndDestinationRequestBody,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[
        Unset, GetArchivedTripsByOriginAndDestinationAcceptLanguage
    ] = GetArchivedTripsByOriginAndDestinationAcceptLanguage.EN,
) -> Response[Union[Problem, TripResponse]]:
    """{Idempotent: GET with body payload} Today and past (last 60days) realtime effective archive. Get
    one-way trips between given origin and destination locations based on archived trips in the past.
    API behaves like /trips with additional properties. **Some attributes of `v3/trips` are not
    supported yet**: viasNot, viasNoTransfer, optimisationMethod, includeAlternateMatch,
    includeNoticeAttributes, includeEconomic, includeUnsharp, includeEarlier, includeEcologyComparison,
    includeOperatingDays, includeRouteProjection, includeGroupReservation, excludeDatedVehicleJourneys,
    excludeFootpathAtOriginAndDestination

     This API may be used to validate delays, for e.g. requested by PARE.

    Args:
        archive_date (datetime.date):
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetArchivedTripsByOriginAndDestinationAcceptLanguage]):
            Default: GetArchivedTripsByOriginAndDestinationAcceptLanguage.EN.
        json_body (TripsByOriginAndDestinationRequestBody): Request parameters (POST body). OJP
            passive instance requires Stop UIC like '850700' whereas active instance enforces
            'OJP:STOP:SBB:8507000|Bern'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Problem, TripResponse]]
    """

    kwargs = _get_kwargs(
        archive_date=archive_date,
        json_body=json_body,
        request_id=request_id,
        accept_language=accept_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    archive_date: datetime.date,
    *,
    client: AuthenticatedClient,
    json_body: TripsByOriginAndDestinationRequestBody,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[
        Unset, GetArchivedTripsByOriginAndDestinationAcceptLanguage
    ] = GetArchivedTripsByOriginAndDestinationAcceptLanguage.EN,
) -> Optional[Union[Problem, TripResponse]]:
    """{Idempotent: GET with body payload} Today and past (last 60days) realtime effective archive. Get
    one-way trips between given origin and destination locations based on archived trips in the past.
    API behaves like /trips with additional properties. **Some attributes of `v3/trips` are not
    supported yet**: viasNot, viasNoTransfer, optimisationMethod, includeAlternateMatch,
    includeNoticeAttributes, includeEconomic, includeUnsharp, includeEarlier, includeEcologyComparison,
    includeOperatingDays, includeRouteProjection, includeGroupReservation, excludeDatedVehicleJourneys,
    excludeFootpathAtOriginAndDestination

     This API may be used to validate delays, for e.g. requested by PARE.

    Args:
        archive_date (datetime.date):
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetArchivedTripsByOriginAndDestinationAcceptLanguage]):
            Default: GetArchivedTripsByOriginAndDestinationAcceptLanguage.EN.
        json_body (TripsByOriginAndDestinationRequestBody): Request parameters (POST body). OJP
            passive instance requires Stop UIC like '850700' whereas active instance enforces
            'OJP:STOP:SBB:8507000|Bern'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Problem, TripResponse]
    """

    return (
        await asyncio_detailed(
            archive_date=archive_date,
            client=client,
            json_body=json_body,
            request_id=request_id,
            accept_language=accept_language,
        )
    ).parsed
