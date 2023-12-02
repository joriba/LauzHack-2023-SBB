from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.feature_collection import FeatureCollection
from ...models.mot import Mot
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    calculate_midpoint: Union[Unset, None, bool] = UNSET,
    from_station_id: Union[Unset, None, int] = UNSET,
    generalization: Union[Unset, None, bool] = UNSET,
    mot: Union[Unset, None, Mot] = UNSET,
    to_station_id: Union[Unset, None, int] = UNSET,
    via: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["calculateMidpoint"] = calculate_midpoint

    params["fromStationID"] = from_station_id

    params["generalization"] = generalization

    json_mot: Union[Unset, None, str] = UNSET
    if not isinstance(mot, Unset):
        json_mot = mot.value if mot else None

    params["mot"] = json_mot

    params["toStationID"] = to_station_id

    params["via"] = via

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/v1/route",
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
    calculate_midpoint: Union[Unset, None, bool] = UNSET,
    from_station_id: Union[Unset, None, int] = UNSET,
    generalization: Union[Unset, None, bool] = UNSET,
    mot: Union[Unset, None, Mot] = UNSET,
    to_station_id: Union[Unset, None, int] = UNSET,
    via: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, FeatureCollection]]:
    """Provides a geographical representation of a train route from start to destination with optional
    vias.

    Args:
        calculate_midpoint (Union[Unset, None, bool]):
        from_station_id (Union[Unset, None, int]):
        generalization (Union[Unset, None, bool]):
        mot (Union[Unset, None, Mot]):
        to_station_id (Union[Unset, None, int]):
        via (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, FeatureCollection]]
    """

    kwargs = _get_kwargs(
        calculate_midpoint=calculate_midpoint,
        from_station_id=from_station_id,
        generalization=generalization,
        mot=mot,
        to_station_id=to_station_id,
        via=via,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    calculate_midpoint: Union[Unset, None, bool] = UNSET,
    from_station_id: Union[Unset, None, int] = UNSET,
    generalization: Union[Unset, None, bool] = UNSET,
    mot: Union[Unset, None, Mot] = UNSET,
    to_station_id: Union[Unset, None, int] = UNSET,
    via: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, FeatureCollection]]:
    """Provides a geographical representation of a train route from start to destination with optional
    vias.

    Args:
        calculate_midpoint (Union[Unset, None, bool]):
        from_station_id (Union[Unset, None, int]):
        generalization (Union[Unset, None, bool]):
        mot (Union[Unset, None, Mot]):
        to_station_id (Union[Unset, None, int]):
        via (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, FeatureCollection]
    """

    return sync_detailed(
        client=client,
        calculate_midpoint=calculate_midpoint,
        from_station_id=from_station_id,
        generalization=generalization,
        mot=mot,
        to_station_id=to_station_id,
        via=via,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    calculate_midpoint: Union[Unset, None, bool] = UNSET,
    from_station_id: Union[Unset, None, int] = UNSET,
    generalization: Union[Unset, None, bool] = UNSET,
    mot: Union[Unset, None, Mot] = UNSET,
    to_station_id: Union[Unset, None, int] = UNSET,
    via: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, FeatureCollection]]:
    """Provides a geographical representation of a train route from start to destination with optional
    vias.

    Args:
        calculate_midpoint (Union[Unset, None, bool]):
        from_station_id (Union[Unset, None, int]):
        generalization (Union[Unset, None, bool]):
        mot (Union[Unset, None, Mot]):
        to_station_id (Union[Unset, None, int]):
        via (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, FeatureCollection]]
    """

    kwargs = _get_kwargs(
        calculate_midpoint=calculate_midpoint,
        from_station_id=from_station_id,
        generalization=generalization,
        mot=mot,
        to_station_id=to_station_id,
        via=via,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    calculate_midpoint: Union[Unset, None, bool] = UNSET,
    from_station_id: Union[Unset, None, int] = UNSET,
    generalization: Union[Unset, None, bool] = UNSET,
    mot: Union[Unset, None, Mot] = UNSET,
    to_station_id: Union[Unset, None, int] = UNSET,
    via: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, FeatureCollection]]:
    """Provides a geographical representation of a train route from start to destination with optional
    vias.

    Args:
        calculate_midpoint (Union[Unset, None, bool]):
        from_station_id (Union[Unset, None, int]):
        generalization (Union[Unset, None, bool]):
        mot (Union[Unset, None, Mot]):
        to_station_id (Union[Unset, None, int]):
        via (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, FeatureCollection]
    """

    return (
        await asyncio_detailed(
            client=client,
            calculate_midpoint=calculate_midpoint,
            from_station_id=from_station_id,
            generalization=generalization,
            mot=mot,
            to_station_id=to_station_id,
            via=via,
        )
    ).parsed
