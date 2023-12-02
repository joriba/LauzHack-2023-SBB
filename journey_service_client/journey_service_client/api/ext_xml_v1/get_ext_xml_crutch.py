from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ext_xml_body import ExtXmlBody
from ...models.ext_xml_response import ExtXmlResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    json_body: ExtXmlBody,
    request_id: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers = {}
    if not isinstance(request_id, Unset):
        headers["Request-ID"] = request_id

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/api/sbb/v1/trips/extXmlCrutch",
        "json": json_json_body,
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ExtXmlResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ExtXmlResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.NO_CONTENT:
        response_204 = ExtXmlResponse.from_dict(response.json())

        return response_204
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ExtXmlResponse.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = ExtXmlResponse.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = ExtXmlResponse.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.UNSUPPORTED_MEDIA_TYPE:
        response_415 = ExtXmlResponse.from_dict(response.json())

        return response_415
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = ExtXmlResponse.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ExtXmlResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: ExtXmlBody,
    request_id: Union[Unset, str] = UNSET,
) -> Response[ExtXmlResponse]:
    """@Deprecated (remains operational until Ticketshop is EOL) Get XmlHandle for Hafas::extXML API.

     Workaround for Ticketshop-link to buy international Tickets and to render Hafas-map for
    de:Streckenverlauf.
    Remark: Trip::reconstructionContext is compatible between Hafas::REST and Hafas::extXML.

    Args:
        request_id (Union[Unset, str]):
        json_body (ExtXmlBody): Request parameters (POST body).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExtXmlResponse]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
        request_id=request_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: ExtXmlBody,
    request_id: Union[Unset, str] = UNSET,
) -> Optional[ExtXmlResponse]:
    """@Deprecated (remains operational until Ticketshop is EOL) Get XmlHandle for Hafas::extXML API.

     Workaround for Ticketshop-link to buy international Tickets and to render Hafas-map for
    de:Streckenverlauf.
    Remark: Trip::reconstructionContext is compatible between Hafas::REST and Hafas::extXML.

    Args:
        request_id (Union[Unset, str]):
        json_body (ExtXmlBody): Request parameters (POST body).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExtXmlResponse
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        request_id=request_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: ExtXmlBody,
    request_id: Union[Unset, str] = UNSET,
) -> Response[ExtXmlResponse]:
    """@Deprecated (remains operational until Ticketshop is EOL) Get XmlHandle for Hafas::extXML API.

     Workaround for Ticketshop-link to buy international Tickets and to render Hafas-map for
    de:Streckenverlauf.
    Remark: Trip::reconstructionContext is compatible between Hafas::REST and Hafas::extXML.

    Args:
        request_id (Union[Unset, str]):
        json_body (ExtXmlBody): Request parameters (POST body).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExtXmlResponse]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
        request_id=request_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: ExtXmlBody,
    request_id: Union[Unset, str] = UNSET,
) -> Optional[ExtXmlResponse]:
    """@Deprecated (remains operational until Ticketshop is EOL) Get XmlHandle for Hafas::extXML API.

     Workaround for Ticketshop-link to buy international Tickets and to render Hafas-map for
    de:Streckenverlauf.
    Remark: Trip::reconstructionContext is compatible between Hafas::REST and Hafas::extXML.

    Args:
        request_id (Union[Unset, str]):
        json_body (ExtXmlBody): Request parameters (POST body).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExtXmlResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            request_id=request_id,
        )
    ).parsed
