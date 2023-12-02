from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="HimSummary")


@_attrs_define
class HimSummary:
    """Trip overall him info.

    Attributes:
        information (bool): Contains INFORMATION message(s).
        construction_site (bool): Contains CONSTRUCTION_SITE message(s).
        disturbance (bool): Contains DISTURBANCE (disruption) message(s).
        delay (bool): Contains delay message(s).
        train_replacement (bool): Contains train-replacement message(s).
        end_message (bool): Contains END-MESSAGE message(s).
    """

    information: bool
    construction_site: bool
    disturbance: bool
    delay: bool
    train_replacement: bool
    end_message: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        information = self.information
        construction_site = self.construction_site
        disturbance = self.disturbance
        delay = self.delay
        train_replacement = self.train_replacement
        end_message = self.end_message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "information": information,
                "constructionSite": construction_site,
                "disturbance": disturbance,
                "delay": delay,
                "trainReplacement": train_replacement,
                "endMessage": end_message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        information = d.pop("information")

        construction_site = d.pop("constructionSite")

        disturbance = d.pop("disturbance")

        delay = d.pop("delay")

        train_replacement = d.pop("trainReplacement")

        end_message = d.pop("endMessage")

        him_summary = cls(
            information=information,
            construction_site=construction_site,
            disturbance=disturbance,
            delay=delay,
            train_replacement=train_replacement,
            end_message=end_message,
        )

        him_summary.additional_properties = d
        return him_summary

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
