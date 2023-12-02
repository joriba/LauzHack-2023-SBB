import datetime
from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_train_stop_assignments_accept_language import GetTrainStopAssignmentsAcceptLanguage
from ...models.problem import Problem
from ...models.train_stop_assignment_response import TrainStopAssignmentResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    service_product_reference: str,
    operator_number: str,
    operating_day: datetime.date,
    place_references: List[str],
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, GetTrainStopAssignmentsAcceptLanguage] = GetTrainStopAssignmentsAcceptLanguage.EN,
) -> Dict[str, Any]:
    headers = {}
    if not isinstance(request_id, Unset):
        headers["Request-ID"] = request_id

    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = str(accept_language)

    params: Dict[str, Any] = {}
    params["serviceProductReference"] = service_product_reference

    params["operatorNumber"] = operator_number

    json_operating_day = operating_day.isoformat()
    params["operatingDay"] = json_operating_day

    json_place_references = place_references

    params["placeReferences"] = json_place_references

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/v3/vehicle-journeys/by-stoppoints",
        "params": params,
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Problem, TrainStopAssignmentResponse]]:
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = Problem.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.OK:
        response_200 = TrainStopAssignmentResponse.from_dict(response.json())

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
) -> Response[Union[Problem, TrainStopAssignmentResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    service_product_reference: str,
    operator_number: str,
    operating_day: datetime.date,
    place_references: List[str],
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, GetTrainStopAssignmentsAcceptLanguage] = GetTrainStopAssignmentsAcceptLanguage.EN,
) -> Response[Union[Problem, TrainStopAssignmentResponse]]:
    """@Deprecated Use v3/vehicle-journeys/{id}/by-stoppoints instead, API will be removed soon!

     Returns known `TrainStopAssignment's` for the given `ServiceJourney::id` matching the given
    `StopPlace's`, if found, or null otherwise. Returns NOT-FOUND (HTTP 404) if no `TrainStopAssignment'
    is found for any given stop. `StopPlace's` requested must relate to passing `ScheduledStopPoint's`
    on the `ServiceJourney`.

    Args:
        service_product_reference (str):
        operator_number (str):
        operating_day (datetime.date):
        place_references (List[str]):
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetTrainStopAssignmentsAcceptLanguage]):  Default:
            GetTrainStopAssignmentsAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Problem, TrainStopAssignmentResponse]]
    """

    kwargs = _get_kwargs(
        service_product_reference=service_product_reference,
        operator_number=operator_number,
        operating_day=operating_day,
        place_references=place_references,
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
    service_product_reference: str,
    operator_number: str,
    operating_day: datetime.date,
    place_references: List[str],
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, GetTrainStopAssignmentsAcceptLanguage] = GetTrainStopAssignmentsAcceptLanguage.EN,
) -> Optional[Union[Problem, TrainStopAssignmentResponse]]:
    """@Deprecated Use v3/vehicle-journeys/{id}/by-stoppoints instead, API will be removed soon!

     Returns known `TrainStopAssignment's` for the given `ServiceJourney::id` matching the given
    `StopPlace's`, if found, or null otherwise. Returns NOT-FOUND (HTTP 404) if no `TrainStopAssignment'
    is found for any given stop. `StopPlace's` requested must relate to passing `ScheduledStopPoint's`
    on the `ServiceJourney`.

    Args:
        service_product_reference (str):
        operator_number (str):
        operating_day (datetime.date):
        place_references (List[str]):
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetTrainStopAssignmentsAcceptLanguage]):  Default:
            GetTrainStopAssignmentsAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Problem, TrainStopAssignmentResponse]
    """

    return sync_detailed(
        client=client,
        service_product_reference=service_product_reference,
        operator_number=operator_number,
        operating_day=operating_day,
        place_references=place_references,
        request_id=request_id,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    service_product_reference: str,
    operator_number: str,
    operating_day: datetime.date,
    place_references: List[str],
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, GetTrainStopAssignmentsAcceptLanguage] = GetTrainStopAssignmentsAcceptLanguage.EN,
) -> Response[Union[Problem, TrainStopAssignmentResponse]]:
    """@Deprecated Use v3/vehicle-journeys/{id}/by-stoppoints instead, API will be removed soon!

     Returns known `TrainStopAssignment's` for the given `ServiceJourney::id` matching the given
    `StopPlace's`, if found, or null otherwise. Returns NOT-FOUND (HTTP 404) if no `TrainStopAssignment'
    is found for any given stop. `StopPlace's` requested must relate to passing `ScheduledStopPoint's`
    on the `ServiceJourney`.

    Args:
        service_product_reference (str):
        operator_number (str):
        operating_day (datetime.date):
        place_references (List[str]):
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetTrainStopAssignmentsAcceptLanguage]):  Default:
            GetTrainStopAssignmentsAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Problem, TrainStopAssignmentResponse]]
    """

    kwargs = _get_kwargs(
        service_product_reference=service_product_reference,
        operator_number=operator_number,
        operating_day=operating_day,
        place_references=place_references,
        request_id=request_id,
        accept_language=accept_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    service_product_reference: str,
    operator_number: str,
    operating_day: datetime.date,
    place_references: List[str],
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, GetTrainStopAssignmentsAcceptLanguage] = GetTrainStopAssignmentsAcceptLanguage.EN,
) -> Optional[Union[Problem, TrainStopAssignmentResponse]]:
    """@Deprecated Use v3/vehicle-journeys/{id}/by-stoppoints instead, API will be removed soon!

     Returns known `TrainStopAssignment's` for the given `ServiceJourney::id` matching the given
    `StopPlace's`, if found, or null otherwise. Returns NOT-FOUND (HTTP 404) if no `TrainStopAssignment'
    is found for any given stop. `StopPlace's` requested must relate to passing `ScheduledStopPoint's`
    on the `ServiceJourney`.

    Args:
        service_product_reference (str):
        operator_number (str):
        operating_day (datetime.date):
        place_references (List[str]):
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetTrainStopAssignmentsAcceptLanguage]):  Default:
            GetTrainStopAssignmentsAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Problem, TrainStopAssignmentResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            service_product_reference=service_product_reference,
            operator_number=operator_number,
            operating_day=operating_day,
            place_references=place_references,
            request_id=request_id,
            accept_language=accept_language,
        )
    ).parsed
