import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dated_vehicle_journey import DatedVehicleJourney
from ...models.get_dated_vehicle_journey_by_id_accept_language import GetDatedVehicleJourneyByIdAcceptLanguage
from ...models.problem import Problem
from ...models.train_stop_assignments_enum import TrainStopAssignmentsEnum
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    date: Union[Unset, None, datetime.date] = UNSET,
    include_operating_days: Union[Unset, None, bool] = False,
    include_route_projection: Union[Unset, None, bool] = False,
    include_intermediate_stops: Union[Unset, None, str] = "ALL",
    include_train_stop_assignments: Union[Unset, None, TrainStopAssignmentsEnum] = TrainStopAssignmentsEnum.NONE,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[
        Unset, GetDatedVehicleJourneyByIdAcceptLanguage
    ] = GetDatedVehicleJourneyByIdAcceptLanguage.EN,
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

    params["includeOperatingDays"] = include_operating_days

    params["includeRouteProjection"] = include_route_projection

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
        "url": "/v3/vehicle-journeys/{id}".format(
            id=id,
        ),
        "params": params,
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[DatedVehicleJourney, Problem]]:
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = Problem.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = Problem.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.OK:
        response_200 = DatedVehicleJourney.from_dict(response.json())

        return response_200
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
    id: str,
    *,
    client: AuthenticatedClient,
    date: Union[Unset, None, datetime.date] = UNSET,
    include_operating_days: Union[Unset, None, bool] = False,
    include_route_projection: Union[Unset, None, bool] = False,
    include_intermediate_stops: Union[Unset, None, str] = "ALL",
    include_train_stop_assignments: Union[Unset, None, TrainStopAssignmentsEnum] = TrainStopAssignmentsEnum.NONE,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[
        Unset, GetDatedVehicleJourneyByIdAcceptLanguage
    ] = GetDatedVehicleJourneyByIdAcceptLanguage.EN,
) -> Response[Union[DatedVehicleJourney, Problem]]:
    """Get complete DatedVehicleJourney by its Journey-Reference.

     This will deliver all current details of the complete vehicle-journey (of the passenger carrying
    `ServiceProduct` such such as train, bus,..). It contains a list of all `ScheduledStopPoints`
    including departure and arrival times (with real-time data if available) and additional information
    like specific Notice's.

    Args:
        id (str):
        date (Union[Unset, None, datetime.date]):
        include_operating_days (Union[Unset, None, bool]):
        include_route_projection (Union[Unset, None, bool]):
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
        accept_language (Union[Unset, GetDatedVehicleJourneyByIdAcceptLanguage]):  Default:
            GetDatedVehicleJourneyByIdAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DatedVehicleJourney, Problem]]
    """

    kwargs = _get_kwargs(
        id=id,
        date=date,
        include_operating_days=include_operating_days,
        include_route_projection=include_route_projection,
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
    include_operating_days: Union[Unset, None, bool] = False,
    include_route_projection: Union[Unset, None, bool] = False,
    include_intermediate_stops: Union[Unset, None, str] = "ALL",
    include_train_stop_assignments: Union[Unset, None, TrainStopAssignmentsEnum] = TrainStopAssignmentsEnum.NONE,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[
        Unset, GetDatedVehicleJourneyByIdAcceptLanguage
    ] = GetDatedVehicleJourneyByIdAcceptLanguage.EN,
) -> Optional[Union[DatedVehicleJourney, Problem]]:
    """Get complete DatedVehicleJourney by its Journey-Reference.

     This will deliver all current details of the complete vehicle-journey (of the passenger carrying
    `ServiceProduct` such such as train, bus,..). It contains a list of all `ScheduledStopPoints`
    including departure and arrival times (with real-time data if available) and additional information
    like specific Notice's.

    Args:
        id (str):
        date (Union[Unset, None, datetime.date]):
        include_operating_days (Union[Unset, None, bool]):
        include_route_projection (Union[Unset, None, bool]):
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
        accept_language (Union[Unset, GetDatedVehicleJourneyByIdAcceptLanguage]):  Default:
            GetDatedVehicleJourneyByIdAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DatedVehicleJourney, Problem]
    """

    return sync_detailed(
        id=id,
        client=client,
        date=date,
        include_operating_days=include_operating_days,
        include_route_projection=include_route_projection,
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
    include_operating_days: Union[Unset, None, bool] = False,
    include_route_projection: Union[Unset, None, bool] = False,
    include_intermediate_stops: Union[Unset, None, str] = "ALL",
    include_train_stop_assignments: Union[Unset, None, TrainStopAssignmentsEnum] = TrainStopAssignmentsEnum.NONE,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[
        Unset, GetDatedVehicleJourneyByIdAcceptLanguage
    ] = GetDatedVehicleJourneyByIdAcceptLanguage.EN,
) -> Response[Union[DatedVehicleJourney, Problem]]:
    """Get complete DatedVehicleJourney by its Journey-Reference.

     This will deliver all current details of the complete vehicle-journey (of the passenger carrying
    `ServiceProduct` such such as train, bus,..). It contains a list of all `ScheduledStopPoints`
    including departure and arrival times (with real-time data if available) and additional information
    like specific Notice's.

    Args:
        id (str):
        date (Union[Unset, None, datetime.date]):
        include_operating_days (Union[Unset, None, bool]):
        include_route_projection (Union[Unset, None, bool]):
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
        accept_language (Union[Unset, GetDatedVehicleJourneyByIdAcceptLanguage]):  Default:
            GetDatedVehicleJourneyByIdAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DatedVehicleJourney, Problem]]
    """

    kwargs = _get_kwargs(
        id=id,
        date=date,
        include_operating_days=include_operating_days,
        include_route_projection=include_route_projection,
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
    include_operating_days: Union[Unset, None, bool] = False,
    include_route_projection: Union[Unset, None, bool] = False,
    include_intermediate_stops: Union[Unset, None, str] = "ALL",
    include_train_stop_assignments: Union[Unset, None, TrainStopAssignmentsEnum] = TrainStopAssignmentsEnum.NONE,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[
        Unset, GetDatedVehicleJourneyByIdAcceptLanguage
    ] = GetDatedVehicleJourneyByIdAcceptLanguage.EN,
) -> Optional[Union[DatedVehicleJourney, Problem]]:
    """Get complete DatedVehicleJourney by its Journey-Reference.

     This will deliver all current details of the complete vehicle-journey (of the passenger carrying
    `ServiceProduct` such such as train, bus,..). It contains a list of all `ScheduledStopPoints`
    including departure and arrival times (with real-time data if available) and additional information
    like specific Notice's.

    Args:
        id (str):
        date (Union[Unset, None, datetime.date]):
        include_operating_days (Union[Unset, None, bool]):
        include_route_projection (Union[Unset, None, bool]):
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
        accept_language (Union[Unset, GetDatedVehicleJourneyByIdAcceptLanguage]):  Default:
            GetDatedVehicleJourneyByIdAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DatedVehicleJourney, Problem]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            date=date,
            include_operating_days=include_operating_days,
            include_route_projection=include_route_projection,
            include_intermediate_stops=include_intermediate_stops,
            include_train_stop_assignments=include_train_stop_assignments,
            request_id=request_id,
            accept_language=accept_language,
        )
    ).parsed
