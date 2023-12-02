import datetime
from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_routes_accept_language import GetRoutesAcceptLanguage
from ...models.get_routes_response_501 import GetRoutesResponse501
from ...models.get_routes_stop_behaviour import GetRoutesStopBehaviour
from ...models.journey_detail import JourneyDetail
from ...models.local_time import LocalTime
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    date: Union[Unset, None, datetime.date] = UNSET,
    include_exit_side: Union[Unset, None, bool] = False,
    limit: Union[Unset, None, int] = 1,
    operator_numbers: Union[Unset, None, List[str]] = UNSET,
    restrict_ch: Union[Unset, None, bool] = True,
    stop_behaviour: Union[Unset, None, GetRoutesStopBehaviour] = GetRoutesStopBehaviour.REAL_BOARDING_ALIGHTING,
    time: Union[Unset, None, "LocalTime"] = UNSET,
    transport_product_category: Union[Unset, None, str] = UNSET,
    transport_product_line: Union[Unset, None, str] = UNSET,
    transport_product_number: Union[Unset, None, str] = UNSET,
    transport_reference_number: Union[Unset, None, str] = UNSET,
    accept_language: Union[Unset, GetRoutesAcceptLanguage] = GetRoutesAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = str(accept_language)

    if not isinstance(request_id, Unset):
        headers["Request-ID"] = request_id

    params: Dict[str, Any] = {}
    json_date: Union[Unset, None, str] = UNSET
    if not isinstance(date, Unset):
        json_date = date.isoformat() if date else None

    params["date"] = json_date

    params["includeExitSide"] = include_exit_side

    params["limit"] = limit

    json_operator_numbers: Union[Unset, None, List[str]] = UNSET
    if not isinstance(operator_numbers, Unset):
        if operator_numbers is None:
            json_operator_numbers = None
        else:
            json_operator_numbers = operator_numbers

    params["operatorNumbers"] = json_operator_numbers

    params["restrictCH"] = restrict_ch

    json_stop_behaviour: Union[Unset, None, str] = UNSET
    if not isinstance(stop_behaviour, Unset):
        json_stop_behaviour = stop_behaviour.value if stop_behaviour else None

    params["stopBehaviour"] = json_stop_behaviour

    json_time: Union[Unset, None, Dict[str, Any]] = UNSET
    if not isinstance(time, Unset):
        json_time = time.to_dict() if time else None

    if not isinstance(json_time, Unset) and json_time is not None:
        params.update(json_time)

    params["transportProductCategory"] = transport_product_category

    params["transportProductLine"] = transport_product_line

    params["transportProductNumber"] = transport_product_number

    params["transportReferenceNumber"] = transport_reference_number

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/b2c/v2/routes",
        "params": params,
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[GetRoutesResponse501, List["JourneyDetail"], Problem]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = JourneyDetail.from_dict(response_200_item_data)

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
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = Problem.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.NOT_IMPLEMENTED:
        response_501 = GetRoutesResponse501.from_dict(response.json())

        return response_501
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[GetRoutesResponse501, List["JourneyDetail"], Problem]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    date: Union[Unset, None, datetime.date] = UNSET,
    include_exit_side: Union[Unset, None, bool] = False,
    limit: Union[Unset, None, int] = 1,
    operator_numbers: Union[Unset, None, List[str]] = UNSET,
    restrict_ch: Union[Unset, None, bool] = True,
    stop_behaviour: Union[Unset, None, GetRoutesStopBehaviour] = GetRoutesStopBehaviour.REAL_BOARDING_ALIGHTING,
    time: Union[Unset, None, "LocalTime"] = UNSET,
    transport_product_category: Union[Unset, None, str] = UNSET,
    transport_product_line: Union[Unset, None, str] = UNSET,
    transport_product_number: Union[Unset, None, str] = UNSET,
    transport_reference_number: Union[Unset, None, str] = UNSET,
    accept_language: Union[Unset, GetRoutesAcceptLanguage] = GetRoutesAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Response[Union[GetRoutesResponse501, List["JourneyDetail"], Problem]]:
    """@Deprecated (SWITCH to v3/vehicle-journeys/by-service)! Get complete vehicle-journeys by transport-
    products (also referred as 'trainSearch').<br>Results might not be 100% exact for e.g. a filter like
    'IC 714' might also result in 'IC **1** 714' but filter like 'IC 1 714' will not resolve 'IC 714'!

     Determines complete journey-details matching given transport-product input (at least
    {`transportProductNumber`} OR  {`transportProductCategory` AND `transportProductLine`} are
    expected.).

    Args:
        date (Union[Unset, None, datetime.date]):
        include_exit_side (Union[Unset, None, bool]):
        limit (Union[Unset, None, int]):  Default: 1.
        operator_numbers (Union[Unset, None, List[str]]):
        restrict_ch (Union[Unset, None, bool]):  Default: True.
        stop_behaviour (Union[Unset, None, GetRoutesStopBehaviour]):  Default:
            GetRoutesStopBehaviour.REAL_BOARDING_ALIGHTING.
        time (Union[Unset, None, LocalTime]): Message event period starting at time daily.
            Example: 13:07.
        transport_product_category (Union[Unset, None, str]):  Example: IC.
        transport_product_line (Union[Unset, None, str]):  Example: 1.
        transport_product_number (Union[Unset, None, str]):  Example: 756.
        transport_reference_number (Union[Unset, None, str]):  Example: 3520.
        accept_language (Union[Unset, GetRoutesAcceptLanguage]):  Default:
            GetRoutesAcceptLanguage.EN.
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetRoutesResponse501, List['JourneyDetail'], Problem]]
    """

    kwargs = _get_kwargs(
        date=date,
        include_exit_side=include_exit_side,
        limit=limit,
        operator_numbers=operator_numbers,
        restrict_ch=restrict_ch,
        stop_behaviour=stop_behaviour,
        time=time,
        transport_product_category=transport_product_category,
        transport_product_line=transport_product_line,
        transport_product_number=transport_product_number,
        transport_reference_number=transport_reference_number,
        accept_language=accept_language,
        request_id=request_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    date: Union[Unset, None, datetime.date] = UNSET,
    include_exit_side: Union[Unset, None, bool] = False,
    limit: Union[Unset, None, int] = 1,
    operator_numbers: Union[Unset, None, List[str]] = UNSET,
    restrict_ch: Union[Unset, None, bool] = True,
    stop_behaviour: Union[Unset, None, GetRoutesStopBehaviour] = GetRoutesStopBehaviour.REAL_BOARDING_ALIGHTING,
    time: Union[Unset, None, "LocalTime"] = UNSET,
    transport_product_category: Union[Unset, None, str] = UNSET,
    transport_product_line: Union[Unset, None, str] = UNSET,
    transport_product_number: Union[Unset, None, str] = UNSET,
    transport_reference_number: Union[Unset, None, str] = UNSET,
    accept_language: Union[Unset, GetRoutesAcceptLanguage] = GetRoutesAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Optional[Union[GetRoutesResponse501, List["JourneyDetail"], Problem]]:
    """@Deprecated (SWITCH to v3/vehicle-journeys/by-service)! Get complete vehicle-journeys by transport-
    products (also referred as 'trainSearch').<br>Results might not be 100% exact for e.g. a filter like
    'IC 714' might also result in 'IC **1** 714' but filter like 'IC 1 714' will not resolve 'IC 714'!

     Determines complete journey-details matching given transport-product input (at least
    {`transportProductNumber`} OR  {`transportProductCategory` AND `transportProductLine`} are
    expected.).

    Args:
        date (Union[Unset, None, datetime.date]):
        include_exit_side (Union[Unset, None, bool]):
        limit (Union[Unset, None, int]):  Default: 1.
        operator_numbers (Union[Unset, None, List[str]]):
        restrict_ch (Union[Unset, None, bool]):  Default: True.
        stop_behaviour (Union[Unset, None, GetRoutesStopBehaviour]):  Default:
            GetRoutesStopBehaviour.REAL_BOARDING_ALIGHTING.
        time (Union[Unset, None, LocalTime]): Message event period starting at time daily.
            Example: 13:07.
        transport_product_category (Union[Unset, None, str]):  Example: IC.
        transport_product_line (Union[Unset, None, str]):  Example: 1.
        transport_product_number (Union[Unset, None, str]):  Example: 756.
        transport_reference_number (Union[Unset, None, str]):  Example: 3520.
        accept_language (Union[Unset, GetRoutesAcceptLanguage]):  Default:
            GetRoutesAcceptLanguage.EN.
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetRoutesResponse501, List['JourneyDetail'], Problem]
    """

    return sync_detailed(
        client=client,
        date=date,
        include_exit_side=include_exit_side,
        limit=limit,
        operator_numbers=operator_numbers,
        restrict_ch=restrict_ch,
        stop_behaviour=stop_behaviour,
        time=time,
        transport_product_category=transport_product_category,
        transport_product_line=transport_product_line,
        transport_product_number=transport_product_number,
        transport_reference_number=transport_reference_number,
        accept_language=accept_language,
        request_id=request_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    date: Union[Unset, None, datetime.date] = UNSET,
    include_exit_side: Union[Unset, None, bool] = False,
    limit: Union[Unset, None, int] = 1,
    operator_numbers: Union[Unset, None, List[str]] = UNSET,
    restrict_ch: Union[Unset, None, bool] = True,
    stop_behaviour: Union[Unset, None, GetRoutesStopBehaviour] = GetRoutesStopBehaviour.REAL_BOARDING_ALIGHTING,
    time: Union[Unset, None, "LocalTime"] = UNSET,
    transport_product_category: Union[Unset, None, str] = UNSET,
    transport_product_line: Union[Unset, None, str] = UNSET,
    transport_product_number: Union[Unset, None, str] = UNSET,
    transport_reference_number: Union[Unset, None, str] = UNSET,
    accept_language: Union[Unset, GetRoutesAcceptLanguage] = GetRoutesAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Response[Union[GetRoutesResponse501, List["JourneyDetail"], Problem]]:
    """@Deprecated (SWITCH to v3/vehicle-journeys/by-service)! Get complete vehicle-journeys by transport-
    products (also referred as 'trainSearch').<br>Results might not be 100% exact for e.g. a filter like
    'IC 714' might also result in 'IC **1** 714' but filter like 'IC 1 714' will not resolve 'IC 714'!

     Determines complete journey-details matching given transport-product input (at least
    {`transportProductNumber`} OR  {`transportProductCategory` AND `transportProductLine`} are
    expected.).

    Args:
        date (Union[Unset, None, datetime.date]):
        include_exit_side (Union[Unset, None, bool]):
        limit (Union[Unset, None, int]):  Default: 1.
        operator_numbers (Union[Unset, None, List[str]]):
        restrict_ch (Union[Unset, None, bool]):  Default: True.
        stop_behaviour (Union[Unset, None, GetRoutesStopBehaviour]):  Default:
            GetRoutesStopBehaviour.REAL_BOARDING_ALIGHTING.
        time (Union[Unset, None, LocalTime]): Message event period starting at time daily.
            Example: 13:07.
        transport_product_category (Union[Unset, None, str]):  Example: IC.
        transport_product_line (Union[Unset, None, str]):  Example: 1.
        transport_product_number (Union[Unset, None, str]):  Example: 756.
        transport_reference_number (Union[Unset, None, str]):  Example: 3520.
        accept_language (Union[Unset, GetRoutesAcceptLanguage]):  Default:
            GetRoutesAcceptLanguage.EN.
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetRoutesResponse501, List['JourneyDetail'], Problem]]
    """

    kwargs = _get_kwargs(
        date=date,
        include_exit_side=include_exit_side,
        limit=limit,
        operator_numbers=operator_numbers,
        restrict_ch=restrict_ch,
        stop_behaviour=stop_behaviour,
        time=time,
        transport_product_category=transport_product_category,
        transport_product_line=transport_product_line,
        transport_product_number=transport_product_number,
        transport_reference_number=transport_reference_number,
        accept_language=accept_language,
        request_id=request_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    date: Union[Unset, None, datetime.date] = UNSET,
    include_exit_side: Union[Unset, None, bool] = False,
    limit: Union[Unset, None, int] = 1,
    operator_numbers: Union[Unset, None, List[str]] = UNSET,
    restrict_ch: Union[Unset, None, bool] = True,
    stop_behaviour: Union[Unset, None, GetRoutesStopBehaviour] = GetRoutesStopBehaviour.REAL_BOARDING_ALIGHTING,
    time: Union[Unset, None, "LocalTime"] = UNSET,
    transport_product_category: Union[Unset, None, str] = UNSET,
    transport_product_line: Union[Unset, None, str] = UNSET,
    transport_product_number: Union[Unset, None, str] = UNSET,
    transport_reference_number: Union[Unset, None, str] = UNSET,
    accept_language: Union[Unset, GetRoutesAcceptLanguage] = GetRoutesAcceptLanguage.EN,
    request_id: Union[Unset, str] = UNSET,
) -> Optional[Union[GetRoutesResponse501, List["JourneyDetail"], Problem]]:
    """@Deprecated (SWITCH to v3/vehicle-journeys/by-service)! Get complete vehicle-journeys by transport-
    products (also referred as 'trainSearch').<br>Results might not be 100% exact for e.g. a filter like
    'IC 714' might also result in 'IC **1** 714' but filter like 'IC 1 714' will not resolve 'IC 714'!

     Determines complete journey-details matching given transport-product input (at least
    {`transportProductNumber`} OR  {`transportProductCategory` AND `transportProductLine`} are
    expected.).

    Args:
        date (Union[Unset, None, datetime.date]):
        include_exit_side (Union[Unset, None, bool]):
        limit (Union[Unset, None, int]):  Default: 1.
        operator_numbers (Union[Unset, None, List[str]]):
        restrict_ch (Union[Unset, None, bool]):  Default: True.
        stop_behaviour (Union[Unset, None, GetRoutesStopBehaviour]):  Default:
            GetRoutesStopBehaviour.REAL_BOARDING_ALIGHTING.
        time (Union[Unset, None, LocalTime]): Message event period starting at time daily.
            Example: 13:07.
        transport_product_category (Union[Unset, None, str]):  Example: IC.
        transport_product_line (Union[Unset, None, str]):  Example: 1.
        transport_product_number (Union[Unset, None, str]):  Example: 756.
        transport_reference_number (Union[Unset, None, str]):  Example: 3520.
        accept_language (Union[Unset, GetRoutesAcceptLanguage]):  Default:
            GetRoutesAcceptLanguage.EN.
        request_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetRoutesResponse501, List['JourneyDetail'], Problem]
    """

    return (
        await asyncio_detailed(
            client=client,
            date=date,
            include_exit_side=include_exit_side,
            limit=limit,
            operator_numbers=operator_numbers,
            restrict_ch=restrict_ch,
            stop_behaviour=stop_behaviour,
            time=time,
            transport_product_category=transport_product_category,
            transport_product_line=transport_product_line,
            transport_product_number=transport_product_number,
            transport_reference_number=transport_reference_number,
            accept_language=accept_language,
            request_id=request_id,
        )
    ).parsed
