import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.audience_enum import AudienceEnum
from ...models.get_situations_by_validity_accept_language import GetSituationsByValidityAcceptLanguage
from ...models.get_situations_by_validity_affected_scope import GetSituationsByValidityAffectedScope
from ...models.problem import Problem
from ...models.situation_cause_enum import SituationCauseEnum
from ...models.situation_response import SituationResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    valid_from_date: Union[Unset, None, datetime.date] = UNSET,
    valid_from_time: Union[Unset, None, str] = UNSET,
    valid_to_date: Union[Unset, None, datetime.date] = UNSET,
    valid_to_time: Union[Unset, None, str] = UNSET,
    affected_scope: Union[Unset, None, GetSituationsByValidityAffectedScope] = UNSET,
    cause: Union[Unset, None, SituationCauseEnum] = UNSET,
    audience: Union[Unset, None, AudienceEnum] = AudienceEnum.B2C_TEXT,
    title: Union[Unset, None, str] = UNSET,
    priority_min: Union[Unset, None, int] = 0,
    priority_max: Union[Unset, None, int] = 40,
    include_projection: Union[Unset, None, bool] = False,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, GetSituationsByValidityAcceptLanguage] = GetSituationsByValidityAcceptLanguage.EN,
) -> Dict[str, Any]:
    headers = {}
    if not isinstance(request_id, Unset):
        headers["Request-ID"] = request_id

    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = str(accept_language)

    params: Dict[str, Any] = {}
    json_valid_from_date: Union[Unset, None, str] = UNSET
    if not isinstance(valid_from_date, Unset):
        json_valid_from_date = valid_from_date.isoformat() if valid_from_date else None

    params["validFromDate"] = json_valid_from_date

    params["validFromTime"] = valid_from_time

    json_valid_to_date: Union[Unset, None, str] = UNSET
    if not isinstance(valid_to_date, Unset):
        json_valid_to_date = valid_to_date.isoformat() if valid_to_date else None

    params["validToDate"] = json_valid_to_date

    params["validToTime"] = valid_to_time

    json_affected_scope: Union[Unset, None, str] = UNSET
    if not isinstance(affected_scope, Unset):
        json_affected_scope = affected_scope.value if affected_scope else None

    params["affectedScope"] = json_affected_scope

    json_cause: Union[Unset, None, str] = UNSET
    if not isinstance(cause, Unset):
        json_cause = cause.value if cause else None

    params["cause"] = json_cause

    json_audience: Union[Unset, None, str] = UNSET
    if not isinstance(audience, Unset):
        json_audience = audience.value if audience else None

    params["audience"] = json_audience

    params["title"] = title

    params["priorityMin"] = priority_min

    params["priorityMax"] = priority_max

    params["includeProjection"] = include_projection

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/v3/situations/by-validity",
        "params": params,
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Problem, SituationResponse]]:
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = Problem.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.OK:
        response_200 = SituationResponse.from_dict(response.json())

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
) -> Response[Union[Problem, SituationResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    valid_from_date: Union[Unset, None, datetime.date] = UNSET,
    valid_from_time: Union[Unset, None, str] = UNSET,
    valid_to_date: Union[Unset, None, datetime.date] = UNSET,
    valid_to_time: Union[Unset, None, str] = UNSET,
    affected_scope: Union[Unset, None, GetSituationsByValidityAffectedScope] = UNSET,
    cause: Union[Unset, None, SituationCauseEnum] = UNSET,
    audience: Union[Unset, None, AudienceEnum] = AudienceEnum.B2C_TEXT,
    title: Union[Unset, None, str] = UNSET,
    priority_min: Union[Unset, None, int] = 0,
    priority_max: Union[Unset, None, int] = 40,
    include_projection: Union[Unset, None, bool] = False,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, GetSituationsByValidityAcceptLanguage] = GetSituationsByValidityAcceptLanguage.EN,
) -> Response[Union[Problem, SituationResponse]]:
    """Get situation-messages within the given time interval.

     Lists active situation-messages within a publication window provided by SBB HIM.

    Args:
        valid_from_date (Union[Unset, None, datetime.date]):  Example: 2023-04-18.
        valid_from_time (Union[Unset, None, str]):  Example: 13:07.
        valid_to_date (Union[Unset, None, datetime.date]):  Example: 2023-04-18.
        valid_to_time (Union[Unset, None, str]):  Example: 13:07.
        affected_scope (Union[Unset, None, GetSituationsByValidityAffectedScope]):
        cause (Union[Unset, None, SituationCauseEnum]):
        audience (Union[Unset, None, AudienceEnum]): Enum whose values can be extended, thus
            default case should be foreseen wenn parsing the response (in Java, avoid `valueOf`,
            prefer `switch` with the value's name and define a default). You may become unexpected
            values if your client is out-of-sync.  Default: AudienceEnum.B2C_TEXT.
        title (Union[Unset, None, str]):
        priority_min (Union[Unset, None, int]):
        priority_max (Union[Unset, None, int]):  Default: 40.
        include_projection (Union[Unset, None, bool]):
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetSituationsByValidityAcceptLanguage]):  Default:
            GetSituationsByValidityAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Problem, SituationResponse]]
    """

    kwargs = _get_kwargs(
        valid_from_date=valid_from_date,
        valid_from_time=valid_from_time,
        valid_to_date=valid_to_date,
        valid_to_time=valid_to_time,
        affected_scope=affected_scope,
        cause=cause,
        audience=audience,
        title=title,
        priority_min=priority_min,
        priority_max=priority_max,
        include_projection=include_projection,
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
    valid_from_date: Union[Unset, None, datetime.date] = UNSET,
    valid_from_time: Union[Unset, None, str] = UNSET,
    valid_to_date: Union[Unset, None, datetime.date] = UNSET,
    valid_to_time: Union[Unset, None, str] = UNSET,
    affected_scope: Union[Unset, None, GetSituationsByValidityAffectedScope] = UNSET,
    cause: Union[Unset, None, SituationCauseEnum] = UNSET,
    audience: Union[Unset, None, AudienceEnum] = AudienceEnum.B2C_TEXT,
    title: Union[Unset, None, str] = UNSET,
    priority_min: Union[Unset, None, int] = 0,
    priority_max: Union[Unset, None, int] = 40,
    include_projection: Union[Unset, None, bool] = False,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, GetSituationsByValidityAcceptLanguage] = GetSituationsByValidityAcceptLanguage.EN,
) -> Optional[Union[Problem, SituationResponse]]:
    """Get situation-messages within the given time interval.

     Lists active situation-messages within a publication window provided by SBB HIM.

    Args:
        valid_from_date (Union[Unset, None, datetime.date]):  Example: 2023-04-18.
        valid_from_time (Union[Unset, None, str]):  Example: 13:07.
        valid_to_date (Union[Unset, None, datetime.date]):  Example: 2023-04-18.
        valid_to_time (Union[Unset, None, str]):  Example: 13:07.
        affected_scope (Union[Unset, None, GetSituationsByValidityAffectedScope]):
        cause (Union[Unset, None, SituationCauseEnum]):
        audience (Union[Unset, None, AudienceEnum]): Enum whose values can be extended, thus
            default case should be foreseen wenn parsing the response (in Java, avoid `valueOf`,
            prefer `switch` with the value's name and define a default). You may become unexpected
            values if your client is out-of-sync.  Default: AudienceEnum.B2C_TEXT.
        title (Union[Unset, None, str]):
        priority_min (Union[Unset, None, int]):
        priority_max (Union[Unset, None, int]):  Default: 40.
        include_projection (Union[Unset, None, bool]):
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetSituationsByValidityAcceptLanguage]):  Default:
            GetSituationsByValidityAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Problem, SituationResponse]
    """

    return sync_detailed(
        client=client,
        valid_from_date=valid_from_date,
        valid_from_time=valid_from_time,
        valid_to_date=valid_to_date,
        valid_to_time=valid_to_time,
        affected_scope=affected_scope,
        cause=cause,
        audience=audience,
        title=title,
        priority_min=priority_min,
        priority_max=priority_max,
        include_projection=include_projection,
        request_id=request_id,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    valid_from_date: Union[Unset, None, datetime.date] = UNSET,
    valid_from_time: Union[Unset, None, str] = UNSET,
    valid_to_date: Union[Unset, None, datetime.date] = UNSET,
    valid_to_time: Union[Unset, None, str] = UNSET,
    affected_scope: Union[Unset, None, GetSituationsByValidityAffectedScope] = UNSET,
    cause: Union[Unset, None, SituationCauseEnum] = UNSET,
    audience: Union[Unset, None, AudienceEnum] = AudienceEnum.B2C_TEXT,
    title: Union[Unset, None, str] = UNSET,
    priority_min: Union[Unset, None, int] = 0,
    priority_max: Union[Unset, None, int] = 40,
    include_projection: Union[Unset, None, bool] = False,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, GetSituationsByValidityAcceptLanguage] = GetSituationsByValidityAcceptLanguage.EN,
) -> Response[Union[Problem, SituationResponse]]:
    """Get situation-messages within the given time interval.

     Lists active situation-messages within a publication window provided by SBB HIM.

    Args:
        valid_from_date (Union[Unset, None, datetime.date]):  Example: 2023-04-18.
        valid_from_time (Union[Unset, None, str]):  Example: 13:07.
        valid_to_date (Union[Unset, None, datetime.date]):  Example: 2023-04-18.
        valid_to_time (Union[Unset, None, str]):  Example: 13:07.
        affected_scope (Union[Unset, None, GetSituationsByValidityAffectedScope]):
        cause (Union[Unset, None, SituationCauseEnum]):
        audience (Union[Unset, None, AudienceEnum]): Enum whose values can be extended, thus
            default case should be foreseen wenn parsing the response (in Java, avoid `valueOf`,
            prefer `switch` with the value's name and define a default). You may become unexpected
            values if your client is out-of-sync.  Default: AudienceEnum.B2C_TEXT.
        title (Union[Unset, None, str]):
        priority_min (Union[Unset, None, int]):
        priority_max (Union[Unset, None, int]):  Default: 40.
        include_projection (Union[Unset, None, bool]):
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetSituationsByValidityAcceptLanguage]):  Default:
            GetSituationsByValidityAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Problem, SituationResponse]]
    """

    kwargs = _get_kwargs(
        valid_from_date=valid_from_date,
        valid_from_time=valid_from_time,
        valid_to_date=valid_to_date,
        valid_to_time=valid_to_time,
        affected_scope=affected_scope,
        cause=cause,
        audience=audience,
        title=title,
        priority_min=priority_min,
        priority_max=priority_max,
        include_projection=include_projection,
        request_id=request_id,
        accept_language=accept_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    valid_from_date: Union[Unset, None, datetime.date] = UNSET,
    valid_from_time: Union[Unset, None, str] = UNSET,
    valid_to_date: Union[Unset, None, datetime.date] = UNSET,
    valid_to_time: Union[Unset, None, str] = UNSET,
    affected_scope: Union[Unset, None, GetSituationsByValidityAffectedScope] = UNSET,
    cause: Union[Unset, None, SituationCauseEnum] = UNSET,
    audience: Union[Unset, None, AudienceEnum] = AudienceEnum.B2C_TEXT,
    title: Union[Unset, None, str] = UNSET,
    priority_min: Union[Unset, None, int] = 0,
    priority_max: Union[Unset, None, int] = 40,
    include_projection: Union[Unset, None, bool] = False,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, GetSituationsByValidityAcceptLanguage] = GetSituationsByValidityAcceptLanguage.EN,
) -> Optional[Union[Problem, SituationResponse]]:
    """Get situation-messages within the given time interval.

     Lists active situation-messages within a publication window provided by SBB HIM.

    Args:
        valid_from_date (Union[Unset, None, datetime.date]):  Example: 2023-04-18.
        valid_from_time (Union[Unset, None, str]):  Example: 13:07.
        valid_to_date (Union[Unset, None, datetime.date]):  Example: 2023-04-18.
        valid_to_time (Union[Unset, None, str]):  Example: 13:07.
        affected_scope (Union[Unset, None, GetSituationsByValidityAffectedScope]):
        cause (Union[Unset, None, SituationCauseEnum]):
        audience (Union[Unset, None, AudienceEnum]): Enum whose values can be extended, thus
            default case should be foreseen wenn parsing the response (in Java, avoid `valueOf`,
            prefer `switch` with the value's name and define a default). You may become unexpected
            values if your client is out-of-sync.  Default: AudienceEnum.B2C_TEXT.
        title (Union[Unset, None, str]):
        priority_min (Union[Unset, None, int]):
        priority_max (Union[Unset, None, int]):  Default: 40.
        include_projection (Union[Unset, None, bool]):
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetSituationsByValidityAcceptLanguage]):  Default:
            GetSituationsByValidityAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Problem, SituationResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            valid_from_date=valid_from_date,
            valid_from_time=valid_from_time,
            valid_to_date=valid_to_date,
            valid_to_time=valid_to_time,
            affected_scope=affected_scope,
            cause=cause,
            audience=audience,
            title=title,
            priority_min=priority_min,
            priority_max=priority_max,
            include_projection=include_projection,
            request_id=request_id,
            accept_language=accept_language,
        )
    ).parsed
