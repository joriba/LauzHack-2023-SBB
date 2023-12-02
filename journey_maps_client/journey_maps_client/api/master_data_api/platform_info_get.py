from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.feature_collection import FeatureCollection
from ...models.floor_connector_type import FloorConnectorType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    station: float,
    platform: Union[float, str],
    *,
    sectors: Union[Unset, None, str] = UNSET,
    nearby_sector: Union[Unset, None, str] = UNSET,
    floor_connector_types: Union[Unset, None, List[FloorConnectorType]] = UNSET,
    details: Union[Unset, None, bool] = False,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["sectors"] = sectors

    params["nearby-sector"] = nearby_sector

    json_floor_connector_types: Union[Unset, None, List[str]] = UNSET
    if not isinstance(floor_connector_types, Unset):
        if floor_connector_types is None:
            json_floor_connector_types = None
        else:
            json_floor_connector_types = []
            for floor_connector_types_item_data in floor_connector_types:
                floor_connector_types_item = floor_connector_types_item_data.value

                json_floor_connector_types.append(floor_connector_types_item)

    params["floor-connector-types"] = json_floor_connector_types

    params["details"] = details

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/v1/master-data/stations/{station}/platforms/{platform}/platform-info".format(
            station=station,
            platform=platform,
        ),
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
    station: float,
    platform: Union[float, str],
    *,
    client: Union[AuthenticatedClient, Client],
    sectors: Union[Unset, None, str] = UNSET,
    nearby_sector: Union[Unset, None, str] = UNSET,
    floor_connector_types: Union[Unset, None, List[FloorConnectorType]] = UNSET,
    details: Union[Unset, None, bool] = False,
) -> Response[Union[Any, FeatureCollection]]:
    """Calculates the midpoint of an entire platform or of its sectors
    as well as the floor-connectors that are reachable from this midpoint.
    The direction to the floor connectors is either LEFT, RIGHT, or NONE, and is
    calculated from the perspective of someone exiting the train
    at the position of the calculated midpoint.

    Args:
        station (float):
        platform (Union[float, str]):
        sectors (Union[Unset, None, str]):
        nearby_sector (Union[Unset, None, str]):
        floor_connector_types (Union[Unset, None, List[FloorConnectorType]]):
        details (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, FeatureCollection]]
    """

    kwargs = _get_kwargs(
        station=station,
        platform=platform,
        sectors=sectors,
        nearby_sector=nearby_sector,
        floor_connector_types=floor_connector_types,
        details=details,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    station: float,
    platform: Union[float, str],
    *,
    client: Union[AuthenticatedClient, Client],
    sectors: Union[Unset, None, str] = UNSET,
    nearby_sector: Union[Unset, None, str] = UNSET,
    floor_connector_types: Union[Unset, None, List[FloorConnectorType]] = UNSET,
    details: Union[Unset, None, bool] = False,
) -> Optional[Union[Any, FeatureCollection]]:
    """Calculates the midpoint of an entire platform or of its sectors
    as well as the floor-connectors that are reachable from this midpoint.
    The direction to the floor connectors is either LEFT, RIGHT, or NONE, and is
    calculated from the perspective of someone exiting the train
    at the position of the calculated midpoint.

    Args:
        station (float):
        platform (Union[float, str]):
        sectors (Union[Unset, None, str]):
        nearby_sector (Union[Unset, None, str]):
        floor_connector_types (Union[Unset, None, List[FloorConnectorType]]):
        details (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, FeatureCollection]
    """

    return sync_detailed(
        station=station,
        platform=platform,
        client=client,
        sectors=sectors,
        nearby_sector=nearby_sector,
        floor_connector_types=floor_connector_types,
        details=details,
    ).parsed


async def asyncio_detailed(
    station: float,
    platform: Union[float, str],
    *,
    client: Union[AuthenticatedClient, Client],
    sectors: Union[Unset, None, str] = UNSET,
    nearby_sector: Union[Unset, None, str] = UNSET,
    floor_connector_types: Union[Unset, None, List[FloorConnectorType]] = UNSET,
    details: Union[Unset, None, bool] = False,
) -> Response[Union[Any, FeatureCollection]]:
    """Calculates the midpoint of an entire platform or of its sectors
    as well as the floor-connectors that are reachable from this midpoint.
    The direction to the floor connectors is either LEFT, RIGHT, or NONE, and is
    calculated from the perspective of someone exiting the train
    at the position of the calculated midpoint.

    Args:
        station (float):
        platform (Union[float, str]):
        sectors (Union[Unset, None, str]):
        nearby_sector (Union[Unset, None, str]):
        floor_connector_types (Union[Unset, None, List[FloorConnectorType]]):
        details (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, FeatureCollection]]
    """

    kwargs = _get_kwargs(
        station=station,
        platform=platform,
        sectors=sectors,
        nearby_sector=nearby_sector,
        floor_connector_types=floor_connector_types,
        details=details,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    station: float,
    platform: Union[float, str],
    *,
    client: Union[AuthenticatedClient, Client],
    sectors: Union[Unset, None, str] = UNSET,
    nearby_sector: Union[Unset, None, str] = UNSET,
    floor_connector_types: Union[Unset, None, List[FloorConnectorType]] = UNSET,
    details: Union[Unset, None, bool] = False,
) -> Optional[Union[Any, FeatureCollection]]:
    """Calculates the midpoint of an entire platform or of its sectors
    as well as the floor-connectors that are reachable from this midpoint.
    The direction to the floor connectors is either LEFT, RIGHT, or NONE, and is
    calculated from the perspective of someone exiting the train
    at the position of the calculated midpoint.

    Args:
        station (float):
        platform (Union[float, str]):
        sectors (Union[Unset, None, str]):
        nearby_sector (Union[Unset, None, str]):
        floor_connector_types (Union[Unset, None, List[FloorConnectorType]]):
        details (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, FeatureCollection]
    """

    return (
        await asyncio_detailed(
            station=station,
            platform=platform,
            client=client,
            sectors=sectors,
            nearby_sector=nearby_sector,
            floor_connector_types=floor_connector_types,
            details=details,
        )
    ).parsed
