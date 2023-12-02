from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.inheritance_response import InheritanceResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    request_id: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers = {}
    if not isinstance(request_id, Unset):
        headers["Request-ID"] = request_id

    return {
        "method": "get",
        "url": "/v3/INCUBATOR/openapi/dummy-patch",
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[InheritanceResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = InheritanceResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[InheritanceResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    request_id: Union[Unset, str] = UNSET,
) -> Response[InheritanceResponse]:
    """PATCH for OpenApi-Plugin-Generator (temporary).

     ApiClient **inherited sub-classes** reference.

    Args:
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InheritanceResponse]
    """

    kwargs = _get_kwargs(
        request_id=request_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    request_id: Union[Unset, str] = UNSET,
) -> Optional[InheritanceResponse]:
    """PATCH for OpenApi-Plugin-Generator (temporary).

     ApiClient **inherited sub-classes** reference.

    Args:
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InheritanceResponse
    """

    return sync_detailed(
        client=client,
        request_id=request_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    request_id: Union[Unset, str] = UNSET,
) -> Response[InheritanceResponse]:
    """PATCH for OpenApi-Plugin-Generator (temporary).

     ApiClient **inherited sub-classes** reference.

    Args:
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InheritanceResponse]
    """

    kwargs = _get_kwargs(
        request_id=request_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    request_id: Union[Unset, str] = UNSET,
) -> Optional[InheritanceResponse]:
    """PATCH for OpenApi-Plugin-Generator (temporary).

     ApiClient **inherited sub-classes** reference.

    Args:
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InheritanceResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            request_id=request_id,
        )
    ).parsed
