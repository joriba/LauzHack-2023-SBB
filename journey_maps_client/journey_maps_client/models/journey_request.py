from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.journey_request_lang import JourneyRequestLang
from ..types import UNSET, Unset

T = TypeVar("T", bound="JourneyRequest")


@_attrs_define
class JourneyRequest:
    """Journey request

    Attributes:
        ctx (str): Reconstruction context. Unique identification of a connection. Reconstruction context can be
            retrieved from a previously requested connection list ("Verbindungsabfrage"). Use base64 encoding, or at least
            UTF-8 and URL encoding. Example: T%24A%3D1%40O%3DLuzern%2C+Wey%40X%3D8312721%40Y%3D47055770%40L%3D8581978%40a%3D
            128%40%24A%3D1%40O%3DLuzern%2C+Bahnhof%40X%3D8310249%40Y%3D47050754%40L%3D8508450%40a%3D128%40%24201806131347%24
            201806131352%24NFO+7+++%24%241%24%C2%A7W%24A%3D1%40O%3DLuzern%2C+Bahnhof%40X%3D8310249%40Y%3D47050754%40L%3D8508
            450%40a%3D128%40%24A%3D1%40O%3DLuzern%40X%3D8310168%40Y%3D47050170%40L%3D8505000%40a%3D128%40%24201806131352%242
            01806131357%24%24%241%24%C2%A7T%24A%3D1%40O%3DLuzern%40X%3D8310168%40Y%3D47050170%40L%3D8505000%40a%3D128%40%24A
            %3D1%40O%3DBern%40X%3D7439122%40Y%3D46948825%40L%3D8507000%40a%3D128%40%24201806131400%24201806131500%24IR+15+++
            %24%241%24%C2%A7W%24A%3D1%40O%3DBern%40X%3D7439122%40Y%3D46948825%40L%3D8507000%40a%3D128%40%24A%3D1%40O%3DBern%
            2C+Bahnhof%40X%3D7440210%40Y%3D46948106%40L%3D8576646%40a%3D128%40%24201806131500%24201806131506%24%24%241%24%C2
            %A7T%24A%3D1%40O%3DBern%2C+Bahnhof%40X%3D7440210%40Y%3D46948106%40L%3D8576646%40a%3D128%40%24A%3D1%40O%3DBern%2C
            +Kursaal%40X%3D7449612%40Y%3D46952889%40L%3D8590020%40a%3D128%40%24201806131507%24201806131511%24NFT+9+++%24%241
            %24
        lang (JourneyRequestLang): Language. Example value: de
        indoor (Union[Unset, bool]):
        include_situations (Union[Unset, bool]): Include route situation-messages as features, concerning public
            transportation (aka HIM, de:Betriebslage und Störungen).
    """

    ctx: str
    lang: JourneyRequestLang
    indoor: Union[Unset, bool] = False
    include_situations: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ctx = self.ctx
        lang = self.lang.value

        indoor = self.indoor
        include_situations = self.include_situations

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ctx": ctx,
                "lang": lang,
            }
        )
        if indoor is not UNSET:
            field_dict["indoor"] = indoor
        if include_situations is not UNSET:
            field_dict["includeSituations"] = include_situations

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ctx = d.pop("ctx")

        lang = JourneyRequestLang(d.pop("lang"))

        indoor = d.pop("indoor", UNSET)

        include_situations = d.pop("includeSituations", UNSET)

        journey_request = cls(
            ctx=ctx,
            lang=lang,
            indoor=indoor,
            include_situations=include_situations,
        )

        journey_request.additional_properties = d
        return journey_request

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
