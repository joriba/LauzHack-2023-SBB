from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.linked_text import LinkedText


T = TypeVar("T", bound="Notice")


@_attrs_define
class Notice:
    """Additional information on operating Vehicle. The information may be usable for passenger. Relates to
    `includeNoticeAttributes`.

        Attributes:
            name (str): 2 letter key. **Derived from MERITS codes** for e.g. UIC Code 916-1 'reservation system code',
                though they are specified by SBB Data-Mgmt. Example: RM.
            type (str): Type of Notice. <br>x-extensible-enum: [ATTRIBUTE,INFO] Example: ATTRIBUTE.
            priority (int): A lower priority value means a higher importance (default=100).
            advertised (bool): Hint whether a passenger should see such a `Notice` being advertised (aka Transmodel
                NOTICE::canBeAdvertised).<br>Be aware if **false**: Data resulting out of this MUST NOT be presented to enduser
                (for e.g. SBB channels), set wisely!
            text (Union[Unset, LinkedText]): Text template with optional formattable parameters. Useful to represent in UIs
                as clickable features like an e-Mail, phone or URL.<br>Usage see for e.g.
                [`Notice::text`](https://github.com/SchweizerischeBundesbahnen/journey-service/blob/master/JSON-
                Objects.md#linkedtext).
            route_index_from (Union[Unset, int]): Relates to `ScheduledStop::routeIndex` where this note is valid from.
            route_index_to (Union[Unset, int]): Relates to `ScheduledStop::routeIndex` where this note is valid to.
    """

    name: str
    type: str
    priority: int
    advertised: bool = False
    text: Union[Unset, "LinkedText"] = UNSET
    route_index_from: Union[Unset, int] = UNSET
    route_index_to: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        type = self.type
        priority = self.priority
        advertised = self.advertised
        text: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.text, Unset):
            text = self.text.to_dict()

        route_index_from = self.route_index_from
        route_index_to = self.route_index_to

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type,
                "priority": priority,
                "advertised": advertised,
            }
        )
        if text is not UNSET:
            field_dict["text"] = text
        if route_index_from is not UNSET:
            field_dict["routeIndexFrom"] = route_index_from
        if route_index_to is not UNSET:
            field_dict["routeIndexTo"] = route_index_to

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.linked_text import LinkedText

        d = src_dict.copy()
        name = d.pop("name")

        type = d.pop("type")

        priority = d.pop("priority")

        advertised = d.pop("advertised")

        _text = d.pop("text", UNSET)
        text: Union[Unset, LinkedText]
        if isinstance(_text, Unset):
            text = UNSET
        else:
            text = LinkedText.from_dict(_text)

        route_index_from = d.pop("routeIndexFrom", UNSET)

        route_index_to = d.pop("routeIndexTo", UNSET)

        notice = cls(
            name=name,
            type=type,
            priority=priority,
            advertised=advertised,
            text=text,
            route_index_from=route_index_from,
            route_index_to=route_index_to,
        )

        notice.additional_properties = d
        return notice

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
