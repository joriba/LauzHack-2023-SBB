from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.audience_enum import AudienceEnum
from ...models.get_situations_by_ids_accept_language import GetSituationsByIdsAcceptLanguage
from ...models.problem import Problem
from ...models.situation_response import SituationResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    ids: List[str],
    *,
    audience: Union[Unset, None, AudienceEnum] = AudienceEnum.B2C_TEXT,
    include_projection: Union[Unset, None, bool] = False,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, GetSituationsByIdsAcceptLanguage] = GetSituationsByIdsAcceptLanguage.EN,
) -> Dict[str, Any]:
    headers = {}
    if not isinstance(request_id, Unset):
        headers["Request-ID"] = request_id

    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = str(accept_language)

    params: Dict[str, Any] = {}
    json_audience: Union[Unset, None, str] = UNSET
    if not isinstance(audience, Unset):
        json_audience = audience.value if audience else None

    params["audience"] = json_audience

    params["includeProjection"] = include_projection

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/v3/situations/{ids}".format(
            ids=ids,
        ),
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
    ids: List[str],
    *,
    client: AuthenticatedClient,
    audience: Union[Unset, None, AudienceEnum] = AudienceEnum.B2C_TEXT,
    include_projection: Union[Unset, None, bool] = False,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, GetSituationsByIdsAcceptLanguage] = GetSituationsByIdsAcceptLanguage.EN,
) -> Response[Union[Problem, SituationResponse]]:
    """Get situation-messages by Id (referencing HIM messages).

     Lists active situation-messages within a publication window provided by SBB HIM.

    Args:
        ids (List[str]):
        audience (Union[Unset, None, AudienceEnum]): Enum whose values can be extended, thus
            default case should be foreseen wenn parsing the response (in Java, avoid `valueOf`,
            prefer `switch` with the value's name and define a default). You may become unexpected
            values if your client is out-of-sync.  Default: AudienceEnum.B2C_TEXT.
        include_projection (Union[Unset, None, bool]):
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetSituationsByIdsAcceptLanguage]):  Default:
            GetSituationsByIdsAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Problem, SituationResponse]]
    """

    kwargs = _get_kwargs(
        ids=ids,
        audience=audience,
        include_projection=include_projection,
        request_id=request_id,
        accept_language=accept_language,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    ids: List[str],
    *,
    client: AuthenticatedClient,
    audience: Union[Unset, None, AudienceEnum] = AudienceEnum.B2C_TEXT,
    include_projection: Union[Unset, None, bool] = False,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, GetSituationsByIdsAcceptLanguage] = GetSituationsByIdsAcceptLanguage.EN,
) -> Optional[Union[Problem, SituationResponse]]:
    """Get situation-messages by Id (referencing HIM messages).

     Lists active situation-messages within a publication window provided by SBB HIM.

    Args:
        ids (List[str]):
        audience (Union[Unset, None, AudienceEnum]): Enum whose values can be extended, thus
            default case should be foreseen wenn parsing the response (in Java, avoid `valueOf`,
            prefer `switch` with the value's name and define a default). You may become unexpected
            values if your client is out-of-sync.  Default: AudienceEnum.B2C_TEXT.
        include_projection (Union[Unset, None, bool]):
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetSituationsByIdsAcceptLanguage]):  Default:
            GetSituationsByIdsAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Problem, SituationResponse]
    """

    return sync_detailed(
        ids=ids,
        client=client,
        audience=audience,
        include_projection=include_projection,
        request_id=request_id,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    ids: List[str],
    *,
    client: AuthenticatedClient,
    audience: Union[Unset, None, AudienceEnum] = AudienceEnum.B2C_TEXT,
    include_projection: Union[Unset, None, bool] = False,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, GetSituationsByIdsAcceptLanguage] = GetSituationsByIdsAcceptLanguage.EN,
) -> Response[Union[Problem, SituationResponse]]:
    """Get situation-messages by Id (referencing HIM messages).

     Lists active situation-messages within a publication window provided by SBB HIM.

    Args:
        ids (List[str]):
        audience (Union[Unset, None, AudienceEnum]): Enum whose values can be extended, thus
            default case should be foreseen wenn parsing the response (in Java, avoid `valueOf`,
            prefer `switch` with the value's name and define a default). You may become unexpected
            values if your client is out-of-sync.  Default: AudienceEnum.B2C_TEXT.
        include_projection (Union[Unset, None, bool]):
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetSituationsByIdsAcceptLanguage]):  Default:
            GetSituationsByIdsAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Problem, SituationResponse]]
    """

    kwargs = _get_kwargs(
        ids=ids,
        audience=audience,
        include_projection=include_projection,
        request_id=request_id,
        accept_language=accept_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    ids: List[str],
    *,
    client: AuthenticatedClient,
    audience: Union[Unset, None, AudienceEnum] = AudienceEnum.B2C_TEXT,
    include_projection: Union[Unset, None, bool] = False,
    request_id: Union[Unset, str] = UNSET,
    accept_language: Union[Unset, GetSituationsByIdsAcceptLanguage] = GetSituationsByIdsAcceptLanguage.EN,
) -> Optional[Union[Problem, SituationResponse]]:
    """Get situation-messages by Id (referencing HIM messages).

     Lists active situation-messages within a publication window provided by SBB HIM.

    Args:
        ids (List[str]):
        audience (Union[Unset, None, AudienceEnum]): Enum whose values can be extended, thus
            default case should be foreseen wenn parsing the response (in Java, avoid `valueOf`,
            prefer `switch` with the value's name and define a default). You may become unexpected
            values if your client is out-of-sync.  Default: AudienceEnum.B2C_TEXT.
        include_projection (Union[Unset, None, bool]):
        request_id (Union[Unset, str]):
        accept_language (Union[Unset, GetSituationsByIdsAcceptLanguage]):  Default:
            GetSituationsByIdsAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Problem, SituationResponse]
    """

    return (
        await asyncio_detailed(
            ids=ids,
            client=client,
            audience=audience,
            include_projection=include_projection,
            request_id=request_id,
            accept_language=accept_language,
        )
    ).parsed
