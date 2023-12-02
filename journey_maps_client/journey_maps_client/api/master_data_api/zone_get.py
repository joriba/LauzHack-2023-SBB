from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.feature_collection import FeatureCollection
from ...models.zone_get_type import ZoneGetType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    filter_: Union[Unset, None, str] = UNSET,
    from_: Union[Unset, None, str] = UNSET,
    to: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, ZoneGetType] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["filter"] = filter_

    params["from"] = from_

    params["to"] = to

    json_type: Union[Unset, None, str] = UNSET
    if not isinstance(type, Unset):
        json_type = type.value if type else None

    params["type"] = json_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/v1/master-data/zone",
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, FeatureCollection]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = FeatureCollection.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.NOT_ACCEPTABLE:
        response_406 = cast(Any, None)
        return response_406
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = cast(Any, None)
        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = cast(Any, None)
        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, FeatureCollection]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    filter_: Union[Unset, None, str] = UNSET,
    from_: Union[Unset, None, str] = UNSET,
    to: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, ZoneGetType] = UNSET,
) -> Response[Union[Any, FeatureCollection]]:
    """Provides geographical representations of fare network zones.

    Args:
        filter_ (Union[Unset, None, str]):
        from_ (Union[Unset, None, str]):
        to (Union[Unset, None, str]):
        type (Union[Unset, None, ZoneGetType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, FeatureCollection]]
    """

    kwargs = _get_kwargs(
        filter_=filter_,
        from_=from_,
        to=to,
        type=type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    filter_: Union[Unset, None, str] = UNSET,
    from_: Union[Unset, None, str] = UNSET,
    to: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, ZoneGetType] = UNSET,
) -> Optional[Union[Any, FeatureCollection]]:
    """Provides geographical representations of fare network zones.

    Args:
        filter_ (Union[Unset, None, str]):
        from_ (Union[Unset, None, str]):
        to (Union[Unset, None, str]):
        type (Union[Unset, None, ZoneGetType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, FeatureCollection]
    """

    return sync_detailed(
        client=client,
        filter_=filter_,
        from_=from_,
        to=to,
        type=type,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    filter_: Union[Unset, None, str] = UNSET,
    from_: Union[Unset, None, str] = UNSET,
    to: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, ZoneGetType] = UNSET,
) -> Response[Union[Any, FeatureCollection]]:
    """Provides geographical representations of fare network zones.

    Args:
        filter_ (Union[Unset, None, str]):
        from_ (Union[Unset, None, str]):
        to (Union[Unset, None, str]):
        type (Union[Unset, None, ZoneGetType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, FeatureCollection]]
    """

    kwargs = _get_kwargs(
        filter_=filter_,
        from_=from_,
        to=to,
        type=type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    filter_: Union[Unset, None, str] = UNSET,
    from_: Union[Unset, None, str] = UNSET,
    to: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, ZoneGetType] = UNSET,
) -> Optional[Union[Any, FeatureCollection]]:
    """Provides geographical representations of fare network zones.

    Args:
        filter_ (Union[Unset, None, str]):
        from_ (Union[Unset, None, str]):
        to (Union[Unset, None, str]):
        type (Union[Unset, None, ZoneGetType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, FeatureCollection]
    """

    return (
        await asyncio_detailed(
            client=client,
            filter_=filter_,
            from_=from_,
            to=to,
            type=type,
        )
    ).parsed
