from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_ojp_trips_by_origin_and_destination_accept_language import (
    GetOjpTripsByOriginAndDestinationAcceptLanguage,
)
from ...models.problem import Problem
from ...models.trip_response import TripResponse
from ...models.trips_by_origin_and_destination_request_body import TripsByOriginAndDestinationRequestBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    json_body: TripsByOriginAndDestinationRequestBody,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[
        Unset, GetOjpTripsByOriginAndDestinationAcceptLanguage
    ] = GetOjpTripsByOriginAndDestinationAcceptLanguage.EN,
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

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/v3/INCUBATOR/ojp/trips/by-origin-destination",
        "json": json_json_body,
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
    *,
    client: AuthenticatedClient,
    json_body: TripsByOriginAndDestinationRequestBody,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[
        Unset, GetOjpTripsByOriginAndDestinationAcceptLanguage
    ] = GetOjpTripsByOriginAndDestinationAcceptLanguage.EN,
    ojp_active_instance: Union[Unset, bool] = False,
    ojp_token: Union[Unset, str] = UNSET,
) -> Response[Union[Problem, TripResponse]]:
    """{Idempotent: GET with body payload} Get one-way trips between given origin and destination
    locations. Each Leg is operated by a certain transport-product, therefore multiple legs means
    changing vehicles.

     The underlying public transportation planner will provide the best journey-connections according to
    your query-parameters, such as via, individual change time (ICT) etc.
    Between 0 and about 12 hits are expectable, related to realtime circumstances.

    Args:
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetOjpTripsByOriginAndDestinationAcceptLanguage]):  Default:
            GetOjpTripsByOriginAndDestinationAcceptLanguage.EN.
        ojp_active_instance (Union[Unset, bool]):
        ojp_token (Union[Unset, str]):
        json_body (TripsByOriginAndDestinationRequestBody): Request parameters (POST body). OJP
            passive instance requires Stop UIC like '850700' whereas active instance enforces
            'OJP:STOP:SBB:8507000|Bern'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Problem, TripResponse]]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
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
    json_body: TripsByOriginAndDestinationRequestBody,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[
        Unset, GetOjpTripsByOriginAndDestinationAcceptLanguage
    ] = GetOjpTripsByOriginAndDestinationAcceptLanguage.EN,
    ojp_active_instance: Union[Unset, bool] = False,
    ojp_token: Union[Unset, str] = UNSET,
) -> Optional[Union[Problem, TripResponse]]:
    """{Idempotent: GET with body payload} Get one-way trips between given origin and destination
    locations. Each Leg is operated by a certain transport-product, therefore multiple legs means
    changing vehicles.

     The underlying public transportation planner will provide the best journey-connections according to
    your query-parameters, such as via, individual change time (ICT) etc.
    Between 0 and about 12 hits are expectable, related to realtime circumstances.

    Args:
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetOjpTripsByOriginAndDestinationAcceptLanguage]):  Default:
            GetOjpTripsByOriginAndDestinationAcceptLanguage.EN.
        ojp_active_instance (Union[Unset, bool]):
        ojp_token (Union[Unset, str]):
        json_body (TripsByOriginAndDestinationRequestBody): Request parameters (POST body). OJP
            passive instance requires Stop UIC like '850700' whereas active instance enforces
            'OJP:STOP:SBB:8507000|Bern'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Problem, TripResponse]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        request_id=request_id,
        accept_language=accept_language,
        ojp_active_instance=ojp_active_instance,
        ojp_token=ojp_token,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: TripsByOriginAndDestinationRequestBody,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[
        Unset, GetOjpTripsByOriginAndDestinationAcceptLanguage
    ] = GetOjpTripsByOriginAndDestinationAcceptLanguage.EN,
    ojp_active_instance: Union[Unset, bool] = False,
    ojp_token: Union[Unset, str] = UNSET,
) -> Response[Union[Problem, TripResponse]]:
    """{Idempotent: GET with body payload} Get one-way trips between given origin and destination
    locations. Each Leg is operated by a certain transport-product, therefore multiple legs means
    changing vehicles.

     The underlying public transportation planner will provide the best journey-connections according to
    your query-parameters, such as via, individual change time (ICT) etc.
    Between 0 and about 12 hits are expectable, related to realtime circumstances.

    Args:
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetOjpTripsByOriginAndDestinationAcceptLanguage]):  Default:
            GetOjpTripsByOriginAndDestinationAcceptLanguage.EN.
        ojp_active_instance (Union[Unset, bool]):
        ojp_token (Union[Unset, str]):
        json_body (TripsByOriginAndDestinationRequestBody): Request parameters (POST body). OJP
            passive instance requires Stop UIC like '850700' whereas active instance enforces
            'OJP:STOP:SBB:8507000|Bern'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Problem, TripResponse]]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
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
    json_body: TripsByOriginAndDestinationRequestBody,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[
        Unset, GetOjpTripsByOriginAndDestinationAcceptLanguage
    ] = GetOjpTripsByOriginAndDestinationAcceptLanguage.EN,
    ojp_active_instance: Union[Unset, bool] = False,
    ojp_token: Union[Unset, str] = UNSET,
) -> Optional[Union[Problem, TripResponse]]:
    """{Idempotent: GET with body payload} Get one-way trips between given origin and destination
    locations. Each Leg is operated by a certain transport-product, therefore multiple legs means
    changing vehicles.

     The underlying public transportation planner will provide the best journey-connections according to
    your query-parameters, such as via, individual change time (ICT) etc.
    Between 0 and about 12 hits are expectable, related to realtime circumstances.

    Args:
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetOjpTripsByOriginAndDestinationAcceptLanguage]):  Default:
            GetOjpTripsByOriginAndDestinationAcceptLanguage.EN.
        ojp_active_instance (Union[Unset, bool]):
        ojp_token (Union[Unset, str]):
        json_body (TripsByOriginAndDestinationRequestBody): Request parameters (POST body). OJP
            passive instance requires Stop UIC like '850700' whereas active instance enforces
            'OJP:STOP:SBB:8507000|Bern'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Problem, TripResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            request_id=request_id,
            accept_language=accept_language,
            ojp_active_instance=ojp_active_instance,
            ojp_token=ojp_token,
        )
    ).parsed
