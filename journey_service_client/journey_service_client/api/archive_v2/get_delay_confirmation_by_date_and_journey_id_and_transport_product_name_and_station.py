import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_delay_confirmation_by_date_and_journey_id_and_transport_product_name_and_station_accept_language import (
    GetDelayConfirmationByDateAndJourneyIdAndTransportProductNameAndStationAcceptLanguage,
)
from ...models.get_delay_confirmation_by_date_and_journey_id_and_transport_product_name_and_station_response_501 import (
    GetDelayConfirmationByDateAndJourneyIdAndTransportProductNameAndStationResponse501,
)
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    archive_date: datetime.date,
    journey_id: str,
    transport_product_name: str,
    station_uic: int,
    *,
    accept_language: Union[
        Unset, GetDelayConfirmationByDateAndJourneyIdAndTransportProductNameAndStationAcceptLanguage
    ] = GetDelayConfirmationByDateAndJourneyIdAndTransportProductNameAndStationAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = str(accept_language)

    if not isinstance(request_id, Unset):
        headers["Request-ID"] = request_id

    return {
        "method": "get",
        "url": "/b2c/v2/delayConfirmation/{archiveDate}/{journeyId}/{transportProductName}/{stationUIC}".format(
            archiveDate=archive_date,
            journeyId=journey_id,
            transportProductName=transport_product_name,
            stationUIC=station_uic,
        ),
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[GetDelayConfirmationByDateAndJourneyIdAndTransportProductNameAndStationResponse501, Problem, str]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = cast(str, response.json())
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
        response_501 = GetDelayConfirmationByDateAndJourneyIdAndTransportProductNameAndStationResponse501.from_dict(
            response.json()
        )

        return response_501
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[GetDelayConfirmationByDateAndJourneyIdAndTransportProductNameAndStationResponse501, Problem, str]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    archive_date: datetime.date,
    journey_id: str,
    transport_product_name: str,
    station_uic: int,
    *,
    client: AuthenticatedClient,
    accept_language: Union[
        Unset, GetDelayConfirmationByDateAndJourneyIdAndTransportProductNameAndStationAcceptLanguage
    ] = GetDelayConfirmationByDateAndJourneyIdAndTransportProductNameAndStationAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Response[Union[GetDelayConfirmationByDateAndJourneyIdAndTransportProductNameAndStationResponse501, Problem, str]]:
    """Returns pdf with given delayed connection. Recorded today back to 5 days ago, captured at arrival
    time for **SBB, BLS, SOB, THURBO, ZB, RegionAlps and TPF**.

    Args:
        archive_date (datetime.date):
        journey_id (str):  Example: 707_170525_8501008_0542_8506302.
        transport_product_name (str):  Example: IC 1 728.
        station_uic (int):  Example: 8507000.
        accept_language (Union[Unset,
            GetDelayConfirmationByDateAndJourneyIdAndTransportProductNameAndStationAcceptLanguage]):
            Default:
            GetDelayConfirmationByDateAndJourneyIdAndTransportProductNameAndStationAcceptLanguage.EN.
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetDelayConfirmationByDateAndJourneyIdAndTransportProductNameAndStationResponse501, Problem, str]]
    """

    kwargs = _get_kwargs(
        archive_date=archive_date,
        journey_id=journey_id,
        transport_product_name=transport_product_name,
        station_uic=station_uic,
        accept_language=accept_language,
        request_id=request_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    archive_date: datetime.date,
    journey_id: str,
    transport_product_name: str,
    station_uic: int,
    *,
    client: AuthenticatedClient,
    accept_language: Union[
        Unset, GetDelayConfirmationByDateAndJourneyIdAndTransportProductNameAndStationAcceptLanguage
    ] = GetDelayConfirmationByDateAndJourneyIdAndTransportProductNameAndStationAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Optional[Union[GetDelayConfirmationByDateAndJourneyIdAndTransportProductNameAndStationResponse501, Problem, str]]:
    """Returns pdf with given delayed connection. Recorded today back to 5 days ago, captured at arrival
    time for **SBB, BLS, SOB, THURBO, ZB, RegionAlps and TPF**.

    Args:
        archive_date (datetime.date):
        journey_id (str):  Example: 707_170525_8501008_0542_8506302.
        transport_product_name (str):  Example: IC 1 728.
        station_uic (int):  Example: 8507000.
        accept_language (Union[Unset,
            GetDelayConfirmationByDateAndJourneyIdAndTransportProductNameAndStationAcceptLanguage]):
            Default:
            GetDelayConfirmationByDateAndJourneyIdAndTransportProductNameAndStationAcceptLanguage.EN.
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetDelayConfirmationByDateAndJourneyIdAndTransportProductNameAndStationResponse501, Problem, str]
    """

    return sync_detailed(
        archive_date=archive_date,
        journey_id=journey_id,
        transport_product_name=transport_product_name,
        station_uic=station_uic,
        client=client,
        accept_language=accept_language,
        request_id=request_id,
    ).parsed


async def asyncio_detailed(
    archive_date: datetime.date,
    journey_id: str,
    transport_product_name: str,
    station_uic: int,
    *,
    client: AuthenticatedClient,
    accept_language: Union[
        Unset, GetDelayConfirmationByDateAndJourneyIdAndTransportProductNameAndStationAcceptLanguage
    ] = GetDelayConfirmationByDateAndJourneyIdAndTransportProductNameAndStationAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Response[Union[GetDelayConfirmationByDateAndJourneyIdAndTransportProductNameAndStationResponse501, Problem, str]]:
    """Returns pdf with given delayed connection. Recorded today back to 5 days ago, captured at arrival
    time for **SBB, BLS, SOB, THURBO, ZB, RegionAlps and TPF**.

    Args:
        archive_date (datetime.date):
        journey_id (str):  Example: 707_170525_8501008_0542_8506302.
        transport_product_name (str):  Example: IC 1 728.
        station_uic (int):  Example: 8507000.
        accept_language (Union[Unset,
            GetDelayConfirmationByDateAndJourneyIdAndTransportProductNameAndStationAcceptLanguage]):
            Default:
            GetDelayConfirmationByDateAndJourneyIdAndTransportProductNameAndStationAcceptLanguage.EN.
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetDelayConfirmationByDateAndJourneyIdAndTransportProductNameAndStationResponse501, Problem, str]]
    """

    kwargs = _get_kwargs(
        archive_date=archive_date,
        journey_id=journey_id,
        transport_product_name=transport_product_name,
        station_uic=station_uic,
        accept_language=accept_language,
        request_id=request_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    archive_date: datetime.date,
    journey_id: str,
    transport_product_name: str,
    station_uic: int,
    *,
    client: AuthenticatedClient,
    accept_language: Union[
        Unset, GetDelayConfirmationByDateAndJourneyIdAndTransportProductNameAndStationAcceptLanguage
    ] = GetDelayConfirmationByDateAndJourneyIdAndTransportProductNameAndStationAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Optional[Union[GetDelayConfirmationByDateAndJourneyIdAndTransportProductNameAndStationResponse501, Problem, str]]:
    """Returns pdf with given delayed connection. Recorded today back to 5 days ago, captured at arrival
    time for **SBB, BLS, SOB, THURBO, ZB, RegionAlps and TPF**.

    Args:
        archive_date (datetime.date):
        journey_id (str):  Example: 707_170525_8501008_0542_8506302.
        transport_product_name (str):  Example: IC 1 728.
        station_uic (int):  Example: 8507000.
        accept_language (Union[Unset,
            GetDelayConfirmationByDateAndJourneyIdAndTransportProductNameAndStationAcceptLanguage]):
            Default:
            GetDelayConfirmationByDateAndJourneyIdAndTransportProductNameAndStationAcceptLanguage.EN.
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetDelayConfirmationByDateAndJourneyIdAndTransportProductNameAndStationResponse501, Problem, str]
    """

    return (
        await asyncio_detailed(
            archive_date=archive_date,
            journey_id=journey_id,
            transport_product_name=transport_product_name,
            station_uic=station_uic,
            client=client,
            accept_language=accept_language,
            request_id=request_id,
        )
    ).parsed
