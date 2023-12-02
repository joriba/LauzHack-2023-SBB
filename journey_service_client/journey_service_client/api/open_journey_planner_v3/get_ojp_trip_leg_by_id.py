import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_ojp_trip_leg_by_id_accept_language import GetOjpTripLegByIdAcceptLanguage
from ...models.problem import Problem
from ...models.trip_response import TripResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    date: datetime.date,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, GetOjpTripLegByIdAcceptLanguage] = GetOjpTripLegByIdAcceptLanguage.EN,
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
    json_date = date.isoformat()
    params["date"] = json_date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/v3/INCUBATOR/ojp/trips/by-leg/{id}".format(
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
    date: datetime.date,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, GetOjpTripLegByIdAcceptLanguage] = GetOjpTripLegByIdAcceptLanguage.EN,
    ojp_active_instance: Union[Unset, bool] = False,
    ojp_token: Union[Unset, str] = UNSET,
) -> Response[Union[Problem, TripResponse]]:
    """Get a refreshed `Leg` for a specific `PTRideLeg::serviceJourney::id` wrapped in a faked Trip.
    Supported by OJP passive instance only.

     Typically there is [1] hit but failure [0] must be expected in realtime scenarios or older data.

    Args:
        id (str):
        date (datetime.date):  Example: 2023-04-18.
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetOjpTripLegByIdAcceptLanguage]):  Default:
            GetOjpTripLegByIdAcceptLanguage.EN.
        ojp_active_instance (Union[Unset, bool]):
        ojp_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Problem, TripResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        date=date,
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
    id: str,
    *,
    client: AuthenticatedClient,
    date: datetime.date,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, GetOjpTripLegByIdAcceptLanguage] = GetOjpTripLegByIdAcceptLanguage.EN,
    ojp_active_instance: Union[Unset, bool] = False,
    ojp_token: Union[Unset, str] = UNSET,
) -> Optional[Union[Problem, TripResponse]]:
    """Get a refreshed `Leg` for a specific `PTRideLeg::serviceJourney::id` wrapped in a faked Trip.
    Supported by OJP passive instance only.

     Typically there is [1] hit but failure [0] must be expected in realtime scenarios or older data.

    Args:
        id (str):
        date (datetime.date):  Example: 2023-04-18.
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetOjpTripLegByIdAcceptLanguage]):  Default:
            GetOjpTripLegByIdAcceptLanguage.EN.
        ojp_active_instance (Union[Unset, bool]):
        ojp_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Problem, TripResponse]
    """

    return sync_detailed(
        id=id,
        client=client,
        date=date,
        request_id=request_id,
        accept_language=accept_language,
        ojp_active_instance=ojp_active_instance,
        ojp_token=ojp_token,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    date: datetime.date,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, GetOjpTripLegByIdAcceptLanguage] = GetOjpTripLegByIdAcceptLanguage.EN,
    ojp_active_instance: Union[Unset, bool] = False,
    ojp_token: Union[Unset, str] = UNSET,
) -> Response[Union[Problem, TripResponse]]:
    """Get a refreshed `Leg` for a specific `PTRideLeg::serviceJourney::id` wrapped in a faked Trip.
    Supported by OJP passive instance only.

     Typically there is [1] hit but failure [0] must be expected in realtime scenarios or older data.

    Args:
        id (str):
        date (datetime.date):  Example: 2023-04-18.
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetOjpTripLegByIdAcceptLanguage]):  Default:
            GetOjpTripLegByIdAcceptLanguage.EN.
        ojp_active_instance (Union[Unset, bool]):
        ojp_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Problem, TripResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        date=date,
        request_id=request_id,
        accept_language=accept_language,
        ojp_active_instance=ojp_active_instance,
        ojp_token=ojp_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    date: datetime.date,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, GetOjpTripLegByIdAcceptLanguage] = GetOjpTripLegByIdAcceptLanguage.EN,
    ojp_active_instance: Union[Unset, bool] = False,
    ojp_token: Union[Unset, str] = UNSET,
) -> Optional[Union[Problem, TripResponse]]:
    """Get a refreshed `Leg` for a specific `PTRideLeg::serviceJourney::id` wrapped in a faked Trip.
    Supported by OJP passive instance only.

     Typically there is [1] hit but failure [0] must be expected in realtime scenarios or older data.

    Args:
        id (str):
        date (datetime.date):  Example: 2023-04-18.
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetOjpTripLegByIdAcceptLanguage]):  Default:
            GetOjpTripLegByIdAcceptLanguage.EN.
        ojp_active_instance (Union[Unset, bool]):
        ojp_token (Union[Unset, str]):

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
            date=date,
            request_id=request_id,
            accept_language=accept_language,
            ojp_active_instance=ojp_active_instance,
            ojp_token=ojp_token,
        )
    ).parsed
