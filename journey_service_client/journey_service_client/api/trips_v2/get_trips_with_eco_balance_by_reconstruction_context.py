from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.eco_map import EcoMap
from ...models.get_trips_with_eco_balance_by_reconstruction_context_accept_language import (
    GetTripsWithEcoBalanceByReconstructionContextAcceptLanguage,
)
from ...models.get_trips_with_eco_balance_by_reconstruction_context_car_class import (
    GetTripsWithEcoBalanceByReconstructionContextCarClass,
)
from ...models.get_trips_with_eco_balance_by_reconstruction_context_car_engine import (
    GetTripsWithEcoBalanceByReconstructionContextCarEngine,
)
from ...models.get_trips_with_eco_balance_by_reconstruction_context_car_euro_norm import (
    GetTripsWithEcoBalanceByReconstructionContextCarEuroNorm,
)
from ...models.get_trips_with_eco_balance_by_reconstruction_context_car_fuel_type import (
    GetTripsWithEcoBalanceByReconstructionContextCarFuelType,
)
from ...models.get_trips_with_eco_balance_by_reconstruction_context_car_load import (
    GetTripsWithEcoBalanceByReconstructionContextCarLoad,
)
from ...models.get_trips_with_eco_balance_by_reconstruction_context_flight_feeder import (
    GetTripsWithEcoBalanceByReconstructionContextFlightFeeder,
)
from ...models.get_trips_with_eco_balance_by_reconstruction_context_flight_load import (
    GetTripsWithEcoBalanceByReconstructionContextFlightLoad,
)
from ...models.get_trips_with_eco_balance_by_reconstruction_context_load import (
    GetTripsWithEcoBalanceByReconstructionContextLoad,
)
from ...models.get_trips_with_eco_balance_by_reconstruction_context_public_transport_load import (
    GetTripsWithEcoBalanceByReconstructionContextPublicTransportLoad,
)
from ...models.json_response import JsonResponse
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    reconstruction_context: str,
    *,
    car_class: Union[
        Unset, None, GetTripsWithEcoBalanceByReconstructionContextCarClass
    ] = GetTripsWithEcoBalanceByReconstructionContextCarClass.MEDIUM_3,
    car_engine: Union[
        Unset, None, GetTripsWithEcoBalanceByReconstructionContextCarEngine
    ] = GetTripsWithEcoBalanceByReconstructionContextCarEngine.AVG,
    car_euro_norm: Union[
        Unset, None, GetTripsWithEcoBalanceByReconstructionContextCarEuroNorm
    ] = GetTripsWithEcoBalanceByReconstructionContextCarEuroNorm.AVG,
    car_fuel_type: Union[
        Unset, None, GetTripsWithEcoBalanceByReconstructionContextCarFuelType
    ] = GetTripsWithEcoBalanceByReconstructionContextCarFuelType.AVG,
    car_load: Union[
        Unset, None, GetTripsWithEcoBalanceByReconstructionContextCarLoad
    ] = GetTripsWithEcoBalanceByReconstructionContextCarLoad.AVG,
    flight_feeder: Union[
        Unset, None, GetTripsWithEcoBalanceByReconstructionContextFlightFeeder
    ] = GetTripsWithEcoBalanceByReconstructionContextFlightFeeder.CAR,
    flight_load: Union[
        Unset, None, GetTripsWithEcoBalanceByReconstructionContextFlightLoad
    ] = GetTripsWithEcoBalanceByReconstructionContextFlightLoad.AVG,
    load: Union[
        Unset, None, GetTripsWithEcoBalanceByReconstructionContextLoad
    ] = GetTripsWithEcoBalanceByReconstructionContextLoad.AVG,
    public_transport_load: Union[
        Unset, None, GetTripsWithEcoBalanceByReconstructionContextPublicTransportLoad
    ] = GetTripsWithEcoBalanceByReconstructionContextPublicTransportLoad.AVG,
    accept_language: Union[
        Unset, GetTripsWithEcoBalanceByReconstructionContextAcceptLanguage
    ] = GetTripsWithEcoBalanceByReconstructionContextAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = str(accept_language)

    if not isinstance(request_id, Unset):
        headers["Request-ID"] = request_id

    params: Dict[str, Any] = {}
    json_car_class: Union[Unset, None, str] = UNSET
    if not isinstance(car_class, Unset):
        json_car_class = car_class.value if car_class else None

    params["carClass"] = json_car_class

    json_car_engine: Union[Unset, None, str] = UNSET
    if not isinstance(car_engine, Unset):
        json_car_engine = car_engine.value if car_engine else None

    params["carEngine"] = json_car_engine

    json_car_euro_norm: Union[Unset, None, str] = UNSET
    if not isinstance(car_euro_norm, Unset):
        json_car_euro_norm = car_euro_norm.value if car_euro_norm else None

    params["carEuroNorm"] = json_car_euro_norm

    json_car_fuel_type: Union[Unset, None, str] = UNSET
    if not isinstance(car_fuel_type, Unset):
        json_car_fuel_type = car_fuel_type.value if car_fuel_type else None

    params["carFuelType"] = json_car_fuel_type

    json_car_load: Union[Unset, None, str] = UNSET
    if not isinstance(car_load, Unset):
        json_car_load = car_load.value if car_load else None

    params["carLoad"] = json_car_load

    json_flight_feeder: Union[Unset, None, str] = UNSET
    if not isinstance(flight_feeder, Unset):
        json_flight_feeder = flight_feeder.value if flight_feeder else None

    params["flightFeeder"] = json_flight_feeder

    json_flight_load: Union[Unset, None, str] = UNSET
    if not isinstance(flight_load, Unset):
        json_flight_load = flight_load.value if flight_load else None

    params["flightLoad"] = json_flight_load

    json_load: Union[Unset, None, str] = UNSET
    if not isinstance(load, Unset):
        json_load = load.value if load else None

    params["load"] = json_load

    json_public_transport_load: Union[Unset, None, str] = UNSET
    if not isinstance(public_transport_load, Unset):
        json_public_transport_load = public_transport_load.value if public_transport_load else None

    params["publicTransportLoad"] = json_public_transport_load

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/b2c/v2/trips/ecoBalance/{reconstructionContext}".format(
            reconstructionContext=reconstruction_context,
        ),
        "params": params,
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[EcoMap, JsonResponse, Problem]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = EcoMap.from_dict(response.json())

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
    if response.status_code == HTTPStatus.UNSUPPORTED_MEDIA_TYPE:
        response_415 = JsonResponse.from_dict(response.json())

        return response_415
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = Problem.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.NOT_IMPLEMENTED:
        response_501 = JsonResponse.from_dict(response.json())

        return response_501
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[EcoMap, JsonResponse, Problem]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    reconstruction_context: str,
    *,
    client: AuthenticatedClient,
    car_class: Union[
        Unset, None, GetTripsWithEcoBalanceByReconstructionContextCarClass
    ] = GetTripsWithEcoBalanceByReconstructionContextCarClass.MEDIUM_3,
    car_engine: Union[
        Unset, None, GetTripsWithEcoBalanceByReconstructionContextCarEngine
    ] = GetTripsWithEcoBalanceByReconstructionContextCarEngine.AVG,
    car_euro_norm: Union[
        Unset, None, GetTripsWithEcoBalanceByReconstructionContextCarEuroNorm
    ] = GetTripsWithEcoBalanceByReconstructionContextCarEuroNorm.AVG,
    car_fuel_type: Union[
        Unset, None, GetTripsWithEcoBalanceByReconstructionContextCarFuelType
    ] = GetTripsWithEcoBalanceByReconstructionContextCarFuelType.AVG,
    car_load: Union[
        Unset, None, GetTripsWithEcoBalanceByReconstructionContextCarLoad
    ] = GetTripsWithEcoBalanceByReconstructionContextCarLoad.AVG,
    flight_feeder: Union[
        Unset, None, GetTripsWithEcoBalanceByReconstructionContextFlightFeeder
    ] = GetTripsWithEcoBalanceByReconstructionContextFlightFeeder.CAR,
    flight_load: Union[
        Unset, None, GetTripsWithEcoBalanceByReconstructionContextFlightLoad
    ] = GetTripsWithEcoBalanceByReconstructionContextFlightLoad.AVG,
    load: Union[
        Unset, None, GetTripsWithEcoBalanceByReconstructionContextLoad
    ] = GetTripsWithEcoBalanceByReconstructionContextLoad.AVG,
    public_transport_load: Union[
        Unset, None, GetTripsWithEcoBalanceByReconstructionContextPublicTransportLoad
    ] = GetTripsWithEcoBalanceByReconstructionContextPublicTransportLoad.AVG,
    accept_language: Union[
        Unset, GetTripsWithEcoBalanceByReconstructionContextAcceptLanguage
    ] = GetTripsWithEcoBalanceByReconstructionContextAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Response[Union[EcoMap, JsonResponse, Problem]]:
    """Get detailed eco-balance values for a given `Trip` (v2.TripV2::reconstructionContext or
    v3.Trip::id). The response is a Map(key=PUBLIC_TRANSPORTATION|CAR|FLIGHT, value=EcoBalanceDetail) to
    compare PT, Car or flight (if distance is far enough for a flight).

     Determines comparable trips internally in relation to transportProduct and ecology-coefficants per
    key.<br>Check [Hafas Manual EcoParams](https://sbb.sharepoint.com/:b:/r/teams/297/Oeffentlich/S3_Pro
    gramm/Anwendungen/Oeffentlich/KIP/Hafas/API/REST-
    Proxy/10_Dokumentation_ReST/HAFAS_ReST_Interface_EcoParams_v.1.4_sbb.pdf).

    Args:
        reconstruction_context (str):  Example: yA88CgJWMRLmBiVDMiVCNkhLSQkJ8ElUJTI0QSUgM3Mzk-
            BAE=.
        car_class (Union[Unset, None, GetTripsWithEcoBalanceByReconstructionContextCarClass]):
            Default: GetTripsWithEcoBalanceByReconstructionContextCarClass.MEDIUM_3.
        car_engine (Union[Unset, None, GetTripsWithEcoBalanceByReconstructionContextCarEngine]):
            Default: GetTripsWithEcoBalanceByReconstructionContextCarEngine.AVG.
        car_euro_norm (Union[Unset, None,
            GetTripsWithEcoBalanceByReconstructionContextCarEuroNorm]):  Default:
            GetTripsWithEcoBalanceByReconstructionContextCarEuroNorm.AVG.
        car_fuel_type (Union[Unset, None,
            GetTripsWithEcoBalanceByReconstructionContextCarFuelType]):  Default:
            GetTripsWithEcoBalanceByReconstructionContextCarFuelType.AVG.
        car_load (Union[Unset, None, GetTripsWithEcoBalanceByReconstructionContextCarLoad]):
            Default: GetTripsWithEcoBalanceByReconstructionContextCarLoad.AVG.
        flight_feeder (Union[Unset, None,
            GetTripsWithEcoBalanceByReconstructionContextFlightFeeder]):  Default:
            GetTripsWithEcoBalanceByReconstructionContextFlightFeeder.CAR.
        flight_load (Union[Unset, None, GetTripsWithEcoBalanceByReconstructionContextFlightLoad]):
            Default: GetTripsWithEcoBalanceByReconstructionContextFlightLoad.AVG.
        load (Union[Unset, None, GetTripsWithEcoBalanceByReconstructionContextLoad]):  Default:
            GetTripsWithEcoBalanceByReconstructionContextLoad.AVG.
        public_transport_load (Union[Unset, None,
            GetTripsWithEcoBalanceByReconstructionContextPublicTransportLoad]):  Default:
            GetTripsWithEcoBalanceByReconstructionContextPublicTransportLoad.AVG.
        accept_language (Union[Unset,
            GetTripsWithEcoBalanceByReconstructionContextAcceptLanguage]):  Default:
            GetTripsWithEcoBalanceByReconstructionContextAcceptLanguage.EN.
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[EcoMap, JsonResponse, Problem]]
    """

    kwargs = _get_kwargs(
        reconstruction_context=reconstruction_context,
        car_class=car_class,
        car_engine=car_engine,
        car_euro_norm=car_euro_norm,
        car_fuel_type=car_fuel_type,
        car_load=car_load,
        flight_feeder=flight_feeder,
        flight_load=flight_load,
        load=load,
        public_transport_load=public_transport_load,
        accept_language=accept_language,
        request_id=request_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    reconstruction_context: str,
    *,
    client: AuthenticatedClient,
    car_class: Union[
        Unset, None, GetTripsWithEcoBalanceByReconstructionContextCarClass
    ] = GetTripsWithEcoBalanceByReconstructionContextCarClass.MEDIUM_3,
    car_engine: Union[
        Unset, None, GetTripsWithEcoBalanceByReconstructionContextCarEngine
    ] = GetTripsWithEcoBalanceByReconstructionContextCarEngine.AVG,
    car_euro_norm: Union[
        Unset, None, GetTripsWithEcoBalanceByReconstructionContextCarEuroNorm
    ] = GetTripsWithEcoBalanceByReconstructionContextCarEuroNorm.AVG,
    car_fuel_type: Union[
        Unset, None, GetTripsWithEcoBalanceByReconstructionContextCarFuelType
    ] = GetTripsWithEcoBalanceByReconstructionContextCarFuelType.AVG,
    car_load: Union[
        Unset, None, GetTripsWithEcoBalanceByReconstructionContextCarLoad
    ] = GetTripsWithEcoBalanceByReconstructionContextCarLoad.AVG,
    flight_feeder: Union[
        Unset, None, GetTripsWithEcoBalanceByReconstructionContextFlightFeeder
    ] = GetTripsWithEcoBalanceByReconstructionContextFlightFeeder.CAR,
    flight_load: Union[
        Unset, None, GetTripsWithEcoBalanceByReconstructionContextFlightLoad
    ] = GetTripsWithEcoBalanceByReconstructionContextFlightLoad.AVG,
    load: Union[
        Unset, None, GetTripsWithEcoBalanceByReconstructionContextLoad
    ] = GetTripsWithEcoBalanceByReconstructionContextLoad.AVG,
    public_transport_load: Union[
        Unset, None, GetTripsWithEcoBalanceByReconstructionContextPublicTransportLoad
    ] = GetTripsWithEcoBalanceByReconstructionContextPublicTransportLoad.AVG,
    accept_language: Union[
        Unset, GetTripsWithEcoBalanceByReconstructionContextAcceptLanguage
    ] = GetTripsWithEcoBalanceByReconstructionContextAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Optional[Union[EcoMap, JsonResponse, Problem]]:
    """Get detailed eco-balance values for a given `Trip` (v2.TripV2::reconstructionContext or
    v3.Trip::id). The response is a Map(key=PUBLIC_TRANSPORTATION|CAR|FLIGHT, value=EcoBalanceDetail) to
    compare PT, Car or flight (if distance is far enough for a flight).

     Determines comparable trips internally in relation to transportProduct and ecology-coefficants per
    key.<br>Check [Hafas Manual EcoParams](https://sbb.sharepoint.com/:b:/r/teams/297/Oeffentlich/S3_Pro
    gramm/Anwendungen/Oeffentlich/KIP/Hafas/API/REST-
    Proxy/10_Dokumentation_ReST/HAFAS_ReST_Interface_EcoParams_v.1.4_sbb.pdf).

    Args:
        reconstruction_context (str):  Example: yA88CgJWMRLmBiVDMiVCNkhLSQkJ8ElUJTI0QSUgM3Mzk-
            BAE=.
        car_class (Union[Unset, None, GetTripsWithEcoBalanceByReconstructionContextCarClass]):
            Default: GetTripsWithEcoBalanceByReconstructionContextCarClass.MEDIUM_3.
        car_engine (Union[Unset, None, GetTripsWithEcoBalanceByReconstructionContextCarEngine]):
            Default: GetTripsWithEcoBalanceByReconstructionContextCarEngine.AVG.
        car_euro_norm (Union[Unset, None,
            GetTripsWithEcoBalanceByReconstructionContextCarEuroNorm]):  Default:
            GetTripsWithEcoBalanceByReconstructionContextCarEuroNorm.AVG.
        car_fuel_type (Union[Unset, None,
            GetTripsWithEcoBalanceByReconstructionContextCarFuelType]):  Default:
            GetTripsWithEcoBalanceByReconstructionContextCarFuelType.AVG.
        car_load (Union[Unset, None, GetTripsWithEcoBalanceByReconstructionContextCarLoad]):
            Default: GetTripsWithEcoBalanceByReconstructionContextCarLoad.AVG.
        flight_feeder (Union[Unset, None,
            GetTripsWithEcoBalanceByReconstructionContextFlightFeeder]):  Default:
            GetTripsWithEcoBalanceByReconstructionContextFlightFeeder.CAR.
        flight_load (Union[Unset, None, GetTripsWithEcoBalanceByReconstructionContextFlightLoad]):
            Default: GetTripsWithEcoBalanceByReconstructionContextFlightLoad.AVG.
        load (Union[Unset, None, GetTripsWithEcoBalanceByReconstructionContextLoad]):  Default:
            GetTripsWithEcoBalanceByReconstructionContextLoad.AVG.
        public_transport_load (Union[Unset, None,
            GetTripsWithEcoBalanceByReconstructionContextPublicTransportLoad]):  Default:
            GetTripsWithEcoBalanceByReconstructionContextPublicTransportLoad.AVG.
        accept_language (Union[Unset,
            GetTripsWithEcoBalanceByReconstructionContextAcceptLanguage]):  Default:
            GetTripsWithEcoBalanceByReconstructionContextAcceptLanguage.EN.
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[EcoMap, JsonResponse, Problem]
    """

    return sync_detailed(
        reconstruction_context=reconstruction_context,
        client=client,
        car_class=car_class,
        car_engine=car_engine,
        car_euro_norm=car_euro_norm,
        car_fuel_type=car_fuel_type,
        car_load=car_load,
        flight_feeder=flight_feeder,
        flight_load=flight_load,
        load=load,
        public_transport_load=public_transport_load,
        accept_language=accept_language,
        request_id=request_id,
    ).parsed


async def asyncio_detailed(
    reconstruction_context: str,
    *,
    client: AuthenticatedClient,
    car_class: Union[
        Unset, None, GetTripsWithEcoBalanceByReconstructionContextCarClass
    ] = GetTripsWithEcoBalanceByReconstructionContextCarClass.MEDIUM_3,
    car_engine: Union[
        Unset, None, GetTripsWithEcoBalanceByReconstructionContextCarEngine
    ] = GetTripsWithEcoBalanceByReconstructionContextCarEngine.AVG,
    car_euro_norm: Union[
        Unset, None, GetTripsWithEcoBalanceByReconstructionContextCarEuroNorm
    ] = GetTripsWithEcoBalanceByReconstructionContextCarEuroNorm.AVG,
    car_fuel_type: Union[
        Unset, None, GetTripsWithEcoBalanceByReconstructionContextCarFuelType
    ] = GetTripsWithEcoBalanceByReconstructionContextCarFuelType.AVG,
    car_load: Union[
        Unset, None, GetTripsWithEcoBalanceByReconstructionContextCarLoad
    ] = GetTripsWithEcoBalanceByReconstructionContextCarLoad.AVG,
    flight_feeder: Union[
        Unset, None, GetTripsWithEcoBalanceByReconstructionContextFlightFeeder
    ] = GetTripsWithEcoBalanceByReconstructionContextFlightFeeder.CAR,
    flight_load: Union[
        Unset, None, GetTripsWithEcoBalanceByReconstructionContextFlightLoad
    ] = GetTripsWithEcoBalanceByReconstructionContextFlightLoad.AVG,
    load: Union[
        Unset, None, GetTripsWithEcoBalanceByReconstructionContextLoad
    ] = GetTripsWithEcoBalanceByReconstructionContextLoad.AVG,
    public_transport_load: Union[
        Unset, None, GetTripsWithEcoBalanceByReconstructionContextPublicTransportLoad
    ] = GetTripsWithEcoBalanceByReconstructionContextPublicTransportLoad.AVG,
    accept_language: Union[
        Unset, GetTripsWithEcoBalanceByReconstructionContextAcceptLanguage
    ] = GetTripsWithEcoBalanceByReconstructionContextAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Response[Union[EcoMap, JsonResponse, Problem]]:
    """Get detailed eco-balance values for a given `Trip` (v2.TripV2::reconstructionContext or
    v3.Trip::id). The response is a Map(key=PUBLIC_TRANSPORTATION|CAR|FLIGHT, value=EcoBalanceDetail) to
    compare PT, Car or flight (if distance is far enough for a flight).

     Determines comparable trips internally in relation to transportProduct and ecology-coefficants per
    key.<br>Check [Hafas Manual EcoParams](https://sbb.sharepoint.com/:b:/r/teams/297/Oeffentlich/S3_Pro
    gramm/Anwendungen/Oeffentlich/KIP/Hafas/API/REST-
    Proxy/10_Dokumentation_ReST/HAFAS_ReST_Interface_EcoParams_v.1.4_sbb.pdf).

    Args:
        reconstruction_context (str):  Example: yA88CgJWMRLmBiVDMiVCNkhLSQkJ8ElUJTI0QSUgM3Mzk-
            BAE=.
        car_class (Union[Unset, None, GetTripsWithEcoBalanceByReconstructionContextCarClass]):
            Default: GetTripsWithEcoBalanceByReconstructionContextCarClass.MEDIUM_3.
        car_engine (Union[Unset, None, GetTripsWithEcoBalanceByReconstructionContextCarEngine]):
            Default: GetTripsWithEcoBalanceByReconstructionContextCarEngine.AVG.
        car_euro_norm (Union[Unset, None,
            GetTripsWithEcoBalanceByReconstructionContextCarEuroNorm]):  Default:
            GetTripsWithEcoBalanceByReconstructionContextCarEuroNorm.AVG.
        car_fuel_type (Union[Unset, None,
            GetTripsWithEcoBalanceByReconstructionContextCarFuelType]):  Default:
            GetTripsWithEcoBalanceByReconstructionContextCarFuelType.AVG.
        car_load (Union[Unset, None, GetTripsWithEcoBalanceByReconstructionContextCarLoad]):
            Default: GetTripsWithEcoBalanceByReconstructionContextCarLoad.AVG.
        flight_feeder (Union[Unset, None,
            GetTripsWithEcoBalanceByReconstructionContextFlightFeeder]):  Default:
            GetTripsWithEcoBalanceByReconstructionContextFlightFeeder.CAR.
        flight_load (Union[Unset, None, GetTripsWithEcoBalanceByReconstructionContextFlightLoad]):
            Default: GetTripsWithEcoBalanceByReconstructionContextFlightLoad.AVG.
        load (Union[Unset, None, GetTripsWithEcoBalanceByReconstructionContextLoad]):  Default:
            GetTripsWithEcoBalanceByReconstructionContextLoad.AVG.
        public_transport_load (Union[Unset, None,
            GetTripsWithEcoBalanceByReconstructionContextPublicTransportLoad]):  Default:
            GetTripsWithEcoBalanceByReconstructionContextPublicTransportLoad.AVG.
        accept_language (Union[Unset,
            GetTripsWithEcoBalanceByReconstructionContextAcceptLanguage]):  Default:
            GetTripsWithEcoBalanceByReconstructionContextAcceptLanguage.EN.
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[EcoMap, JsonResponse, Problem]]
    """

    kwargs = _get_kwargs(
        reconstruction_context=reconstruction_context,
        car_class=car_class,
        car_engine=car_engine,
        car_euro_norm=car_euro_norm,
        car_fuel_type=car_fuel_type,
        car_load=car_load,
        flight_feeder=flight_feeder,
        flight_load=flight_load,
        load=load,
        public_transport_load=public_transport_load,
        accept_language=accept_language,
        request_id=request_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    reconstruction_context: str,
    *,
    client: AuthenticatedClient,
    car_class: Union[
        Unset, None, GetTripsWithEcoBalanceByReconstructionContextCarClass
    ] = GetTripsWithEcoBalanceByReconstructionContextCarClass.MEDIUM_3,
    car_engine: Union[
        Unset, None, GetTripsWithEcoBalanceByReconstructionContextCarEngine
    ] = GetTripsWithEcoBalanceByReconstructionContextCarEngine.AVG,
    car_euro_norm: Union[
        Unset, None, GetTripsWithEcoBalanceByReconstructionContextCarEuroNorm
    ] = GetTripsWithEcoBalanceByReconstructionContextCarEuroNorm.AVG,
    car_fuel_type: Union[
        Unset, None, GetTripsWithEcoBalanceByReconstructionContextCarFuelType
    ] = GetTripsWithEcoBalanceByReconstructionContextCarFuelType.AVG,
    car_load: Union[
        Unset, None, GetTripsWithEcoBalanceByReconstructionContextCarLoad
    ] = GetTripsWithEcoBalanceByReconstructionContextCarLoad.AVG,
    flight_feeder: Union[
        Unset, None, GetTripsWithEcoBalanceByReconstructionContextFlightFeeder
    ] = GetTripsWithEcoBalanceByReconstructionContextFlightFeeder.CAR,
    flight_load: Union[
        Unset, None, GetTripsWithEcoBalanceByReconstructionContextFlightLoad
    ] = GetTripsWithEcoBalanceByReconstructionContextFlightLoad.AVG,
    load: Union[
        Unset, None, GetTripsWithEcoBalanceByReconstructionContextLoad
    ] = GetTripsWithEcoBalanceByReconstructionContextLoad.AVG,
    public_transport_load: Union[
        Unset, None, GetTripsWithEcoBalanceByReconstructionContextPublicTransportLoad
    ] = GetTripsWithEcoBalanceByReconstructionContextPublicTransportLoad.AVG,
    accept_language: Union[
        Unset, GetTripsWithEcoBalanceByReconstructionContextAcceptLanguage
    ] = GetTripsWithEcoBalanceByReconstructionContextAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Optional[Union[EcoMap, JsonResponse, Problem]]:
    """Get detailed eco-balance values for a given `Trip` (v2.TripV2::reconstructionContext or
    v3.Trip::id). The response is a Map(key=PUBLIC_TRANSPORTATION|CAR|FLIGHT, value=EcoBalanceDetail) to
    compare PT, Car or flight (if distance is far enough for a flight).

     Determines comparable trips internally in relation to transportProduct and ecology-coefficants per
    key.<br>Check [Hafas Manual EcoParams](https://sbb.sharepoint.com/:b:/r/teams/297/Oeffentlich/S3_Pro
    gramm/Anwendungen/Oeffentlich/KIP/Hafas/API/REST-
    Proxy/10_Dokumentation_ReST/HAFAS_ReST_Interface_EcoParams_v.1.4_sbb.pdf).

    Args:
        reconstruction_context (str):  Example: yA88CgJWMRLmBiVDMiVCNkhLSQkJ8ElUJTI0QSUgM3Mzk-
            BAE=.
        car_class (Union[Unset, None, GetTripsWithEcoBalanceByReconstructionContextCarClass]):
            Default: GetTripsWithEcoBalanceByReconstructionContextCarClass.MEDIUM_3.
        car_engine (Union[Unset, None, GetTripsWithEcoBalanceByReconstructionContextCarEngine]):
            Default: GetTripsWithEcoBalanceByReconstructionContextCarEngine.AVG.
        car_euro_norm (Union[Unset, None,
            GetTripsWithEcoBalanceByReconstructionContextCarEuroNorm]):  Default:
            GetTripsWithEcoBalanceByReconstructionContextCarEuroNorm.AVG.
        car_fuel_type (Union[Unset, None,
            GetTripsWithEcoBalanceByReconstructionContextCarFuelType]):  Default:
            GetTripsWithEcoBalanceByReconstructionContextCarFuelType.AVG.
        car_load (Union[Unset, None, GetTripsWithEcoBalanceByReconstructionContextCarLoad]):
            Default: GetTripsWithEcoBalanceByReconstructionContextCarLoad.AVG.
        flight_feeder (Union[Unset, None,
            GetTripsWithEcoBalanceByReconstructionContextFlightFeeder]):  Default:
            GetTripsWithEcoBalanceByReconstructionContextFlightFeeder.CAR.
        flight_load (Union[Unset, None, GetTripsWithEcoBalanceByReconstructionContextFlightLoad]):
            Default: GetTripsWithEcoBalanceByReconstructionContextFlightLoad.AVG.
        load (Union[Unset, None, GetTripsWithEcoBalanceByReconstructionContextLoad]):  Default:
            GetTripsWithEcoBalanceByReconstructionContextLoad.AVG.
        public_transport_load (Union[Unset, None,
            GetTripsWithEcoBalanceByReconstructionContextPublicTransportLoad]):  Default:
            GetTripsWithEcoBalanceByReconstructionContextPublicTransportLoad.AVG.
        accept_language (Union[Unset,
            GetTripsWithEcoBalanceByReconstructionContextAcceptLanguage]):  Default:
            GetTripsWithEcoBalanceByReconstructionContextAcceptLanguage.EN.
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[EcoMap, JsonResponse, Problem]
    """

    return (
        await asyncio_detailed(
            reconstruction_context=reconstruction_context,
            client=client,
            car_class=car_class,
            car_engine=car_engine,
            car_euro_norm=car_euro_norm,
            car_fuel_type=car_fuel_type,
            car_load=car_load,
            flight_feeder=flight_feeder,
            flight_load=flight_load,
            load=load,
            public_transport_load=public_transport_load,
            accept_language=accept_language,
            request_id=request_id,
        )
    ).parsed
