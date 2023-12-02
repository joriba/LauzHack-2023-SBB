from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.affected_journeys_at_stop_places_request_body import AffectedJourneysAtStopPlacesRequestBody
from ...models.get_affected_journeys_at_stop_places_accept_language import GetAffectedJourneysAtStopPlacesAcceptLanguage
from ...models.problem import Problem
from ...models.service_journey_affected_response import ServiceJourneyAffectedResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    json_body: AffectedJourneysAtStopPlacesRequestBody,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[
        Unset, GetAffectedJourneysAtStopPlacesAcceptLanguage
    ] = GetAffectedJourneysAtStopPlacesAcceptLanguage.EN,
) -> Dict[str, Any]:
    headers = {}
    if not isinstance(request_id, Unset):
        headers["Request-ID"] = request_id

    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = str(accept_language)

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/v3/vehicle-journeys/affected/by-journeys-at-stopplaces",
        "json": json_json_body,
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Problem, ServiceJourneyAffectedResponse]]:
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = Problem.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.OK:
        response_200 = ServiceJourneyAffectedResponse.from_dict(response.json())

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
) -> Response[Union[Problem, ServiceJourneyAffectedResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: AffectedJourneysAtStopPlacesRequestBody,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[
        Unset, GetAffectedJourneysAtStopPlacesAcceptLanguage
    ] = GetAffectedJourneysAtStopPlacesAcceptLanguage.EN,
) -> Response[Union[Problem, ServiceJourneyAffectedResponse]]:
    """{Idempotent: GET with body payload}Get affected `ServiceJourney`'s by crossing concrete
    `StopPlace's` on matching `DatedVehicleJourney`'s.

     Specific for HIM-SX info.

    Args:
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetAffectedJourneysAtStopPlacesAcceptLanguage]):  Default:
            GetAffectedJourneysAtStopPlacesAcceptLanguage.EN.
        json_body (AffectedJourneysAtStopPlacesRequestBody): Request parameters (POST body).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Problem, ServiceJourneyAffectedResponse]]
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
    json_body: AffectedJourneysAtStopPlacesRequestBody,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[
        Unset, GetAffectedJourneysAtStopPlacesAcceptLanguage
    ] = GetAffectedJourneysAtStopPlacesAcceptLanguage.EN,
) -> Optional[Union[Problem, ServiceJourneyAffectedResponse]]:
    """{Idempotent: GET with body payload}Get affected `ServiceJourney`'s by crossing concrete
    `StopPlace's` on matching `DatedVehicleJourney`'s.

     Specific for HIM-SX info.

    Args:
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetAffectedJourneysAtStopPlacesAcceptLanguage]):  Default:
            GetAffectedJourneysAtStopPlacesAcceptLanguage.EN.
        json_body (AffectedJourneysAtStopPlacesRequestBody): Request parameters (POST body).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Problem, ServiceJourneyAffectedResponse]
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
    json_body: AffectedJourneysAtStopPlacesRequestBody,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[
        Unset, GetAffectedJourneysAtStopPlacesAcceptLanguage
    ] = GetAffectedJourneysAtStopPlacesAcceptLanguage.EN,
) -> Response[Union[Problem, ServiceJourneyAffectedResponse]]:
    """{Idempotent: GET with body payload}Get affected `ServiceJourney`'s by crossing concrete
    `StopPlace's` on matching `DatedVehicleJourney`'s.

     Specific for HIM-SX info.

    Args:
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetAffectedJourneysAtStopPlacesAcceptLanguage]):  Default:
            GetAffectedJourneysAtStopPlacesAcceptLanguage.EN.
        json_body (AffectedJourneysAtStopPlacesRequestBody): Request parameters (POST body).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Problem, ServiceJourneyAffectedResponse]]
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
    json_body: AffectedJourneysAtStopPlacesRequestBody,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[
        Unset, GetAffectedJourneysAtStopPlacesAcceptLanguage
    ] = GetAffectedJourneysAtStopPlacesAcceptLanguage.EN,
) -> Optional[Union[Problem, ServiceJourneyAffectedResponse]]:
    """{Idempotent: GET with body payload}Get affected `ServiceJourney`'s by crossing concrete
    `StopPlace's` on matching `DatedVehicleJourney`'s.

     Specific for HIM-SX info.

    Args:
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetAffectedJourneysAtStopPlacesAcceptLanguage]):  Default:
            GetAffectedJourneysAtStopPlacesAcceptLanguage.EN.
        json_body (AffectedJourneysAtStopPlacesRequestBody): Request parameters (POST body).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Problem, ServiceJourneyAffectedResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            request_id=request_id,
            accept_language=accept_language,
        )
    ).parsed
