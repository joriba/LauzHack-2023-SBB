import datetime
from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_stop_places_accept_language import GetStopPlacesAcceptLanguage
from ...models.get_stop_places_sort_order import GetStopPlacesSortOrder
from ...models.problem import Problem
from ...models.stop_place_detailed_response import StopPlaceDetailedResponse
from ...models.vehicle_mode_enum import VehicleModeEnum
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    country_code: Union[Unset, None, str] = UNSET,
    sort_order: Union[Unset, None, GetStopPlacesSortOrder] = UNSET,
    valid_date: Union[Unset, None, datetime.date] = UNSET,
    valid_from: Union[Unset, None, datetime.date] = UNSET,
    valid_to: Union[Unset, None, datetime.date] = UNSET,
    vehicle_modes: Union[Unset, None, List[VehicleModeEnum]] = UNSET,
    name_match: Union[Unset, None, str] = UNSET,
    tariff_zone: Union[Unset, None, str] = UNSET,
    nearby: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, GetStopPlacesAcceptLanguage] = GetStopPlacesAcceptLanguage.EN,
) -> Dict[str, Any]:
    headers = {}
    if not isinstance(request_id, Unset):
        headers["Request-ID"] = request_id

    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = str(accept_language)

    params: Dict[str, Any] = {}
    params["countryCode"] = country_code

    json_sort_order: Union[Unset, None, str] = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value if sort_order else None

    params["sortOrder"] = json_sort_order

    json_valid_date: Union[Unset, None, str] = UNSET
    if not isinstance(valid_date, Unset):
        json_valid_date = valid_date.isoformat() if valid_date else None

    params["validDate"] = json_valid_date

    json_valid_from: Union[Unset, None, str] = UNSET
    if not isinstance(valid_from, Unset):
        json_valid_from = valid_from.isoformat() if valid_from else None

    params["validFrom"] = json_valid_from

    json_valid_to: Union[Unset, None, str] = UNSET
    if not isinstance(valid_to, Unset):
        json_valid_to = valid_to.isoformat() if valid_to else None

    params["validTo"] = json_valid_to

    json_vehicle_modes: Union[Unset, None, List[str]] = UNSET
    if not isinstance(vehicle_modes, Unset):
        if vehicle_modes is None:
            json_vehicle_modes = None
        else:
            json_vehicle_modes = []
            for vehicle_modes_item_data in vehicle_modes:
                vehicle_modes_item = vehicle_modes_item_data.value

                json_vehicle_modes.append(vehicle_modes_item)

    params["vehicleModes"] = json_vehicle_modes

    params["nameMatch"] = name_match

    params["tariffZone"] = tariff_zone

    params["nearby"] = nearby

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/v3/stop-places",
        "params": params,
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Problem, StopPlaceDetailedResponse]]:
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = Problem.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.OK:
        response_200 = StopPlaceDetailedResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.NOT_MODIFIED:
        response_304 = Problem.from_dict(response.json())

        return response_304
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = Problem.from_dict(response.json())

        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Problem, StopPlaceDetailedResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    country_code: Union[Unset, None, str] = UNSET,
    sort_order: Union[Unset, None, GetStopPlacesSortOrder] = UNSET,
    valid_date: Union[Unset, None, datetime.date] = UNSET,
    valid_from: Union[Unset, None, datetime.date] = UNSET,
    valid_to: Union[Unset, None, datetime.date] = UNSET,
    vehicle_modes: Union[Unset, None, List[VehicleModeEnum]] = UNSET,
    name_match: Union[Unset, None, str] = UNSET,
    tariff_zone: Union[Unset, None, str] = UNSET,
    nearby: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, GetStopPlacesAcceptLanguage] = GetStopPlacesAcceptLanguage.EN,
) -> Response[Union[Problem, StopPlaceDetailedResponse]]:
    """Get the matching `StopPlaceDetailed` (aka stations, bus stops, etc.) known resp. routed by public
    transportation.

      Provides a download of all transferable `StopPlaceDetailed` known by DiDok (UIC source) resp. INFO+
    (planned routes).<br>There are more than 65'000 such entries.<br>{To compress large responses, set
    header `accept-encoding` as `gzip`.}All Stations will be updated on a weekly base, because of rare
    changes, please do not use this service more frequently!

    Args:
        country_code (Union[Unset, None, str]):  Example: CH.
        sort_order (Union[Unset, None, GetStopPlacesSortOrder]):
        valid_date (Union[Unset, None, datetime.date]):
        valid_from (Union[Unset, None, datetime.date]):
        valid_to (Union[Unset, None, datetime.date]):
        vehicle_modes (Union[Unset, None, List[VehicleModeEnum]]):
        name_match (Union[Unset, None, str]):
        tariff_zone (Union[Unset, None, str]):
        nearby (Union[Unset, None, str]):
        limit (Union[Unset, None, int]):
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetStopPlacesAcceptLanguage]):  Default:
            GetStopPlacesAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Problem, StopPlaceDetailedResponse]]
    """

    kwargs = _get_kwargs(
        country_code=country_code,
        sort_order=sort_order,
        valid_date=valid_date,
        valid_from=valid_from,
        valid_to=valid_to,
        vehicle_modes=vehicle_modes,
        name_match=name_match,
        tariff_zone=tariff_zone,
        nearby=nearby,
        limit=limit,
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
    country_code: Union[Unset, None, str] = UNSET,
    sort_order: Union[Unset, None, GetStopPlacesSortOrder] = UNSET,
    valid_date: Union[Unset, None, datetime.date] = UNSET,
    valid_from: Union[Unset, None, datetime.date] = UNSET,
    valid_to: Union[Unset, None, datetime.date] = UNSET,
    vehicle_modes: Union[Unset, None, List[VehicleModeEnum]] = UNSET,
    name_match: Union[Unset, None, str] = UNSET,
    tariff_zone: Union[Unset, None, str] = UNSET,
    nearby: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, GetStopPlacesAcceptLanguage] = GetStopPlacesAcceptLanguage.EN,
) -> Optional[Union[Problem, StopPlaceDetailedResponse]]:
    """Get the matching `StopPlaceDetailed` (aka stations, bus stops, etc.) known resp. routed by public
    transportation.

      Provides a download of all transferable `StopPlaceDetailed` known by DiDok (UIC source) resp. INFO+
    (planned routes).<br>There are more than 65'000 such entries.<br>{To compress large responses, set
    header `accept-encoding` as `gzip`.}All Stations will be updated on a weekly base, because of rare
    changes, please do not use this service more frequently!

    Args:
        country_code (Union[Unset, None, str]):  Example: CH.
        sort_order (Union[Unset, None, GetStopPlacesSortOrder]):
        valid_date (Union[Unset, None, datetime.date]):
        valid_from (Union[Unset, None, datetime.date]):
        valid_to (Union[Unset, None, datetime.date]):
        vehicle_modes (Union[Unset, None, List[VehicleModeEnum]]):
        name_match (Union[Unset, None, str]):
        tariff_zone (Union[Unset, None, str]):
        nearby (Union[Unset, None, str]):
        limit (Union[Unset, None, int]):
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetStopPlacesAcceptLanguage]):  Default:
            GetStopPlacesAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Problem, StopPlaceDetailedResponse]
    """

    return sync_detailed(
        client=client,
        country_code=country_code,
        sort_order=sort_order,
        valid_date=valid_date,
        valid_from=valid_from,
        valid_to=valid_to,
        vehicle_modes=vehicle_modes,
        name_match=name_match,
        tariff_zone=tariff_zone,
        nearby=nearby,
        limit=limit,
        request_id=request_id,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    country_code: Union[Unset, None, str] = UNSET,
    sort_order: Union[Unset, None, GetStopPlacesSortOrder] = UNSET,
    valid_date: Union[Unset, None, datetime.date] = UNSET,
    valid_from: Union[Unset, None, datetime.date] = UNSET,
    valid_to: Union[Unset, None, datetime.date] = UNSET,
    vehicle_modes: Union[Unset, None, List[VehicleModeEnum]] = UNSET,
    name_match: Union[Unset, None, str] = UNSET,
    tariff_zone: Union[Unset, None, str] = UNSET,
    nearby: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, GetStopPlacesAcceptLanguage] = GetStopPlacesAcceptLanguage.EN,
) -> Response[Union[Problem, StopPlaceDetailedResponse]]:
    """Get the matching `StopPlaceDetailed` (aka stations, bus stops, etc.) known resp. routed by public
    transportation.

      Provides a download of all transferable `StopPlaceDetailed` known by DiDok (UIC source) resp. INFO+
    (planned routes).<br>There are more than 65'000 such entries.<br>{To compress large responses, set
    header `accept-encoding` as `gzip`.}All Stations will be updated on a weekly base, because of rare
    changes, please do not use this service more frequently!

    Args:
        country_code (Union[Unset, None, str]):  Example: CH.
        sort_order (Union[Unset, None, GetStopPlacesSortOrder]):
        valid_date (Union[Unset, None, datetime.date]):
        valid_from (Union[Unset, None, datetime.date]):
        valid_to (Union[Unset, None, datetime.date]):
        vehicle_modes (Union[Unset, None, List[VehicleModeEnum]]):
        name_match (Union[Unset, None, str]):
        tariff_zone (Union[Unset, None, str]):
        nearby (Union[Unset, None, str]):
        limit (Union[Unset, None, int]):
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetStopPlacesAcceptLanguage]):  Default:
            GetStopPlacesAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Problem, StopPlaceDetailedResponse]]
    """

    kwargs = _get_kwargs(
        country_code=country_code,
        sort_order=sort_order,
        valid_date=valid_date,
        valid_from=valid_from,
        valid_to=valid_to,
        vehicle_modes=vehicle_modes,
        name_match=name_match,
        tariff_zone=tariff_zone,
        nearby=nearby,
        limit=limit,
        request_id=request_id,
        accept_language=accept_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    country_code: Union[Unset, None, str] = UNSET,
    sort_order: Union[Unset, None, GetStopPlacesSortOrder] = UNSET,
    valid_date: Union[Unset, None, datetime.date] = UNSET,
    valid_from: Union[Unset, None, datetime.date] = UNSET,
    valid_to: Union[Unset, None, datetime.date] = UNSET,
    vehicle_modes: Union[Unset, None, List[VehicleModeEnum]] = UNSET,
    name_match: Union[Unset, None, str] = UNSET,
    tariff_zone: Union[Unset, None, str] = UNSET,
    nearby: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, GetStopPlacesAcceptLanguage] = GetStopPlacesAcceptLanguage.EN,
) -> Optional[Union[Problem, StopPlaceDetailedResponse]]:
    """Get the matching `StopPlaceDetailed` (aka stations, bus stops, etc.) known resp. routed by public
    transportation.

      Provides a download of all transferable `StopPlaceDetailed` known by DiDok (UIC source) resp. INFO+
    (planned routes).<br>There are more than 65'000 such entries.<br>{To compress large responses, set
    header `accept-encoding` as `gzip`.}All Stations will be updated on a weekly base, because of rare
    changes, please do not use this service more frequently!

    Args:
        country_code (Union[Unset, None, str]):  Example: CH.
        sort_order (Union[Unset, None, GetStopPlacesSortOrder]):
        valid_date (Union[Unset, None, datetime.date]):
        valid_from (Union[Unset, None, datetime.date]):
        valid_to (Union[Unset, None, datetime.date]):
        vehicle_modes (Union[Unset, None, List[VehicleModeEnum]]):
        name_match (Union[Unset, None, str]):
        tariff_zone (Union[Unset, None, str]):
        nearby (Union[Unset, None, str]):
        limit (Union[Unset, None, int]):
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetStopPlacesAcceptLanguage]):  Default:
            GetStopPlacesAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Problem, StopPlaceDetailedResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            country_code=country_code,
            sort_order=sort_order,
            valid_date=valid_date,
            valid_from=valid_from,
            valid_to=valid_to,
            vehicle_modes=vehicle_modes,
            name_match=name_match,
            tariff_zone=tariff_zone,
            nearby=nearby,
            limit=limit,
            request_id=request_id,
            accept_language=accept_language,
        )
    ).parsed
