import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.audience_link import AudienceLink


T = TypeVar("T", bound="Audience")


@_attrs_define
class Audience:
    """Audience (like enduser channels, operator-employees, ..) to be informed (aka: de:Publikationskanäle).

    Attributes:
        type (str): <br>x-extensible-enum:  see `AudienceEnum`. Example: B2C_TEXT.
        urls (List['AudienceLink']):
        valid_from_date (Union[Unset, datetime.date]): Valid-from date, to be combined with time. Example: 2022-08-30.
        valid_from_time (Union[Unset, str]): Valid-from time, to be combined with date. Example: 08:45.
        valid_to_date (Union[Unset, datetime.date]): Valid-to date, to be combined with time. Example: 2022-09-06.
        valid_to_time (Union[Unset, str]): Valid-to time, to be combined with date. Example: 17:15.
    """

    type: str
    urls: List["AudienceLink"]
    valid_from_date: Union[Unset, datetime.date] = UNSET
    valid_from_time: Union[Unset, str] = UNSET
    valid_to_date: Union[Unset, datetime.date] = UNSET
    valid_to_time: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        urls = []
        for urls_item_data in self.urls:
            urls_item = urls_item_data.to_dict()

            urls.append(urls_item)

        valid_from_date: Union[Unset, str] = UNSET
        if not isinstance(self.valid_from_date, Unset):
            valid_from_date = self.valid_from_date.isoformat()

        valid_from_time = self.valid_from_time
        valid_to_date: Union[Unset, str] = UNSET
        if not isinstance(self.valid_to_date, Unset):
            valid_to_date = self.valid_to_date.isoformat()

        valid_to_time = self.valid_to_time

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "urls": urls,
            }
        )
        if valid_from_date is not UNSET:
            field_dict["validFromDate"] = valid_from_date
        if valid_from_time is not UNSET:
            field_dict["validFromTime"] = valid_from_time
        if valid_to_date is not UNSET:
            field_dict["validToDate"] = valid_to_date
        if valid_to_time is not UNSET:
            field_dict["validToTime"] = valid_to_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.audience_link import AudienceLink

        d = src_dict.copy()
        type = d.pop("type")

        urls = []
        _urls = d.pop("urls")
        for urls_item_data in _urls:
            urls_item = AudienceLink.from_dict(urls_item_data)

            urls.append(urls_item)

        _valid_from_date = d.pop("validFromDate", UNSET)
        valid_from_date: Union[Unset, datetime.date]
        if isinstance(_valid_from_date, Unset):
            valid_from_date = UNSET
        else:
            valid_from_date = isoparse(_valid_from_date).date()

        valid_from_time = d.pop("validFromTime", UNSET)

        _valid_to_date = d.pop("validToDate", UNSET)
        valid_to_date: Union[Unset, datetime.date]
        if isinstance(_valid_to_date, Unset):
            valid_to_date = UNSET
        else:
            valid_to_date = isoparse(_valid_to_date).date()

        valid_to_time = d.pop("validToTime", UNSET)

        audience = cls(
            type=type,
            urls=urls,
            valid_from_date=valid_from_date,
            valid_from_time=valid_from_time,
            valid_to_date=valid_to_date,
            valid_to_time=valid_to_time,
        )

        audience.additional_properties = d
        return audience

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
