from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.feature_collection import FeatureCollection
from ...models.transfer_get_lang import TransferGetLang
from ...models.transport_type import TransportType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client_query: str,
    client_version: str,
    from_sector_labels: Union[Unset, None, List[str]] = UNSET,
    from_direction: Union[Unset, None, str] = UNSET,
    from_is_disruption: Union[Unset, None, bool] = False,
    from_lat_lng: Union[Unset, None, str] = UNSET,
    from_line: Union[Unset, None, str] = UNSET,
    from_name: Union[Unset, None, str] = UNSET,
    from_station_id: Union[Unset, None, int] = UNSET,
    from_track: Union[Unset, None, str] = UNSET,
    from_transport_type: Union[Unset, None, TransportType] = UNSET,
    indoor: Union[Unset, None, bool] = UNSET,
    lang: TransferGetLang,
    to_direction: Union[Unset, None, str] = UNSET,
    to_is_disruption: Union[Unset, None, bool] = False,
    to_lat_lng: Union[Unset, None, str] = UNSET,
    to_line: Union[Unset, None, str] = UNSET,
    to_name: Union[Unset, None, str] = UNSET,
    to_sector_labels: Union[Unset, None, List[str]] = UNSET,
    to_station_id: Union[Unset, None, int] = UNSET,
    to_track: Union[Unset, None, str] = UNSET,
    to_transport_type: Union[Unset, None, TransportType] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["client"] = client_query

    params["clientVersion"] = client_version

    json_from_sector_labels: Union[Unset, None, List[str]] = UNSET
    if not isinstance(from_sector_labels, Unset):
        if from_sector_labels is None:
            json_from_sector_labels = None
        else:
            json_from_sector_labels = from_sector_labels

    params["fromSectorLabels"] = json_from_sector_labels

    params["fromDirection"] = from_direction

    params["fromIsDisruption"] = from_is_disruption

    params["fromLatLng"] = from_lat_lng

    params["fromLine"] = from_line

    params["fromName"] = from_name

    params["fromStationID"] = from_station_id

    params["fromTrack"] = from_track

    json_from_transport_type: Union[Unset, None, str] = UNSET
    if not isinstance(from_transport_type, Unset):
        json_from_transport_type = from_transport_type.value if from_transport_type else None

    params["fromTransportType"] = json_from_transport_type

    params["indoor"] = indoor

    json_lang = lang.value

    params["lang"] = json_lang

    params["toDirection"] = to_direction

    params["toIsDisruption"] = to_is_disruption

    params["toLatLng"] = to_lat_lng

    params["toLine"] = to_line

    params["toName"] = to_name

    json_to_sector_labels: Union[Unset, None, List[str]] = UNSET
    if not isinstance(to_sector_labels, Unset):
        if to_sector_labels is None:
            json_to_sector_labels = None
        else:
            json_to_sector_labels = to_sector_labels

    params["toSectorLabels"] = json_to_sector_labels

    params["toStationID"] = to_station_id

    params["toTrack"] = to_track

    json_to_transport_type: Union[Unset, None, str] = UNSET
    if not isinstance(to_transport_type, Unset):
        json_to_transport_type = to_transport_type.value if to_transport_type else None

    params["toTransportType"] = json_to_transport_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/v1/transfer",
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
    client_query: str,
    client_version: str,
    from_sector_labels: Union[Unset, None, List[str]] = UNSET,
    from_direction: Union[Unset, None, str] = UNSET,
    from_is_disruption: Union[Unset, None, bool] = False,
    from_lat_lng: Union[Unset, None, str] = UNSET,
    from_line: Union[Unset, None, str] = UNSET,
    from_name: Union[Unset, None, str] = UNSET,
    from_station_id: Union[Unset, None, int] = UNSET,
    from_track: Union[Unset, None, str] = UNSET,
    from_transport_type: Union[Unset, None, TransportType] = UNSET,
    indoor: Union[Unset, None, bool] = UNSET,
    lang: TransferGetLang,
    to_direction: Union[Unset, None, str] = UNSET,
    to_is_disruption: Union[Unset, None, bool] = False,
    to_lat_lng: Union[Unset, None, str] = UNSET,
    to_line: Union[Unset, None, str] = UNSET,
    to_name: Union[Unset, None, str] = UNSET,
    to_sector_labels: Union[Unset, None, List[str]] = UNSET,
    to_station_id: Union[Unset, None, int] = UNSET,
    to_track: Union[Unset, None, str] = UNSET,
    to_transport_type: Union[Unset, None, TransportType] = UNSET,
) -> Response[Union[Any, FeatureCollection]]:
    """Provides an enriched geographical representation of a transfer including ROKAS enhanced pedestrian
    routing.

     Try it: https://journey-maps.api.sbb.ch:443/v1/transfer?client=sbb-mobile-web-prod&clientVersion=1&c
    rs=4326&fromDirection=Horw%2C%20Biregghof&fromLine=7&fromName=Luzern%2C%20Bahnhof&fromStationID=8508
    450&fromTrack=A&fromTransportType=bus&lang=de&toDirection=Emmenbr%C3%BCcke%2C%20Sprengi&toLine=2&toN
    ame=Luzern%2C%20Bahnhof&toStationID=8508450&toTrack=F&toTransportType=bus

    Args:
        client_query (str):
        client_version (str):
        from_sector_labels (Union[Unset, None, List[str]]):
        from_direction (Union[Unset, None, str]):
        from_is_disruption (Union[Unset, None, bool]):
        from_lat_lng (Union[Unset, None, str]):
        from_line (Union[Unset, None, str]):
        from_name (Union[Unset, None, str]):
        from_station_id (Union[Unset, None, int]):
        from_track (Union[Unset, None, str]):
        from_transport_type (Union[Unset, None, TransportType]):
        indoor (Union[Unset, None, bool]):
        lang (TransferGetLang):
        to_direction (Union[Unset, None, str]):
        to_is_disruption (Union[Unset, None, bool]):
        to_lat_lng (Union[Unset, None, str]):
        to_line (Union[Unset, None, str]):
        to_name (Union[Unset, None, str]):
        to_sector_labels (Union[Unset, None, List[str]]):
        to_station_id (Union[Unset, None, int]):
        to_track (Union[Unset, None, str]):
        to_transport_type (Union[Unset, None, TransportType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, FeatureCollection]]
    """

    kwargs = _get_kwargs(
        client_query=client_query,
        client_version=client_version,
        from_sector_labels=from_sector_labels,
        from_direction=from_direction,
        from_is_disruption=from_is_disruption,
        from_lat_lng=from_lat_lng,
        from_line=from_line,
        from_name=from_name,
        from_station_id=from_station_id,
        from_track=from_track,
        from_transport_type=from_transport_type,
        indoor=indoor,
        lang=lang,
        to_direction=to_direction,
        to_is_disruption=to_is_disruption,
        to_lat_lng=to_lat_lng,
        to_line=to_line,
        to_name=to_name,
        to_sector_labels=to_sector_labels,
        to_station_id=to_station_id,
        to_track=to_track,
        to_transport_type=to_transport_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    client_query: str,
    client_version: str,
    from_sector_labels: Union[Unset, None, List[str]] = UNSET,
    from_direction: Union[Unset, None, str] = UNSET,
    from_is_disruption: Union[Unset, None, bool] = False,
    from_lat_lng: Union[Unset, None, str] = UNSET,
    from_line: Union[Unset, None, str] = UNSET,
    from_name: Union[Unset, None, str] = UNSET,
    from_station_id: Union[Unset, None, int] = UNSET,
    from_track: Union[Unset, None, str] = UNSET,
    from_transport_type: Union[Unset, None, TransportType] = UNSET,
    indoor: Union[Unset, None, bool] = UNSET,
    lang: TransferGetLang,
    to_direction: Union[Unset, None, str] = UNSET,
    to_is_disruption: Union[Unset, None, bool] = False,
    to_lat_lng: Union[Unset, None, str] = UNSET,
    to_line: Union[Unset, None, str] = UNSET,
    to_name: Union[Unset, None, str] = UNSET,
    to_sector_labels: Union[Unset, None, List[str]] = UNSET,
    to_station_id: Union[Unset, None, int] = UNSET,
    to_track: Union[Unset, None, str] = UNSET,
    to_transport_type: Union[Unset, None, TransportType] = UNSET,
) -> Optional[Union[Any, FeatureCollection]]:
    """Provides an enriched geographical representation of a transfer including ROKAS enhanced pedestrian
    routing.

     Try it: https://journey-maps.api.sbb.ch:443/v1/transfer?client=sbb-mobile-web-prod&clientVersion=1&c
    rs=4326&fromDirection=Horw%2C%20Biregghof&fromLine=7&fromName=Luzern%2C%20Bahnhof&fromStationID=8508
    450&fromTrack=A&fromTransportType=bus&lang=de&toDirection=Emmenbr%C3%BCcke%2C%20Sprengi&toLine=2&toN
    ame=Luzern%2C%20Bahnhof&toStationID=8508450&toTrack=F&toTransportType=bus

    Args:
        client_query (str):
        client_version (str):
        from_sector_labels (Union[Unset, None, List[str]]):
        from_direction (Union[Unset, None, str]):
        from_is_disruption (Union[Unset, None, bool]):
        from_lat_lng (Union[Unset, None, str]):
        from_line (Union[Unset, None, str]):
        from_name (Union[Unset, None, str]):
        from_station_id (Union[Unset, None, int]):
        from_track (Union[Unset, None, str]):
        from_transport_type (Union[Unset, None, TransportType]):
        indoor (Union[Unset, None, bool]):
        lang (TransferGetLang):
        to_direction (Union[Unset, None, str]):
        to_is_disruption (Union[Unset, None, bool]):
        to_lat_lng (Union[Unset, None, str]):
        to_line (Union[Unset, None, str]):
        to_name (Union[Unset, None, str]):
        to_sector_labels (Union[Unset, None, List[str]]):
        to_station_id (Union[Unset, None, int]):
        to_track (Union[Unset, None, str]):
        to_transport_type (Union[Unset, None, TransportType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, FeatureCollection]
    """

    return sync_detailed(
        client=client,
        client_query=client_query,
        client_version=client_version,
        from_sector_labels=from_sector_labels,
        from_direction=from_direction,
        from_is_disruption=from_is_disruption,
        from_lat_lng=from_lat_lng,
        from_line=from_line,
        from_name=from_name,
        from_station_id=from_station_id,
        from_track=from_track,
        from_transport_type=from_transport_type,
        indoor=indoor,
        lang=lang,
        to_direction=to_direction,
        to_is_disruption=to_is_disruption,
        to_lat_lng=to_lat_lng,
        to_line=to_line,
        to_name=to_name,
        to_sector_labels=to_sector_labels,
        to_station_id=to_station_id,
        to_track=to_track,
        to_transport_type=to_transport_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    client_query: str,
    client_version: str,
    from_sector_labels: Union[Unset, None, List[str]] = UNSET,
    from_direction: Union[Unset, None, str] = UNSET,
    from_is_disruption: Union[Unset, None, bool] = False,
    from_lat_lng: Union[Unset, None, str] = UNSET,
    from_line: Union[Unset, None, str] = UNSET,
    from_name: Union[Unset, None, str] = UNSET,
    from_station_id: Union[Unset, None, int] = UNSET,
    from_track: Union[Unset, None, str] = UNSET,
    from_transport_type: Union[Unset, None, TransportType] = UNSET,
    indoor: Union[Unset, None, bool] = UNSET,
    lang: TransferGetLang,
    to_direction: Union[Unset, None, str] = UNSET,
    to_is_disruption: Union[Unset, None, bool] = False,
    to_lat_lng: Union[Unset, None, str] = UNSET,
    to_line: Union[Unset, None, str] = UNSET,
    to_name: Union[Unset, None, str] = UNSET,
    to_sector_labels: Union[Unset, None, List[str]] = UNSET,
    to_station_id: Union[Unset, None, int] = UNSET,
    to_track: Union[Unset, None, str] = UNSET,
    to_transport_type: Union[Unset, None, TransportType] = UNSET,
) -> Response[Union[Any, FeatureCollection]]:
    """Provides an enriched geographical representation of a transfer including ROKAS enhanced pedestrian
    routing.

     Try it: https://journey-maps.api.sbb.ch:443/v1/transfer?client=sbb-mobile-web-prod&clientVersion=1&c
    rs=4326&fromDirection=Horw%2C%20Biregghof&fromLine=7&fromName=Luzern%2C%20Bahnhof&fromStationID=8508
    450&fromTrack=A&fromTransportType=bus&lang=de&toDirection=Emmenbr%C3%BCcke%2C%20Sprengi&toLine=2&toN
    ame=Luzern%2C%20Bahnhof&toStationID=8508450&toTrack=F&toTransportType=bus

    Args:
        client_query (str):
        client_version (str):
        from_sector_labels (Union[Unset, None, List[str]]):
        from_direction (Union[Unset, None, str]):
        from_is_disruption (Union[Unset, None, bool]):
        from_lat_lng (Union[Unset, None, str]):
        from_line (Union[Unset, None, str]):
        from_name (Union[Unset, None, str]):
        from_station_id (Union[Unset, None, int]):
        from_track (Union[Unset, None, str]):
        from_transport_type (Union[Unset, None, TransportType]):
        indoor (Union[Unset, None, bool]):
        lang (TransferGetLang):
        to_direction (Union[Unset, None, str]):
        to_is_disruption (Union[Unset, None, bool]):
        to_lat_lng (Union[Unset, None, str]):
        to_line (Union[Unset, None, str]):
        to_name (Union[Unset, None, str]):
        to_sector_labels (Union[Unset, None, List[str]]):
        to_station_id (Union[Unset, None, int]):
        to_track (Union[Unset, None, str]):
        to_transport_type (Union[Unset, None, TransportType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, FeatureCollection]]
    """

    kwargs = _get_kwargs(
        client_query=client_query,
        client_version=client_version,
        from_sector_labels=from_sector_labels,
        from_direction=from_direction,
        from_is_disruption=from_is_disruption,
        from_lat_lng=from_lat_lng,
        from_line=from_line,
        from_name=from_name,
        from_station_id=from_station_id,
        from_track=from_track,
        from_transport_type=from_transport_type,
        indoor=indoor,
        lang=lang,
        to_direction=to_direction,
        to_is_disruption=to_is_disruption,
        to_lat_lng=to_lat_lng,
        to_line=to_line,
        to_name=to_name,
        to_sector_labels=to_sector_labels,
        to_station_id=to_station_id,
        to_track=to_track,
        to_transport_type=to_transport_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    client_query: str,
    client_version: str,
    from_sector_labels: Union[Unset, None, List[str]] = UNSET,
    from_direction: Union[Unset, None, str] = UNSET,
    from_is_disruption: Union[Unset, None, bool] = False,
    from_lat_lng: Union[Unset, None, str] = UNSET,
    from_line: Union[Unset, None, str] = UNSET,
    from_name: Union[Unset, None, str] = UNSET,
    from_station_id: Union[Unset, None, int] = UNSET,
    from_track: Union[Unset, None, str] = UNSET,
    from_transport_type: Union[Unset, None, TransportType] = UNSET,
    indoor: Union[Unset, None, bool] = UNSET,
    lang: TransferGetLang,
    to_direction: Union[Unset, None, str] = UNSET,
    to_is_disruption: Union[Unset, None, bool] = False,
    to_lat_lng: Union[Unset, None, str] = UNSET,
    to_line: Union[Unset, None, str] = UNSET,
    to_name: Union[Unset, None, str] = UNSET,
    to_sector_labels: Union[Unset, None, List[str]] = UNSET,
    to_station_id: Union[Unset, None, int] = UNSET,
    to_track: Union[Unset, None, str] = UNSET,
    to_transport_type: Union[Unset, None, TransportType] = UNSET,
) -> Optional[Union[Any, FeatureCollection]]:
    """Provides an enriched geographical representation of a transfer including ROKAS enhanced pedestrian
    routing.

     Try it: https://journey-maps.api.sbb.ch:443/v1/transfer?client=sbb-mobile-web-prod&clientVersion=1&c
    rs=4326&fromDirection=Horw%2C%20Biregghof&fromLine=7&fromName=Luzern%2C%20Bahnhof&fromStationID=8508
    450&fromTrack=A&fromTransportType=bus&lang=de&toDirection=Emmenbr%C3%BCcke%2C%20Sprengi&toLine=2&toN
    ame=Luzern%2C%20Bahnhof&toStationID=8508450&toTrack=F&toTransportType=bus

    Args:
        client_query (str):
        client_version (str):
        from_sector_labels (Union[Unset, None, List[str]]):
        from_direction (Union[Unset, None, str]):
        from_is_disruption (Union[Unset, None, bool]):
        from_lat_lng (Union[Unset, None, str]):
        from_line (Union[Unset, None, str]):
        from_name (Union[Unset, None, str]):
        from_station_id (Union[Unset, None, int]):
        from_track (Union[Unset, None, str]):
        from_transport_type (Union[Unset, None, TransportType]):
        indoor (Union[Unset, None, bool]):
        lang (TransferGetLang):
        to_direction (Union[Unset, None, str]):
        to_is_disruption (Union[Unset, None, bool]):
        to_lat_lng (Union[Unset, None, str]):
        to_line (Union[Unset, None, str]):
        to_name (Union[Unset, None, str]):
        to_sector_labels (Union[Unset, None, List[str]]):
        to_station_id (Union[Unset, None, int]):
        to_track (Union[Unset, None, str]):
        to_transport_type (Union[Unset, None, TransportType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, FeatureCollection]
    """

    return (
        await asyncio_detailed(
            client=client,
            client_query=client_query,
            client_version=client_version,
            from_sector_labels=from_sector_labels,
            from_direction=from_direction,
            from_is_disruption=from_is_disruption,
            from_lat_lng=from_lat_lng,
            from_line=from_line,
            from_name=from_name,
            from_station_id=from_station_id,
            from_track=from_track,
            from_transport_type=from_transport_type,
            indoor=indoor,
            lang=lang,
            to_direction=to_direction,
            to_is_disruption=to_is_disruption,
            to_lat_lng=to_lat_lng,
            to_line=to_line,
            to_name=to_name,
            to_sector_labels=to_sector_labels,
            to_station_id=to_station_id,
            to_track=to_track,
            to_transport_type=to_transport_type,
        )
    ).parsed
