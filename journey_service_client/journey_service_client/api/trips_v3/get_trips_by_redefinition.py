from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_trips_by_redefinition_accept_language import GetTripsByRedefinitionAcceptLanguage
from ...models.problem import Problem
from ...models.trip_response import TripResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    redefined_origin: Union[Unset, None, str] = UNSET,
    redefined_destination: Union[Unset, None, str] = UNSET,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, GetTripsByRedefinitionAcceptLanguage] = GetTripsByRedefinitionAcceptLanguage.EN,
) -> Dict[str, Any]:
    headers = {}
    if not isinstance(request_id, Unset):
        headers["Request-ID"] = request_id

    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = str(accept_language)

    params: Dict[str, Any] = {}
    params["redefinedOrigin"] = redefined_origin

    params["redefinedDestination"] = redefined_destination

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/v3/INCUBATOR/trips/by-redefinition/{id}".format(
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
    id: str,
    *,
    client: AuthenticatedClient,
    redefined_origin: Union[Unset, None, str] = UNSET,
    redefined_destination: Union[Unset, None, str] = UNSET,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, GetTripsByRedefinitionAcceptLanguage] = GetTripsByRedefinitionAcceptLanguage.EN,
) -> Response[Union[Problem, TripResponse]]:
    """Split given `Trip` referenced by its `id` by redefined origin and/or destination into a partial
    (shortened) subtrip (where a typical split-point might be a `StopPlace::isTariffborder`).

     Usage: for e.g. strip-off international journey-part from trips starting or ending in Switzerland to
    get a valid NOVA ticketing offre.

    Args:
        id (str):
        redefined_origin (Union[Unset, None, str]):  Example: 8500090.
        redefined_destination (Union[Unset, None, str]):  Example: 8500010.
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetTripsByRedefinitionAcceptLanguage]):  Default:
            GetTripsByRedefinitionAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Problem, TripResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        redefined_origin=redefined_origin,
        redefined_destination=redefined_destination,
        request_id=request_id,
        accept_language=accept_language,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    redefined_origin: Union[Unset, None, str] = UNSET,
    redefined_destination: Union[Unset, None, str] = UNSET,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, GetTripsByRedefinitionAcceptLanguage] = GetTripsByRedefinitionAcceptLanguage.EN,
) -> Optional[Union[Problem, TripResponse]]:
    """Split given `Trip` referenced by its `id` by redefined origin and/or destination into a partial
    (shortened) subtrip (where a typical split-point might be a `StopPlace::isTariffborder`).

     Usage: for e.g. strip-off international journey-part from trips starting or ending in Switzerland to
    get a valid NOVA ticketing offre.

    Args:
        id (str):
        redefined_origin (Union[Unset, None, str]):  Example: 8500090.
        redefined_destination (Union[Unset, None, str]):  Example: 8500010.
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetTripsByRedefinitionAcceptLanguage]):  Default:
            GetTripsByRedefinitionAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Problem, TripResponse]
    """

    return sync_detailed(
        id=id,
        client=client,
        redefined_origin=redefined_origin,
        redefined_destination=redefined_destination,
        request_id=request_id,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    redefined_origin: Union[Unset, None, str] = UNSET,
    redefined_destination: Union[Unset, None, str] = UNSET,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, GetTripsByRedefinitionAcceptLanguage] = GetTripsByRedefinitionAcceptLanguage.EN,
) -> Response[Union[Problem, TripResponse]]:
    """Split given `Trip` referenced by its `id` by redefined origin and/or destination into a partial
    (shortened) subtrip (where a typical split-point might be a `StopPlace::isTariffborder`).

     Usage: for e.g. strip-off international journey-part from trips starting or ending in Switzerland to
    get a valid NOVA ticketing offre.

    Args:
        id (str):
        redefined_origin (Union[Unset, None, str]):  Example: 8500090.
        redefined_destination (Union[Unset, None, str]):  Example: 8500010.
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetTripsByRedefinitionAcceptLanguage]):  Default:
            GetTripsByRedefinitionAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Problem, TripResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        redefined_origin=redefined_origin,
        redefined_destination=redefined_destination,
        request_id=request_id,
        accept_language=accept_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    redefined_origin: Union[Unset, None, str] = UNSET,
    redefined_destination: Union[Unset, None, str] = UNSET,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, GetTripsByRedefinitionAcceptLanguage] = GetTripsByRedefinitionAcceptLanguage.EN,
) -> Optional[Union[Problem, TripResponse]]:
    """Split given `Trip` referenced by its `id` by redefined origin and/or destination into a partial
    (shortened) subtrip (where a typical split-point might be a `StopPlace::isTariffborder`).

     Usage: for e.g. strip-off international journey-part from trips starting or ending in Switzerland to
    get a valid NOVA ticketing offre.

    Args:
        id (str):
        redefined_origin (Union[Unset, None, str]):  Example: 8500090.
        redefined_destination (Union[Unset, None, str]):  Example: 8500010.
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetTripsByRedefinitionAcceptLanguage]):  Default:
            GetTripsByRedefinitionAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Problem, TripResponse]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            redefined_origin=redefined_origin,
            redefined_destination=redefined_destination,
            request_id=request_id,
            accept_language=accept_language,
        )
    ).parsed
