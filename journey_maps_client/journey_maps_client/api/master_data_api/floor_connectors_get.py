from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.feature_collection import FeatureCollection
from ...models.floor_connector_type import FloorConnectorType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    station: int,
    platform: int,
    *,
    types: Union[Unset, None, List[FloorConnectorType]] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    json_types: Union[Unset, None, List[str]] = UNSET
    if not isinstance(types, Unset):
        if types is None:
            json_types = None
        else:
            json_types = []
            for types_item_data in types:
                types_item = types_item_data.value

                json_types.append(types_item)

    params["types"] = json_types

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/v1/master-data/stations/{station}/platforms/{platform}/floor-connectors".format(
            station=station,
            platform=platform,
        ),
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, List["FeatureCollection"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = FeatureCollection.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[Union[Any, List["FeatureCollection"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    station: int,
    platform: int,
    *,
    client: Union[AuthenticatedClient, Client],
    types: Union[Unset, None, List[FloorConnectorType]] = UNSET,
) -> Response[Union[Any, List["FeatureCollection"]]]:
    """Provides all floor connectors in a stations on a specific platform (de: Gleis).

    Args:
        station (int):
        platform (int):
        types (Union[Unset, None, List[FloorConnectorType]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['FeatureCollection']]]
    """

    kwargs = _get_kwargs(
        station=station,
        platform=platform,
        types=types,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    station: int,
    platform: int,
    *,
    client: Union[AuthenticatedClient, Client],
    types: Union[Unset, None, List[FloorConnectorType]] = UNSET,
) -> Optional[Union[Any, List["FeatureCollection"]]]:
    """Provides all floor connectors in a stations on a specific platform (de: Gleis).

    Args:
        station (int):
        platform (int):
        types (Union[Unset, None, List[FloorConnectorType]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['FeatureCollection']]
    """

    return sync_detailed(
        station=station,
        platform=platform,
        client=client,
        types=types,
    ).parsed


async def asyncio_detailed(
    station: int,
    platform: int,
    *,
    client: Union[AuthenticatedClient, Client],
    types: Union[Unset, None, List[FloorConnectorType]] = UNSET,
) -> Response[Union[Any, List["FeatureCollection"]]]:
    """Provides all floor connectors in a stations on a specific platform (de: Gleis).

    Args:
        station (int):
        platform (int):
        types (Union[Unset, None, List[FloorConnectorType]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['FeatureCollection']]]
    """

    kwargs = _get_kwargs(
        station=station,
        platform=platform,
        types=types,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    station: int,
    platform: int,
    *,
    client: Union[AuthenticatedClient, Client],
    types: Union[Unset, None, List[FloorConnectorType]] = UNSET,
) -> Optional[Union[Any, List["FeatureCollection"]]]:
    """Provides all floor connectors in a stations on a specific platform (de: Gleis).

    Args:
        station (int):
        platform (int):
        types (Union[Unset, None, List[FloorConnectorType]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['FeatureCollection']]
    """

    return (
        await asyncio_detailed(
            station=station,
            platform=platform,
            client=client,
            types=types,
        )
    ).parsed
