from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.message_channel_type_name import MessageChannelTypeName
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.url_link_type import UrlLinkType


T = TypeVar("T", bound="MessageChannelType")


@_attrs_define
class MessageChannelType:
    """Audience (like enduser channels, operator-employees, ..) to be informed (aka: de:Publikationskanäle). Make sure to
    inform the proper target-users.

        Attributes:
            name (Union[Unset, MessageChannelTypeName]):
            urls (Union[Unset, List['UrlLinkType']]):
            valid_from_time (Union[Unset, str]):
            valid_from_date (Union[Unset, str]):
            valid_to_time (Union[Unset, str]):
            valid_to_date (Union[Unset, str]):
    """

    name: Union[Unset, MessageChannelTypeName] = UNSET
    urls: Union[Unset, List["UrlLinkType"]] = UNSET
    valid_from_time: Union[Unset, str] = UNSET
    valid_from_date: Union[Unset, str] = UNSET
    valid_to_time: Union[Unset, str] = UNSET
    valid_to_date: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name: Union[Unset, str] = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.value

        urls: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.urls, Unset):
            urls = []
            for urls_item_data in self.urls:
                urls_item = urls_item_data.to_dict()

                urls.append(urls_item)

        valid_from_time = self.valid_from_time
        valid_from_date = self.valid_from_date
        valid_to_time = self.valid_to_time
        valid_to_date = self.valid_to_date

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if urls is not UNSET:
            field_dict["urls"] = urls
        if valid_from_time is not UNSET:
            field_dict["validFromTime"] = valid_from_time
        if valid_from_date is not UNSET:
            field_dict["validFromDate"] = valid_from_date
        if valid_to_time is not UNSET:
            field_dict["validToTime"] = valid_to_time
        if valid_to_date is not UNSET:
            field_dict["validToDate"] = valid_to_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.url_link_type import UrlLinkType

        d = src_dict.copy()
        _name = d.pop("name", UNSET)
        name: Union[Unset, MessageChannelTypeName]
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = MessageChannelTypeName(_name)

        urls = []
        _urls = d.pop("urls", UNSET)
        for urls_item_data in _urls or []:
            urls_item = UrlLinkType.from_dict(urls_item_data)

            urls.append(urls_item)

        valid_from_time = d.pop("validFromTime", UNSET)

        valid_from_date = d.pop("validFromDate", UNSET)

        valid_to_time = d.pop("validToTime", UNSET)

        valid_to_date = d.pop("validToDate", UNSET)

        message_channel_type = cls(
            name=name,
            urls=urls,
            valid_from_time=valid_from_time,
            valid_from_date=valid_from_date,
            valid_to_time=valid_to_time,
            valid_to_date=valid_to_date,
        )

        message_channel_type.additional_properties = d
        return message_channel_type

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
