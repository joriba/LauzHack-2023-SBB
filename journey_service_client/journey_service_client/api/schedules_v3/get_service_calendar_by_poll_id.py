from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.service_calendar_by_origin_and_destination_download_response import (
    ServiceCalendarByOriginAndDestinationDownloadResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    poll_id: str,
    *,
    request_id: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers = {}
    if not isinstance(request_id, Unset):
        headers["Request-ID"] = request_id

    return {
        "method": "get",
        "url": "/v3/service-calendar/by-origin-destination/{pollId}".format(
            pollId=poll_id,
        ),
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ServiceCalendarByOriginAndDestinationDownloadResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ServiceCalendarByOriginAndDestinationDownloadResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ServiceCalendarByOriginAndDestinationDownloadResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    poll_id: str,
    *,
    client: AuthenticatedClient,
    request_id: Union[Unset, str] = UNSET,
) -> Response[ServiceCalendarByOriginAndDestinationDownloadResponse]:
    """Returns instruction for polling 'personal timetable (pdf)' or link to download pdf if it created
    meanwhile.

     Needs a precedent call to: v3/service-calendar/by-origin-destination

    Args:
        poll_id (str):
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServiceCalendarByOriginAndDestinationDownloadResponse]
    """

    kwargs = _get_kwargs(
        poll_id=poll_id,
        request_id=request_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    poll_id: str,
    *,
    client: AuthenticatedClient,
    request_id: Union[Unset, str] = UNSET,
) -> Optional[ServiceCalendarByOriginAndDestinationDownloadResponse]:
    """Returns instruction for polling 'personal timetable (pdf)' or link to download pdf if it created
    meanwhile.

     Needs a precedent call to: v3/service-calendar/by-origin-destination

    Args:
        poll_id (str):
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServiceCalendarByOriginAndDestinationDownloadResponse
    """

    return sync_detailed(
        poll_id=poll_id,
        client=client,
        request_id=request_id,
    ).parsed


async def asyncio_detailed(
    poll_id: str,
    *,
    client: AuthenticatedClient,
    request_id: Union[Unset, str] = UNSET,
) -> Response[ServiceCalendarByOriginAndDestinationDownloadResponse]:
    """Returns instruction for polling 'personal timetable (pdf)' or link to download pdf if it created
    meanwhile.

     Needs a precedent call to: v3/service-calendar/by-origin-destination

    Args:
        poll_id (str):
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServiceCalendarByOriginAndDestinationDownloadResponse]
    """

    kwargs = _get_kwargs(
        poll_id=poll_id,
        request_id=request_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    poll_id: str,
    *,
    client: AuthenticatedClient,
    request_id: Union[Unset, str] = UNSET,
) -> Optional[ServiceCalendarByOriginAndDestinationDownloadResponse]:
    """Returns instruction for polling 'personal timetable (pdf)' or link to download pdf if it created
    meanwhile.

     Needs a precedent call to: v3/service-calendar/by-origin-destination

    Args:
        poll_id (str):
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServiceCalendarByOriginAndDestinationDownloadResponse
    """

    return (
        await asyncio_detailed(
            poll_id=poll_id,
            client=client,
            request_id=request_id,
        )
    ).parsed
