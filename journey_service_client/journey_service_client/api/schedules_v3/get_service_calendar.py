from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem import Problem
from ...models.service_calendar import ServiceCalendar
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
        "url": "/v3/service-calendar",
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Problem, ServiceCalendar]]:
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = Problem.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.OK:
        response_200 = ServiceCalendar.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.NOT_MODIFIED:
        response_304 = Problem.from_dict(response.json())

        return response_304
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = Problem.from_dict(response.json())

        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Problem, ServiceCalendar]]:
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
) -> Response[Union[Problem, ServiceCalendar]]:
    """Get current Journey Planner timetable periods supported by underlying systems (in Switzerland we
    deal with yearly operating-periods changing around 2nd Sunday of december).

     Therefore `StopPlace's`, `ServiceJourney's` and their scheduled times and service-days might change
    as well (usually having change impact for e.g. on regular commuters)!

    Args:
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Problem, ServiceCalendar]]
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
) -> Optional[Union[Problem, ServiceCalendar]]:
    """Get current Journey Planner timetable periods supported by underlying systems (in Switzerland we
    deal with yearly operating-periods changing around 2nd Sunday of december).

     Therefore `StopPlace's`, `ServiceJourney's` and their scheduled times and service-days might change
    as well (usually having change impact for e.g. on regular commuters)!

    Args:
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Problem, ServiceCalendar]
    """

    return sync_detailed(
        client=client,
        request_id=request_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    request_id: Union[Unset, str] = UNSET,
) -> Response[Union[Problem, ServiceCalendar]]:
    """Get current Journey Planner timetable periods supported by underlying systems (in Switzerland we
    deal with yearly operating-periods changing around 2nd Sunday of december).

     Therefore `StopPlace's`, `ServiceJourney's` and their scheduled times and service-days might change
    as well (usually having change impact for e.g. on regular commuters)!

    Args:
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Problem, ServiceCalendar]]
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
) -> Optional[Union[Problem, ServiceCalendar]]:
    """Get current Journey Planner timetable periods supported by underlying systems (in Switzerland we
    deal with yearly operating-periods changing around 2nd Sunday of december).

     Therefore `StopPlace's`, `ServiceJourney's` and their scheduled times and service-days might change
    as well (usually having change impact for e.g. on regular commuters)!

    Args:
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Problem, ServiceCalendar]
    """

    return (
        await asyncio_detailed(
            client=client,
            request_id=request_id,
        )
    ).parsed
