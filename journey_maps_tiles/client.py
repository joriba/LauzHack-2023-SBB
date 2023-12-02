#!/usr/bin/env python3
# Automatically generated file by swagger_to. DO NOT EDIT OR APPEND ANYTHING!
"""Implements the client for Data."""

# pylint: skip-file
# pydocstyle: add-ignore=D105,D107,D401

import contextlib
import json
from typing import Any, BinaryIO, Dict, List, MutableMapping, Optional, cast

import requests
import requests.auth


def from_obj(obj: Any, expected: List[type], path: str = '') -> Any:
    """
    Checks and converts the given obj along the expected types.

    :param obj: to be converted
    :param expected: list of types representing the (nested) structure
    :param path: to the object used for debugging
    :return: the converted object
    """
    if not expected:
        raise ValueError("`expected` is empty, but at least one type needs to be specified.")

    exp = expected[0]

    if exp == float:
        if isinstance(obj, int):
            return float(obj)

        if isinstance(obj, float):
            return obj

        raise ValueError(
            'Expected object of type int or float at {!r}, but got {}.'.format(path, type(obj)))

    if exp in [bool, int, str, list, dict]:
        if not isinstance(obj, exp):
            raise ValueError(
                'Expected object of type {} at {!r}, but got {}.'.format(exp, path, type(obj)))

    if exp in [bool, int, float, str]:
        return obj

    if exp == list:
        lst = []  # type: List[Any]
        for i, value in enumerate(obj):
            lst.append(
                from_obj(value, expected=expected[1:], path='{}[{}]'.format(path, i)))

        return lst

    if exp == dict:
        adict = dict()  # type: Dict[str, Any]
        for key, value in obj.items():
            if not isinstance(key, str):
                raise ValueError(
                    'Expected a key of type str at path {!r}, got: {}'.format(path, type(key)))

            adict[key] = from_obj(value, expected=expected[1:], path='{}[{!r}]'.format(path, key))

        return adict

    if exp == Error:
        return error_from_obj(obj, path=path)

    raise ValueError("Unexpected `expected` type: {}".format(exp))


def to_jsonable(obj: Any, expected: List[type], path: str = "") -> Any:
    """
    Checks and converts the given object along the expected types to a JSON-able representation.

    :param obj: to be converted
    :param expected: list of types representing the (nested) structure
    :param path: path to the object used for debugging
    :return: JSON-able representation of the object
    """
    if not expected:
        raise ValueError("`expected` is empty, but at least one type needs to be specified.")

    exp = expected[0]
    if not isinstance(obj, exp):
        raise ValueError('Expected object of type {} at path {!r}, but got {}.'.format(
            exp, path, type(obj)))

    # Assert on primitive types to help type-hinting.
    if exp == bool:
        assert isinstance(obj, bool)
        return obj

    if exp == int:
        assert isinstance(obj, int)
        return obj

    if exp == float:
        assert isinstance(obj, float)
        return obj

    if exp == str:
        assert isinstance(obj, str)
        return obj

    if exp == list:
        assert isinstance(obj, list)

        lst = []  # type: List[Any]
        for i, value in enumerate(obj):
            lst.append(
                to_jsonable(value, expected=expected[1:], path='{}[{}]'.format(path, i)))

        return lst

    if exp == dict:
        assert isinstance(obj, dict)

        adict = dict()  # type: Dict[str, Any]
        for key, value in obj.items():
            if not isinstance(key, str):
                raise ValueError(
                    'Expected a key of type str at path {!r}, got: {}'.format(path, type(key)))

            adict[key] = to_jsonable(
                value,
                expected=expected[1:],
                path='{}[{!r}]'.format(path, key))

        return adict

    if exp == Error:
        assert isinstance(obj, Error)
        return error_to_jsonable(obj, path=path)

    raise ValueError("Unexpected `expected` type: {}".format(exp))


class Error:
    """Error detail to be returned if 4xx/5xx, according to [RFC-7807](https://tools.ietf.org/html/rfc7807)"""

    def __init__(
            self,
            message: str,
            status: int) -> None:
        """Initializes with the given values."""
        # A short, human-readable summary of the problem type
        self.message = message

        # Http status code of the error (4xx/5xx) problem.
        self.status = status

    def to_jsonable(self) -> MutableMapping[str, Any]:
        """
        Dispatches the conversion to error_to_jsonable.

        :return: JSON-able representation
        """
        return error_to_jsonable(self)


def new_error() -> Error:
    """Generates an instance of Error with default values."""
    return Error(
        message='',
        status=0)


def error_from_obj(obj: Any, path: str = "") -> Error:
    """
    Generates an instance of Error from a dictionary object.

    :param obj: a JSON-ed dictionary object representing an instance of Error
    :param path: path to the object used for debugging
    :return: parsed instance of Error
    """
    if not isinstance(obj, dict):
        raise ValueError('Expected a dict at path {}, but got: {}'.format(path, type(obj)))

    for key in obj:
        if not isinstance(key, str):
            raise ValueError(
                'Expected a key of type str at path {}, but got: {}'.format(path, type(key)))

    message_from_obj = from_obj(
        obj['message'],
        expected=[str],
        path=path + '.message')  # type: str

    status_from_obj = from_obj(
        obj['status'],
        expected=[int],
        path=path + '.status')  # type: int

    return Error(
        message=message_from_obj,
        status=status_from_obj)


def error_to_jsonable(
        error: Error,
        path: str = "") -> MutableMapping[str, Any]:
    """
    Generates a JSON-able mapping from an instance of Error.

    :param error: instance of Error to be JSON-ized
    :param path: path to the error used for debugging
    :return: a JSON-able representation
    """
    res = dict()  # type: Dict[str, Any]

    res['message'] = error.message

    res['status'] = error.status

    return res


class RemoteCaller:
    """Executes the remote calls to the server."""

    def __init__(
        self,
        url_prefix: str,
        auth: Optional[requests.auth.AuthBase] = None,
        session: Optional[requests.Session] = None) -> None:
        self.url_prefix = url_prefix
        self.auth = auth
        self.session = session

        if not self.session:
            self.session = requests.Session()
            self.session.auth = self.auth

    def get_styles(self) -> str:
        """
        A list of all style definition files.

        :return: Successful operation
        """
        url = self.url_prefix + '/styles.json'

        resp = self.session.request(method='get', url=url)

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[str])

    def get_style(
            self,
            id: str) -> str:
        """
        A style definition file is a document that defines the visual appearance of a map: what data to draw, the order to draw it in, and how to style the data when drawing it. A style document is a JSON object with specific root level and nested properties. This specification defines and describes these properties. See : https://docs.mapbox.com/mapbox-gl-js/style-spec/

        :param id: Style definition id.

        :return: Successful operation
        """
        url = "".join([
            self.url_prefix,
            '/styles/',
            str(id),
            '/style.json'])

        resp = self.session.request(
            method='get',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[str])

    def get_rasters(
            self,
            id: str,
            x: int,
            y: int,
            z: int,
            format: str) -> str:
        """
        A rendered raster tile is a server side computed part of the map delivered as an image.

        :param id: Style id.
        :param x: X position
        :param y: Y position
        :param z: Z position
        :param format: Format usually png, jpg or webp

        :return: Successful operation
        """
        url = "".join([
            self.url_prefix,
            '/styles/',
            str(id),
            '/',
            str(z),
            '/',
            str(x),
            '/',
            str(y),
            '.',
            str(format)])

        resp = self.session.request(
            method='get',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[str])

    def get_sprite(
            self,
            id: str,
            format: str) -> str:
        """
        A sprite is an image bundle used by the style definition file.

        :param id: Style definition id.
        :param format: Sprite format can be one of : png, jpg, jpeg, webp.

        :return: Successful operation
        """
        url = "".join([
            self.url_prefix,
            '/styles/',
            str(id),
            '/sprite.',
            str(format)])

        resp = self.session.request(
            method='get',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[str])

    def get_sprite_rez(
            self,
            id: str,
            format: str,
            resolution: str) -> str:
        """
        A sprite is an image bundle used by the style definition file.

        :param id: Style definition id.
        :param format: Sprite format can be one of : png, jpg, jpeg, webp.
        :param resolution: Sprite resolution can be one of : @2x, @3x, @4x.

        :return: Successful operation
        """
        url = "".join([
            self.url_prefix,
            '/styles/',
            str(id),
            '/sprite',
            str(resolution),
            '.',
            str(format)])

        resp = self.session.request(
            method='get',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[str])

    def get_wmts(
            self,
            id: str) -> str:
        """
        An XML file describing the style capabilities.

        :param id: Style definition id.

        :return: Successful operation
        """
        url = "".join([
            self.url_prefix,
            '/styles/',
            str(id),
            '/wmts.xml'])

        resp = self.session.request(
            method='get',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[str])

    def get_font(
            self,
            fontstack: str,
            start: int,
            end: int) -> str:
        """
        Fonts defined and used by the style definition file.

        :param fontstack: Font name as defined in the stryle definition file.
        :param start: Start of the glyphs range.
        :param end: Ends of the glyphs range.

        :return: Successful operation
        """
        url = "".join([
            self.url_prefix,
            '/fonts/',
            str(fontstack),
            '/',
            str(start),
            '-',
            str(end),
            '.pbf'])

        resp = self.session.request(
            method='get',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[str])

    def get_mbtiles_json(
            self,
            mbtiles: str) -> str:
        """
        Data sources used by the style definition file.

        :param mbtiles: MB tile name

        :return: Successful operation
        """
        url = "".join([
            self.url_prefix,
            '/data/',
            str(mbtiles),
            '.json'])

        resp = self.session.request(
            method='get',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[str])

    def get_mbtiles(
            self,
            mbtiles: str,
            x: int,
            y: int,
            z: int,
            format: str) -> str:
        """
        Data sources used by the style definition file.

        :param mbtiles: MB tile name
        :param x: X position
        :param y: Y position
        :param z: Z position
        :param format: Format usually png, jpg or pbf

        :return: Successful operation
        """
        url = "".join([
            self.url_prefix,
            '/data/',
            str(mbtiles),
            '/',
            str(z),
            '/',
            str(x),
            '/',
            str(y),
            '.',
            str(format)])

        resp = self.session.request(
            method='get',
            url=url,
        )

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[str])

    def get_health(self) -> str:
        """
        Give a 200 Ok if the service is running, else 503 Starting.

        :return: Service Ok
        """
        url = self.url_prefix + '/health'

        resp = self.session.request(method='get', url=url)

        with contextlib.closing(resp):
            resp.raise_for_status()
            return from_obj(
                obj=resp.json(),
                expected=[str])


# Automatically generated file by swagger_to. DO NOT EDIT OR APPEND ANYTHING!
