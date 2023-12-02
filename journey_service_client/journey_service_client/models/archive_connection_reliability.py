from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ArchiveConnectionReliability")


@_attrs_define
class ArchiveConnectionReliability:
    """Reliability of the connection or potential alternative connections **in the past** that will indicate the likelihood
    of getting the user to the requested destination in time (given by `Archive API /v3/archive/{archiveDate}/trips`
    only).

        Attributes:
            original (str): Reliability of the connection itself regarding its realtime status including cancellations,
                delays etc. to the get to the destination in time.<br>x-extensible-enum: [UNKNOWN,GUARANTEED,HIGH,LOW,ABORTIVE]
                Default: 'UNKNOWN'.
            alternative (str): Reliability of an alternative connection to the original connection regarding its realtime
                status including cancellations, delays etc.<br>x-extensible-enum: [UNKNOWN,GUARANTEED,HIGH,LOW,ABORTIVE]
    """

    alternative: str
    original: str = "UNKNOWN"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        original = self.original
        alternative = self.alternative

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "original": original,
                "alternative": alternative,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        original = d.pop("original")

        alternative = d.pop("alternative")

        archive_connection_reliability = cls(
            original=original,
            alternative=alternative,
        )

        archive_connection_reliability.additional_properties = d
        return archive_connection_reliability

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
