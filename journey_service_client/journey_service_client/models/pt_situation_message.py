from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.audience import Audience
    from ..models.links import Links
    from ..models.publication_window import PublicationWindow


T = TypeVar("T", bound="PTSituationMessage")


@_attrs_define
class PTSituationMessage:
    """A public transportation situation broadcast message affecting the planned PT operation (source HIM, aki
    Siri::PtSituation).<br>Situations might be caused by a disruption (like an incident, construction site, deviation
    etc) and typically relate to some area (geofence) and passing `ServiceProduct` resp. concrete `ServiceJourney's`.

        Attributes:
            id (str): Identity of message (aka HIM ID). Example: x944292.
            priority (int): Priority rank (the smaller the higher): low = 80, medium = 60, high = 40, de:Grossereignis = 20
                Example: 80.
            title (str): Heading of message formatted according to SBB business rule (aka HIM head) Example: Einschränkungen
                im Bahnverkehr: Bern.
            detail (str): Complete Footer/text of message formatted according to SBB business rule (HTML tags like BR(eak)
                are possible). Scoped for browser based UIs (aka HIM text). Example: Grund: Ausserordentliche
                Bauarbeiten.<br>Dauer der Einschränkung: unbestimmt.<br>Die SBB wird so schnell wie möglich weiter informieren..
            detail_short (str): Abbreviated Footer/text of message formatted according to SBB business rule (HTML tags like
                BR(eak) are possible). Scoped for App UIs. Example: Der Bahnverkehr im Bahnhof Bern ist beeinträchtigt..
            audiences (List['Audience']):
            alternate_id (Union[Unset, str]): Alternate identity of message (aka HIM externalID). This may contain values
                set by 'Via' service and therefore relate to RCS-ALEA ID useful for Liveticker, if given. Example:
                2195004195693.
            distribution_period (Union[Unset, PublicationWindow]): A period during which the situation should be published.
            links (Union[Unset, Links]): List of links as per [HATEOAS](https://en.wikipedia.org/wiki/HATEOAS) principle.
    """

    id: str
    priority: int
    title: str
    detail: str
    detail_short: str
    audiences: List["Audience"]
    alternate_id: Union[Unset, str] = UNSET
    distribution_period: Union[Unset, "PublicationWindow"] = UNSET
    links: Union[Unset, "Links"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        priority = self.priority
        title = self.title
        detail = self.detail
        detail_short = self.detail_short
        audiences = []
        for audiences_item_data in self.audiences:
            audiences_item = audiences_item_data.to_dict()

            audiences.append(audiences_item)

        alternate_id = self.alternate_id
        distribution_period: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.distribution_period, Unset):
            distribution_period = self.distribution_period.to_dict()

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "priority": priority,
                "title": title,
                "detail": detail,
                "detailShort": detail_short,
                "audiences": audiences,
            }
        )
        if alternate_id is not UNSET:
            field_dict["alternateId"] = alternate_id
        if distribution_period is not UNSET:
            field_dict["distributionPeriod"] = distribution_period
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.audience import Audience
        from ..models.links import Links
        from ..models.publication_window import PublicationWindow

        d = src_dict.copy()
        id = d.pop("id")

        priority = d.pop("priority")

        title = d.pop("title")

        detail = d.pop("detail")

        detail_short = d.pop("detailShort")

        audiences = []
        _audiences = d.pop("audiences")
        for audiences_item_data in _audiences:
            audiences_item = Audience.from_dict(audiences_item_data)

            audiences.append(audiences_item)

        alternate_id = d.pop("alternateId", UNSET)

        _distribution_period = d.pop("distributionPeriod", UNSET)
        distribution_period: Union[Unset, PublicationWindow]
        if isinstance(_distribution_period, Unset):
            distribution_period = UNSET
        else:
            distribution_period = PublicationWindow.from_dict(_distribution_period)

        _links = d.pop("links", UNSET)
        links: Union[Unset, Links]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = Links.from_dict(_links)

        pt_situation_message = cls(
            id=id,
            priority=priority,
            title=title,
            detail=detail,
            detail_short=detail_short,
            audiences=audiences,
            alternate_id=alternate_id,
            distribution_period=distribution_period,
            links=links,
        )

        pt_situation_message.additional_properties = d
        return pt_situation_message

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
