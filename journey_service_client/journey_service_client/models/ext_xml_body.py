import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.ext_xml_body_document_language import ExtXmlBodyDocumentLanguage
from ..models.ext_xml_body_stop_behaviour import ExtXmlBodyStopBehaviour
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExtXmlBody")


@_attrs_define
class ExtXmlBody:
    """Request parameters (POST body).

    Attributes:
        reconstruction_context (str): Trip::reconstructionContext of the journey. Example: T%24A%3D1%40O%3DBern%40X%3D74
            39122%40Y%3D46948825%40L%3D8507000%40a%3D128%40%24A%3D1%40O%3DZ%C3%BCrich+HB%40X%3D8540193%40Y%3D47378177%40L%3D
            8503000%40a%3D128%40%24201803021632%24201803021728%24IC+1++++%24%241%24.
        stop_behaviour (ExtXmlBodyStopBehaviour): Stop behaviour of trip considering boarding and alighting.
        date (datetime.date): Date of reconstruction. Example: 2023-04-18.
        document_language (Union[Unset, ExtXmlBodyDocumentLanguage]): Supported languages (translations).
        date_zone_id (Union[Unset, str]): @Deprecated Irrelevant
        polyline (Union[Unset, bool]): Set to true if de:Streckenverlaufskarte must be prepared.<br>This parameter has
            an impact on performance and/or response volume, set wisely!
    """

    reconstruction_context: str
    stop_behaviour: ExtXmlBodyStopBehaviour
    date: datetime.date
    document_language: Union[Unset, ExtXmlBodyDocumentLanguage] = UNSET
    date_zone_id: Union[Unset, str] = UNSET
    polyline: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        reconstruction_context = self.reconstruction_context
        stop_behaviour = self.stop_behaviour.value

        date = self.date.isoformat()
        document_language: Union[Unset, str] = UNSET
        if not isinstance(self.document_language, Unset):
            document_language = self.document_language.value

        date_zone_id = self.date_zone_id
        polyline = self.polyline

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reconstructionContext": reconstruction_context,
                "stopBehaviour": stop_behaviour,
                "date": date,
            }
        )
        if document_language is not UNSET:
            field_dict["documentLanguage"] = document_language
        if date_zone_id is not UNSET:
            field_dict["dateZoneId"] = date_zone_id
        if polyline is not UNSET:
            field_dict["polyline"] = polyline

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        reconstruction_context = d.pop("reconstructionContext")

        stop_behaviour = ExtXmlBodyStopBehaviour(d.pop("stopBehaviour"))

        date = isoparse(d.pop("date")).date()

        _document_language = d.pop("documentLanguage", UNSET)
        document_language: Union[Unset, ExtXmlBodyDocumentLanguage]
        if isinstance(_document_language, Unset):
            document_language = UNSET
        else:
            document_language = ExtXmlBodyDocumentLanguage(_document_language)

        date_zone_id = d.pop("dateZoneId", UNSET)

        polyline = d.pop("polyline", UNSET)

        ext_xml_body = cls(
            reconstruction_context=reconstruction_context,
            stop_behaviour=stop_behaviour,
            date=date,
            document_language=document_language,
            date_zone_id=date_zone_id,
            polyline=polyline,
        )

        ext_xml_body.additional_properties = d
        return ext_xml_body

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
