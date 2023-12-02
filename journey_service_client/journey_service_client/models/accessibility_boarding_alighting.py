from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.linked_text import LinkedText


T = TypeVar("T", bound="AccessibilityBoardingAlighting")


@_attrs_define
class AccessibilityBoardingAlighting:
    """Hint for handicaped people at a StopPlace to board or alight a Vehicle on a PTRideLeg. Relates to `forBoarding` and
    `forAlighting`.

        Attributes:
            limitation (str): The most relevant boarding/alighting accessibility restriction.<br>x-extensible-enum: [NO_HINT
                ,BOARDING_ALIGHTING_SELF,BOARDING_ALIGHTING_BY_CREW,BOARDING_ALIGHTING_BY_NOTIFICATION,BOARDING_ALIGHTING_SHUTTL
                E_TRANSPORT,BOARDING_ALIGHTING_NOT_POSSIBLE]
            name (str): Textual value for `limitation`.<br>(Translated according to Accept-Language.)
            description (str): Further description about `limitation` consequences.<br>(Translated according to Accept-
                Language.)
            assistance_service (LinkedText): Text template with optional formattable parameters. Useful to represent in UIs
                as clickable features like an e-Mail, phone or URL.<br>Usage see for e.g.
                [`Notice::text`](https://github.com/SchweizerischeBundesbahnen/journey-service/blob/master/JSON-
                Objects.md#linkedtext).
            corporate_identity_icon (str): Icon-identifier to represent the related `limitation`. See [SBB Corporate-
                Identity catalog (CDN, aka FIGMA Icons)](https://www.figma.com/file/UQBd7cHKav0hr9oXYp7opJ/SBB-Icons?node-
                id=395%3A2952&t=ad26LgREBbTANSK5-1) Example: sa-rs.
    """

    limitation: str
    name: str
    description: str
    assistance_service: "LinkedText"
    corporate_identity_icon: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        limitation = self.limitation
        name = self.name
        description = self.description
        assistance_service = self.assistance_service.to_dict()

        corporate_identity_icon = self.corporate_identity_icon

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "limitation": limitation,
                "name": name,
                "description": description,
                "assistanceService": assistance_service,
                "corporateIdentityIcon": corporate_identity_icon,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.linked_text import LinkedText

        d = src_dict.copy()
        limitation = d.pop("limitation")

        name = d.pop("name")

        description = d.pop("description")

        assistance_service = LinkedText.from_dict(d.pop("assistanceService"))

        corporate_identity_icon = d.pop("corporateIdentityIcon")

        accessibility_boarding_alighting = cls(
            limitation=limitation,
            name=name,
            description=description,
            assistance_service=assistance_service,
            corporate_identity_icon=corporate_identity_icon,
        )

        accessibility_boarding_alighting.additional_properties = d
        return accessibility_boarding_alighting

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
