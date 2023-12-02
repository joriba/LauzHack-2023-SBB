from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.facility_for_info_portal_response import FacilityForInfoPortalResponse
from ...models.get_facility_for_info_portal_accept_language import GetFacilityForInfoPortalAcceptLanguage
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, GetFacilityForInfoPortalAcceptLanguage] = GetFacilityForInfoPortalAcceptLanguage.EN,
) -> Dict[str, Any]:
    headers = {}
    if not isinstance(request_id, Unset):
        headers["Request-ID"] = request_id

    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = str(accept_language)

    return {
        "method": "get",
        "url": "/v3/INCUBATOR/stop-places/{id}/facility-info-portal".format(
            id=id,
        ),
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[FacilityForInfoPortalResponse, Problem]]:
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = Problem.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.OK:
        response_200 = FacilityForInfoPortalResponse.from_dict(response.json())

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
) -> Response[Union[FacilityForInfoPortalResponse, Problem]]:
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
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, GetFacilityForInfoPortalAcceptLanguage] = GetFacilityForInfoPortalAcceptLanguage.EN,
) -> Response[Union[FacilityForInfoPortalResponse, Problem]]:
    """Get the facility as for InfoPortal.

     Get the facility as for InfoPortal. Temporary solution before it goes to a PlaceService.

    Args:
        id (str):
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetFacilityForInfoPortalAcceptLanguage]):  Default:
            GetFacilityForInfoPortalAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[FacilityForInfoPortalResponse, Problem]]
    """

    kwargs = _get_kwargs(
        id=id,
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
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, GetFacilityForInfoPortalAcceptLanguage] = GetFacilityForInfoPortalAcceptLanguage.EN,
) -> Optional[Union[FacilityForInfoPortalResponse, Problem]]:
    """Get the facility as for InfoPortal.

     Get the facility as for InfoPortal. Temporary solution before it goes to a PlaceService.

    Args:
        id (str):
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetFacilityForInfoPortalAcceptLanguage]):  Default:
            GetFacilityForInfoPortalAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[FacilityForInfoPortalResponse, Problem]
    """

    return sync_detailed(
        id=id,
        client=client,
        request_id=request_id,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, GetFacilityForInfoPortalAcceptLanguage] = GetFacilityForInfoPortalAcceptLanguage.EN,
) -> Response[Union[FacilityForInfoPortalResponse, Problem]]:
    """Get the facility as for InfoPortal.

     Get the facility as for InfoPortal. Temporary solution before it goes to a PlaceService.

    Args:
        id (str):
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetFacilityForInfoPortalAcceptLanguage]):  Default:
            GetFacilityForInfoPortalAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[FacilityForInfoPortalResponse, Problem]]
    """

    kwargs = _get_kwargs(
        id=id,
        request_id=request_id,
        accept_language=accept_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, GetFacilityForInfoPortalAcceptLanguage] = GetFacilityForInfoPortalAcceptLanguage.EN,
) -> Optional[Union[FacilityForInfoPortalResponse, Problem]]:
    """Get the facility as for InfoPortal.

     Get the facility as for InfoPortal. Temporary solution before it goes to a PlaceService.

    Args:
        id (str):
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetFacilityForInfoPortalAcceptLanguage]):  Default:
            GetFacilityForInfoPortalAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[FacilityForInfoPortalResponse, Problem]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            request_id=request_id,
            accept_language=accept_language,
        )
    ).parsed
