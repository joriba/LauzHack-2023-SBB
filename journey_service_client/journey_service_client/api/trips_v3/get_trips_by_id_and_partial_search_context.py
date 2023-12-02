from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.alternate_match_enum import AlternateMatchEnum
from ...models.get_trips_by_id_and_partial_search_context_accept_language import (
    GetTripsByIdAndPartialSearchContextAcceptLanguage,
)
from ...models.problem import Problem
from ...models.trip_response import TripResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    via_earlier_later_context: str,
    *,
    additional_transfer_time: Union[Unset, None, int] = 0,
    include_alternate_match: Union[Unset, None, AlternateMatchEnum] = AlternateMatchEnum.IRRELEVANT,
    include_route_projection: Union[Unset, None, bool] = False,
    include_summary: Union[Unset, None, bool] = False,
    include_intermediate_stops: Union[Unset, None, str] = "ALL",
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[
        Unset, GetTripsByIdAndPartialSearchContextAcceptLanguage
    ] = GetTripsByIdAndPartialSearchContextAcceptLanguage.EN,
) -> Dict[str, Any]:
    headers = {}
    if not isinstance(request_id, Unset):
        headers["Request-ID"] = request_id

    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = str(accept_language)

    params: Dict[str, Any] = {}
    params["additionalTransferTime"] = additional_transfer_time

    json_include_alternate_match: Union[Unset, None, str] = UNSET
    if not isinstance(include_alternate_match, Unset):
        json_include_alternate_match = include_alternate_match.value if include_alternate_match else None

    params["includeAlternateMatch"] = json_include_alternate_match

    params["includeRouteProjection"] = include_route_projection

    params["includeSummary"] = include_summary

    params["includeIntermediateStops"] = include_intermediate_stops

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/v3/trips/{id}/{viaEarlierLaterContext}".format(
            id=id,
            viaEarlierLaterContext=via_earlier_later_context,
        ),
        "params": params,
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Problem, TripResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = TripResponse.from_dict(response.json())

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
) -> Response[Union[Problem, TripResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    via_earlier_later_context: str,
    *,
    client: AuthenticatedClient,
    additional_transfer_time: Union[Unset, None, int] = 0,
    include_alternate_match: Union[Unset, None, AlternateMatchEnum] = AlternateMatchEnum.IRRELEVANT,
    include_route_projection: Union[Unset, None, bool] = False,
    include_summary: Union[Unset, None, bool] = False,
    include_intermediate_stops: Union[Unset, None, str] = "ALL",
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[
        Unset, GetTripsByIdAndPartialSearchContextAcceptLanguage
    ] = GetTripsByIdAndPartialSearchContextAcceptLanguage.EN,
) -> Response[Union[Problem, TripResponse]]:
    """Get a `Trip` [0..1] with changed arrival/departure times at a concrete via on a given `Trip::id`
    (aka partialTripSearch).

     Useful to find a slightly different trip with earlier arrival or later departure for a desired Via.
    Trip-pagination cannot be provided in this case.

    Args:
        id (str):  Example: yA88CgJWMRLmBiVDMiVCNkhLSQkJ8ElUJTI0QSUgM3Mzk-BAE=.
        via_earlier_later_context (str):  Example:
            PS=F$T=151200$L=A=1@O=Olten@X=7907703@Y=47351938@U=85@L=8500218@$.
        additional_transfer_time (Union[Unset, None, int]):
        include_alternate_match (Union[Unset, None, AlternateMatchEnum]): Post-filter to adjust
            cancelled/alternate 1:1 Trip cases per response (de:Ausfall/Ersatz) according to SBB BR,
            where other Trip's remain as is.<br>x-extensible-enum:
            - IRRELEVANT: no adaption
            - BOTH: as IRRELEVANT but some Note's will be cloned from cancelled to 1:1 alternate Trip
            - ALTERNATE_ONLY: suppresses cancelled 1:1 Trip's if matched with alternates
            - CANCELLED_ONLY: suppress exactly matching 1:1 alternates Default:
            AlternateMatchEnum.IRRELEVANT.
        include_route_projection (Union[Unset, None, bool]):
        include_summary (Union[Unset, None, bool]):
        include_intermediate_stops (Union[Unset, None, str]):  Default: 'ALL'.
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetTripsByIdAndPartialSearchContextAcceptLanguage]):
            Default: GetTripsByIdAndPartialSearchContextAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Problem, TripResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        via_earlier_later_context=via_earlier_later_context,
        additional_transfer_time=additional_transfer_time,
        include_alternate_match=include_alternate_match,
        include_route_projection=include_route_projection,
        include_summary=include_summary,
        include_intermediate_stops=include_intermediate_stops,
        request_id=request_id,
        accept_language=accept_language,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    via_earlier_later_context: str,
    *,
    client: AuthenticatedClient,
    additional_transfer_time: Union[Unset, None, int] = 0,
    include_alternate_match: Union[Unset, None, AlternateMatchEnum] = AlternateMatchEnum.IRRELEVANT,
    include_route_projection: Union[Unset, None, bool] = False,
    include_summary: Union[Unset, None, bool] = False,
    include_intermediate_stops: Union[Unset, None, str] = "ALL",
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[
        Unset, GetTripsByIdAndPartialSearchContextAcceptLanguage
    ] = GetTripsByIdAndPartialSearchContextAcceptLanguage.EN,
) -> Optional[Union[Problem, TripResponse]]:
    """Get a `Trip` [0..1] with changed arrival/departure times at a concrete via on a given `Trip::id`
    (aka partialTripSearch).

     Useful to find a slightly different trip with earlier arrival or later departure for a desired Via.
    Trip-pagination cannot be provided in this case.

    Args:
        id (str):  Example: yA88CgJWMRLmBiVDMiVCNkhLSQkJ8ElUJTI0QSUgM3Mzk-BAE=.
        via_earlier_later_context (str):  Example:
            PS=F$T=151200$L=A=1@O=Olten@X=7907703@Y=47351938@U=85@L=8500218@$.
        additional_transfer_time (Union[Unset, None, int]):
        include_alternate_match (Union[Unset, None, AlternateMatchEnum]): Post-filter to adjust
            cancelled/alternate 1:1 Trip cases per response (de:Ausfall/Ersatz) according to SBB BR,
            where other Trip's remain as is.<br>x-extensible-enum:
            - IRRELEVANT: no adaption
            - BOTH: as IRRELEVANT but some Note's will be cloned from cancelled to 1:1 alternate Trip
            - ALTERNATE_ONLY: suppresses cancelled 1:1 Trip's if matched with alternates
            - CANCELLED_ONLY: suppress exactly matching 1:1 alternates Default:
            AlternateMatchEnum.IRRELEVANT.
        include_route_projection (Union[Unset, None, bool]):
        include_summary (Union[Unset, None, bool]):
        include_intermediate_stops (Union[Unset, None, str]):  Default: 'ALL'.
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetTripsByIdAndPartialSearchContextAcceptLanguage]):
            Default: GetTripsByIdAndPartialSearchContextAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Problem, TripResponse]
    """

    return sync_detailed(
        id=id,
        via_earlier_later_context=via_earlier_later_context,
        client=client,
        additional_transfer_time=additional_transfer_time,
        include_alternate_match=include_alternate_match,
        include_route_projection=include_route_projection,
        include_summary=include_summary,
        include_intermediate_stops=include_intermediate_stops,
        request_id=request_id,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    id: str,
    via_earlier_later_context: str,
    *,
    client: AuthenticatedClient,
    additional_transfer_time: Union[Unset, None, int] = 0,
    include_alternate_match: Union[Unset, None, AlternateMatchEnum] = AlternateMatchEnum.IRRELEVANT,
    include_route_projection: Union[Unset, None, bool] = False,
    include_summary: Union[Unset, None, bool] = False,
    include_intermediate_stops: Union[Unset, None, str] = "ALL",
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[
        Unset, GetTripsByIdAndPartialSearchContextAcceptLanguage
    ] = GetTripsByIdAndPartialSearchContextAcceptLanguage.EN,
) -> Response[Union[Problem, TripResponse]]:
    """Get a `Trip` [0..1] with changed arrival/departure times at a concrete via on a given `Trip::id`
    (aka partialTripSearch).

     Useful to find a slightly different trip with earlier arrival or later departure for a desired Via.
    Trip-pagination cannot be provided in this case.

    Args:
        id (str):  Example: yA88CgJWMRLmBiVDMiVCNkhLSQkJ8ElUJTI0QSUgM3Mzk-BAE=.
        via_earlier_later_context (str):  Example:
            PS=F$T=151200$L=A=1@O=Olten@X=7907703@Y=47351938@U=85@L=8500218@$.
        additional_transfer_time (Union[Unset, None, int]):
        include_alternate_match (Union[Unset, None, AlternateMatchEnum]): Post-filter to adjust
            cancelled/alternate 1:1 Trip cases per response (de:Ausfall/Ersatz) according to SBB BR,
            where other Trip's remain as is.<br>x-extensible-enum:
            - IRRELEVANT: no adaption
            - BOTH: as IRRELEVANT but some Note's will be cloned from cancelled to 1:1 alternate Trip
            - ALTERNATE_ONLY: suppresses cancelled 1:1 Trip's if matched with alternates
            - CANCELLED_ONLY: suppress exactly matching 1:1 alternates Default:
            AlternateMatchEnum.IRRELEVANT.
        include_route_projection (Union[Unset, None, bool]):
        include_summary (Union[Unset, None, bool]):
        include_intermediate_stops (Union[Unset, None, str]):  Default: 'ALL'.
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetTripsByIdAndPartialSearchContextAcceptLanguage]):
            Default: GetTripsByIdAndPartialSearchContextAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Problem, TripResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        via_earlier_later_context=via_earlier_later_context,
        additional_transfer_time=additional_transfer_time,
        include_alternate_match=include_alternate_match,
        include_route_projection=include_route_projection,
        include_summary=include_summary,
        include_intermediate_stops=include_intermediate_stops,
        request_id=request_id,
        accept_language=accept_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    via_earlier_later_context: str,
    *,
    client: AuthenticatedClient,
    additional_transfer_time: Union[Unset, None, int] = 0,
    include_alternate_match: Union[Unset, None, AlternateMatchEnum] = AlternateMatchEnum.IRRELEVANT,
    include_route_projection: Union[Unset, None, bool] = False,
    include_summary: Union[Unset, None, bool] = False,
    include_intermediate_stops: Union[Unset, None, str] = "ALL",
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[
        Unset, GetTripsByIdAndPartialSearchContextAcceptLanguage
    ] = GetTripsByIdAndPartialSearchContextAcceptLanguage.EN,
) -> Optional[Union[Problem, TripResponse]]:
    """Get a `Trip` [0..1] with changed arrival/departure times at a concrete via on a given `Trip::id`
    (aka partialTripSearch).

     Useful to find a slightly different trip with earlier arrival or later departure for a desired Via.
    Trip-pagination cannot be provided in this case.

    Args:
        id (str):  Example: yA88CgJWMRLmBiVDMiVCNkhLSQkJ8ElUJTI0QSUgM3Mzk-BAE=.
        via_earlier_later_context (str):  Example:
            PS=F$T=151200$L=A=1@O=Olten@X=7907703@Y=47351938@U=85@L=8500218@$.
        additional_transfer_time (Union[Unset, None, int]):
        include_alternate_match (Union[Unset, None, AlternateMatchEnum]): Post-filter to adjust
            cancelled/alternate 1:1 Trip cases per response (de:Ausfall/Ersatz) according to SBB BR,
            where other Trip's remain as is.<br>x-extensible-enum:
            - IRRELEVANT: no adaption
            - BOTH: as IRRELEVANT but some Note's will be cloned from cancelled to 1:1 alternate Trip
            - ALTERNATE_ONLY: suppresses cancelled 1:1 Trip's if matched with alternates
            - CANCELLED_ONLY: suppress exactly matching 1:1 alternates Default:
            AlternateMatchEnum.IRRELEVANT.
        include_route_projection (Union[Unset, None, bool]):
        include_summary (Union[Unset, None, bool]):
        include_intermediate_stops (Union[Unset, None, str]):  Default: 'ALL'.
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetTripsByIdAndPartialSearchContextAcceptLanguage]):
            Default: GetTripsByIdAndPartialSearchContextAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Problem, TripResponse]
    """

    return (
        await asyncio_detailed(
            id=id,
            via_earlier_later_context=via_earlier_later_context,
            client=client,
            additional_transfer_time=additional_transfer_time,
            include_alternate_match=include_alternate_match,
            include_route_projection=include_route_projection,
            include_summary=include_summary,
            include_intermediate_stops=include_intermediate_stops,
            request_id=request_id,
            accept_language=accept_language,
        )
    ).parsed
