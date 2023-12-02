from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem import Problem
from ...models.trip_subscription_deletion_response import TripSubscriptionDeletionResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    subscription_id: str,
    *,
    request_id: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers = {}
    if not isinstance(request_id, Unset):
        headers["Request-ID"] = request_id

    return {
        "method": "delete",
        "url": "/v3/trips/subscriptions/{subscriptionId}".format(
            subscriptionId=subscription_id,
        ),
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Problem, TripSubscriptionDeletionResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = TripSubscriptionDeletionResponse.from_dict(response.json())

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
) -> Response[Union[Problem, TripSubscriptionDeletionResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    subscription_id: str,
    *,
    client: AuthenticatedClient,
    request_id: Union[Unset, str] = UNSET,
) -> Response[Union[Problem, TripSubscriptionDeletionResponse]]:
    """Delete a `Trip` subscription.

     Monitoring for the given subscriptionId will be terminated.

    Args:
        subscription_id (str):
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Problem, TripSubscriptionDeletionResponse]]
    """

    kwargs = _get_kwargs(
        subscription_id=subscription_id,
        request_id=request_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    subscription_id: str,
    *,
    client: AuthenticatedClient,
    request_id: Union[Unset, str] = UNSET,
) -> Optional[Union[Problem, TripSubscriptionDeletionResponse]]:
    """Delete a `Trip` subscription.

     Monitoring for the given subscriptionId will be terminated.

    Args:
        subscription_id (str):
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Problem, TripSubscriptionDeletionResponse]
    """

    return sync_detailed(
        subscription_id=subscription_id,
        client=client,
        request_id=request_id,
    ).parsed


async def asyncio_detailed(
    subscription_id: str,
    *,
    client: AuthenticatedClient,
    request_id: Union[Unset, str] = UNSET,
) -> Response[Union[Problem, TripSubscriptionDeletionResponse]]:
    """Delete a `Trip` subscription.

     Monitoring for the given subscriptionId will be terminated.

    Args:
        subscription_id (str):
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Problem, TripSubscriptionDeletionResponse]]
    """

    kwargs = _get_kwargs(
        subscription_id=subscription_id,
        request_id=request_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    subscription_id: str,
    *,
    client: AuthenticatedClient,
    request_id: Union[Unset, str] = UNSET,
) -> Optional[Union[Problem, TripSubscriptionDeletionResponse]]:
    """Delete a `Trip` subscription.

     Monitoring for the given subscriptionId will be terminated.

    Args:
        subscription_id (str):
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Problem, TripSubscriptionDeletionResponse]
    """

    return (
        await asyncio_detailed(
            subscription_id=subscription_id,
            client=client,
            request_id=request_id,
        )
    ).parsed
