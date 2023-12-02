import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_routes_by_journey_reference_accept_language import GetRoutesByJourneyReferenceAcceptLanguage
from ...models.get_routes_by_journey_reference_response_501 import GetRoutesByJourneyReferenceResponse501
from ...models.get_routes_by_journey_reference_stop_behaviour import GetRoutesByJourneyReferenceStopBehaviour
from ...models.journey_detail import JourneyDetail
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    journey_reference: str,
    *,
    accessibility: Union[Unset, None, bool] = False,
    date: Union[Unset, None, datetime.date] = UNSET,
    include_operating_days: Union[Unset, None, bool] = False,
    polyline: Union[Unset, None, bool] = False,
    stop_behaviour: Union[
        Unset, None, GetRoutesByJourneyReferenceStopBehaviour
    ] = GetRoutesByJourneyReferenceStopBehaviour.ORIGIN_DESTINATION_ONLY,
    accept_language: Union[
        Unset, GetRoutesByJourneyReferenceAcceptLanguage
    ] = GetRoutesByJourneyReferenceAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = str(accept_language)

    if not isinstance(request_id, Unset):
        headers["Request-ID"] = request_id

    params: Dict[str, Any] = {}
    params["accessibility"] = accessibility

    json_date: Union[Unset, None, str] = UNSET
    if not isinstance(date, Unset):
        json_date = date.isoformat() if date else None

    params["date"] = json_date

    params["includeOperatingDays"] = include_operating_days

    params["polyline"] = polyline

    json_stop_behaviour: Union[Unset, None, str] = UNSET
    if not isinstance(stop_behaviour, Unset):
        json_stop_behaviour = stop_behaviour.value if stop_behaviour else None

    params["stopBehaviour"] = json_stop_behaviour

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/b2c/v2/routes/{journeyReference}".format(
            journeyReference=journey_reference,
        ),
        "params": params,
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[GetRoutesByJourneyReferenceResponse501, JourneyDetail, Problem]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = JourneyDetail.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = Problem.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = Problem.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = Problem.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = Problem.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = Problem.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.NOT_IMPLEMENTED:
        response_501 = GetRoutesByJourneyReferenceResponse501.from_dict(response.json())

        return response_501
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[GetRoutesByJourneyReferenceResponse501, JourneyDetail, Problem]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    journey_reference: str,
    *,
    client: AuthenticatedClient,
    accessibility: Union[Unset, None, bool] = False,
    date: Union[Unset, None, datetime.date] = UNSET,
    include_operating_days: Union[Unset, None, bool] = False,
    polyline: Union[Unset, None, bool] = False,
    stop_behaviour: Union[
        Unset, None, GetRoutesByJourneyReferenceStopBehaviour
    ] = GetRoutesByJourneyReferenceStopBehaviour.ORIGIN_DESTINATION_ONLY,
    accept_language: Union[
        Unset, GetRoutesByJourneyReferenceAcceptLanguage
    ] = GetRoutesByJourneyReferenceAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Response[Union[GetRoutesByJourneyReferenceResponse501, JourneyDetail, Problem]]:
    """@Deprecated (SWITCH to v3/vehicle-journeys/{id})! Get complete journey of a vehicle including its
    stops (de: Zuglauf mit Haltestellen), where a `LegV2`, `DepartureV2` or `Arrival` might just
    represent a partial journey of it.

     The journey-detail will deliver information about the complete path of a vehicle (resp. transport-
    product such as train, bus,..).<br>The journey identifier is part of a trip or station-board
    response. It contains a list of all stops/stations of this journey including all departure and
    arrival times (with real-time data if available) and additional information like specific attributes
    about facilities and other texts.

    Args:
        journey_reference (str):  Example: 1|17166|0|85|18032019.
        accessibility (Union[Unset, None, bool]):
        date (Union[Unset, None, datetime.date]):
        include_operating_days (Union[Unset, None, bool]):
        polyline (Union[Unset, None, bool]):
        stop_behaviour (Union[Unset, None, GetRoutesByJourneyReferenceStopBehaviour]):  Default:
            GetRoutesByJourneyReferenceStopBehaviour.ORIGIN_DESTINATION_ONLY.
        accept_language (Union[Unset, GetRoutesByJourneyReferenceAcceptLanguage]):  Default:
            GetRoutesByJourneyReferenceAcceptLanguage.EN.
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetRoutesByJourneyReferenceResponse501, JourneyDetail, Problem]]
    """

    kwargs = _get_kwargs(
        journey_reference=journey_reference,
        accessibility=accessibility,
        date=date,
        include_operating_days=include_operating_days,
        polyline=polyline,
        stop_behaviour=stop_behaviour,
        accept_language=accept_language,
        request_id=request_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    journey_reference: str,
    *,
    client: AuthenticatedClient,
    accessibility: Union[Unset, None, bool] = False,
    date: Union[Unset, None, datetime.date] = UNSET,
    include_operating_days: Union[Unset, None, bool] = False,
    polyline: Union[Unset, None, bool] = False,
    stop_behaviour: Union[
        Unset, None, GetRoutesByJourneyReferenceStopBehaviour
    ] = GetRoutesByJourneyReferenceStopBehaviour.ORIGIN_DESTINATION_ONLY,
    accept_language: Union[
        Unset, GetRoutesByJourneyReferenceAcceptLanguage
    ] = GetRoutesByJourneyReferenceAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Optional[Union[GetRoutesByJourneyReferenceResponse501, JourneyDetail, Problem]]:
    """@Deprecated (SWITCH to v3/vehicle-journeys/{id})! Get complete journey of a vehicle including its
    stops (de: Zuglauf mit Haltestellen), where a `LegV2`, `DepartureV2` or `Arrival` might just
    represent a partial journey of it.

     The journey-detail will deliver information about the complete path of a vehicle (resp. transport-
    product such as train, bus,..).<br>The journey identifier is part of a trip or station-board
    response. It contains a list of all stops/stations of this journey including all departure and
    arrival times (with real-time data if available) and additional information like specific attributes
    about facilities and other texts.

    Args:
        journey_reference (str):  Example: 1|17166|0|85|18032019.
        accessibility (Union[Unset, None, bool]):
        date (Union[Unset, None, datetime.date]):
        include_operating_days (Union[Unset, None, bool]):
        polyline (Union[Unset, None, bool]):
        stop_behaviour (Union[Unset, None, GetRoutesByJourneyReferenceStopBehaviour]):  Default:
            GetRoutesByJourneyReferenceStopBehaviour.ORIGIN_DESTINATION_ONLY.
        accept_language (Union[Unset, GetRoutesByJourneyReferenceAcceptLanguage]):  Default:
            GetRoutesByJourneyReferenceAcceptLanguage.EN.
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetRoutesByJourneyReferenceResponse501, JourneyDetail, Problem]
    """

    return sync_detailed(
        journey_reference=journey_reference,
        client=client,
        accessibility=accessibility,
        date=date,
        include_operating_days=include_operating_days,
        polyline=polyline,
        stop_behaviour=stop_behaviour,
        accept_language=accept_language,
        request_id=request_id,
    ).parsed


async def asyncio_detailed(
    journey_reference: str,
    *,
    client: AuthenticatedClient,
    accessibility: Union[Unset, None, bool] = False,
    date: Union[Unset, None, datetime.date] = UNSET,
    include_operating_days: Union[Unset, None, bool] = False,
    polyline: Union[Unset, None, bool] = False,
    stop_behaviour: Union[
        Unset, None, GetRoutesByJourneyReferenceStopBehaviour
    ] = GetRoutesByJourneyReferenceStopBehaviour.ORIGIN_DESTINATION_ONLY,
    accept_language: Union[
        Unset, GetRoutesByJourneyReferenceAcceptLanguage
    ] = GetRoutesByJourneyReferenceAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Response[Union[GetRoutesByJourneyReferenceResponse501, JourneyDetail, Problem]]:
    """@Deprecated (SWITCH to v3/vehicle-journeys/{id})! Get complete journey of a vehicle including its
    stops (de: Zuglauf mit Haltestellen), where a `LegV2`, `DepartureV2` or `Arrival` might just
    represent a partial journey of it.

     The journey-detail will deliver information about the complete path of a vehicle (resp. transport-
    product such as train, bus,..).<br>The journey identifier is part of a trip or station-board
    response. It contains a list of all stops/stations of this journey including all departure and
    arrival times (with real-time data if available) and additional information like specific attributes
    about facilities and other texts.

    Args:
        journey_reference (str):  Example: 1|17166|0|85|18032019.
        accessibility (Union[Unset, None, bool]):
        date (Union[Unset, None, datetime.date]):
        include_operating_days (Union[Unset, None, bool]):
        polyline (Union[Unset, None, bool]):
        stop_behaviour (Union[Unset, None, GetRoutesByJourneyReferenceStopBehaviour]):  Default:
            GetRoutesByJourneyReferenceStopBehaviour.ORIGIN_DESTINATION_ONLY.
        accept_language (Union[Unset, GetRoutesByJourneyReferenceAcceptLanguage]):  Default:
            GetRoutesByJourneyReferenceAcceptLanguage.EN.
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetRoutesByJourneyReferenceResponse501, JourneyDetail, Problem]]
    """

    kwargs = _get_kwargs(
        journey_reference=journey_reference,
        accessibility=accessibility,
        date=date,
        include_operating_days=include_operating_days,
        polyline=polyline,
        stop_behaviour=stop_behaviour,
        accept_language=accept_language,
        request_id=request_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    journey_reference: str,
    *,
    client: AuthenticatedClient,
    accessibility: Union[Unset, None, bool] = False,
    date: Union[Unset, None, datetime.date] = UNSET,
    include_operating_days: Union[Unset, None, bool] = False,
    polyline: Union[Unset, None, bool] = False,
    stop_behaviour: Union[
        Unset, None, GetRoutesByJourneyReferenceStopBehaviour
    ] = GetRoutesByJourneyReferenceStopBehaviour.ORIGIN_DESTINATION_ONLY,
    accept_language: Union[
        Unset, GetRoutesByJourneyReferenceAcceptLanguage
    ] = GetRoutesByJourneyReferenceAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Optional[Union[GetRoutesByJourneyReferenceResponse501, JourneyDetail, Problem]]:
    """@Deprecated (SWITCH to v3/vehicle-journeys/{id})! Get complete journey of a vehicle including its
    stops (de: Zuglauf mit Haltestellen), where a `LegV2`, `DepartureV2` or `Arrival` might just
    represent a partial journey of it.

     The journey-detail will deliver information about the complete path of a vehicle (resp. transport-
    product such as train, bus,..).<br>The journey identifier is part of a trip or station-board
    response. It contains a list of all stops/stations of this journey including all departure and
    arrival times (with real-time data if available) and additional information like specific attributes
    about facilities and other texts.

    Args:
        journey_reference (str):  Example: 1|17166|0|85|18032019.
        accessibility (Union[Unset, None, bool]):
        date (Union[Unset, None, datetime.date]):
        include_operating_days (Union[Unset, None, bool]):
        polyline (Union[Unset, None, bool]):
        stop_behaviour (Union[Unset, None, GetRoutesByJourneyReferenceStopBehaviour]):  Default:
            GetRoutesByJourneyReferenceStopBehaviour.ORIGIN_DESTINATION_ONLY.
        accept_language (Union[Unset, GetRoutesByJourneyReferenceAcceptLanguage]):  Default:
            GetRoutesByJourneyReferenceAcceptLanguage.EN.
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetRoutesByJourneyReferenceResponse501, JourneyDetail, Problem]
    """

    return (
        await asyncio_detailed(
            journey_reference=journey_reference,
            client=client,
            accessibility=accessibility,
            date=date,
            include_operating_days=include_operating_days,
            polyline=polyline,
            stop_behaviour=stop_behaviour,
            accept_language=accept_language,
            request_id=request_id,
        )
    ).parsed
