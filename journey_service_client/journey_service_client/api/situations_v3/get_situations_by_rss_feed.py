from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.audience_enum import AudienceEnum
from ...models.get_situations_by_rss_feed_accept_language import GetSituationsByRSSFeedAcceptLanguage
from ...models.get_situations_by_rss_feed_language import GetSituationsByRSSFeedLanguage
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    language: Union[Unset, None, GetSituationsByRSSFeedLanguage] = GetSituationsByRSSFeedLanguage.EN,
    causes: Union[Unset, None, List[str]] = UNSET,
    audience: Union[Unset, None, AudienceEnum] = AudienceEnum.B2C_TEXT,
    priority_min: Union[Unset, None, int] = 0,
    priority_max: Union[Unset, None, int] = 40,
    affected_regions: Union[Unset, None, List[str]] = UNSET,
    accept_language: Union[Unset, GetSituationsByRSSFeedAcceptLanguage] = GetSituationsByRSSFeedAcceptLanguage.EN,
) -> Dict[str, Any]:
    headers = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = str(accept_language)

    params: Dict[str, Any] = {}
    json_language: Union[Unset, None, str] = UNSET
    if not isinstance(language, Unset):
        json_language = language.value if language else None

    params["language"] = json_language

    json_causes: Union[Unset, None, List[str]] = UNSET
    if not isinstance(causes, Unset):
        if causes is None:
            json_causes = None
        else:
            json_causes = causes

    params["causes"] = json_causes

    json_audience: Union[Unset, None, str] = UNSET
    if not isinstance(audience, Unset):
        json_audience = audience.value if audience else None

    params["audience"] = json_audience

    params["priorityMin"] = priority_min

    params["priorityMax"] = priority_max

    json_affected_regions: Union[Unset, None, List[str]] = UNSET
    if not isinstance(affected_regions, Unset):
        if affected_regions is None:
            json_affected_regions = None
        else:
            json_affected_regions = affected_regions

    params["affectedRegions"] = json_affected_regions

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/v3/situations/by-rss-feed",
        "params": params,
        "headers": headers,
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Problem]:
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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    language: Union[Unset, None, GetSituationsByRSSFeedLanguage] = GetSituationsByRSSFeedLanguage.EN,
    causes: Union[Unset, None, List[str]] = UNSET,
    audience: Union[Unset, None, AudienceEnum] = AudienceEnum.B2C_TEXT,
    priority_min: Union[Unset, None, int] = 0,
    priority_max: Union[Unset, None, int] = 40,
    affected_regions: Union[Unset, None, List[str]] = UNSET,
    accept_language: Union[Unset, GetSituationsByRSSFeedAcceptLanguage] = GetSituationsByRSSFeedAcceptLanguage.EN,
) -> Response[Problem]:
    """Get `PTSituationMessage's` by RSS-Feed.

     Lists active situation-messages within a publication window provided by SBB HIM. Format: RSS-Feed as
    an XML 1.0 dialect, see [Web content: Really Simple
    Syndication](https://validator.w3.org/feed/docs/rss2.html#requiredChannelElements).

    Args:
        language (Union[Unset, None, GetSituationsByRSSFeedLanguage]):  Default:
            GetSituationsByRSSFeedLanguage.EN.
        causes (Union[Unset, None, List[str]]):
        audience (Union[Unset, None, AudienceEnum]): Enum whose values can be extended, thus
            default case should be foreseen wenn parsing the response (in Java, avoid `valueOf`,
            prefer `switch` with the value's name and define a default). You may become unexpected
            values if your client is out-of-sync.  Default: AudienceEnum.B2C_TEXT.
        priority_min (Union[Unset, None, int]):
        priority_max (Union[Unset, None, int]):  Default: 40.
        affected_regions (Union[Unset, None, List[str]]):
        accept_language (Union[Unset, GetSituationsByRSSFeedAcceptLanguage]):  Default:
            GetSituationsByRSSFeedAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem]
    """

    kwargs = _get_kwargs(
        language=language,
        causes=causes,
        audience=audience,
        priority_min=priority_min,
        priority_max=priority_max,
        affected_regions=affected_regions,
        accept_language=accept_language,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    language: Union[Unset, None, GetSituationsByRSSFeedLanguage] = GetSituationsByRSSFeedLanguage.EN,
    causes: Union[Unset, None, List[str]] = UNSET,
    audience: Union[Unset, None, AudienceEnum] = AudienceEnum.B2C_TEXT,
    priority_min: Union[Unset, None, int] = 0,
    priority_max: Union[Unset, None, int] = 40,
    affected_regions: Union[Unset, None, List[str]] = UNSET,
    accept_language: Union[Unset, GetSituationsByRSSFeedAcceptLanguage] = GetSituationsByRSSFeedAcceptLanguage.EN,
) -> Optional[Problem]:
    """Get `PTSituationMessage's` by RSS-Feed.

     Lists active situation-messages within a publication window provided by SBB HIM. Format: RSS-Feed as
    an XML 1.0 dialect, see [Web content: Really Simple
    Syndication](https://validator.w3.org/feed/docs/rss2.html#requiredChannelElements).

    Args:
        language (Union[Unset, None, GetSituationsByRSSFeedLanguage]):  Default:
            GetSituationsByRSSFeedLanguage.EN.
        causes (Union[Unset, None, List[str]]):
        audience (Union[Unset, None, AudienceEnum]): Enum whose values can be extended, thus
            default case should be foreseen wenn parsing the response (in Java, avoid `valueOf`,
            prefer `switch` with the value's name and define a default). You may become unexpected
            values if your client is out-of-sync.  Default: AudienceEnum.B2C_TEXT.
        priority_min (Union[Unset, None, int]):
        priority_max (Union[Unset, None, int]):  Default: 40.
        affected_regions (Union[Unset, None, List[str]]):
        accept_language (Union[Unset, GetSituationsByRSSFeedAcceptLanguage]):  Default:
            GetSituationsByRSSFeedAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem
    """

    return sync_detailed(
        client=client,
        language=language,
        causes=causes,
        audience=audience,
        priority_min=priority_min,
        priority_max=priority_max,
        affected_regions=affected_regions,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    language: Union[Unset, None, GetSituationsByRSSFeedLanguage] = GetSituationsByRSSFeedLanguage.EN,
    causes: Union[Unset, None, List[str]] = UNSET,
    audience: Union[Unset, None, AudienceEnum] = AudienceEnum.B2C_TEXT,
    priority_min: Union[Unset, None, int] = 0,
    priority_max: Union[Unset, None, int] = 40,
    affected_regions: Union[Unset, None, List[str]] = UNSET,
    accept_language: Union[Unset, GetSituationsByRSSFeedAcceptLanguage] = GetSituationsByRSSFeedAcceptLanguage.EN,
) -> Response[Problem]:
    """Get `PTSituationMessage's` by RSS-Feed.

     Lists active situation-messages within a publication window provided by SBB HIM. Format: RSS-Feed as
    an XML 1.0 dialect, see [Web content: Really Simple
    Syndication](https://validator.w3.org/feed/docs/rss2.html#requiredChannelElements).

    Args:
        language (Union[Unset, None, GetSituationsByRSSFeedLanguage]):  Default:
            GetSituationsByRSSFeedLanguage.EN.
        causes (Union[Unset, None, List[str]]):
        audience (Union[Unset, None, AudienceEnum]): Enum whose values can be extended, thus
            default case should be foreseen wenn parsing the response (in Java, avoid `valueOf`,
            prefer `switch` with the value's name and define a default). You may become unexpected
            values if your client is out-of-sync.  Default: AudienceEnum.B2C_TEXT.
        priority_min (Union[Unset, None, int]):
        priority_max (Union[Unset, None, int]):  Default: 40.
        affected_regions (Union[Unset, None, List[str]]):
        accept_language (Union[Unset, GetSituationsByRSSFeedAcceptLanguage]):  Default:
            GetSituationsByRSSFeedAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem]
    """

    kwargs = _get_kwargs(
        language=language,
        causes=causes,
        audience=audience,
        priority_min=priority_min,
        priority_max=priority_max,
        affected_regions=affected_regions,
        accept_language=accept_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    language: Union[Unset, None, GetSituationsByRSSFeedLanguage] = GetSituationsByRSSFeedLanguage.EN,
    causes: Union[Unset, None, List[str]] = UNSET,
    audience: Union[Unset, None, AudienceEnum] = AudienceEnum.B2C_TEXT,
    priority_min: Union[Unset, None, int] = 0,
    priority_max: Union[Unset, None, int] = 40,
    affected_regions: Union[Unset, None, List[str]] = UNSET,
    accept_language: Union[Unset, GetSituationsByRSSFeedAcceptLanguage] = GetSituationsByRSSFeedAcceptLanguage.EN,
) -> Optional[Problem]:
    """Get `PTSituationMessage's` by RSS-Feed.

     Lists active situation-messages within a publication window provided by SBB HIM. Format: RSS-Feed as
    an XML 1.0 dialect, see [Web content: Really Simple
    Syndication](https://validator.w3.org/feed/docs/rss2.html#requiredChannelElements).

    Args:
        language (Union[Unset, None, GetSituationsByRSSFeedLanguage]):  Default:
            GetSituationsByRSSFeedLanguage.EN.
        causes (Union[Unset, None, List[str]]):
        audience (Union[Unset, None, AudienceEnum]): Enum whose values can be extended, thus
            default case should be foreseen wenn parsing the response (in Java, avoid `valueOf`,
            prefer `switch` with the value's name and define a default). You may become unexpected
            values if your client is out-of-sync.  Default: AudienceEnum.B2C_TEXT.
        priority_min (Union[Unset, None, int]):
        priority_max (Union[Unset, None, int]):  Default: 40.
        affected_regions (Union[Unset, None, List[str]]):
        accept_language (Union[Unset, GetSituationsByRSSFeedAcceptLanguage]):  Default:
            GetSituationsByRSSFeedAcceptLanguage.EN.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            language=language,
            causes=causes,
            audience=audience,
            priority_min=priority_min,
            priority_max=priority_max,
            affected_regions=affected_regions,
            accept_language=accept_language,
        )
    ).parsed
