from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_train_formation_by_reconstruction_context_accept_language import (
    GetTrainFormationByReconstructionContextAcceptLanguage,
)
from ...models.get_train_formation_by_reconstruction_context_destination_type import (
    GetTrainFormationByReconstructionContextDestinationType,
)
from ...models.get_train_formation_by_reconstruction_context_origin_type import (
    GetTrainFormationByReconstructionContextOriginType,
)
from ...models.json_response import JsonResponse
from ...models.problem import Problem
from ...models.train_formation import TrainFormation
from ...types import UNSET, Response, Unset


def _get_kwargs(
    reconstruction_context: str,
    *,
    destination_value: str,
    origin_value: str,
    destination_type: Union[
        Unset, None, GetTrainFormationByReconstructionContextDestinationType
    ] = GetTrainFormationByReconstructionContextDestinationType.STATION,
    origin_type: Union[
        Unset, None, GetTrainFormationByReconstructionContextOriginType
    ] = GetTrainFormationByReconstructionContextOriginType.STATION,
    leaving_direction_enforce_left: Union[Unset, None, bool] = True,
    accept_language: Union[
        Unset, GetTrainFormationByReconstructionContextAcceptLanguage
    ] = GetTrainFormationByReconstructionContextAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = str(accept_language)

    if not isinstance(request_id, Unset):
        headers["Request-ID"] = request_id

    params: Dict[str, Any] = {}
    params["destinationValue"] = destination_value

    params["originValue"] = origin_value

    json_destination_type: Union[Unset, None, str] = UNSET
    if not isinstance(destination_type, Unset):
        json_destination_type = destination_type.value if destination_type else None

    params["destinationType"] = json_destination_type

    json_origin_type: Union[Unset, None, str] = UNSET
    if not isinstance(origin_type, Unset):
        json_origin_type = origin_type.value if origin_type else None

    params["originType"] = json_origin_type

    params["leavingDirectionEnforceLeft"] = leaving_direction_enforce_left

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/b2c/v2/trainFormation/{reconstructionContext}".format(
            reconstructionContext=reconstruction_context,
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
    reconstruction_context: str,
    *,
    client: AuthenticatedClient,
    destination_value: str,
    origin_value: str,
    destination_type: Union[
        Unset, None, GetTrainFormationByReconstructionContextDestinationType
    ] = GetTrainFormationByReconstructionContextDestinationType.STATION,
    origin_type: Union[
        Unset, None, GetTrainFormationByReconstructionContextOriginType
    ] = GetTrainFormationByReconstructionContextOriginType.STATION,
    leaving_direction_enforce_left: Union[Unset, None, bool] = True,
    accept_language: Union[
        Unset, GetTrainFormationByReconstructionContextAcceptLanguage
    ] = GetTrainFormationByReconstructionContextAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Response[Union[JsonResponse, Problem, TrainFormation]]:
    """(SWITCH to v3/trips/{id} &includeTrainStopAssignments!) Get the train-formation (composition of
    wagons) for a specific trip (most successful for SBB vehicles of vehicleType=TRAIN).

     @Deprecated (SWITCH to v3/trips/{id}&Whether `PTRideLeg's` should include `CompoundTrain's`(aka
    formation, composition). However, `CompoundTrain's` at any `ScheduledStopPoint` on the
    `ServiceJourney` may be loaded separately by `/v3/vehicle-journeys/by-stoppoints`.
    Possible values:
    - NONE none at all, though a `PTRideLeg::trainStopAssignmentHint` is always given.
    - ORIGIN  `TrainStopAssignment's` are added to first (departure) `ScheduledStopPoint` of each
    `PTRideLeg`
    - ORIGIN_DESTINATION `TrainStopAssignment's` are added to first (departure) and last (arrival)
    `ScheduledStopPoint` of each `PTRideLeg` having a `TrainStopAssignment` resp. a `CompoundTrain`.)!
    Train-formations are considered as daily realtime data and are therefore available TODAY
    only.<br>Assumes the search of a previous trip (by /trips) and tries to reconstruct it by its
    TripV2::reconstructionContext.<br>If successful and the given origin and destination are on the same
    Leg, the relevant train-formations will be determined for origin and destination if available.

    Args:
        reconstruction_context (str):  Example: yA88CgJWMRLmBiVDMiVCNkhLSQkJ8ElUJTI0QSUgM3Mzk-
            BAE=.
        destination_value (str):  Example: 8503000.
        origin_value (str):  Example: 8507000.
        destination_type (Union[Unset, None,
            GetTrainFormationByReconstructionContextDestinationType]):  Default:
            GetTrainFormationByReconstructionContextDestinationType.STATION.
        origin_type (Union[Unset, None, GetTrainFormationByReconstructionContextOriginType]):
            Default: GetTrainFormationByReconstructionContextOriginType.STATION.
        leaving_direction_enforce_left (Union[Unset, None, bool]):  Default: True.
        accept_language (Union[Unset, GetTrainFormationByReconstructionContextAcceptLanguage]):
            Default: GetTrainFormationByReconstructionContextAcceptLanguage.EN.
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[JsonResponse, Problem, TrainFormation]]
    """

    kwargs = _get_kwargs(
        reconstruction_context=reconstruction_context,
        destination_value=destination_value,
        origin_value=origin_value,
        destination_type=destination_type,
        origin_type=origin_type,
        leaving_direction_enforce_left=leaving_direction_enforce_left,
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
    destination_value: str,
    origin_value: str,
    destination_type: Union[
        Unset, None, GetTrainFormationByReconstructionContextDestinationType
    ] = GetTrainFormationByReconstructionContextDestinationType.STATION,
    origin_type: Union[
        Unset, None, GetTrainFormationByReconstructionContextOriginType
    ] = GetTrainFormationByReconstructionContextOriginType.STATION,
    leaving_direction_enforce_left: Union[Unset, None, bool] = True,
    accept_language: Union[
        Unset, GetTrainFormationByReconstructionContextAcceptLanguage
    ] = GetTrainFormationByReconstructionContextAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Optional[Union[JsonResponse, Problem, TrainFormation]]:
    """(SWITCH to v3/trips/{id} &includeTrainStopAssignments!) Get the train-formation (composition of
    wagons) for a specific trip (most successful for SBB vehicles of vehicleType=TRAIN).

     @Deprecated (SWITCH to v3/trips/{id}&Whether `PTRideLeg's` should include `CompoundTrain's`(aka
    formation, composition). However, `CompoundTrain's` at any `ScheduledStopPoint` on the
    `ServiceJourney` may be loaded separately by `/v3/vehicle-journeys/by-stoppoints`.
    Possible values:
    - NONE none at all, though a `PTRideLeg::trainStopAssignmentHint` is always given.
    - ORIGIN  `TrainStopAssignment's` are added to first (departure) `ScheduledStopPoint` of each
    `PTRideLeg`
    - ORIGIN_DESTINATION `TrainStopAssignment's` are added to first (departure) and last (arrival)
    `ScheduledStopPoint` of each `PTRideLeg` having a `TrainStopAssignment` resp. a `CompoundTrain`.)!
    Train-formations are considered as daily realtime data and are therefore available TODAY
    only.<br>Assumes the search of a previous trip (by /trips) and tries to reconstruct it by its
    TripV2::reconstructionContext.<br>If successful and the given origin and destination are on the same
    Leg, the relevant train-formations will be determined for origin and destination if available.

    Args:
        reconstruction_context (str):  Example: yA88CgJWMRLmBiVDMiVCNkhLSQkJ8ElUJTI0QSUgM3Mzk-
            BAE=.
        destination_value (str):  Example: 8503000.
        origin_value (str):  Example: 8507000.
        destination_type (Union[Unset, None,
            GetTrainFormationByReconstructionContextDestinationType]):  Default:
            GetTrainFormationByReconstructionContextDestinationType.STATION.
        origin_type (Union[Unset, None, GetTrainFormationByReconstructionContextOriginType]):
            Default: GetTrainFormationByReconstructionContextOriginType.STATION.
        leaving_direction_enforce_left (Union[Unset, None, bool]):  Default: True.
        accept_language (Union[Unset, GetTrainFormationByReconstructionContextAcceptLanguage]):
            Default: GetTrainFormationByReconstructionContextAcceptLanguage.EN.
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[JsonResponse, Problem, TrainFormation]
    """

    return sync_detailed(
        reconstruction_context=reconstruction_context,
        client=client,
        destination_value=destination_value,
        origin_value=origin_value,
        destination_type=destination_type,
        origin_type=origin_type,
        leaving_direction_enforce_left=leaving_direction_enforce_left,
        accept_language=accept_language,
        request_id=request_id,
    ).parsed


async def asyncio_detailed(
    reconstruction_context: str,
    *,
    client: AuthenticatedClient,
    destination_value: str,
    origin_value: str,
    destination_type: Union[
        Unset, None, GetTrainFormationByReconstructionContextDestinationType
    ] = GetTrainFormationByReconstructionContextDestinationType.STATION,
    origin_type: Union[
        Unset, None, GetTrainFormationByReconstructionContextOriginType
    ] = GetTrainFormationByReconstructionContextOriginType.STATION,
    leaving_direction_enforce_left: Union[Unset, None, bool] = True,
    accept_language: Union[
        Unset, GetTrainFormationByReconstructionContextAcceptLanguage
    ] = GetTrainFormationByReconstructionContextAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Response[Union[JsonResponse, Problem, TrainFormation]]:
    """(SWITCH to v3/trips/{id} &includeTrainStopAssignments!) Get the train-formation (composition of
    wagons) for a specific trip (most successful for SBB vehicles of vehicleType=TRAIN).

     @Deprecated (SWITCH to v3/trips/{id}&Whether `PTRideLeg's` should include `CompoundTrain's`(aka
    formation, composition). However, `CompoundTrain's` at any `ScheduledStopPoint` on the
    `ServiceJourney` may be loaded separately by `/v3/vehicle-journeys/by-stoppoints`.
    Possible values:
    - NONE none at all, though a `PTRideLeg::trainStopAssignmentHint` is always given.
    - ORIGIN  `TrainStopAssignment's` are added to first (departure) `ScheduledStopPoint` of each
    `PTRideLeg`
    - ORIGIN_DESTINATION `TrainStopAssignment's` are added to first (departure) and last (arrival)
    `ScheduledStopPoint` of each `PTRideLeg` having a `TrainStopAssignment` resp. a `CompoundTrain`.)!
    Train-formations are considered as daily realtime data and are therefore available TODAY
    only.<br>Assumes the search of a previous trip (by /trips) and tries to reconstruct it by its
    TripV2::reconstructionContext.<br>If successful and the given origin and destination are on the same
    Leg, the relevant train-formations will be determined for origin and destination if available.

    Args:
        reconstruction_context (str):  Example: yA88CgJWMRLmBiVDMiVCNkhLSQkJ8ElUJTI0QSUgM3Mzk-
            BAE=.
        destination_value (str):  Example: 8503000.
        origin_value (str):  Example: 8507000.
        destination_type (Union[Unset, None,
            GetTrainFormationByReconstructionContextDestinationType]):  Default:
            GetTrainFormationByReconstructionContextDestinationType.STATION.
        origin_type (Union[Unset, None, GetTrainFormationByReconstructionContextOriginType]):
            Default: GetTrainFormationByReconstructionContextOriginType.STATION.
        leaving_direction_enforce_left (Union[Unset, None, bool]):  Default: True.
        accept_language (Union[Unset, GetTrainFormationByReconstructionContextAcceptLanguage]):
            Default: GetTrainFormationByReconstructionContextAcceptLanguage.EN.
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[JsonResponse, Problem, TrainFormation]]
    """

    kwargs = _get_kwargs(
        reconstruction_context=reconstruction_context,
        destination_value=destination_value,
        origin_value=origin_value,
        destination_type=destination_type,
        origin_type=origin_type,
        leaving_direction_enforce_left=leaving_direction_enforce_left,
        accept_language=accept_language,
        request_id=request_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    reconstruction_context: str,
    *,
    client: AuthenticatedClient,
    destination_value: str,
    origin_value: str,
    destination_type: Union[
        Unset, None, GetTrainFormationByReconstructionContextDestinationType
    ] = GetTrainFormationByReconstructionContextDestinationType.STATION,
    origin_type: Union[
        Unset, None, GetTrainFormationByReconstructionContextOriginType
    ] = GetTrainFormationByReconstructionContextOriginType.STATION,
    leaving_direction_enforce_left: Union[Unset, None, bool] = True,
    accept_language: Union[
        Unset, GetTrainFormationByReconstructionContextAcceptLanguage
    ] = GetTrainFormationByReconstructionContextAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Optional[Union[JsonResponse, Problem, TrainFormation]]:
    """(SWITCH to v3/trips/{id} &includeTrainStopAssignments!) Get the train-formation (composition of
    wagons) for a specific trip (most successful for SBB vehicles of vehicleType=TRAIN).

     @Deprecated (SWITCH to v3/trips/{id}&Whether `PTRideLeg's` should include `CompoundTrain's`(aka
    formation, composition). However, `CompoundTrain's` at any `ScheduledStopPoint` on the
    `ServiceJourney` may be loaded separately by `/v3/vehicle-journeys/by-stoppoints`.
    Possible values:
    - NONE none at all, though a `PTRideLeg::trainStopAssignmentHint` is always given.
    - ORIGIN  `TrainStopAssignment's` are added to first (departure) `ScheduledStopPoint` of each
    `PTRideLeg`
    - ORIGIN_DESTINATION `TrainStopAssignment's` are added to first (departure) and last (arrival)
    `ScheduledStopPoint` of each `PTRideLeg` having a `TrainStopAssignment` resp. a `CompoundTrain`.)!
    Train-formations are considered as daily realtime data and are therefore available TODAY
    only.<br>Assumes the search of a previous trip (by /trips) and tries to reconstruct it by its
    TripV2::reconstructionContext.<br>If successful and the given origin and destination are on the same
    Leg, the relevant train-formations will be determined for origin and destination if available.

    Args:
        reconstruction_context (str):  Example: yA88CgJWMRLmBiVDMiVCNkhLSQkJ8ElUJTI0QSUgM3Mzk-
            BAE=.
        destination_value (str):  Example: 8503000.
        origin_value (str):  Example: 8507000.
        destination_type (Union[Unset, None,
            GetTrainFormationByReconstructionContextDestinationType]):  Default:
            GetTrainFormationByReconstructionContextDestinationType.STATION.
        origin_type (Union[Unset, None, GetTrainFormationByReconstructionContextOriginType]):
            Default: GetTrainFormationByReconstructionContextOriginType.STATION.
        leaving_direction_enforce_left (Union[Unset, None, bool]):  Default: True.
        accept_language (Union[Unset, GetTrainFormationByReconstructionContextAcceptLanguage]):
            Default: GetTrainFormationByReconstructionContextAcceptLanguage.EN.
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[JsonResponse, Problem, TrainFormation]
    """

    return (
        await asyncio_detailed(
            reconstruction_context=reconstruction_context,
            client=client,
            destination_value=destination_value,
            origin_value=origin_value,
            destination_type=destination_type,
            origin_type=origin_type,
            leaving_direction_enforce_left=leaving_direction_enforce_left,
            accept_language=accept_language,
            request_id=request_id,
        )
    ).parsed
