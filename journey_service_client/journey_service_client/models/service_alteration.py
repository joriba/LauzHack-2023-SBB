from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceAlteration")


@_attrs_define
class ServiceAlteration:
    """Status (realtime changes) to a `ServiceJourney` and might impact planned routing.

    Attributes:
        cancelled (bool): true: Journey is `cancelled` (de:Ausfall), default=false.
        partially_cancelled (bool): true: Journey is partially cancelled (de:Teilausfall) at beginning or end,
            default=false.
        reachable (bool): true: vehicle (`ServiceProduct`) change connection from `PTRideLeg` to `PTRideLeg` is possible
            (de: Anschluss kann gehalten werden, see `Trip::status::valid`); false: de:nicht mehr erreichbare Fahrt Default:
            True.
        redirected (bool): true: journey is redirected (aka OJP deviation).
        cancelled_formatted (Union[Unset, str]): If `cancelled`, enduser cancellation info.<br>(Translated according to
            Accept-Language.) Example: Ausfall.
        partially_cancelled_formatted (Union[Unset, str]): If `partiallyCancelled`, enduser info.<br>(Translated
            according to Accept-Language.) Example: Ausfall.
        reachable_formatted (Union[Unset, str]): Transport-product change from Leg to Leg info according to SBB business
            rules. Relates to reachable. Example: Your connecting train will be waiting, please change trains immediately..
        redirected_formatted (Union[Unset, str]): Text intended for passengers about a planned stop being skipped,
            relates to `redirected`.<br>(Translated according to Accept-Language.) Example: This vehicle is not stopping at
            all stations..
        unplanned_stop_points_formatted (Union[Unset, str]): Text intended for passengers about an additional non-
            planned stop at a station.<br>(Translated according to Accept-Language.) Example: This vehicle is making
            exceptional stops. This can lead to increased travel time..
        delay_formatted (Union[Unset, str]): Enduser text, saying whether there is a delay on PTRideLeg (referring to
            first/last Stop).<br>(Translated according to Accept-Language.) Example: Delay.
        quay_changed_formatted (Union[Unset, str]): Enduser text, saying whether there is a `Quay` change on
            `ServiceJourney` (typically referring to first and/or last `ScheduledStopPoint` on a `PTRideLeg`), which
            indicates the passengers to be careful at boarding/alighting.<br>(Translated according to Accept-Language.)
            Example: Gleisänderung.
    """

    cancelled: bool = False
    partially_cancelled: bool = False
    reachable: bool = True
    redirected: bool = False
    cancelled_formatted: Union[Unset, str] = UNSET
    partially_cancelled_formatted: Union[Unset, str] = UNSET
    reachable_formatted: Union[Unset, str] = UNSET
    redirected_formatted: Union[Unset, str] = UNSET
    unplanned_stop_points_formatted: Union[Unset, str] = UNSET
    delay_formatted: Union[Unset, str] = UNSET
    quay_changed_formatted: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cancelled = self.cancelled
        partially_cancelled = self.partially_cancelled
        reachable = self.reachable
        redirected = self.redirected
        cancelled_formatted = self.cancelled_formatted
        partially_cancelled_formatted = self.partially_cancelled_formatted
        reachable_formatted = self.reachable_formatted
        redirected_formatted = self.redirected_formatted
        unplanned_stop_points_formatted = self.unplanned_stop_points_formatted
        delay_formatted = self.delay_formatted
        quay_changed_formatted = self.quay_changed_formatted

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cancelled": cancelled,
                "partiallyCancelled": partially_cancelled,
                "reachable": reachable,
                "redirected": redirected,
            }
        )
        if cancelled_formatted is not UNSET:
            field_dict["cancelledFormatted"] = cancelled_formatted
        if partially_cancelled_formatted is not UNSET:
            field_dict["partiallyCancelledFormatted"] = partially_cancelled_formatted
        if reachable_formatted is not UNSET:
            field_dict["reachableFormatted"] = reachable_formatted
        if redirected_formatted is not UNSET:
            field_dict["redirectedFormatted"] = redirected_formatted
        if unplanned_stop_points_formatted is not UNSET:
            field_dict["unplannedStopPointsFormatted"] = unplanned_stop_points_formatted
        if delay_formatted is not UNSET:
            field_dict["delayFormatted"] = delay_formatted
        if quay_changed_formatted is not UNSET:
            field_dict["quayChangedFormatted"] = quay_changed_formatted

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cancelled = d.pop("cancelled")

        partially_cancelled = d.pop("partiallyCancelled")

        reachable = d.pop("reachable")

        redirected = d.pop("redirected")

        cancelled_formatted = d.pop("cancelledFormatted", UNSET)

        partially_cancelled_formatted = d.pop("partiallyCancelledFormatted", UNSET)

        reachable_formatted = d.pop("reachableFormatted", UNSET)

        redirected_formatted = d.pop("redirectedFormatted", UNSET)

        unplanned_stop_points_formatted = d.pop("unplannedStopPointsFormatted", UNSET)

        delay_formatted = d.pop("delayFormatted", UNSET)

        quay_changed_formatted = d.pop("quayChangedFormatted", UNSET)

        service_alteration = cls(
            cancelled=cancelled,
            partially_cancelled=partially_cancelled,
            reachable=reachable,
            redirected=redirected,
            cancelled_formatted=cancelled_formatted,
            partially_cancelled_formatted=partially_cancelled_formatted,
            reachable_formatted=reachable_formatted,
            redirected_formatted=redirected_formatted,
            unplanned_stop_points_formatted=unplanned_stop_points_formatted,
            delay_formatted=delay_formatted,
            quay_changed_formatted=quay_changed_formatted,
        )

        service_alteration.additional_properties = d
        return service_alteration

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
