from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_train_formation_by_journey_reference_and_stop_accept_language import (
    GetTrainFormationByJourneyReferenceAndStopAcceptLanguage,
)
from ...models.get_train_formation_by_journey_reference_and_stop_stop_type import (
    GetTrainFormationByJourneyReferenceAndStopStopType,
)
from ...models.json_response import JsonResponse
from ...models.problem import Problem
from ...models.train_formation import TrainFormation
from ...types import UNSET, Response, Unset


def _get_kwargs(
    journey_reference: str,
    stop_value: str,
    *,
    stop_type: Union[
        Unset, None, GetTrainFormationByJourneyReferenceAndStopStopType
    ] = GetTrainFormationByJourneyReferenceAndStopStopType.STATION,
    leaving_direction_enforce_left: Union[Unset, None, bool] = True,
    accept_language: Union[
        Unset, GetTrainFormationByJourneyReferenceAndStopAcceptLanguage
    ] = GetTrainFormationByJourneyReferenceAndStopAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = str(accept_language)

    if not isinstance(request_id, Unset):
        headers["Request-ID"] = request_id

    params: Dict[str, Any] = {}
    json_stop_type: Union[Unset, None, str] = UNSET
    if not isinstance(stop_type, Unset):
        json_stop_type = stop_type.value if stop_type else None

    params["stopType"] = json_stop_type

    params["leavingDirectionEnforceLeft"] = leaving_direction_enforce_left

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/b2c/v2/trainFormation/{journeyReference}/{stopValue}".format(
            journeyReference=journey_reference,
            stopValue=stop_value,
        ),
        "params": params,
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[JsonResponse, Problem, TrainFormation]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = TrainFormation.from_dict(response.json())

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
    if response.status_code == HTTPStatus.UNSUPPORTED_MEDIA_TYPE:
        response_415 = JsonResponse.from_dict(response.json())

        return response_415
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
) -> Response[Union[JsonResponse, Problem, TrainFormation]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    journey_reference: str,
    stop_value: str,
    *,
    client: AuthenticatedClient,
    stop_type: Union[
        Unset, None, GetTrainFormationByJourneyReferenceAndStopStopType
    ] = GetTrainFormationByJourneyReferenceAndStopStopType.STATION,
    leaving_direction_enforce_left: Union[Unset, None, bool] = True,
    accept_language: Union[
        Unset, GetTrainFormationByJourneyReferenceAndStopAcceptLanguage
    ] = GetTrainFormationByJourneyReferenceAndStopAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Response[Union[JsonResponse, Problem, TrainFormation]]:
    """@Deprecated (SWITCH to v3/vehicle-journeys/{id} &includeTrainStopAssignments)! Get the train-
    formation (composition of wagons) for a specific JourneyDetail (for e.g. of an SBB transport-product
    of vehicleType=TRAIN). Found TrainFormation::originFormation corresponds to stopValue.

     Train-formations are considered as daily realtime data and are therefore available TODAY
    only.<br>Assumes the search of a previous journeyDetail (by /routes, /departures or /arrivals) and
    tries to reconstruct it by its journeyReference.

    Args:
        journey_reference (str):  Example: 1|17166|0|85|18032019.
        stop_value (str):
        stop_type (Union[Unset, None, GetTrainFormationByJourneyReferenceAndStopStopType]):
            Default: GetTrainFormationByJourneyReferenceAndStopStopType.STATION.
        leaving_direction_enforce_left (Union[Unset, None, bool]):  Default: True.
        accept_language (Union[Unset, GetTrainFormationByJourneyReferenceAndStopAcceptLanguage]):
            Default: GetTrainFormationByJourneyReferenceAndStopAcceptLanguage.EN.
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[JsonResponse, Problem, TrainFormation]]
    """

    kwargs = _get_kwargs(
        journey_reference=journey_reference,
        stop_value=stop_value,
        stop_type=stop_type,
        leaving_direction_enforce_left=leaving_direction_enforce_left,
        accept_language=accept_language,
        request_id=request_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    journey_reference: str,
    stop_value: str,
    *,
    client: AuthenticatedClient,
    stop_type: Union[
        Unset, None, GetTrainFormationByJourneyReferenceAndStopStopType
    ] = GetTrainFormationByJourneyReferenceAndStopStopType.STATION,
    leaving_direction_enforce_left: Union[Unset, None, bool] = True,
    accept_language: Union[
        Unset, GetTrainFormationByJourneyReferenceAndStopAcceptLanguage
    ] = GetTrainFormationByJourneyReferenceAndStopAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Optional[Union[JsonResponse, Problem, TrainFormation]]:
    """@Deprecated (SWITCH to v3/vehicle-journeys/{id} &includeTrainStopAssignments)! Get the train-
    formation (composition of wagons) for a specific JourneyDetail (for e.g. of an SBB transport-product
    of vehicleType=TRAIN). Found TrainFormation::originFormation corresponds to stopValue.

     Train-formations are considered as daily realtime data and are therefore available TODAY
    only.<br>Assumes the search of a previous journeyDetail (by /routes, /departures or /arrivals) and
    tries to reconstruct it by its journeyReference.

    Args:
        journey_reference (str):  Example: 1|17166|0|85|18032019.
        stop_value (str):
        stop_type (Union[Unset, None, GetTrainFormationByJourneyReferenceAndStopStopType]):
            Default: GetTrainFormationByJourneyReferenceAndStopStopType.STATION.
        leaving_direction_enforce_left (Union[Unset, None, bool]):  Default: True.
        accept_language (Union[Unset, GetTrainFormationByJourneyReferenceAndStopAcceptLanguage]):
            Default: GetTrainFormationByJourneyReferenceAndStopAcceptLanguage.EN.
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[JsonResponse, Problem, TrainFormation]
    """

    return sync_detailed(
        journey_reference=journey_reference,
        stop_value=stop_value,
        client=client,
        stop_type=stop_type,
        leaving_direction_enforce_left=leaving_direction_enforce_left,
        accept_language=accept_language,
        request_id=request_id,
    ).parsed


async def asyncio_detailed(
    journey_reference: str,
    stop_value: str,
    *,
    client: AuthenticatedClient,
    stop_type: Union[
        Unset, None, GetTrainFormationByJourneyReferenceAndStopStopType
    ] = GetTrainFormationByJourneyReferenceAndStopStopType.STATION,
    leaving_direction_enforce_left: Union[Unset, None, bool] = True,
    accept_language: Union[
        Unset, GetTrainFormationByJourneyReferenceAndStopAcceptLanguage
    ] = GetTrainFormationByJourneyReferenceAndStopAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Response[Union[JsonResponse, Problem, TrainFormation]]:
    """@Deprecated (SWITCH to v3/vehicle-journeys/{id} &includeTrainStopAssignments)! Get the train-
    formation (composition of wagons) for a specific JourneyDetail (for e.g. of an SBB transport-product
    of vehicleType=TRAIN). Found TrainFormation::originFormation corresponds to stopValue.

     Train-formations are considered as daily realtime data and are therefore available TODAY
    only.<br>Assumes the search of a previous journeyDetail (by /routes, /departures or /arrivals) and
    tries to reconstruct it by its journeyReference.

    Args:
        journey_reference (str):  Example: 1|17166|0|85|18032019.
        stop_value (str):
        stop_type (Union[Unset, None, GetTrainFormationByJourneyReferenceAndStopStopType]):
            Default: GetTrainFormationByJourneyReferenceAndStopStopType.STATION.
        leaving_direction_enforce_left (Union[Unset, None, bool]):  Default: True.
        accept_language (Union[Unset, GetTrainFormationByJourneyReferenceAndStopAcceptLanguage]):
            Default: GetTrainFormationByJourneyReferenceAndStopAcceptLanguage.EN.
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[JsonResponse, Problem, TrainFormation]]
    """

    kwargs = _get_kwargs(
        journey_reference=journey_reference,
        stop_value=stop_value,
        stop_type=stop_type,
        leaving_direction_enforce_left=leaving_direction_enforce_left,
        accept_language=accept_language,
        request_id=request_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    journey_reference: str,
    stop_value: str,
    *,
    client: AuthenticatedClient,
    stop_type: Union[
        Unset, None, GetTrainFormationByJourneyReferenceAndStopStopType
    ] = GetTrainFormationByJourneyReferenceAndStopStopType.STATION,
    leaving_direction_enforce_left: Union[Unset, None, bool] = True,
    accept_language: Union[
        Unset, GetTrainFormationByJourneyReferenceAndStopAcceptLanguage
    ] = GetTrainFormationByJourneyReferenceAndStopAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Optional[Union[JsonResponse, Problem, TrainFormation]]:
    """@Deprecated (SWITCH to v3/vehicle-journeys/{id} &includeTrainStopAssignments)! Get the train-
    formation (composition of wagons) for a specific JourneyDetail (for e.g. of an SBB transport-product
    of vehicleType=TRAIN). Found TrainFormation::originFormation corresponds to stopValue.

     Train-formations are considered as daily realtime data and are therefore available TODAY
    only.<br>Assumes the search of a previous journeyDetail (by /routes, /departures or /arrivals) and
    tries to reconstruct it by its journeyReference.

    Args:
        journey_reference (str):  Example: 1|17166|0|85|18032019.
        stop_value (str):
        stop_type (Union[Unset, None, GetTrainFormationByJourneyReferenceAndStopStopType]):
            Default: GetTrainFormationByJourneyReferenceAndStopStopType.STATION.
        leaving_direction_enforce_left (Union[Unset, None, bool]):  Default: True.
        accept_language (Union[Unset, GetTrainFormationByJourneyReferenceAndStopAcceptLanguage]):
            Default: GetTrainFormationByJourneyReferenceAndStopAcceptLanguage.EN.
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[JsonResponse, Problem, TrainFormation]
    """

    return (
        await asyncio_detailed(
            journey_reference=journey_reference,
            stop_value=stop_value,
            client=client,
            stop_type=stop_type,
            leaving_direction_enforce_left=leaving_direction_enforce_left,
            accept_language=accept_language,
            request_id=request_id,
        )
    ).parsed
