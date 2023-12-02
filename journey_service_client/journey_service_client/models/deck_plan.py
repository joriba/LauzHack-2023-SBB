from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeckPlan")


@_attrs_define
class DeckPlan:
    """Plan of the build plan of vehicle-type such as a car (data quality might not be guaranted properly for all
    `TrainElement's`).

        Attributes:
            type_technical (Union[Unset, str]): Vehicle-type resp. technical expression of a physical `TrainElement` (car,
                wagon) within a `CompoundTrain` (aka de:FahrzeugType gemäss Zugbildungsplan (ZBP)), source CERES.(On
                `TrainElement` always given, but not guaranteed on `CompoundTrain`.) Example: RABe533_SBB.
            type_advertised (Union[Unset, str]): Popular train-model like 'Dosto', 'Domino', 'ICN', .. Relates to
                `typeTechnical`. Example: Flirt.
            type_advertised_link (Union[Unset, str]): Related to `typeAdvertised`. Specialized sub-site of [unsere
                Züge](https://www.sbb.ch/de/bahnhof-services/waehrend-der-reise/unsere-zuege.html), [über uns -
                Flotte](https://www.bls.ch/de/unternehmen/ueber-uns/flotte#/), [Fahrzeuge -
                Flotte](https://www.sob.ch/dienstleistungen/fahrzeuge/flotte). Example: https://www.sbb.ch/de/bahnhof-
                services/waehrend-der-reise/unsere-zuege/flirt.html.
            build_category (Union[Unset, str]): May contain a concrete descrpition of about how many decks (aka floors) a
                car may provide. Example: Regionalverkehrszug, einstöckig.
    """

    type_technical: Union[Unset, str] = UNSET
    type_advertised: Union[Unset, str] = UNSET
    type_advertised_link: Union[Unset, str] = UNSET
    build_category: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type_technical = self.type_technical
        type_advertised = self.type_advertised
        type_advertised_link = self.type_advertised_link
        build_category = self.build_category

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_technical is not UNSET:
            field_dict["typeTechnical"] = type_technical
        if type_advertised is not UNSET:
            field_dict["typeAdvertised"] = type_advertised
        if type_advertised_link is not UNSET:
            field_dict["typeAdvertisedLink"] = type_advertised_link
        if build_category is not UNSET:
            field_dict["buildCategory"] = build_category

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type_technical = d.pop("typeTechnical", UNSET)

        type_advertised = d.pop("typeAdvertised", UNSET)

        type_advertised_link = d.pop("typeAdvertisedLink", UNSET)

        build_category = d.pop("buildCategory", UNSET)

        deck_plan = cls(
            type_technical=type_technical,
            type_advertised=type_advertised,
            type_advertised_link=type_advertised_link,
            build_category=build_category,
        )

        deck_plan.additional_properties = d
        return deck_plan

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
