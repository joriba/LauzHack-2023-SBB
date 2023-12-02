from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_trips_by_leg_accept_language import GetTripsByLegAcceptLanguage
from ...models.problem import Problem
from ...models.trip_response import TripResponse
from ...models.trips_by_leg_request_body import TripsByLegRequestBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    json_body: TripsByLegRequestBody,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, GetTripsByLegAcceptLanguage] = GetTripsByLegAcceptLanguage.EN,
) -> Dict[str, Any]:
    headers = {}
    if not isinstance(request_id, Unset):
        headers["Request-ID"] = request_id

    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = str(accept_language)

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/v3/trips/by-leg",
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
    json_body: TripsByLegRequestBody,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, GetTripsByLegAcceptLanguage] = GetTripsByLegAcceptLanguage.EN,
) -> Response[Union[Problem, TripResponse]]:
    """{Idempotent: GET with body payload} Perform a trip search starting at a position on a current
    `PTRideLeg` where a passenger is on its way on a planned Trip (aka search on trip (sot)).

     Assuming there is a known disturbance coming, this API is useful to find other Trip options to get
    to the final destination from the view of the passenger's current position.

    Args:
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetTripsByLegAcceptLanguage]):  Default:
            GetTripsByLegAcceptLanguage.EN.
        json_body (TripsByLegRequestBody): Request parameters (POST body).

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
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    json_body: TripsByLegRequestBody,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, GetTripsByLegAcceptLanguage] = GetTripsByLegAcceptLanguage.EN,
) -> Optional[Union[Problem, TripResponse]]:
    """{Idempotent: GET with body payload} Perform a trip search starting at a position on a current
    `PTRideLeg` where a passenger is on its way on a planned Trip (aka search on trip (sot)).

     Assuming there is a known disturbance coming, this API is useful to find other Trip options to get
    to the final destination from the view of the passenger's current position.

    Args:
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetTripsByLegAcceptLanguage]):  Default:
            GetTripsByLegAcceptLanguage.EN.
        json_body (TripsByLegRequestBody): Request parameters (POST body).

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
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: TripsByLegRequestBody,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, GetTripsByLegAcceptLanguage] = GetTripsByLegAcceptLanguage.EN,
) -> Response[Union[Problem, TripResponse]]:
    """{Idempotent: GET with body payload} Perform a trip search starting at a position on a current
    `PTRideLeg` where a passenger is on its way on a planned Trip (aka search on trip (sot)).

     Assuming there is a known disturbance coming, this API is useful to find other Trip options to get
    to the final destination from the view of the passenger's current position.

    Args:
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetTripsByLegAcceptLanguage]):  Default:
            GetTripsByLegAcceptLanguage.EN.
        json_body (TripsByLegRequestBody): Request parameters (POST body).

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
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: TripsByLegRequestBody,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, GetTripsByLegAcceptLanguage] = GetTripsByLegAcceptLanguage.EN,
) -> Optional[Union[Problem, TripResponse]]:
    """{Idempotent: GET with body payload} Perform a trip search starting at a position on a current
    `PTRideLeg` where a passenger is on its way on a planned Trip (aka search on trip (sot)).

     Assuming there is a known disturbance coming, this API is useful to find other Trip options to get
    to the final destination from the view of the passenger's current position.

    Args:
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetTripsByLegAcceptLanguage]):  Default:
            GetTripsByLegAcceptLanguage.EN.
        json_body (TripsByLegRequestBody): Request parameters (POST body).

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
        )
    ).parsed
