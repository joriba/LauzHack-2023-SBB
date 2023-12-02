import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.alternate_match_enum import AlternateMatchEnum
from ...models.get_trips_by_id_accept_language import GetTripsByIdAcceptLanguage
from ...models.problem import Problem
from ...models.realtime_mode_enum import RealtimeModeEnum
from ...models.train_stop_assignments_enum import TrainStopAssignmentsEnum
from ...models.trip_response import TripResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    date: Union[Unset, None, datetime.date] = UNSET,
    realtime_mode: Union[Unset, None, RealtimeModeEnum] = RealtimeModeEnum.REALTIME,
    retry_fuzzy: Union[Unset, None, bool] = False,
    include_alternate_match: Union[Unset, None, AlternateMatchEnum] = AlternateMatchEnum.IRRELEVANT,
    include_route_projection: Union[Unset, None, bool] = False,
    include_operating_days: Union[Unset, None, bool] = False,
    include_summary: Union[Unset, None, bool] = False,
    include_intermediate_stops: Union[Unset, None, str] = "ALL",
    include_train_stop_assignments: Union[Unset, None, TrainStopAssignmentsEnum] = TrainStopAssignmentsEnum.NONE,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, GetTripsByIdAcceptLanguage] = GetTripsByIdAcceptLanguage.EN,
) -> Dict[str, Any]:
    headers = {}
    if not isinstance(request_id, Unset):
        headers["Request-ID"] = request_id

    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = str(accept_language)

    params: Dict[str, Any] = {}
    json_date: Union[Unset, None, str] = UNSET
    if not isinstance(date, Unset):
        json_date = date.isoformat() if date else None

    params["date"] = json_date

    json_realtime_mode: Union[Unset, None, str] = UNSET
    if not isinstance(realtime_mode, Unset):
        json_realtime_mode = realtime_mode.value if realtime_mode else None

    params["realtimeMode"] = json_realtime_mode

    params["retryFuzzy"] = retry_fuzzy

    json_include_alternate_match: Union[Unset, None, str] = UNSET
    if not isinstance(include_alternate_match, Unset):
        json_include_alternate_match = include_alternate_match.value if include_alternate_match else None

    params["includeAlternateMatch"] = json_include_alternate_match

    params["includeRouteProjection"] = include_route_projection

    params["includeOperatingDays"] = include_operating_days

    params["includeSummary"] = include_summary

    params["includeIntermediateStops"] = include_intermediate_stops

    json_include_train_stop_assignments: Union[Unset, None, str] = UNSET
    if not isinstance(include_train_stop_assignments, Unset):
        json_include_train_stop_assignments = (
            include_train_stop_assignments.value if include_train_stop_assignments else None
        )

    params["includeTrainStopAssignments"] = json_include_train_stop_assignments

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/v3/trips/{id}".format(
            id=id,
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
    *,
    client: AuthenticatedClient,
    date: Union[Unset, None, datetime.date] = UNSET,
    realtime_mode: Union[Unset, None, RealtimeModeEnum] = RealtimeModeEnum.REALTIME,
    retry_fuzzy: Union[Unset, None, bool] = False,
    include_alternate_match: Union[Unset, None, AlternateMatchEnum] = AlternateMatchEnum.IRRELEVANT,
    include_route_projection: Union[Unset, None, bool] = False,
    include_operating_days: Union[Unset, None, bool] = False,
    include_summary: Union[Unset, None, bool] = False,
    include_intermediate_stops: Union[Unset, None, str] = "ALL",
    include_train_stop_assignments: Union[Unset, None, TrainStopAssignmentsEnum] = TrainStopAssignmentsEnum.NONE,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, GetTripsByIdAcceptLanguage] = GetTripsByIdAcceptLanguage.EN,
) -> Response[Union[Problem, TripResponse]]:
    """Get corresponding trip for a specific Trip::id.

     Typically there is [1] hit but failing `Problem` must be expected in realtime scenarios or older
    `Trip::id's`. Rare [2] hit cases might resolve from includeAlternateMatch=BOTH.

    Args:
        id (str):
        date (Union[Unset, None, datetime.date]):  Example: 2023-04-18.
        realtime_mode (Union[Unset, None, RealtimeModeEnum]): <br>x-extensible-enum:
            - `REALTIME` potentially planned and RT **including non-rideable** (like cancelled)
            - `REALTIME_RIDEABLE` as `REALTIME` but **excluding non-rideable**
            - `OFF` **planned only** Default: RealtimeModeEnum.REALTIME.
        retry_fuzzy (Union[Unset, None, bool]):
        include_alternate_match (Union[Unset, None, AlternateMatchEnum]): Post-filter to adjust
            cancelled/alternate 1:1 Trip cases per response (de:Ausfall/Ersatz) according to SBB BR,
            where other Trip's remain as is.<br>x-extensible-enum:
            - IRRELEVANT: no adaption
            - BOTH: as IRRELEVANT but some Note's will be cloned from cancelled to 1:1 alternate Trip
            - ALTERNATE_ONLY: suppresses cancelled 1:1 Trip's if matched with alternates
            - CANCELLED_ONLY: suppress exactly matching 1:1 alternates Default:
            AlternateMatchEnum.IRRELEVANT.
        include_route_projection (Union[Unset, None, bool]):
        include_operating_days (Union[Unset, None, bool]):
        include_summary (Union[Unset, None, bool]):
        include_intermediate_stops (Union[Unset, None, str]):  Default: 'ALL'.
        include_train_stop_assignments (Union[Unset, None, TrainStopAssignmentsEnum]): Whether
            `PTRideLeg's` should include `CompoundTrain's`(aka formation, composition). However,
            `CompoundTrain's` at any `ScheduledStopPoint` on the `ServiceJourney` may be loaded
            separately by `/v3/vehicle-journeys/by-stoppoints`.
            Possible values:
            - NONE none at all, though a `PTRideLeg::trainStopAssignmentHint` is always given.
            - ORIGIN  `TrainStopAssignment's` are added to first (departure) `ScheduledStopPoint` of
            each `PTRideLeg`
            - ORIGIN_DESTINATION `TrainStopAssignment's` are added to first (departure) and last
            (arrival) `ScheduledStopPoint` of each `PTRideLeg` having a `TrainStopAssignment` resp. a
            `CompoundTrain`. Default: TrainStopAssignmentsEnum.NONE.
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetTripsByIdAcceptLanguage]):  Default:
            GetTripsByIdAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Problem, TripResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        date=date,
        realtime_mode=realtime_mode,
        retry_fuzzy=retry_fuzzy,
        include_alternate_match=include_alternate_match,
        include_route_projection=include_route_projection,
        include_operating_days=include_operating_days,
        include_summary=include_summary,
        include_intermediate_stops=include_intermediate_stops,
        include_train_stop_assignments=include_train_stop_assignments,
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
    date: Union[Unset, None, datetime.date] = UNSET,
    realtime_mode: Union[Unset, None, RealtimeModeEnum] = RealtimeModeEnum.REALTIME,
    retry_fuzzy: Union[Unset, None, bool] = False,
    include_alternate_match: Union[Unset, None, AlternateMatchEnum] = AlternateMatchEnum.IRRELEVANT,
    include_route_projection: Union[Unset, None, bool] = False,
    include_operating_days: Union[Unset, None, bool] = False,
    include_summary: Union[Unset, None, bool] = False,
    include_intermediate_stops: Union[Unset, None, str] = "ALL",
    include_train_stop_assignments: Union[Unset, None, TrainStopAssignmentsEnum] = TrainStopAssignmentsEnum.NONE,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, GetTripsByIdAcceptLanguage] = GetTripsByIdAcceptLanguage.EN,
) -> Optional[Union[Problem, TripResponse]]:
    """Get corresponding trip for a specific Trip::id.

     Typically there is [1] hit but failing `Problem` must be expected in realtime scenarios or older
    `Trip::id's`. Rare [2] hit cases might resolve from includeAlternateMatch=BOTH.

    Args:
        id (str):
        date (Union[Unset, None, datetime.date]):  Example: 2023-04-18.
        realtime_mode (Union[Unset, None, RealtimeModeEnum]): <br>x-extensible-enum:
            - `REALTIME` potentially planned and RT **including non-rideable** (like cancelled)
            - `REALTIME_RIDEABLE` as `REALTIME` but **excluding non-rideable**
            - `OFF` **planned only** Default: RealtimeModeEnum.REALTIME.
        retry_fuzzy (Union[Unset, None, bool]):
        include_alternate_match (Union[Unset, None, AlternateMatchEnum]): Post-filter to adjust
            cancelled/alternate 1:1 Trip cases per response (de:Ausfall/Ersatz) according to SBB BR,
            where other Trip's remain as is.<br>x-extensible-enum:
            - IRRELEVANT: no adaption
            - BOTH: as IRRELEVANT but some Note's will be cloned from cancelled to 1:1 alternate Trip
            - ALTERNATE_ONLY: suppresses cancelled 1:1 Trip's if matched with alternates
            - CANCELLED_ONLY: suppress exactly matching 1:1 alternates Default:
            AlternateMatchEnum.IRRELEVANT.
        include_route_projection (Union[Unset, None, bool]):
        include_operating_days (Union[Unset, None, bool]):
        include_summary (Union[Unset, None, bool]):
        include_intermediate_stops (Union[Unset, None, str]):  Default: 'ALL'.
        include_train_stop_assignments (Union[Unset, None, TrainStopAssignmentsEnum]): Whether
            `PTRideLeg's` should include `CompoundTrain's`(aka formation, composition). However,
            `CompoundTrain's` at any `ScheduledStopPoint` on the `ServiceJourney` may be loaded
            separately by `/v3/vehicle-journeys/by-stoppoints`.
            Possible values:
            - NONE none at all, though a `PTRideLeg::trainStopAssignmentHint` is always given.
            - ORIGIN  `TrainStopAssignment's` are added to first (departure) `ScheduledStopPoint` of
            each `PTRideLeg`
            - ORIGIN_DESTINATION `TrainStopAssignment's` are added to first (departure) and last
            (arrival) `ScheduledStopPoint` of each `PTRideLeg` having a `TrainStopAssignment` resp. a
            `CompoundTrain`. Default: TrainStopAssignmentsEnum.NONE.
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetTripsByIdAcceptLanguage]):  Default:
            GetTripsByIdAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Problem, TripResponse]
    """

    return sync_detailed(
        id=id,
        client=client,
        date=date,
        realtime_mode=realtime_mode,
        retry_fuzzy=retry_fuzzy,
        include_alternate_match=include_alternate_match,
        include_route_projection=include_route_projection,
        include_operating_days=include_operating_days,
        include_summary=include_summary,
        include_intermediate_stops=include_intermediate_stops,
        include_train_stop_assignments=include_train_stop_assignments,
        request_id=request_id,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    date: Union[Unset, None, datetime.date] = UNSET,
    realtime_mode: Union[Unset, None, RealtimeModeEnum] = RealtimeModeEnum.REALTIME,
    retry_fuzzy: Union[Unset, None, bool] = False,
    include_alternate_match: Union[Unset, None, AlternateMatchEnum] = AlternateMatchEnum.IRRELEVANT,
    include_route_projection: Union[Unset, None, bool] = False,
    include_operating_days: Union[Unset, None, bool] = False,
    include_summary: Union[Unset, None, bool] = False,
    include_intermediate_stops: Union[Unset, None, str] = "ALL",
    include_train_stop_assignments: Union[Unset, None, TrainStopAssignmentsEnum] = TrainStopAssignmentsEnum.NONE,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, GetTripsByIdAcceptLanguage] = GetTripsByIdAcceptLanguage.EN,
) -> Response[Union[Problem, TripResponse]]:
    """Get corresponding trip for a specific Trip::id.

     Typically there is [1] hit but failing `Problem` must be expected in realtime scenarios or older
    `Trip::id's`. Rare [2] hit cases might resolve from includeAlternateMatch=BOTH.

    Args:
        id (str):
        date (Union[Unset, None, datetime.date]):  Example: 2023-04-18.
        realtime_mode (Union[Unset, None, RealtimeModeEnum]): <br>x-extensible-enum:
            - `REALTIME` potentially planned and RT **including non-rideable** (like cancelled)
            - `REALTIME_RIDEABLE` as `REALTIME` but **excluding non-rideable**
            - `OFF` **planned only** Default: RealtimeModeEnum.REALTIME.
        retry_fuzzy (Union[Unset, None, bool]):
        include_alternate_match (Union[Unset, None, AlternateMatchEnum]): Post-filter to adjust
            cancelled/alternate 1:1 Trip cases per response (de:Ausfall/Ersatz) according to SBB BR,
            where other Trip's remain as is.<br>x-extensible-enum:
            - IRRELEVANT: no adaption
            - BOTH: as IRRELEVANT but some Note's will be cloned from cancelled to 1:1 alternate Trip
            - ALTERNATE_ONLY: suppresses cancelled 1:1 Trip's if matched with alternates
            - CANCELLED_ONLY: suppress exactly matching 1:1 alternates Default:
            AlternateMatchEnum.IRRELEVANT.
        include_route_projection (Union[Unset, None, bool]):
        include_operating_days (Union[Unset, None, bool]):
        include_summary (Union[Unset, None, bool]):
        include_intermediate_stops (Union[Unset, None, str]):  Default: 'ALL'.
        include_train_stop_assignments (Union[Unset, None, TrainStopAssignmentsEnum]): Whether
            `PTRideLeg's` should include `CompoundTrain's`(aka formation, composition). However,
            `CompoundTrain's` at any `ScheduledStopPoint` on the `ServiceJourney` may be loaded
            separately by `/v3/vehicle-journeys/by-stoppoints`.
            Possible values:
            - NONE none at all, though a `PTRideLeg::trainStopAssignmentHint` is always given.
            - ORIGIN  `TrainStopAssignment's` are added to first (departure) `ScheduledStopPoint` of
            each `PTRideLeg`
            - ORIGIN_DESTINATION `TrainStopAssignment's` are added to first (departure) and last
            (arrival) `ScheduledStopPoint` of each `PTRideLeg` having a `TrainStopAssignment` resp. a
            `CompoundTrain`. Default: TrainStopAssignmentsEnum.NONE.
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetTripsByIdAcceptLanguage]):  Default:
            GetTripsByIdAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Problem, TripResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        date=date,
        realtime_mode=realtime_mode,
        retry_fuzzy=retry_fuzzy,
        include_alternate_match=include_alternate_match,
        include_route_projection=include_route_projection,
        include_operating_days=include_operating_days,
        include_summary=include_summary,
        include_intermediate_stops=include_intermediate_stops,
        include_train_stop_assignments=include_train_stop_assignments,
        request_id=request_id,
        accept_language=accept_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    date: Union[Unset, None, datetime.date] = UNSET,
    realtime_mode: Union[Unset, None, RealtimeModeEnum] = RealtimeModeEnum.REALTIME,
    retry_fuzzy: Union[Unset, None, bool] = False,
    include_alternate_match: Union[Unset, None, AlternateMatchEnum] = AlternateMatchEnum.IRRELEVANT,
    include_route_projection: Union[Unset, None, bool] = False,
    include_operating_days: Union[Unset, None, bool] = False,
    include_summary: Union[Unset, None, bool] = False,
    include_intermediate_stops: Union[Unset, None, str] = "ALL",
    include_train_stop_assignments: Union[Unset, None, TrainStopAssignmentsEnum] = TrainStopAssignmentsEnum.NONE,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, GetTripsByIdAcceptLanguage] = GetTripsByIdAcceptLanguage.EN,
) -> Optional[Union[Problem, TripResponse]]:
    """Get corresponding trip for a specific Trip::id.

     Typically there is [1] hit but failing `Problem` must be expected in realtime scenarios or older
    `Trip::id's`. Rare [2] hit cases might resolve from includeAlternateMatch=BOTH.

    Args:
        id (str):
        date (Union[Unset, None, datetime.date]):  Example: 2023-04-18.
        realtime_mode (Union[Unset, None, RealtimeModeEnum]): <br>x-extensible-enum:
            - `REALTIME` potentially planned and RT **including non-rideable** (like cancelled)
            - `REALTIME_RIDEABLE` as `REALTIME` but **excluding non-rideable**
            - `OFF` **planned only** Default: RealtimeModeEnum.REALTIME.
        retry_fuzzy (Union[Unset, None, bool]):
        include_alternate_match (Union[Unset, None, AlternateMatchEnum]): Post-filter to adjust
            cancelled/alternate 1:1 Trip cases per response (de:Ausfall/Ersatz) according to SBB BR,
            where other Trip's remain as is.<br>x-extensible-enum:
            - IRRELEVANT: no adaption
            - BOTH: as IRRELEVANT but some Note's will be cloned from cancelled to 1:1 alternate Trip
            - ALTERNATE_ONLY: suppresses cancelled 1:1 Trip's if matched with alternates
            - CANCELLED_ONLY: suppress exactly matching 1:1 alternates Default:
            AlternateMatchEnum.IRRELEVANT.
        include_route_projection (Union[Unset, None, bool]):
        include_operating_days (Union[Unset, None, bool]):
        include_summary (Union[Unset, None, bool]):
        include_intermediate_stops (Union[Unset, None, str]):  Default: 'ALL'.
        include_train_stop_assignments (Union[Unset, None, TrainStopAssignmentsEnum]): Whether
            `PTRideLeg's` should include `CompoundTrain's`(aka formation, composition). However,
            `CompoundTrain's` at any `ScheduledStopPoint` on the `ServiceJourney` may be loaded
            separately by `/v3/vehicle-journeys/by-stoppoints`.
            Possible values:
            - NONE none at all, though a `PTRideLeg::trainStopAssignmentHint` is always given.
            - ORIGIN  `TrainStopAssignment's` are added to first (departure) `ScheduledStopPoint` of
            each `PTRideLeg`
            - ORIGIN_DESTINATION `TrainStopAssignment's` are added to first (departure) and last
            (arrival) `ScheduledStopPoint` of each `PTRideLeg` having a `TrainStopAssignment` resp. a
            `CompoundTrain`. Default: TrainStopAssignmentsEnum.NONE.
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetTripsByIdAcceptLanguage]):  Default:
            GetTripsByIdAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Problem, TripResponse]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            date=date,
            realtime_mode=realtime_mode,
            retry_fuzzy=retry_fuzzy,
            include_alternate_match=include_alternate_match,
            include_route_projection=include_route_projection,
            include_operating_days=include_operating_days,
            include_summary=include_summary,
            include_intermediate_stops=include_intermediate_stops,
            include_train_stop_assignments=include_train_stop_assignments,
            request_id=request_id,
            accept_language=accept_language,
        )
    ).parsed
