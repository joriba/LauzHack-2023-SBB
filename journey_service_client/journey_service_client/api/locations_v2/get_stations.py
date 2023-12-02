import datetime
from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_stations_accept_language import GetStationsAcceptLanguage
from ...models.get_stations_response_501 import GetStationsResponse501
from ...models.get_stations_sort_order import GetStationsSortOrder
from ...models.get_stations_vehicle_types_item import GetStationsVehicleTypesItem
from ...models.problem import Problem
from ...models.stations_page import StationsPage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    country: Union[Unset, None, str] = UNSET,
    page_number: Union[Unset, None, int] = 0,
    page_size: Union[Unset, None, int] = UNSET,
    sort_order: Union[Unset, None, GetStationsSortOrder] = GetStationsSortOrder.NAME,
    valid_date: Union[Unset, None, datetime.date] = UNSET,
    vehicle_types: Union[Unset, None, List[GetStationsVehicleTypesItem]] = UNSET,
    accept_language: Union[Unset, GetStationsAcceptLanguage] = GetStationsAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = str(accept_language)

    if not isinstance(request_id, Unset):
        headers["Request-ID"] = request_id

    params: Dict[str, Any] = {}
    params["country"] = country

    params["pageNumber"] = page_number

    params["pageSize"] = page_size

    json_sort_order: Union[Unset, None, str] = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value if sort_order else None

    params["sortOrder"] = json_sort_order

    json_valid_date: Union[Unset, None, str] = UNSET
    if not isinstance(valid_date, Unset):
        json_valid_date = valid_date.isoformat() if valid_date else None

    params["validDate"] = json_valid_date

    json_vehicle_types: Union[Unset, None, List[str]] = UNSET
    if not isinstance(vehicle_types, Unset):
        if vehicle_types is None:
            json_vehicle_types = None
        else:
            json_vehicle_types = []
            for vehicle_types_item_data in vehicle_types:
                vehicle_types_item = vehicle_types_item_data.value

                json_vehicle_types.append(vehicle_types_item)

    params["vehicleTypes"] = json_vehicle_types

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/b2c/v2/stations",
        "params": params,
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[GetStationsResponse501, Problem, StationsPage]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = StationsPage.from_dict(response.json())

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
        response_501 = GetStationsResponse501.from_dict(response.json())

        return response_501
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[GetStationsResponse501, Problem, StationsPage]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    country: Union[Unset, None, str] = UNSET,
    page_number: Union[Unset, None, int] = 0,
    page_size: Union[Unset, None, int] = UNSET,
    sort_order: Union[Unset, None, GetStationsSortOrder] = GetStationsSortOrder.NAME,
    valid_date: Union[Unset, None, datetime.date] = UNSET,
    vehicle_types: Union[Unset, None, List[GetStationsVehicleTypesItem]] = UNSET,
    accept_language: Union[Unset, GetStationsAcceptLanguage] = GetStationsAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Response[Union[GetStationsResponse501, Problem, StationsPage]]:
    """@Deprecated (SWITCH to v3/stop-places)! Get all STATION's known resp. routed by public
    transportation.

     Provides a download of all transferable STATION's known and routed by Hafas and managed by DiDok
    (UIC source) resp. INFO+ (planned routes).
    There are more than 65'000 such STATION's, therefore a paging mechanism is provided to step through
    all potential hits.
    All Station's will be updated on a weekly base, because of rare changes, please do not use this
    service more frequently!

    Args:
        country (Union[Unset, None, str]):  Example: CH.
        page_number (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        sort_order (Union[Unset, None, GetStationsSortOrder]):  Default:
            GetStationsSortOrder.NAME.
        valid_date (Union[Unset, None, datetime.date]):
        vehicle_types (Union[Unset, None, List[GetStationsVehicleTypesItem]]):
        accept_language (Union[Unset, GetStationsAcceptLanguage]):  Default:
            GetStationsAcceptLanguage.EN.
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetStationsResponse501, Problem, StationsPage]]
    """

    kwargs = _get_kwargs(
        country=country,
        page_number=page_number,
        page_size=page_size,
        sort_order=sort_order,
        valid_date=valid_date,
        vehicle_types=vehicle_types,
        accept_language=accept_language,
        request_id=request_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    country: Union[Unset, None, str] = UNSET,
    page_number: Union[Unset, None, int] = 0,
    page_size: Union[Unset, None, int] = UNSET,
    sort_order: Union[Unset, None, GetStationsSortOrder] = GetStationsSortOrder.NAME,
    valid_date: Union[Unset, None, datetime.date] = UNSET,
    vehicle_types: Union[Unset, None, List[GetStationsVehicleTypesItem]] = UNSET,
    accept_language: Union[Unset, GetStationsAcceptLanguage] = GetStationsAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Optional[Union[GetStationsResponse501, Problem, StationsPage]]:
    """@Deprecated (SWITCH to v3/stop-places)! Get all STATION's known resp. routed by public
    transportation.

     Provides a download of all transferable STATION's known and routed by Hafas and managed by DiDok
    (UIC source) resp. INFO+ (planned routes).
    There are more than 65'000 such STATION's, therefore a paging mechanism is provided to step through
    all potential hits.
    All Station's will be updated on a weekly base, because of rare changes, please do not use this
    service more frequently!

    Args:
        country (Union[Unset, None, str]):  Example: CH.
        page_number (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        sort_order (Union[Unset, None, GetStationsSortOrder]):  Default:
            GetStationsSortOrder.NAME.
        valid_date (Union[Unset, None, datetime.date]):
        vehicle_types (Union[Unset, None, List[GetStationsVehicleTypesItem]]):
        accept_language (Union[Unset, GetStationsAcceptLanguage]):  Default:
            GetStationsAcceptLanguage.EN.
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetStationsResponse501, Problem, StationsPage]
    """

    return sync_detailed(
        client=client,
        country=country,
        page_number=page_number,
        page_size=page_size,
        sort_order=sort_order,
        valid_date=valid_date,
        vehicle_types=vehicle_types,
        accept_language=accept_language,
        request_id=request_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    country: Union[Unset, None, str] = UNSET,
    page_number: Union[Unset, None, int] = 0,
    page_size: Union[Unset, None, int] = UNSET,
    sort_order: Union[Unset, None, GetStationsSortOrder] = GetStationsSortOrder.NAME,
    valid_date: Union[Unset, None, datetime.date] = UNSET,
    vehicle_types: Union[Unset, None, List[GetStationsVehicleTypesItem]] = UNSET,
    accept_language: Union[Unset, GetStationsAcceptLanguage] = GetStationsAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Response[Union[GetStationsResponse501, Problem, StationsPage]]:
    """@Deprecated (SWITCH to v3/stop-places)! Get all STATION's known resp. routed by public
    transportation.

     Provides a download of all transferable STATION's known and routed by Hafas and managed by DiDok
    (UIC source) resp. INFO+ (planned routes).
    There are more than 65'000 such STATION's, therefore a paging mechanism is provided to step through
    all potential hits.
    All Station's will be updated on a weekly base, because of rare changes, please do not use this
    service more frequently!

    Args:
        country (Union[Unset, None, str]):  Example: CH.
        page_number (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        sort_order (Union[Unset, None, GetStationsSortOrder]):  Default:
            GetStationsSortOrder.NAME.
        valid_date (Union[Unset, None, datetime.date]):
        vehicle_types (Union[Unset, None, List[GetStationsVehicleTypesItem]]):
        accept_language (Union[Unset, GetStationsAcceptLanguage]):  Default:
            GetStationsAcceptLanguage.EN.
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetStationsResponse501, Problem, StationsPage]]
    """

    kwargs = _get_kwargs(
        country=country,
        page_number=page_number,
        page_size=page_size,
        sort_order=sort_order,
        valid_date=valid_date,
        vehicle_types=vehicle_types,
        accept_language=accept_language,
        request_id=request_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    country: Union[Unset, None, str] = UNSET,
    page_number: Union[Unset, None, int] = 0,
    page_size: Union[Unset, None, int] = UNSET,
    sort_order: Union[Unset, None, GetStationsSortOrder] = GetStationsSortOrder.NAME,
    valid_date: Union[Unset, None, datetime.date] = UNSET,
    vehicle_types: Union[Unset, None, List[GetStationsVehicleTypesItem]] = UNSET,
    accept_language: Union[Unset, GetStationsAcceptLanguage] = GetStationsAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Optional[Union[GetStationsResponse501, Problem, StationsPage]]:
    """@Deprecated (SWITCH to v3/stop-places)! Get all STATION's known resp. routed by public
    transportation.

     Provides a download of all transferable STATION's known and routed by Hafas and managed by DiDok
    (UIC source) resp. INFO+ (planned routes).
    There are more than 65'000 such STATION's, therefore a paging mechanism is provided to step through
    all potential hits.
    All Station's will be updated on a weekly base, because of rare changes, please do not use this
    service more frequently!

    Args:
        country (Union[Unset, None, str]):  Example: CH.
        page_number (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        sort_order (Union[Unset, None, GetStationsSortOrder]):  Default:
            GetStationsSortOrder.NAME.
        valid_date (Union[Unset, None, datetime.date]):
        vehicle_types (Union[Unset, None, List[GetStationsVehicleTypesItem]]):
        accept_language (Union[Unset, GetStationsAcceptLanguage]):  Default:
            GetStationsAcceptLanguage.EN.
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetStationsResponse501, Problem, StationsPage]
    """

    return (
        await asyncio_detailed(
            client=client,
            country=country,
            page_number=page_number,
            page_size=page_size,
            sort_order=sort_order,
            valid_date=valid_date,
            vehicle_types=vehicle_types,
            accept_language=accept_language,
            request_id=request_id,
        )
    ).parsed
