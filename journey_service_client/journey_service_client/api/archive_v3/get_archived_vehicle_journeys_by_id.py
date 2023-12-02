import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dated_vehicle_journey import DatedVehicleJourney
from ...models.get_archived_vehicle_journeys_by_id_accept_language import GetArchivedVehicleJourneysByIdAcceptLanguage
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    archive_date: datetime.date,
    id: str,
    *,
    include_intermediate_stops: Union[Unset, None, str] = "ALL",
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[
        Unset, GetArchivedVehicleJourneysByIdAcceptLanguage
    ] = GetArchivedVehicleJourneysByIdAcceptLanguage.EN,
) -> Dict[str, Any]:
    headers = {}
    if not isinstance(request_id, Unset):
        headers["Request-ID"] = request_id

    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = str(accept_language)

    params: Dict[str, Any] = {}
    params["includeIntermediateStops"] = include_intermediate_stops

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/v3/archive/{archiveDate}/vehicle-journeys/{id}".format(
            archiveDate=archive_date,
            id=id,
        ),
        "params": params,
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[DatedVehicleJourney, Problem]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DatedVehicleJourney.from_dict(response.json())

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
) -> Response[Union[DatedVehicleJourney, Problem]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    archive_date: datetime.date,
    id: str,
    *,
    client: AuthenticatedClient,
    include_intermediate_stops: Union[Unset, None, str] = "ALL",
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[
        Unset, GetArchivedVehicleJourneysByIdAcceptLanguage
    ] = GetArchivedVehicleJourneysByIdAcceptLanguage.EN,
) -> Response[Union[DatedVehicleJourney, Problem]]:
    """Today and past (last 60days) realtime effective archive. Get complete vehicle-journey including its
    ScheduledStopPoint's (de: Zuglauf mit Haltestellen) of a specific PTRideLeg, DatedVehicleJourney,
    Departure or ArrivalV3).

     The DatedVehicleJourney will deliver information about the complete route of a vehicle (resp.
    ServiceProduct such as train, bus,..).

    Args:
        archive_date (datetime.date):
        id (str):
        include_intermediate_stops (Union[Unset, None, str]):  Default: 'ALL'.
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetArchivedVehicleJourneysByIdAcceptLanguage]):  Default:
            GetArchivedVehicleJourneysByIdAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DatedVehicleJourney, Problem]]
    """

    kwargs = _get_kwargs(
        archive_date=archive_date,
        id=id,
        include_intermediate_stops=include_intermediate_stops,
        request_id=request_id,
        accept_language=accept_language,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    archive_date: datetime.date,
    id: str,
    *,
    client: AuthenticatedClient,
    include_intermediate_stops: Union[Unset, None, str] = "ALL",
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[
        Unset, GetArchivedVehicleJourneysByIdAcceptLanguage
    ] = GetArchivedVehicleJourneysByIdAcceptLanguage.EN,
) -> Optional[Union[DatedVehicleJourney, Problem]]:
    """Today and past (last 60days) realtime effective archive. Get complete vehicle-journey including its
    ScheduledStopPoint's (de: Zuglauf mit Haltestellen) of a specific PTRideLeg, DatedVehicleJourney,
    Departure or ArrivalV3).

     The DatedVehicleJourney will deliver information about the complete route of a vehicle (resp.
    ServiceProduct such as train, bus,..).

    Args:
        archive_date (datetime.date):
        id (str):
        include_intermediate_stops (Union[Unset, None, str]):  Default: 'ALL'.
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetArchivedVehicleJourneysByIdAcceptLanguage]):  Default:
            GetArchivedVehicleJourneysByIdAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DatedVehicleJourney, Problem]
    """

    return sync_detailed(
        archive_date=archive_date,
        id=id,
        client=client,
        include_intermediate_stops=include_intermediate_stops,
        request_id=request_id,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    archive_date: datetime.date,
    id: str,
    *,
    client: AuthenticatedClient,
    include_intermediate_stops: Union[Unset, None, str] = "ALL",
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[
        Unset, GetArchivedVehicleJourneysByIdAcceptLanguage
    ] = GetArchivedVehicleJourneysByIdAcceptLanguage.EN,
) -> Response[Union[DatedVehicleJourney, Problem]]:
    """Today and past (last 60days) realtime effective archive. Get complete vehicle-journey including its
    ScheduledStopPoint's (de: Zuglauf mit Haltestellen) of a specific PTRideLeg, DatedVehicleJourney,
    Departure or ArrivalV3).

     The DatedVehicleJourney will deliver information about the complete route of a vehicle (resp.
    ServiceProduct such as train, bus,..).

    Args:
        archive_date (datetime.date):
        id (str):
        include_intermediate_stops (Union[Unset, None, str]):  Default: 'ALL'.
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetArchivedVehicleJourneysByIdAcceptLanguage]):  Default:
            GetArchivedVehicleJourneysByIdAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DatedVehicleJourney, Problem]]
    """

    kwargs = _get_kwargs(
        archive_date=archive_date,
        id=id,
        include_intermediate_stops=include_intermediate_stops,
        request_id=request_id,
        accept_language=accept_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    archive_date: datetime.date,
    id: str,
    *,
    client: AuthenticatedClient,
    include_intermediate_stops: Union[Unset, None, str] = "ALL",
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[
        Unset, GetArchivedVehicleJourneysByIdAcceptLanguage
    ] = GetArchivedVehicleJourneysByIdAcceptLanguage.EN,
) -> Optional[Union[DatedVehicleJourney, Problem]]:
    """Today and past (last 60days) realtime effective archive. Get complete vehicle-journey including its
    ScheduledStopPoint's (de: Zuglauf mit Haltestellen) of a specific PTRideLeg, DatedVehicleJourney,
    Departure or ArrivalV3).

     The DatedVehicleJourney will deliver information about the complete route of a vehicle (resp.
    ServiceProduct such as train, bus,..).

    Args:
        archive_date (datetime.date):
        id (str):
        include_intermediate_stops (Union[Unset, None, str]):  Default: 'ALL'.
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetArchivedVehicleJourneysByIdAcceptLanguage]):  Default:
            GetArchivedVehicleJourneysByIdAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DatedVehicleJourney, Problem]
    """

    return (
        await asyncio_detailed(
            archive_date=archive_date,
            id=id,
            client=client,
            include_intermediate_stops=include_intermediate_stops,
            request_id=request_id,
            accept_language=accept_language,
        )
    ).parsed
