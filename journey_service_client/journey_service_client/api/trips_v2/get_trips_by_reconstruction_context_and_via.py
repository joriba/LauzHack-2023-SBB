from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_trips_by_reconstruction_context_and_via_accept_language import (
    GetTripsByReconstructionContextAndViaAcceptLanguage,
)
from ...models.get_trips_by_reconstruction_context_and_via_infos import GetTripsByReconstructionContextAndViaInfos
from ...models.get_trips_by_reconstruction_context_and_via_response_501 import (
    GetTripsByReconstructionContextAndViaResponse501,
)
from ...models.get_trips_by_reconstruction_context_and_via_stop_behaviour import (
    GetTripsByReconstructionContextAndViaStopBehaviour,
)
from ...models.problem import Problem
from ...models.trip_v2 import TripV2
from ...types import UNSET, Response, Unset


def _get_kwargs(
    reconstruction_context: str,
    via_value: str,
    *,
    create_summary: Union[Unset, None, bool] = False,
    infos: Union[Unset, None, GetTripsByReconstructionContextAndViaInfos] = UNSET,
    polyline: Union[Unset, None, bool] = False,
    stop_behaviour: Union[
        Unset, None, GetTripsByReconstructionContextAndViaStopBehaviour
    ] = GetTripsByReconstructionContextAndViaStopBehaviour.REAL_BOARDING_ALIGHTING,
    via_depart_later: Union[Unset, None, bool] = True,
    via_journey_reference: Union[Unset, None, str] = UNSET,
    accept_language: Union[
        Unset, GetTripsByReconstructionContextAndViaAcceptLanguage
    ] = GetTripsByReconstructionContextAndViaAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = str(accept_language)

    if not isinstance(request_id, Unset):
        headers["Request-ID"] = request_id

    params: Dict[str, Any] = {}
    params["createSummary"] = create_summary

    json_infos: Union[Unset, None, str] = UNSET
    if not isinstance(infos, Unset):
        json_infos = infos.value if infos else None

    params["infos"] = json_infos

    params["polyline"] = polyline

    json_stop_behaviour: Union[Unset, None, str] = UNSET
    if not isinstance(stop_behaviour, Unset):
        json_stop_behaviour = stop_behaviour.value if stop_behaviour else None

    params["stopBehaviour"] = json_stop_behaviour

    params["viaDepartLater"] = via_depart_later

    params["viaJourneyReference"] = via_journey_reference

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/b2c/v2/INCUBATOR/trips/{reconstructionContext}/{viaValue}".format(
            reconstructionContext=reconstruction_context,
            viaValue=via_value,
        ),
        "params": params,
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[GetTripsByReconstructionContextAndViaResponse501, List["TripV2"], Problem]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = TripV2.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = Problem.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.NOT_IMPLEMENTED:
        response_501 = GetTripsByReconstructionContextAndViaResponse501.from_dict(response.json())

        return response_501
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[GetTripsByReconstructionContextAndViaResponse501, List["TripV2"], Problem]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    reconstruction_context: str,
    via_value: str,
    *,
    client: AuthenticatedClient,
    create_summary: Union[Unset, None, bool] = False,
    infos: Union[Unset, None, GetTripsByReconstructionContextAndViaInfos] = UNSET,
    polyline: Union[Unset, None, bool] = False,
    stop_behaviour: Union[
        Unset, None, GetTripsByReconstructionContextAndViaStopBehaviour
    ] = GetTripsByReconstructionContextAndViaStopBehaviour.REAL_BOARDING_ALIGHTING,
    via_depart_later: Union[Unset, None, bool] = True,
    via_journey_reference: Union[Unset, None, str] = UNSET,
    accept_language: Union[
        Unset, GetTripsByReconstructionContextAndViaAcceptLanguage
    ] = GetTripsByReconstructionContextAndViaAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Response[Union[GetTripsByReconstructionContextAndViaResponse501, List["TripV2"], Problem]]:
    """@Deprecated (SWITCH to v3/trips/{id}/{viaEarlierLaterContext})! Get alternate trip (list with 2
    entries: [alternateTrip, originTrip]) with alternate leg proposals at given Via earlier or later
    (aka Partial-Search).

     Useful to find alternate trip with earlier arrival or later departure for desired Via.<br>Scroll-
    Context cannot be provided in this case.

    Args:
        reconstruction_context (str):  Example: yA88CgJWMRLmBiVDMiVCNkhLSQkJ8ElUJTI0QSUgM3Mzk-
            BAE=.
        via_value (str):  Example: 8507000.
        create_summary (Union[Unset, None, bool]):
        infos (Union[Unset, None, GetTripsByReconstructionContextAndViaInfos]):
        polyline (Union[Unset, None, bool]):
        stop_behaviour (Union[Unset, None, GetTripsByReconstructionContextAndViaStopBehaviour]):
            Default: GetTripsByReconstructionContextAndViaStopBehaviour.REAL_BOARDING_ALIGHTING.
        via_depart_later (Union[Unset, None, bool]):  Default: True.
        via_journey_reference (Union[Unset, None, str]):  Example: 1|17166|0|85|18032019.
        accept_language (Union[Unset, GetTripsByReconstructionContextAndViaAcceptLanguage]):
            Default: GetTripsByReconstructionContextAndViaAcceptLanguage.EN.
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetTripsByReconstructionContextAndViaResponse501, List['TripV2'], Problem]]
    """

    kwargs = _get_kwargs(
        reconstruction_context=reconstruction_context,
        via_value=via_value,
        create_summary=create_summary,
        infos=infos,
        polyline=polyline,
        stop_behaviour=stop_behaviour,
        via_depart_later=via_depart_later,
        via_journey_reference=via_journey_reference,
        accept_language=accept_language,
        request_id=request_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    reconstruction_context: str,
    via_value: str,
    *,
    client: AuthenticatedClient,
    create_summary: Union[Unset, None, bool] = False,
    infos: Union[Unset, None, GetTripsByReconstructionContextAndViaInfos] = UNSET,
    polyline: Union[Unset, None, bool] = False,
    stop_behaviour: Union[
        Unset, None, GetTripsByReconstructionContextAndViaStopBehaviour
    ] = GetTripsByReconstructionContextAndViaStopBehaviour.REAL_BOARDING_ALIGHTING,
    via_depart_later: Union[Unset, None, bool] = True,
    via_journey_reference: Union[Unset, None, str] = UNSET,
    accept_language: Union[
        Unset, GetTripsByReconstructionContextAndViaAcceptLanguage
    ] = GetTripsByReconstructionContextAndViaAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Optional[Union[GetTripsByReconstructionContextAndViaResponse501, List["TripV2"], Problem]]:
    """@Deprecated (SWITCH to v3/trips/{id}/{viaEarlierLaterContext})! Get alternate trip (list with 2
    entries: [alternateTrip, originTrip]) with alternate leg proposals at given Via earlier or later
    (aka Partial-Search).

     Useful to find alternate trip with earlier arrival or later departure for desired Via.<br>Scroll-
    Context cannot be provided in this case.

    Args:
        reconstruction_context (str):  Example: yA88CgJWMRLmBiVDMiVCNkhLSQkJ8ElUJTI0QSUgM3Mzk-
            BAE=.
        via_value (str):  Example: 8507000.
        create_summary (Union[Unset, None, bool]):
        infos (Union[Unset, None, GetTripsByReconstructionContextAndViaInfos]):
        polyline (Union[Unset, None, bool]):
        stop_behaviour (Union[Unset, None, GetTripsByReconstructionContextAndViaStopBehaviour]):
            Default: GetTripsByReconstructionContextAndViaStopBehaviour.REAL_BOARDING_ALIGHTING.
        via_depart_later (Union[Unset, None, bool]):  Default: True.
        via_journey_reference (Union[Unset, None, str]):  Example: 1|17166|0|85|18032019.
        accept_language (Union[Unset, GetTripsByReconstructionContextAndViaAcceptLanguage]):
            Default: GetTripsByReconstructionContextAndViaAcceptLanguage.EN.
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetTripsByReconstructionContextAndViaResponse501, List['TripV2'], Problem]
    """

    return sync_detailed(
        reconstruction_context=reconstruction_context,
        via_value=via_value,
        client=client,
        create_summary=create_summary,
        infos=infos,
        polyline=polyline,
        stop_behaviour=stop_behaviour,
        via_depart_later=via_depart_later,
        via_journey_reference=via_journey_reference,
        accept_language=accept_language,
        request_id=request_id,
    ).parsed


async def asyncio_detailed(
    reconstruction_context: str,
    via_value: str,
    *,
    client: AuthenticatedClient,
    create_summary: Union[Unset, None, bool] = False,
    infos: Union[Unset, None, GetTripsByReconstructionContextAndViaInfos] = UNSET,
    polyline: Union[Unset, None, bool] = False,
    stop_behaviour: Union[
        Unset, None, GetTripsByReconstructionContextAndViaStopBehaviour
    ] = GetTripsByReconstructionContextAndViaStopBehaviour.REAL_BOARDING_ALIGHTING,
    via_depart_later: Union[Unset, None, bool] = True,
    via_journey_reference: Union[Unset, None, str] = UNSET,
    accept_language: Union[
        Unset, GetTripsByReconstructionContextAndViaAcceptLanguage
    ] = GetTripsByReconstructionContextAndViaAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Response[Union[GetTripsByReconstructionContextAndViaResponse501, List["TripV2"], Problem]]:
    """@Deprecated (SWITCH to v3/trips/{id}/{viaEarlierLaterContext})! Get alternate trip (list with 2
    entries: [alternateTrip, originTrip]) with alternate leg proposals at given Via earlier or later
    (aka Partial-Search).

     Useful to find alternate trip with earlier arrival or later departure for desired Via.<br>Scroll-
    Context cannot be provided in this case.

    Args:
        reconstruction_context (str):  Example: yA88CgJWMRLmBiVDMiVCNkhLSQkJ8ElUJTI0QSUgM3Mzk-
            BAE=.
        via_value (str):  Example: 8507000.
        create_summary (Union[Unset, None, bool]):
        infos (Union[Unset, None, GetTripsByReconstructionContextAndViaInfos]):
        polyline (Union[Unset, None, bool]):
        stop_behaviour (Union[Unset, None, GetTripsByReconstructionContextAndViaStopBehaviour]):
            Default: GetTripsByReconstructionContextAndViaStopBehaviour.REAL_BOARDING_ALIGHTING.
        via_depart_later (Union[Unset, None, bool]):  Default: True.
        via_journey_reference (Union[Unset, None, str]):  Example: 1|17166|0|85|18032019.
        accept_language (Union[Unset, GetTripsByReconstructionContextAndViaAcceptLanguage]):
            Default: GetTripsByReconstructionContextAndViaAcceptLanguage.EN.
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetTripsByReconstructionContextAndViaResponse501, List['TripV2'], Problem]]
    """

    kwargs = _get_kwargs(
        reconstruction_context=reconstruction_context,
        via_value=via_value,
        create_summary=create_summary,
        infos=infos,
        polyline=polyline,
        stop_behaviour=stop_behaviour,
        via_depart_later=via_depart_later,
        via_journey_reference=via_journey_reference,
        accept_language=accept_language,
        request_id=request_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    reconstruction_context: str,
    via_value: str,
    *,
    client: AuthenticatedClient,
    create_summary: Union[Unset, None, bool] = False,
    infos: Union[Unset, None, GetTripsByReconstructionContextAndViaInfos] = UNSET,
    polyline: Union[Unset, None, bool] = False,
    stop_behaviour: Union[
        Unset, None, GetTripsByReconstructionContextAndViaStopBehaviour
    ] = GetTripsByReconstructionContextAndViaStopBehaviour.REAL_BOARDING_ALIGHTING,
    via_depart_later: Union[Unset, None, bool] = True,
    via_journey_reference: Union[Unset, None, str] = UNSET,
    accept_language: Union[
        Unset, GetTripsByReconstructionContextAndViaAcceptLanguage
    ] = GetTripsByReconstructionContextAndViaAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Optional[Union[GetTripsByReconstructionContextAndViaResponse501, List["TripV2"], Problem]]:
    """@Deprecated (SWITCH to v3/trips/{id}/{viaEarlierLaterContext})! Get alternate trip (list with 2
    entries: [alternateTrip, originTrip]) with alternate leg proposals at given Via earlier or later
    (aka Partial-Search).

     Useful to find alternate trip with earlier arrival or later departure for desired Via.<br>Scroll-
    Context cannot be provided in this case.

    Args:
        reconstruction_context (str):  Example: yA88CgJWMRLmBiVDMiVCNkhLSQkJ8ElUJTI0QSUgM3Mzk-
            BAE=.
        via_value (str):  Example: 8507000.
        create_summary (Union[Unset, None, bool]):
        infos (Union[Unset, None, GetTripsByReconstructionContextAndViaInfos]):
        polyline (Union[Unset, None, bool]):
        stop_behaviour (Union[Unset, None, GetTripsByReconstructionContextAndViaStopBehaviour]):
            Default: GetTripsByReconstructionContextAndViaStopBehaviour.REAL_BOARDING_ALIGHTING.
        via_depart_later (Union[Unset, None, bool]):  Default: True.
        via_journey_reference (Union[Unset, None, str]):  Example: 1|17166|0|85|18032019.
        accept_language (Union[Unset, GetTripsByReconstructionContextAndViaAcceptLanguage]):
            Default: GetTripsByReconstructionContextAndViaAcceptLanguage.EN.
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetTripsByReconstructionContextAndViaResponse501, List['TripV2'], Problem]
    """

    return (
        await asyncio_detailed(
            reconstruction_context=reconstruction_context,
            via_value=via_value,
            client=client,
            create_summary=create_summary,
            infos=infos,
            polyline=polyline,
            stop_behaviour=stop_behaviour,
            via_depart_later=via_depart_later,
            via_journey_reference=via_journey_reference,
            accept_language=accept_language,
            request_id=request_id,
        )
    ).parsed
