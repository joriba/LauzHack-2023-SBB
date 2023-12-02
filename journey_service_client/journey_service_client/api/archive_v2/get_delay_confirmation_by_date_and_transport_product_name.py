import datetime
from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_delay_confirmation_by_date_and_transport_product_name_accept_language import (
    GetDelayConfirmationByDateAndTransportProductNameAcceptLanguage,
)
from ...models.get_delay_confirmation_by_date_and_transport_product_name_response_501 import (
    GetDelayConfirmationByDateAndTransportProductNameResponse501,
)
from ...models.problem import Problem
from ...models.trip_v2 import TripV2
from ...types import UNSET, Response, Unset


def _get_kwargs(
    archive_date: datetime.date,
    transport_product_name: str,
    *,
    accept_language: Union[
        Unset, GetDelayConfirmationByDateAndTransportProductNameAcceptLanguage
    ] = GetDelayConfirmationByDateAndTransportProductNameAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = str(accept_language)

    if not isinstance(request_id, Unset):
        headers["Request-ID"] = request_id

    return {
        "method": "get",
        "url": "/b2c/v2/delayConfirmation/{archiveDate}/{transportProductName}".format(
            archiveDate=archive_date,
            transportProductName=transport_product_name,
        ),
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[GetDelayConfirmationByDateAndTransportProductNameResponse501, List["TripV2"], Problem]]:
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
        response_501 = GetDelayConfirmationByDateAndTransportProductNameResponse501.from_dict(response.json())

        return response_501
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[GetDelayConfirmationByDateAndTransportProductNameResponse501, List["TripV2"], Problem]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    archive_date: datetime.date,
    transport_product_name: str,
    *,
    client: AuthenticatedClient,
    accept_language: Union[
        Unset, GetDelayConfirmationByDateAndTransportProductNameAcceptLanguage
    ] = GetDelayConfirmationByDateAndTransportProductNameAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Response[Union[GetDelayConfirmationByDateAndTransportProductNameResponse501, List["TripV2"], Problem]]:
    """Returns a list with delayed connections for given train name (e.g. 'IC 728'). Recorded today back to
    5 days ago, captured at arrival time for **SBB, BLS, SOB, THURBO, ZB, RegionAlps and TPF**.

    Args:
        archive_date (datetime.date):
        transport_product_name (str):  Example: IC 1 728.
        accept_language (Union[Unset,
            GetDelayConfirmationByDateAndTransportProductNameAcceptLanguage]):  Default:
            GetDelayConfirmationByDateAndTransportProductNameAcceptLanguage.EN.
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetDelayConfirmationByDateAndTransportProductNameResponse501, List['TripV2'], Problem]]
    """

    kwargs = _get_kwargs(
        archive_date=archive_date,
        transport_product_name=transport_product_name,
        accept_language=accept_language,
        request_id=request_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    archive_date: datetime.date,
    transport_product_name: str,
    *,
    client: AuthenticatedClient,
    accept_language: Union[
        Unset, GetDelayConfirmationByDateAndTransportProductNameAcceptLanguage
    ] = GetDelayConfirmationByDateAndTransportProductNameAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Optional[Union[GetDelayConfirmationByDateAndTransportProductNameResponse501, List["TripV2"], Problem]]:
    """Returns a list with delayed connections for given train name (e.g. 'IC 728'). Recorded today back to
    5 days ago, captured at arrival time for **SBB, BLS, SOB, THURBO, ZB, RegionAlps and TPF**.

    Args:
        archive_date (datetime.date):
        transport_product_name (str):  Example: IC 1 728.
        accept_language (Union[Unset,
            GetDelayConfirmationByDateAndTransportProductNameAcceptLanguage]):  Default:
            GetDelayConfirmationByDateAndTransportProductNameAcceptLanguage.EN.
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetDelayConfirmationByDateAndTransportProductNameResponse501, List['TripV2'], Problem]
    """

    return sync_detailed(
        archive_date=archive_date,
        transport_product_name=transport_product_name,
        client=client,
        accept_language=accept_language,
        request_id=request_id,
    ).parsed


async def asyncio_detailed(
    archive_date: datetime.date,
    transport_product_name: str,
    *,
    client: AuthenticatedClient,
    accept_language: Union[
        Unset, GetDelayConfirmationByDateAndTransportProductNameAcceptLanguage
    ] = GetDelayConfirmationByDateAndTransportProductNameAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Response[Union[GetDelayConfirmationByDateAndTransportProductNameResponse501, List["TripV2"], Problem]]:
    """Returns a list with delayed connections for given train name (e.g. 'IC 728'). Recorded today back to
    5 days ago, captured at arrival time for **SBB, BLS, SOB, THURBO, ZB, RegionAlps and TPF**.

    Args:
        archive_date (datetime.date):
        transport_product_name (str):  Example: IC 1 728.
        accept_language (Union[Unset,
            GetDelayConfirmationByDateAndTransportProductNameAcceptLanguage]):  Default:
            GetDelayConfirmationByDateAndTransportProductNameAcceptLanguage.EN.
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetDelayConfirmationByDateAndTransportProductNameResponse501, List['TripV2'], Problem]]
    """

    kwargs = _get_kwargs(
        archive_date=archive_date,
        transport_product_name=transport_product_name,
        accept_language=accept_language,
        request_id=request_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    archive_date: datetime.date,
    transport_product_name: str,
    *,
    client: AuthenticatedClient,
    accept_language: Union[
        Unset, GetDelayConfirmationByDateAndTransportProductNameAcceptLanguage
    ] = GetDelayConfirmationByDateAndTransportProductNameAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Optional[Union[GetDelayConfirmationByDateAndTransportProductNameResponse501, List["TripV2"], Problem]]:
    """Returns a list with delayed connections for given train name (e.g. 'IC 728'). Recorded today back to
    5 days ago, captured at arrival time for **SBB, BLS, SOB, THURBO, ZB, RegionAlps and TPF**.

    Args:
        archive_date (datetime.date):
        transport_product_name (str):  Example: IC 1 728.
        accept_language (Union[Unset,
            GetDelayConfirmationByDateAndTransportProductNameAcceptLanguage]):  Default:
            GetDelayConfirmationByDateAndTransportProductNameAcceptLanguage.EN.
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetDelayConfirmationByDateAndTransportProductNameResponse501, List['TripV2'], Problem]
    """

    return (
        await asyncio_detailed(
            archive_date=archive_date,
            transport_product_name=transport_product_name,
            client=client,
            accept_language=accept_language,
            request_id=request_id,
        )
    ).parsed
