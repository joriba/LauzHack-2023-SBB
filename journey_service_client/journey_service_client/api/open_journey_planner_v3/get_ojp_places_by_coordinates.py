from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_ojp_places_by_coordinates_accept_language import GetOjpPlacesByCoordinatesAcceptLanguage
from ...models.get_ojp_places_by_coordinates_type_item import GetOjpPlacesByCoordinatesTypeItem
from ...models.place_response import PlaceResponse
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    longitude: float,
    latitude: float,
    radius: Union[Unset, None, int] = 1000,
    limit: Union[Unset, None, int] = 10,
    type: Union[Unset, None, List[GetOjpPlacesByCoordinatesTypeItem]] = UNSET,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, GetOjpPlacesByCoordinatesAcceptLanguage] = GetOjpPlacesByCoordinatesAcceptLanguage.EN,
    ojp_active_instance: Union[Unset, bool] = False,
    ojp_token: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers = {}
    if not isinstance(request_id, Unset):
        headers["Request-ID"] = request_id

    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = str(accept_language)

    if not isinstance(ojp_active_instance, Unset):
        headers["OJP-Active-Instance"] = "true" if ojp_active_instance else "false"

    if not isinstance(ojp_token, Unset):
        headers["OJP-Token"] = ojp_token

    params: Dict[str, Any] = {}
    params["longitude"] = longitude

    params["latitude"] = latitude

    params["radius"] = radius

    params["limit"] = limit

    json_type: Union[Unset, None, List[str]] = UNSET
    if not isinstance(type, Unset):
        if type is None:
            json_type = None
        else:
            json_type = []
            for type_item_data in type:
                type_item = type_item_data.value

                json_type.append(type_item)

    params["type"] = json_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/v3/INCUBATOR/ojp/places/by-coordinates",
        "params": params,
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[PlaceResponse, Problem]]:
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = Problem.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = Problem.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.OK:
        response_200 = PlaceResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[PlaceResponse, Problem]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    longitude: float,
    latitude: float,
    radius: Union[Unset, None, int] = 1000,
    limit: Union[Unset, None, int] = 10,
    type: Union[Unset, None, List[GetOjpPlacesByCoordinatesTypeItem]] = UNSET,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, GetOjpPlacesByCoordinatesAcceptLanguage] = GetOjpPlacesByCoordinatesAcceptLanguage.EN,
    ojp_active_instance: Union[Unset, bool] = False,
    ojp_token: Union[Unset, str] = UNSET,
) -> Response[Union[PlaceResponse, Problem]]:
    """Get places nearby given coordinates by longitude/latitude.

     Gives places as a list ordered by their distance to the centre coordinates.

    Args:
        longitude (float):  Example: 8.5441.
        latitude (float):  Example: 47.4115.
        radius (Union[Unset, None, int]):  Default: 1000.
        limit (Union[Unset, None, int]):  Default: 10. Example: 10.
        type (Union[Unset, None, List[GetOjpPlacesByCoordinatesTypeItem]]):
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetOjpPlacesByCoordinatesAcceptLanguage]):  Default:
            GetOjpPlacesByCoordinatesAcceptLanguage.EN.
        ojp_active_instance (Union[Unset, bool]):
        ojp_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PlaceResponse, Problem]]
    """

    kwargs = _get_kwargs(
        longitude=longitude,
        latitude=latitude,
        radius=radius,
        limit=limit,
        type=type,
        request_id=request_id,
        accept_language=accept_language,
        ojp_active_instance=ojp_active_instance,
        ojp_token=ojp_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    longitude: float,
    latitude: float,
    radius: Union[Unset, None, int] = 1000,
    limit: Union[Unset, None, int] = 10,
    type: Union[Unset, None, List[GetOjpPlacesByCoordinatesTypeItem]] = UNSET,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, GetOjpPlacesByCoordinatesAcceptLanguage] = GetOjpPlacesByCoordinatesAcceptLanguage.EN,
    ojp_active_instance: Union[Unset, bool] = False,
    ojp_token: Union[Unset, str] = UNSET,
) -> Optional[Union[PlaceResponse, Problem]]:
    """Get places nearby given coordinates by longitude/latitude.

     Gives places as a list ordered by their distance to the centre coordinates.

    Args:
        longitude (float):  Example: 8.5441.
        latitude (float):  Example: 47.4115.
        radius (Union[Unset, None, int]):  Default: 1000.
        limit (Union[Unset, None, int]):  Default: 10. Example: 10.
        type (Union[Unset, None, List[GetOjpPlacesByCoordinatesTypeItem]]):
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetOjpPlacesByCoordinatesAcceptLanguage]):  Default:
            GetOjpPlacesByCoordinatesAcceptLanguage.EN.
        ojp_active_instance (Union[Unset, bool]):
        ojp_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PlaceResponse, Problem]
    """

    return sync_detailed(
        client=client,
        longitude=longitude,
        latitude=latitude,
        radius=radius,
        limit=limit,
        type=type,
        request_id=request_id,
        accept_language=accept_language,
        ojp_active_instance=ojp_active_instance,
        ojp_token=ojp_token,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    longitude: float,
    latitude: float,
    radius: Union[Unset, None, int] = 1000,
    limit: Union[Unset, None, int] = 10,
    type: Union[Unset, None, List[GetOjpPlacesByCoordinatesTypeItem]] = UNSET,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, GetOjpPlacesByCoordinatesAcceptLanguage] = GetOjpPlacesByCoordinatesAcceptLanguage.EN,
    ojp_active_instance: Union[Unset, bool] = False,
    ojp_token: Union[Unset, str] = UNSET,
) -> Response[Union[PlaceResponse, Problem]]:
    """Get places nearby given coordinates by longitude/latitude.

     Gives places as a list ordered by their distance to the centre coordinates.

    Args:
        longitude (float):  Example: 8.5441.
        latitude (float):  Example: 47.4115.
        radius (Union[Unset, None, int]):  Default: 1000.
        limit (Union[Unset, None, int]):  Default: 10. Example: 10.
        type (Union[Unset, None, List[GetOjpPlacesByCoordinatesTypeItem]]):
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetOjpPlacesByCoordinatesAcceptLanguage]):  Default:
            GetOjpPlacesByCoordinatesAcceptLanguage.EN.
        ojp_active_instance (Union[Unset, bool]):
        ojp_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PlaceResponse, Problem]]
    """

    kwargs = _get_kwargs(
        longitude=longitude,
        latitude=latitude,
        radius=radius,
        limit=limit,
        type=type,
        request_id=request_id,
        accept_language=accept_language,
        ojp_active_instance=ojp_active_instance,
        ojp_token=ojp_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    longitude: float,
    latitude: float,
    radius: Union[Unset, None, int] = 1000,
    limit: Union[Unset, None, int] = 10,
    type: Union[Unset, None, List[GetOjpPlacesByCoordinatesTypeItem]] = UNSET,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, GetOjpPlacesByCoordinatesAcceptLanguage] = GetOjpPlacesByCoordinatesAcceptLanguage.EN,
    ojp_active_instance: Union[Unset, bool] = False,
    ojp_token: Union[Unset, str] = UNSET,
) -> Optional[Union[PlaceResponse, Problem]]:
    """Get places nearby given coordinates by longitude/latitude.

     Gives places as a list ordered by their distance to the centre coordinates.

    Args:
        longitude (float):  Example: 8.5441.
        latitude (float):  Example: 47.4115.
        radius (Union[Unset, None, int]):  Default: 1000.
        limit (Union[Unset, None, int]):  Default: 10. Example: 10.
        type (Union[Unset, None, List[GetOjpPlacesByCoordinatesTypeItem]]):
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetOjpPlacesByCoordinatesAcceptLanguage]):  Default:
            GetOjpPlacesByCoordinatesAcceptLanguage.EN.
        ojp_active_instance (Union[Unset, bool]):
        ojp_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PlaceResponse, Problem]
    """

    return (
        await asyncio_detailed(
            client=client,
            longitude=longitude,
            latitude=latitude,
            radius=radius,
            limit=limit,
            type=type,
            request_id=request_id,
            accept_language=accept_language,
            ojp_active_instance=ojp_active_instance,
            ojp_token=ojp_token,
        )
    ).parsed
