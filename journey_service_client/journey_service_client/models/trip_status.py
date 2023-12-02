from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TripStatus")


@_attrs_define
class TripStatus:
    """Realtime overall status of a `Trip` (depends on `PTRideLeg::serviceJourney` status).

    Attributes:
        alternative (bool): false: Planned connection; true: Realtime alternative
        valid (bool): true: Trip is possible to ride based on the current realtime situation (related to
            `Trip::serviceCalendar`, `PTRideLeg::reachable`, etc); false: **Fatal resp. not rideable as a 'whole' Trip'
            anymore** (aka OJP infeasible, ODSM invalid). Important: if this valid toggles from true to false, the passenger
            might not be able to perform his Trip, by means individual re-planning might be necessary. Default: True.
        cancelled (bool): `PTRideLeg` cancelled (de:Ausfall), relates to `cancelledFormatted`.
        partially_cancelled (bool): `PTRideLeg` partially cancelled (de:Teilausfall), relates to `cancelledFormatted`.
        quay_changed (bool): Contains at least one platform change (de:Gleis-/Kante-/Steg-Änderung) on any `PTRideLeg`.
        delayed (bool): Contains at least one delay (de:Verspätung) on any `PTRideLeg`.
        delayed_unknown (bool): Contains at least one unknown delay (de:Unbestimmte Verspätung) on any `PTRideLeg`.
        reachable (bool): If not true, changing `PTRideLeg's` is not guaranteed (de:Anschluss gehalten). Default: True.
        not_serviced_stop_points (bool): Contains at least one `StopPlace` which is not serviced (de:ausserordentliche
            Durchfahrt) on any `PTRideLeg`. Releates to `ScheduledStopPoint::stopStatus==NOT_SERVICED`.
        unplanned_stop_points (bool): true: contains additional `StopPlace` resp. `ScheduledStopPoint`
            (de:ausserordentlicher Halt). Releates to `ScheduledStopPoint::stopStatus==UNPLANNED` and
            `ServiceAlteration::unplannedStopPointsFormatted` (aka OJP Unplanned).
        alternative_formatted (Union[Unset, str]): Text intended for passengers about an alternative Trip, relates to
            `alternative`.<br>(Translated according to Accept-Language.) Example: Alternative Verbindung aufgrund der
            aktuellen Betriebslage. Bitte prüfen Sie diese kurz vor Reisebeginn nochmals auf Änderungen..
        cancelled_formatted (Union[Unset, str]): If `cancelled` or `partiallyCancelled` is true, enduser info about
            `Trip`.<br>(Translated according to Accept-Language.) Example: Diese Verbindung fällt aus..
        mobility_restricted_transfer_critical (Union[Unset, bool]): Hint whether at least one vehicle transfer is
            critical for passengers with a handicap, related to `includeAccessibility` other than `ALL` and
            `PTRideLeg::navigationPathAssignment` (otherwise null).
    """

    alternative: bool = False
    valid: bool = True
    cancelled: bool = False
    partially_cancelled: bool = False
    quay_changed: bool = False
    delayed: bool = False
    delayed_unknown: bool = False
    reachable: bool = True
    not_serviced_stop_points: bool = False
    unplanned_stop_points: bool = False
    alternative_formatted: Union[Unset, str] = UNSET
    cancelled_formatted: Union[Unset, str] = UNSET
    mobility_restricted_transfer_critical: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        alternative = self.alternative
        valid = self.valid
        cancelled = self.cancelled
        partially_cancelled = self.partially_cancelled
        quay_changed = self.quay_changed
        delayed = self.delayed
        delayed_unknown = self.delayed_unknown
        reachable = self.reachable
        not_serviced_stop_points = self.not_serviced_stop_points
        unplanned_stop_points = self.unplanned_stop_points
        alternative_formatted = self.alternative_formatted
        cancelled_formatted = self.cancelled_formatted
        mobility_restricted_transfer_critical = self.mobility_restricted_transfer_critical

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alternative": alternative,
                "valid": valid,
                "cancelled": cancelled,
                "partiallyCancelled": partially_cancelled,
                "quayChanged": quay_changed,
                "delayed": delayed,
                "delayedUnknown": delayed_unknown,
                "reachable": reachable,
                "notServicedStopPoints": not_serviced_stop_points,
                "unplannedStopPoints": unplanned_stop_points,
            }
        )
        if alternative_formatted is not UNSET:
            field_dict["alternativeFormatted"] = alternative_formatted
        if cancelled_formatted is not UNSET:
            field_dict["cancelledFormatted"] = cancelled_formatted
        if mobility_restricted_transfer_critical is not UNSET:
            field_dict["mobilityRestrictedTransferCritical"] = mobility_restricted_transfer_critical

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        alternative = d.pop("alternative")

        valid = d.pop("valid")

        cancelled = d.pop("cancelled")

        partially_cancelled = d.pop("partiallyCancelled")

        quay_changed = d.pop("quayChanged")

        delayed = d.pop("delayed")

        delayed_unknown = d.pop("delayedUnknown")

        reachable = d.pop("reachable")

        not_serviced_stop_points = d.pop("notServicedStopPoints")

        unplanned_stop_points = d.pop("unplannedStopPoints")

        alternative_formatted = d.pop("alternativeFormatted", UNSET)

        cancelled_formatted = d.pop("cancelledFormatted", UNSET)

        mobility_restricted_transfer_critical = d.pop("mobilityRestrictedTransferCritical", UNSET)

        trip_status = cls(
            alternative=alternative,
            valid=valid,
            cancelled=cancelled,
            partially_cancelled=partially_cancelled,
            quay_changed=quay_changed,
            delayed=delayed,
            delayed_unknown=delayed_unknown,
            reachable=reachable,
            not_serviced_stop_points=not_serviced_stop_points,
            unplanned_stop_points=unplanned_stop_points,
            alternative_formatted=alternative_formatted,
            cancelled_formatted=cancelled_formatted,
            mobility_restricted_transfer_critical=mobility_restricted_transfer_critical,
        )

        trip_status.additional_properties = d
        return trip_status

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
