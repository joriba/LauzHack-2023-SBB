import datetime
from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.departure_v2 import DepartureV2
from ...models.get_departures_by_origin_accept_language import GetDeparturesByOriginAcceptLanguage
from ...models.get_departures_by_origin_response_501 import GetDeparturesByOriginResponse501
from ...models.get_departures_by_origin_transport_products_item import GetDeparturesByOriginTransportProductsItem
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    origin_uic: int,
    *,
    date_time: Union[Unset, None, datetime.datetime] = UNSET,
    direction_uic: Union[Unset, None, int] = UNSET,
    duration: Union[Unset, None, int] = 60,
    filter_equivalent_stops: Union[Unset, None, bool] = True,
    include_rank: Union[Unset, None, bool] = False,
    limit: Union[Unset, None, int] = 20,
    transport_products: Union[Unset, None, List[GetDeparturesByOriginTransportProductsItem]] = UNSET,
    tracks: Union[Unset, None, List[str]] = UNSET,
    accept_language: Union[Unset, GetDeparturesByOriginAcceptLanguage] = GetDeparturesByOriginAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = str(accept_language)

    if not isinstance(request_id, Unset):
        headers["Request-ID"] = request_id

    params: Dict[str, Any] = {}
    json_date_time: Union[Unset, None, str] = UNSET
    if not isinstance(date_time, Unset):
        json_date_time = date_time.isoformat() if date_time else None

    params["dateTime"] = json_date_time

    params["directionUIC"] = direction_uic

    params["duration"] = duration

    params["filterEquivalentStops"] = filter_equivalent_stops

    params["includeRank"] = include_rank

    params["limit"] = limit

    json_transport_products: Union[Unset, None, List[str]] = UNSET
    if not isinstance(transport_products, Unset):
        if transport_products is None:
            json_transport_products = None
        else:
            json_transport_products = []
            for transport_products_item_data in transport_products:
                transport_products_item = transport_products_item_data.value

                json_transport_products.append(transport_products_item)

    params["transportProducts"] = json_transport_products

    json_tracks: Union[Unset, None, List[str]] = UNSET
    if not isinstance(tracks, Unset):
        if tracks is None:
            json_tracks = None
        else:
            json_tracks = tracks

    params["tracks"] = json_tracks

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/b2c/v2/departures/{originUIC}".format(
            originUIC=origin_uic,
        ),
        "params": params,
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[GetDeparturesByOriginResponse501, List["DepartureV2"], Problem]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = DepartureV2.from_dict(response_200_item_data)

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
        response_501 = GetDeparturesByOriginResponse501.from_dict(response.json())

        return response_501
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[GetDeparturesByOriginResponse501, List["DepartureV2"], Problem]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    origin_uic: int,
    *,
    client: AuthenticatedClient,
    date_time: Union[Unset, None, datetime.datetime] = UNSET,
    direction_uic: Union[Unset, None, int] = UNSET,
    duration: Union[Unset, None, int] = 60,
    filter_equivalent_stops: Union[Unset, None, bool] = True,
    include_rank: Union[Unset, None, bool] = False,
    limit: Union[Unset, None, int] = 20,
    transport_products: Union[Unset, None, List[GetDeparturesByOriginTransportProductsItem]] = UNSET,
    tracks: Union[Unset, None, List[str]] = UNSET,
    accept_language: Union[Unset, GetDeparturesByOriginAcceptLanguage] = GetDeparturesByOriginAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Response[Union[GetDeparturesByOriginResponse501, List["DepartureV2"], Problem]]:
    """@Deprecated (SWITCH to v3/vehicle-journeys/by-departure/{origin})!<br>Get departures from a station.

     Determines next departures from a Stop and point in time within duration (the results always contain
    all departures running to the last minute found even if the requested maximum limit was overrun).

    Args:
        origin_uic (int):  Example: 8507000.
        date_time (Union[Unset, None, datetime.datetime]):  Example: 2023-04-18T14:55:00+01:00.
        direction_uic (Union[Unset, None, int]):  Example: 8503000.
        duration (Union[Unset, None, int]):  Default: 60.
        filter_equivalent_stops (Union[Unset, None, bool]):  Default: True.
        include_rank (Union[Unset, None, bool]):
        limit (Union[Unset, None, int]):  Default: 20.
        transport_products (Union[Unset, None, List[GetDeparturesByOriginTransportProductsItem]]):
        tracks (Union[Unset, None, List[str]]):
        accept_language (Union[Unset, GetDeparturesByOriginAcceptLanguage]):  Default:
            GetDeparturesByOriginAcceptLanguage.EN.
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetDeparturesByOriginResponse501, List['DepartureV2'], Problem]]
    """

    kwargs = _get_kwargs(
        origin_uic=origin_uic,
        date_time=date_time,
        direction_uic=direction_uic,
        duration=duration,
        filter_equivalent_stops=filter_equivalent_stops,
        include_rank=include_rank,
        limit=limit,
        transport_products=transport_products,
        tracks=tracks,
        accept_language=accept_language,
        request_id=request_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    origin_uic: int,
    *,
    client: AuthenticatedClient,
    date_time: Union[Unset, None, datetime.datetime] = UNSET,
    direction_uic: Union[Unset, None, int] = UNSET,
    duration: Union[Unset, None, int] = 60,
    filter_equivalent_stops: Union[Unset, None, bool] = True,
    include_rank: Union[Unset, None, bool] = False,
    limit: Union[Unset, None, int] = 20,
    transport_products: Union[Unset, None, List[GetDeparturesByOriginTransportProductsItem]] = UNSET,
    tracks: Union[Unset, None, List[str]] = UNSET,
    accept_language: Union[Unset, GetDeparturesByOriginAcceptLanguage] = GetDeparturesByOriginAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Optional[Union[GetDeparturesByOriginResponse501, List["DepartureV2"], Problem]]:
    """@Deprecated (SWITCH to v3/vehicle-journeys/by-departure/{origin})!<br>Get departures from a station.

     Determines next departures from a Stop and point in time within duration (the results always contain
    all departures running to the last minute found even if the requested maximum limit was overrun).

    Args:
        origin_uic (int):  Example: 8507000.
        date_time (Union[Unset, None, datetime.datetime]):  Example: 2023-04-18T14:55:00+01:00.
        direction_uic (Union[Unset, None, int]):  Example: 8503000.
        duration (Union[Unset, None, int]):  Default: 60.
        filter_equivalent_stops (Union[Unset, None, bool]):  Default: True.
        include_rank (Union[Unset, None, bool]):
        limit (Union[Unset, None, int]):  Default: 20.
        transport_products (Union[Unset, None, List[GetDeparturesByOriginTransportProductsItem]]):
        tracks (Union[Unset, None, List[str]]):
        accept_language (Union[Unset, GetDeparturesByOriginAcceptLanguage]):  Default:
            GetDeparturesByOriginAcceptLanguage.EN.
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetDeparturesByOriginResponse501, List['DepartureV2'], Problem]
    """

    return sync_detailed(
        origin_uic=origin_uic,
        client=client,
        date_time=date_time,
        direction_uic=direction_uic,
        duration=duration,
        filter_equivalent_stops=filter_equivalent_stops,
        include_rank=include_rank,
        limit=limit,
        transport_products=transport_products,
        tracks=tracks,
        accept_language=accept_language,
        request_id=request_id,
    ).parsed


async def asyncio_detailed(
    origin_uic: int,
    *,
    client: AuthenticatedClient,
    date_time: Union[Unset, None, datetime.datetime] = UNSET,
    direction_uic: Union[Unset, None, int] = UNSET,
    duration: Union[Unset, None, int] = 60,
    filter_equivalent_stops: Union[Unset, None, bool] = True,
    include_rank: Union[Unset, None, bool] = False,
    limit: Union[Unset, None, int] = 20,
    transport_products: Union[Unset, None, List[GetDeparturesByOriginTransportProductsItem]] = UNSET,
    tracks: Union[Unset, None, List[str]] = UNSET,
    accept_language: Union[Unset, GetDeparturesByOriginAcceptLanguage] = GetDeparturesByOriginAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Response[Union[GetDeparturesByOriginResponse501, List["DepartureV2"], Problem]]:
    """@Deprecated (SWITCH to v3/vehicle-journeys/by-departure/{origin})!<br>Get departures from a station.

     Determines next departures from a Stop and point in time within duration (the results always contain
    all departures running to the last minute found even if the requested maximum limit was overrun).

    Args:
        origin_uic (int):  Example: 8507000.
        date_time (Union[Unset, None, datetime.datetime]):  Example: 2023-04-18T14:55:00+01:00.
        direction_uic (Union[Unset, None, int]):  Example: 8503000.
        duration (Union[Unset, None, int]):  Default: 60.
        filter_equivalent_stops (Union[Unset, None, bool]):  Default: True.
        include_rank (Union[Unset, None, bool]):
        limit (Union[Unset, None, int]):  Default: 20.
        transport_products (Union[Unset, None, List[GetDeparturesByOriginTransportProductsItem]]):
        tracks (Union[Unset, None, List[str]]):
        accept_language (Union[Unset, GetDeparturesByOriginAcceptLanguage]):  Default:
            GetDeparturesByOriginAcceptLanguage.EN.
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetDeparturesByOriginResponse501, List['DepartureV2'], Problem]]
    """

    kwargs = _get_kwargs(
        origin_uic=origin_uic,
        date_time=date_time,
        direction_uic=direction_uic,
        duration=duration,
        filter_equivalent_stops=filter_equivalent_stops,
        include_rank=include_rank,
        limit=limit,
        transport_products=transport_products,
        tracks=tracks,
        accept_language=accept_language,
        request_id=request_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    origin_uic: int,
    *,
    client: AuthenticatedClient,
    date_time: Union[Unset, None, datetime.datetime] = UNSET,
    direction_uic: Union[Unset, None, int] = UNSET,
    duration: Union[Unset, None, int] = 60,
    filter_equivalent_stops: Union[Unset, None, bool] = True,
    include_rank: Union[Unset, None, bool] = False,
    limit: Union[Unset, None, int] = 20,
    transport_products: Union[Unset, None, List[GetDeparturesByOriginTransportProductsItem]] = UNSET,
    tracks: Union[Unset, None, List[str]] = UNSET,
    accept_language: Union[Unset, GetDeparturesByOriginAcceptLanguage] = GetDeparturesByOriginAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Optional[Union[GetDeparturesByOriginResponse501, List["DepartureV2"], Problem]]:
    """@Deprecated (SWITCH to v3/vehicle-journeys/by-departure/{origin})!<br>Get departures from a station.

     Determines next departures from a Stop and point in time within duration (the results always contain
    all departures running to the last minute found even if the requested maximum limit was overrun).

    Args:
        origin_uic (int):  Example: 8507000.
        date_time (Union[Unset, None, datetime.datetime]):  Example: 2023-04-18T14:55:00+01:00.
        direction_uic (Union[Unset, None, int]):  Example: 8503000.
        duration (Union[Unset, None, int]):  Default: 60.
        filter_equivalent_stops (Union[Unset, None, bool]):  Default: True.
        include_rank (Union[Unset, None, bool]):
        limit (Union[Unset, None, int]):  Default: 20.
        transport_products (Union[Unset, None, List[GetDeparturesByOriginTransportProductsItem]]):
        tracks (Union[Unset, None, List[str]]):
        accept_language (Union[Unset, GetDeparturesByOriginAcceptLanguage]):  Default:
            GetDeparturesByOriginAcceptLanguage.EN.
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetDeparturesByOriginResponse501, List['DepartureV2'], Problem]
    """

    return (
        await asyncio_detailed(
            origin_uic=origin_uic,
            client=client,
            date_time=date_time,
            direction_uic=direction_uic,
            duration=duration,
            filter_equivalent_stops=filter_equivalent_stops,
            include_rank=include_rank,
            limit=limit,
            transport_products=transport_products,
            tracks=tracks,
            accept_language=accept_language,
            request_id=request_id,
        )
    ).parsed
