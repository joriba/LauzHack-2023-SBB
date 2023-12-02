from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem import Problem
from ...models.trip_subscription_request_body import TripSubscriptionRequestBody
from ...models.trip_subscription_response import TripSubscriptionResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    json_body: TripSubscriptionRequestBody,
    request_id: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers = {}
    if not isinstance(request_id, Unset):
        headers["Request-ID"] = request_id

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/v3/trips/subscriptions",
        "json": json_json_body,
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Problem, TripSubscriptionResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = TripSubscriptionResponse.from_dict(response.json())

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
) -> Response[Union[Problem, TripSubscriptionResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: TripSubscriptionRequestBody,
    request_id: Union[Unset, str] = UNSET,
) -> Response[Union[Problem, TripSubscriptionResponse]]:
    """Subscribe a given `Trip::id` to be monitored for realtime changes while riding.

     **Single** (one specific `Trip` only) or **periodical** (specific `Trip` repeatedly for e.g. on a
    Monday) subscription is supported.

    Args:
        request_id (Union[Unset, str]):
        json_body (TripSubscriptionRequestBody): Request body.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Problem, TripSubscriptionResponse]]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
        request_id=request_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    json_body: TripSubscriptionRequestBody,
    request_id: Union[Unset, str] = UNSET,
) -> Optional[Union[Problem, TripSubscriptionResponse]]:
    """Subscribe a given `Trip::id` to be monitored for realtime changes while riding.

     **Single** (one specific `Trip` only) or **periodical** (specific `Trip` repeatedly for e.g. on a
    Monday) subscription is supported.

    Args:
        request_id (Union[Unset, str]):
        json_body (TripSubscriptionRequestBody): Request body.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Problem, TripSubscriptionResponse]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        request_id=request_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: TripSubscriptionRequestBody,
    request_id: Union[Unset, str] = UNSET,
) -> Response[Union[Problem, TripSubscriptionResponse]]:
    """Subscribe a given `Trip::id` to be monitored for realtime changes while riding.

     **Single** (one specific `Trip` only) or **periodical** (specific `Trip` repeatedly for e.g. on a
    Monday) subscription is supported.

    Args:
        request_id (Union[Unset, str]):
        json_body (TripSubscriptionRequestBody): Request body.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Problem, TripSubscriptionResponse]]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
        request_id=request_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: TripSubscriptionRequestBody,
    request_id: Union[Unset, str] = UNSET,
) -> Optional[Union[Problem, TripSubscriptionResponse]]:
    """Subscribe a given `Trip::id` to be monitored for realtime changes while riding.

     **Single** (one specific `Trip` only) or **periodical** (specific `Trip` repeatedly for e.g. on a
    Monday) subscription is supported.

    Args:
        request_id (Union[Unset, str]):
        json_body (TripSubscriptionRequestBody): Request body.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Problem, TripSubscriptionResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            request_id=request_id,
        )
    ).parsed
