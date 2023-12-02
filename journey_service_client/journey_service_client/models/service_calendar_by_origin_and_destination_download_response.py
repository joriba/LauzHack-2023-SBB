from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceCalendarByOriginAndDestinationDownloadResponse")


@_attrs_define
class ServiceCalendarByOriginAndDestinationDownloadResponse:
    """Contains either pollId if PDF is still being generated or final PDF download URL for enduser.

    Attributes:
        poll_id (Union[Unset, str]): Id to further poll until related `downloadUrl` is provided, might take a few
            seconds.) Example: https://p2w.sbb.hafas.cloud/bin/tb/query-p2w.exe/fny?tb2json=1&id=yhi6.6g62.kxsn.gcwx.
        download_url (Union[Unset, str]): Link to **download specific timetable (PDF)** (independent of J-S and may be
            done by any enduser). Example: https://p2w.sbb.hafas.cloud/bin/tb/query-
            p2w.exe/GeneveZuerich_hb.pdf?pathinfo=/dn&dwn=t9/t9i2ugw2kxcjxuwg_1_1.pdf.
    """

    poll_id: Union[Unset, str] = UNSET
    download_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        poll_id = self.poll_id
        download_url = self.download_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if poll_id is not UNSET:
            field_dict["pollId"] = poll_id
        if download_url is not UNSET:
            field_dict["downloadUrl"] = download_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        poll_id = d.pop("pollId", UNSET)

        download_url = d.pop("downloadUrl", UNSET)

        service_calendar_by_origin_and_destination_download_response = cls(
            poll_id=poll_id,
            download_url=download_url,
        )

        service_calendar_by_origin_and_destination_download_response.additional_properties = d
        return service_calendar_by_origin_and_destination_download_response

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
