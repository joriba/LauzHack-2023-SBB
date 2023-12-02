import datetime
from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dated_vehicle_journey_response import DatedVehicleJourneyResponse
from ...models.get_dated_vehicle_journeys_by_service_accept_language import (
    GetDatedVehicleJourneysByServiceAcceptLanguage,
)
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    service_product_reference: str,
    *,
    date: Union[Unset, None, datetime.date] = UNSET,
    time: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = 1,
    operator_references: Union[Unset, None, List[str]] = UNSET,
    restrict_ch: Union[Unset, None, bool] = True,
    region_number: Union[Unset, None, str] = UNSET,
    include_exit_side: Union[Unset, None, bool] = False,
    include_intermediate_stops: Union[Unset, None, str] = "ALL",
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[
        Unset, GetDatedVehicleJourneysByServiceAcceptLanguage
    ] = GetDatedVehicleJourneysByServiceAcceptLanguage.EN,
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

    params["limit"] = limit

    json_operator_references: Union[Unset, None, List[str]] = UNSET
    if not isinstance(operator_references, Unset):
        if operator_references is None:
            json_operator_references = None
        else:
            json_operator_references = operator_references

    params["operatorReferences"] = json_operator_references

    params["restrictCH"] = restrict_ch

    params["regionNumber"] = region_number

    params["includeExitSide"] = include_exit_side

    params["includeIntermediateStops"] = include_intermediate_stops

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/v3/vehicle-journeys/by-service/{serviceProductReference}".format(
            serviceProductReference=service_product_reference,
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
    service_product_reference: str,
    *,
    client: AuthenticatedClient,
    date: Union[Unset, None, datetime.date] = UNSET,
    time: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = 1,
    operator_references: Union[Unset, None, List[str]] = UNSET,
    restrict_ch: Union[Unset, None, bool] = True,
    region_number: Union[Unset, None, str] = UNSET,
    include_exit_side: Union[Unset, None, bool] = False,
    include_intermediate_stops: Union[Unset, None, str] = "ALL",
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[
        Unset, GetDatedVehicleJourneysByServiceAcceptLanguage
    ] = GetDatedVehicleJourneysByServiceAcceptLanguage.EN,
) -> Response[Union[DatedVehicleJourneyResponse, Problem]]:
    """Get vehicle-journeys by `ServiceProduct` reference (aka train-search).

     Determines complete journey-details (aka de:Fahrt/Zuglauf) matching given parameters.

    Args:
        service_product_reference (str):
        date (Union[Unset, None, datetime.date]):
        time (Union[Unset, None, str]):  Example: 13:07.
        limit (Union[Unset, None, int]):  Default: 1.
        operator_references (Union[Unset, None, List[str]]):
        restrict_ch (Union[Unset, None, bool]):  Default: True.
        region_number (Union[Unset, None, str]):  Example: 3520.
        include_exit_side (Union[Unset, None, bool]):
        include_intermediate_stops (Union[Unset, None, str]):  Default: 'ALL'.
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetDatedVehicleJourneysByServiceAcceptLanguage]):  Default:
            GetDatedVehicleJourneysByServiceAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DatedVehicleJourneyResponse, Problem]]
    """

    kwargs = _get_kwargs(
        service_product_reference=service_product_reference,
        date=date,
        time=time,
        limit=limit,
        operator_references=operator_references,
        restrict_ch=restrict_ch,
        region_number=region_number,
        include_exit_side=include_exit_side,
        include_intermediate_stops=include_intermediate_stops,
        request_id=request_id,
        accept_language=accept_language,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    service_product_reference: str,
    *,
    client: AuthenticatedClient,
    date: Union[Unset, None, datetime.date] = UNSET,
    time: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = 1,
    operator_references: Union[Unset, None, List[str]] = UNSET,
    restrict_ch: Union[Unset, None, bool] = True,
    region_number: Union[Unset, None, str] = UNSET,
    include_exit_side: Union[Unset, None, bool] = False,
    include_intermediate_stops: Union[Unset, None, str] = "ALL",
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[
        Unset, GetDatedVehicleJourneysByServiceAcceptLanguage
    ] = GetDatedVehicleJourneysByServiceAcceptLanguage.EN,
) -> Optional[Union[DatedVehicleJourneyResponse, Problem]]:
    """Get vehicle-journeys by `ServiceProduct` reference (aka train-search).

     Determines complete journey-details (aka de:Fahrt/Zuglauf) matching given parameters.

    Args:
        service_product_reference (str):
        date (Union[Unset, None, datetime.date]):
        time (Union[Unset, None, str]):  Example: 13:07.
        limit (Union[Unset, None, int]):  Default: 1.
        operator_references (Union[Unset, None, List[str]]):
        restrict_ch (Union[Unset, None, bool]):  Default: True.
        region_number (Union[Unset, None, str]):  Example: 3520.
        include_exit_side (Union[Unset, None, bool]):
        include_intermediate_stops (Union[Unset, None, str]):  Default: 'ALL'.
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetDatedVehicleJourneysByServiceAcceptLanguage]):  Default:
            GetDatedVehicleJourneysByServiceAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DatedVehicleJourneyResponse, Problem]
    """

    return sync_detailed(
        service_product_reference=service_product_reference,
        client=client,
        date=date,
        time=time,
        limit=limit,
        operator_references=operator_references,
        restrict_ch=restrict_ch,
        region_number=region_number,
        include_exit_side=include_exit_side,
        include_intermediate_stops=include_intermediate_stops,
        request_id=request_id,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    service_product_reference: str,
    *,
    client: AuthenticatedClient,
    date: Union[Unset, None, datetime.date] = UNSET,
    time: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = 1,
    operator_references: Union[Unset, None, List[str]] = UNSET,
    restrict_ch: Union[Unset, None, bool] = True,
    region_number: Union[Unset, None, str] = UNSET,
    include_exit_side: Union[Unset, None, bool] = False,
    include_intermediate_stops: Union[Unset, None, str] = "ALL",
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[
        Unset, GetDatedVehicleJourneysByServiceAcceptLanguage
    ] = GetDatedVehicleJourneysByServiceAcceptLanguage.EN,
) -> Response[Union[DatedVehicleJourneyResponse, Problem]]:
    """Get vehicle-journeys by `ServiceProduct` reference (aka train-search).

     Determines complete journey-details (aka de:Fahrt/Zuglauf) matching given parameters.

    Args:
        service_product_reference (str):
        date (Union[Unset, None, datetime.date]):
        time (Union[Unset, None, str]):  Example: 13:07.
        limit (Union[Unset, None, int]):  Default: 1.
        operator_references (Union[Unset, None, List[str]]):
        restrict_ch (Union[Unset, None, bool]):  Default: True.
        region_number (Union[Unset, None, str]):  Example: 3520.
        include_exit_side (Union[Unset, None, bool]):
        include_intermediate_stops (Union[Unset, None, str]):  Default: 'ALL'.
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetDatedVehicleJourneysByServiceAcceptLanguage]):  Default:
            GetDatedVehicleJourneysByServiceAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DatedVehicleJourneyResponse, Problem]]
    """

    kwargs = _get_kwargs(
        service_product_reference=service_product_reference,
        date=date,
        time=time,
        limit=limit,
        operator_references=operator_references,
        restrict_ch=restrict_ch,
        region_number=region_number,
        include_exit_side=include_exit_side,
        include_intermediate_stops=include_intermediate_stops,
        request_id=request_id,
        accept_language=accept_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_product_reference: str,
    *,
    client: AuthenticatedClient,
    date: Union[Unset, None, datetime.date] = UNSET,
    time: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = 1,
    operator_references: Union[Unset, None, List[str]] = UNSET,
    restrict_ch: Union[Unset, None, bool] = True,
    region_number: Union[Unset, None, str] = UNSET,
    include_exit_side: Union[Unset, None, bool] = False,
    include_intermediate_stops: Union[Unset, None, str] = "ALL",
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[
        Unset, GetDatedVehicleJourneysByServiceAcceptLanguage
    ] = GetDatedVehicleJourneysByServiceAcceptLanguage.EN,
) -> Optional[Union[DatedVehicleJourneyResponse, Problem]]:
    """Get vehicle-journeys by `ServiceProduct` reference (aka train-search).

     Determines complete journey-details (aka de:Fahrt/Zuglauf) matching given parameters.

    Args:
        service_product_reference (str):
        date (Union[Unset, None, datetime.date]):
        time (Union[Unset, None, str]):  Example: 13:07.
        limit (Union[Unset, None, int]):  Default: 1.
        operator_references (Union[Unset, None, List[str]]):
        restrict_ch (Union[Unset, None, bool]):  Default: True.
        region_number (Union[Unset, None, str]):  Example: 3520.
        include_exit_side (Union[Unset, None, bool]):
        include_intermediate_stops (Union[Unset, None, str]):  Default: 'ALL'.
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetDatedVehicleJourneysByServiceAcceptLanguage]):  Default:
            GetDatedVehicleJourneysByServiceAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DatedVehicleJourneyResponse, Problem]
    """

    return (
        await asyncio_detailed(
            service_product_reference=service_product_reference,
            client=client,
            date=date,
            time=time,
            limit=limit,
            operator_references=operator_references,
            restrict_ch=restrict_ch,
            region_number=region_number,
            include_exit_side=include_exit_side,
            include_intermediate_stops=include_intermediate_stops,
            request_id=request_id,
            accept_language=accept_language,
        )
    ).parsed
