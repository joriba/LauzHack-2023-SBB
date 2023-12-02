import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_archived_places_by_name_accept_language import GetArchivedPlacesByNameAcceptLanguage
from ...models.place_response import PlaceResponse
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    archive_date: datetime.date,
    *,
    name_match: str,
    limit: Union[Unset, None, int] = 10,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, GetArchivedPlacesByNameAcceptLanguage] = GetArchivedPlacesByNameAcceptLanguage.EN,
) -> Dict[str, Any]:
    headers = {}
    if not isinstance(request_id, Unset):
        headers["Request-ID"] = request_id

    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = str(accept_language)

    params: Dict[str, Any] = {}
    params["nameMatch"] = name_match

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/v3/archive/{archiveDate}/places".format(
            archiveDate=archive_date,
        ),
        "params": params,
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[PlaceResponse, Problem]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PlaceResponse.from_dict(response.json())

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
) -> Response[Union[PlaceResponse, Problem]]:
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
    name_match: str,
    limit: Union[Unset, None, int] = 10,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, GetArchivedPlacesByNameAcceptLanguage] = GetArchivedPlacesByNameAcceptLanguage.EN,
) -> Response[Union[PlaceResponse, Problem]]:
    """Today and past (last 60days) realtime effective archive. Get Locations of type StopPlace by its
    name.

     The response is a flat (non-inherited) structure of concrete places.

    Args:
        archive_date (datetime.date):
        name_match (str):
        limit (Union[Unset, None, int]):  Default: 10. Example: 10.
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetArchivedPlacesByNameAcceptLanguage]):  Default:
            GetArchivedPlacesByNameAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PlaceResponse, Problem]]
    """

    kwargs = _get_kwargs(
        archive_date=archive_date,
        name_match=name_match,
        limit=limit,
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
    name_match: str,
    limit: Union[Unset, None, int] = 10,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, GetArchivedPlacesByNameAcceptLanguage] = GetArchivedPlacesByNameAcceptLanguage.EN,
) -> Optional[Union[PlaceResponse, Problem]]:
    """Today and past (last 60days) realtime effective archive. Get Locations of type StopPlace by its
    name.

     The response is a flat (non-inherited) structure of concrete places.

    Args:
        archive_date (datetime.date):
        name_match (str):
        limit (Union[Unset, None, int]):  Default: 10. Example: 10.
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetArchivedPlacesByNameAcceptLanguage]):  Default:
            GetArchivedPlacesByNameAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PlaceResponse, Problem]
    """

    return sync_detailed(
        archive_date=archive_date,
        client=client,
        name_match=name_match,
        limit=limit,
        request_id=request_id,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    archive_date: datetime.date,
    *,
    client: AuthenticatedClient,
    name_match: str,
    limit: Union[Unset, None, int] = 10,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, GetArchivedPlacesByNameAcceptLanguage] = GetArchivedPlacesByNameAcceptLanguage.EN,
) -> Response[Union[PlaceResponse, Problem]]:
    """Today and past (last 60days) realtime effective archive. Get Locations of type StopPlace by its
    name.

     The response is a flat (non-inherited) structure of concrete places.

    Args:
        archive_date (datetime.date):
        name_match (str):
        limit (Union[Unset, None, int]):  Default: 10. Example: 10.
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetArchivedPlacesByNameAcceptLanguage]):  Default:
            GetArchivedPlacesByNameAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PlaceResponse, Problem]]
    """

    kwargs = _get_kwargs(
        archive_date=archive_date,
        name_match=name_match,
        limit=limit,
        request_id=request_id,
        accept_language=accept_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    archive_date: datetime.date,
    *,
    client: AuthenticatedClient,
    name_match: str,
    limit: Union[Unset, None, int] = 10,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, GetArchivedPlacesByNameAcceptLanguage] = GetArchivedPlacesByNameAcceptLanguage.EN,
) -> Optional[Union[PlaceResponse, Problem]]:
    """Today and past (last 60days) realtime effective archive. Get Locations of type StopPlace by its
    name.

     The response is a flat (non-inherited) structure of concrete places.

    Args:
        archive_date (datetime.date):
        name_match (str):
        limit (Union[Unset, None, int]):  Default: 10. Example: 10.
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetArchivedPlacesByNameAcceptLanguage]):  Default:
            GetArchivedPlacesByNameAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PlaceResponse, Problem]
    """

    return (
        await asyncio_detailed(
            archive_date=archive_date,
            client=client,
            name_match=name_match,
            limit=limit,
            request_id=request_id,
            accept_language=accept_language,
        )
    ).parsed
