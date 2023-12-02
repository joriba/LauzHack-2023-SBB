import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_trips_by_reconstruction_context_accept_language import GetTripsByReconstructionContextAcceptLanguage
from ...models.get_trips_by_reconstruction_context_alternate_match import GetTripsByReconstructionContextAlternateMatch
from ...models.get_trips_by_reconstruction_context_infos import GetTripsByReconstructionContextInfos
from ...models.get_trips_by_reconstruction_context_realtime_mode import GetTripsByReconstructionContextRealtimeMode
from ...models.get_trips_by_reconstruction_context_stop_behaviour import GetTripsByReconstructionContextStopBehaviour
from ...models.json_response import JsonResponse
from ...models.problem import Problem
from ...models.trip_v2 import TripV2
from ...types import UNSET, Response, Unset


def _get_kwargs(
    reconstruction_context: str,
    *,
    alternate_match: Union[
        Unset, None, GetTripsByReconstructionContextAlternateMatch
    ] = GetTripsByReconstructionContextAlternateMatch.IRRELEVANT,
    create_summary: Union[Unset, None, bool] = False,
    date: Union[Unset, None, datetime.date] = UNSET,
    include_operating_days: Union[Unset, None, bool] = False,
    infos: Union[Unset, None, GetTripsByReconstructionContextInfos] = UNSET,
    polyline: Union[Unset, None, bool] = False,
    redefined_destination_value: Union[Unset, None, str] = UNSET,
    redefined_origin_value: Union[Unset, None, str] = UNSET,
    stop_behaviour: Union[
        Unset, None, GetTripsByReconstructionContextStopBehaviour
    ] = GetTripsByReconstructionContextStopBehaviour.ORIGIN_DESTINATION_ONLY,
    realtime_mode: Union[Unset, None, GetTripsByReconstructionContextRealtimeMode] = UNSET,
    accept_language: Union[
        Unset, GetTripsByReconstructionContextAcceptLanguage
    ] = GetTripsByReconstructionContextAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = str(accept_language)

    if not isinstance(request_id, Unset):
        headers["Request-ID"] = request_id

    params: Dict[str, Any] = {}
    json_alternate_match: Union[Unset, None, str] = UNSET
    if not isinstance(alternate_match, Unset):
        json_alternate_match = alternate_match.value if alternate_match else None

    params["alternateMatch"] = json_alternate_match

    params["createSummary"] = create_summary

    json_date: Union[Unset, None, str] = UNSET
    if not isinstance(date, Unset):
        json_date = date.isoformat() if date else None

    params["date"] = json_date

    params["includeOperatingDays"] = include_operating_days

    json_infos: Union[Unset, None, str] = UNSET
    if not isinstance(infos, Unset):
        json_infos = infos.value if infos else None

    params["infos"] = json_infos

    params["polyline"] = polyline

    params["redefinedDestinationValue"] = redefined_destination_value

    params["redefinedOriginValue"] = redefined_origin_value

    json_stop_behaviour: Union[Unset, None, str] = UNSET
    if not isinstance(stop_behaviour, Unset):
        json_stop_behaviour = stop_behaviour.value if stop_behaviour else None

    params["stopBehaviour"] = json_stop_behaviour

    json_realtime_mode: Union[Unset, None, str] = UNSET
    if not isinstance(realtime_mode, Unset):
        json_realtime_mode = realtime_mode.value if realtime_mode else None

    params["realtimeMode"] = json_realtime_mode

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/b2c/v2/trips/{reconstructionContext}".format(
            reconstructionContext=reconstruction_context,
        ),
        "params": params,
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[JsonResponse, Problem, TripV2]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = TripV2.from_dict(response.json())

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
        response_501 = JsonResponse.from_dict(response.json())

        return response_501
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[JsonResponse, Problem, TripV2]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    reconstruction_context: str,
    *,
    client: AuthenticatedClient,
    alternate_match: Union[
        Unset, None, GetTripsByReconstructionContextAlternateMatch
    ] = GetTripsByReconstructionContextAlternateMatch.IRRELEVANT,
    create_summary: Union[Unset, None, bool] = False,
    date: Union[Unset, None, datetime.date] = UNSET,
    include_operating_days: Union[Unset, None, bool] = False,
    infos: Union[Unset, None, GetTripsByReconstructionContextInfos] = UNSET,
    polyline: Union[Unset, None, bool] = False,
    redefined_destination_value: Union[Unset, None, str] = UNSET,
    redefined_origin_value: Union[Unset, None, str] = UNSET,
    stop_behaviour: Union[
        Unset, None, GetTripsByReconstructionContextStopBehaviour
    ] = GetTripsByReconstructionContextStopBehaviour.ORIGIN_DESTINATION_ONLY,
    realtime_mode: Union[Unset, None, GetTripsByReconstructionContextRealtimeMode] = UNSET,
    accept_language: Union[
        Unset, GetTripsByReconstructionContextAcceptLanguage
    ] = GetTripsByReconstructionContextAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Response[Union[JsonResponse, Problem, TripV2]]:
    """@Deprecated (SWITCH to v3/trips/{id})! Get corresponding trip for a specific
    TripV2::reconstructionContext.

     Typically there is 1 hit but failure is highly probable in realtime scenarios or older
    reconstructionContext's.

    Args:
        reconstruction_context (str):  Example: yA88CgJWMRLmBiVDMiVCNkhLSQkJ8ElUJTI0QSUgM3Mzk-
            BAE=.
        alternate_match (Union[Unset, None, GetTripsByReconstructionContextAlternateMatch]):
            Default: GetTripsByReconstructionContextAlternateMatch.IRRELEVANT.
        create_summary (Union[Unset, None, bool]):
        date (Union[Unset, None, datetime.date]):
        include_operating_days (Union[Unset, None, bool]):
        infos (Union[Unset, None, GetTripsByReconstructionContextInfos]):
        polyline (Union[Unset, None, bool]):
        redefined_destination_value (Union[Unset, None, str]):  Example: 8500010.
        redefined_origin_value (Union[Unset, None, str]):  Example: 8500090.
        stop_behaviour (Union[Unset, None, GetTripsByReconstructionContextStopBehaviour]):
            Default: GetTripsByReconstructionContextStopBehaviour.ORIGIN_DESTINATION_ONLY.
        realtime_mode (Union[Unset, None, GetTripsByReconstructionContextRealtimeMode]):
        accept_language (Union[Unset, GetTripsByReconstructionContextAcceptLanguage]):  Default:
            GetTripsByReconstructionContextAcceptLanguage.EN.
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[JsonResponse, Problem, TripV2]]
    """

    kwargs = _get_kwargs(
        reconstruction_context=reconstruction_context,
        alternate_match=alternate_match,
        create_summary=create_summary,
        date=date,
        include_operating_days=include_operating_days,
        infos=infos,
        polyline=polyline,
        redefined_destination_value=redefined_destination_value,
        redefined_origin_value=redefined_origin_value,
        stop_behaviour=stop_behaviour,
        realtime_mode=realtime_mode,
        accept_language=accept_language,
        request_id=request_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    reconstruction_context: str,
    *,
    client: AuthenticatedClient,
    alternate_match: Union[
        Unset, None, GetTripsByReconstructionContextAlternateMatch
    ] = GetTripsByReconstructionContextAlternateMatch.IRRELEVANT,
    create_summary: Union[Unset, None, bool] = False,
    date: Union[Unset, None, datetime.date] = UNSET,
    include_operating_days: Union[Unset, None, bool] = False,
    infos: Union[Unset, None, GetTripsByReconstructionContextInfos] = UNSET,
    polyline: Union[Unset, None, bool] = False,
    redefined_destination_value: Union[Unset, None, str] = UNSET,
    redefined_origin_value: Union[Unset, None, str] = UNSET,
    stop_behaviour: Union[
        Unset, None, GetTripsByReconstructionContextStopBehaviour
    ] = GetTripsByReconstructionContextStopBehaviour.ORIGIN_DESTINATION_ONLY,
    realtime_mode: Union[Unset, None, GetTripsByReconstructionContextRealtimeMode] = UNSET,
    accept_language: Union[
        Unset, GetTripsByReconstructionContextAcceptLanguage
    ] = GetTripsByReconstructionContextAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Optional[Union[JsonResponse, Problem, TripV2]]:
    """@Deprecated (SWITCH to v3/trips/{id})! Get corresponding trip for a specific
    TripV2::reconstructionContext.

     Typically there is 1 hit but failure is highly probable in realtime scenarios or older
    reconstructionContext's.

    Args:
        reconstruction_context (str):  Example: yA88CgJWMRLmBiVDMiVCNkhLSQkJ8ElUJTI0QSUgM3Mzk-
            BAE=.
        alternate_match (Union[Unset, None, GetTripsByReconstructionContextAlternateMatch]):
            Default: GetTripsByReconstructionContextAlternateMatch.IRRELEVANT.
        create_summary (Union[Unset, None, bool]):
        date (Union[Unset, None, datetime.date]):
        include_operating_days (Union[Unset, None, bool]):
        infos (Union[Unset, None, GetTripsByReconstructionContextInfos]):
        polyline (Union[Unset, None, bool]):
        redefined_destination_value (Union[Unset, None, str]):  Example: 8500010.
        redefined_origin_value (Union[Unset, None, str]):  Example: 8500090.
        stop_behaviour (Union[Unset, None, GetTripsByReconstructionContextStopBehaviour]):
            Default: GetTripsByReconstructionContextStopBehaviour.ORIGIN_DESTINATION_ONLY.
        realtime_mode (Union[Unset, None, GetTripsByReconstructionContextRealtimeMode]):
        accept_language (Union[Unset, GetTripsByReconstructionContextAcceptLanguage]):  Default:
            GetTripsByReconstructionContextAcceptLanguage.EN.
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[JsonResponse, Problem, TripV2]
    """

    return sync_detailed(
        reconstruction_context=reconstruction_context,
        client=client,
        alternate_match=alternate_match,
        create_summary=create_summary,
        date=date,
        include_operating_days=include_operating_days,
        infos=infos,
        polyline=polyline,
        redefined_destination_value=redefined_destination_value,
        redefined_origin_value=redefined_origin_value,
        stop_behaviour=stop_behaviour,
        realtime_mode=realtime_mode,
        accept_language=accept_language,
        request_id=request_id,
    ).parsed


async def asyncio_detailed(
    reconstruction_context: str,
    *,
    client: AuthenticatedClient,
    alternate_match: Union[
        Unset, None, GetTripsByReconstructionContextAlternateMatch
    ] = GetTripsByReconstructionContextAlternateMatch.IRRELEVANT,
    create_summary: Union[Unset, None, bool] = False,
    date: Union[Unset, None, datetime.date] = UNSET,
    include_operating_days: Union[Unset, None, bool] = False,
    infos: Union[Unset, None, GetTripsByReconstructionContextInfos] = UNSET,
    polyline: Union[Unset, None, bool] = False,
    redefined_destination_value: Union[Unset, None, str] = UNSET,
    redefined_origin_value: Union[Unset, None, str] = UNSET,
    stop_behaviour: Union[
        Unset, None, GetTripsByReconstructionContextStopBehaviour
    ] = GetTripsByReconstructionContextStopBehaviour.ORIGIN_DESTINATION_ONLY,
    realtime_mode: Union[Unset, None, GetTripsByReconstructionContextRealtimeMode] = UNSET,
    accept_language: Union[
        Unset, GetTripsByReconstructionContextAcceptLanguage
    ] = GetTripsByReconstructionContextAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Response[Union[JsonResponse, Problem, TripV2]]:
    """@Deprecated (SWITCH to v3/trips/{id})! Get corresponding trip for a specific
    TripV2::reconstructionContext.

     Typically there is 1 hit but failure is highly probable in realtime scenarios or older
    reconstructionContext's.

    Args:
        reconstruction_context (str):  Example: yA88CgJWMRLmBiVDMiVCNkhLSQkJ8ElUJTI0QSUgM3Mzk-
            BAE=.
        alternate_match (Union[Unset, None, GetTripsByReconstructionContextAlternateMatch]):
            Default: GetTripsByReconstructionContextAlternateMatch.IRRELEVANT.
        create_summary (Union[Unset, None, bool]):
        date (Union[Unset, None, datetime.date]):
        include_operating_days (Union[Unset, None, bool]):
        infos (Union[Unset, None, GetTripsByReconstructionContextInfos]):
        polyline (Union[Unset, None, bool]):
        redefined_destination_value (Union[Unset, None, str]):  Example: 8500010.
        redefined_origin_value (Union[Unset, None, str]):  Example: 8500090.
        stop_behaviour (Union[Unset, None, GetTripsByReconstructionContextStopBehaviour]):
            Default: GetTripsByReconstructionContextStopBehaviour.ORIGIN_DESTINATION_ONLY.
        realtime_mode (Union[Unset, None, GetTripsByReconstructionContextRealtimeMode]):
        accept_language (Union[Unset, GetTripsByReconstructionContextAcceptLanguage]):  Default:
            GetTripsByReconstructionContextAcceptLanguage.EN.
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[JsonResponse, Problem, TripV2]]
    """

    kwargs = _get_kwargs(
        reconstruction_context=reconstruction_context,
        alternate_match=alternate_match,
        create_summary=create_summary,
        date=date,
        include_operating_days=include_operating_days,
        infos=infos,
        polyline=polyline,
        redefined_destination_value=redefined_destination_value,
        redefined_origin_value=redefined_origin_value,
        stop_behaviour=stop_behaviour,
        realtime_mode=realtime_mode,
        accept_language=accept_language,
        request_id=request_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    reconstruction_context: str,
    *,
    client: AuthenticatedClient,
    alternate_match: Union[
        Unset, None, GetTripsByReconstructionContextAlternateMatch
    ] = GetTripsByReconstructionContextAlternateMatch.IRRELEVANT,
    create_summary: Union[Unset, None, bool] = False,
    date: Union[Unset, None, datetime.date] = UNSET,
    include_operating_days: Union[Unset, None, bool] = False,
    infos: Union[Unset, None, GetTripsByReconstructionContextInfos] = UNSET,
    polyline: Union[Unset, None, bool] = False,
    redefined_destination_value: Union[Unset, None, str] = UNSET,
    redefined_origin_value: Union[Unset, None, str] = UNSET,
    stop_behaviour: Union[
        Unset, None, GetTripsByReconstructionContextStopBehaviour
    ] = GetTripsByReconstructionContextStopBehaviour.ORIGIN_DESTINATION_ONLY,
    realtime_mode: Union[Unset, None, GetTripsByReconstructionContextRealtimeMode] = UNSET,
    accept_language: Union[
        Unset, GetTripsByReconstructionContextAcceptLanguage
    ] = GetTripsByReconstructionContextAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Optional[Union[JsonResponse, Problem, TripV2]]:
    """@Deprecated (SWITCH to v3/trips/{id})! Get corresponding trip for a specific
    TripV2::reconstructionContext.

     Typically there is 1 hit but failure is highly probable in realtime scenarios or older
    reconstructionContext's.

    Args:
        reconstruction_context (str):  Example: yA88CgJWMRLmBiVDMiVCNkhLSQkJ8ElUJTI0QSUgM3Mzk-
            BAE=.
        alternate_match (Union[Unset, None, GetTripsByReconstructionContextAlternateMatch]):
            Default: GetTripsByReconstructionContextAlternateMatch.IRRELEVANT.
        create_summary (Union[Unset, None, bool]):
        date (Union[Unset, None, datetime.date]):
        include_operating_days (Union[Unset, None, bool]):
        infos (Union[Unset, None, GetTripsByReconstructionContextInfos]):
        polyline (Union[Unset, None, bool]):
        redefined_destination_value (Union[Unset, None, str]):  Example: 8500010.
        redefined_origin_value (Union[Unset, None, str]):  Example: 8500090.
        stop_behaviour (Union[Unset, None, GetTripsByReconstructionContextStopBehaviour]):
            Default: GetTripsByReconstructionContextStopBehaviour.ORIGIN_DESTINATION_ONLY.
        realtime_mode (Union[Unset, None, GetTripsByReconstructionContextRealtimeMode]):
        accept_language (Union[Unset, GetTripsByReconstructionContextAcceptLanguage]):  Default:
            GetTripsByReconstructionContextAcceptLanguage.EN.
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[JsonResponse, Problem, TripV2]
    """

    return (
        await asyncio_detailed(
            reconstruction_context=reconstruction_context,
            client=client,
            alternate_match=alternate_match,
            create_summary=create_summary,
            date=date,
            include_operating_days=include_operating_days,
            infos=infos,
            polyline=polyline,
            redefined_destination_value=redefined_destination_value,
            redefined_origin_value=redefined_origin_value,
            stop_behaviour=stop_behaviour,
            realtime_mode=realtime_mode,
            accept_language=accept_language,
            request_id=request_id,
        )
    ).parsed
