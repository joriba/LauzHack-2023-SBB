import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_stop_place_by_id_accept_language import GetStopPlaceByIdAcceptLanguage
from ...models.problem import Problem
from ...models.stop_place_detailed import StopPlaceDetailed
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    date: Union[Unset, None, datetime.date] = UNSET,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, GetStopPlaceByIdAcceptLanguage] = GetStopPlaceByIdAcceptLanguage.EN,
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

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/v3/stop-places/{id}".format(
            id=id,
        ),
        "params": params,
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Problem, StopPlaceDetailed]]:
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = Problem.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.OK:
        response_200 = StopPlaceDetailed.from_dict(response.json())

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
) -> Response[Union[Problem, StopPlaceDetailed]]:
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
    date: Union[Unset, None, datetime.date] = UNSET,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, GetStopPlaceByIdAcceptLanguage] = GetStopPlaceByIdAcceptLanguage.EN,
) -> Response[Union[Problem, StopPlaceDetailed]]:
    """Get the `StopPlaceDetailed` (aka stations, bus stops, etc.) known resp. routed by public
    transportation.

     Get the stop place by its id. All Stations will be updated on a weekly base, because of rare
    changes, please do not use this service more frequently!

    Args:
        id (str):
        date (Union[Unset, None, datetime.date]):
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetStopPlaceByIdAcceptLanguage]):  Default:
            GetStopPlaceByIdAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Problem, StopPlaceDetailed]]
    """

    kwargs = _get_kwargs(
        id=id,
        date=date,
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
    date: Union[Unset, None, datetime.date] = UNSET,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, GetStopPlaceByIdAcceptLanguage] = GetStopPlaceByIdAcceptLanguage.EN,
) -> Optional[Union[Problem, StopPlaceDetailed]]:
    """Get the `StopPlaceDetailed` (aka stations, bus stops, etc.) known resp. routed by public
    transportation.

     Get the stop place by its id. All Stations will be updated on a weekly base, because of rare
    changes, please do not use this service more frequently!

    Args:
        id (str):
        date (Union[Unset, None, datetime.date]):
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetStopPlaceByIdAcceptLanguage]):  Default:
            GetStopPlaceByIdAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Problem, StopPlaceDetailed]
    """

    return sync_detailed(
        id=id,
        client=client,
        date=date,
        request_id=request_id,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    date: Union[Unset, None, datetime.date] = UNSET,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, GetStopPlaceByIdAcceptLanguage] = GetStopPlaceByIdAcceptLanguage.EN,
) -> Response[Union[Problem, StopPlaceDetailed]]:
    """Get the `StopPlaceDetailed` (aka stations, bus stops, etc.) known resp. routed by public
    transportation.

     Get the stop place by its id. All Stations will be updated on a weekly base, because of rare
    changes, please do not use this service more frequently!

    Args:
        id (str):
        date (Union[Unset, None, datetime.date]):
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetStopPlaceByIdAcceptLanguage]):  Default:
            GetStopPlaceByIdAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Problem, StopPlaceDetailed]]
    """

    kwargs = _get_kwargs(
        id=id,
        date=date,
        request_id=request_id,
        accept_language=accept_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    date: Union[Unset, None, datetime.date] = UNSET,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, GetStopPlaceByIdAcceptLanguage] = GetStopPlaceByIdAcceptLanguage.EN,
) -> Optional[Union[Problem, StopPlaceDetailed]]:
    """Get the `StopPlaceDetailed` (aka stations, bus stops, etc.) known resp. routed by public
    transportation.

     Get the stop place by its id. All Stations will be updated on a weekly base, because of rare
    changes, please do not use this service more frequently!

    Args:
        id (str):
        date (Union[Unset, None, datetime.date]):
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetStopPlaceByIdAcceptLanguage]):  Default:
            GetStopPlaceByIdAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Problem, StopPlaceDetailed]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            date=date,
            request_id=request_id,
            accept_language=accept_language,
        )
    ).parsed
