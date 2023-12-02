import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.navigation_path_assignment import NavigationPathAssignment
    from ..models.quay import Quay
    from ..models.train_stop_assignment import TrainStopAssignment


T = TypeVar("T", bound="StopCall")


@_attrs_define
class StopCall:
    """Passing a `ScheduledStopPoint` on a `ServiceJourney` may have two 'views': one for arrival and one for departure
    aspects (aka OJP LegAlight::StopPoint, LegBoard::StopPoint; NeTeX Call (which is a VIEW on a `ScheduledStopPoint`).

        Attributes:
            quay_changed (bool): Related to `quayAimed` and `quayRt`.**false** even if the related `StopCall::quayRt` is
                set, this is not considered a realtime change (acc. to SBB busines rules); **true** real `*QuayRt` change, also
                see `ServiceAlteration::quayChangedFormatted`.
            time_aimed (Union[Unset, datetime.datetime]): Date/time
                ([ISO-8601](https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) UTC with time-numoffset (like '+02:00'))
                **planned**, relates to `timeRt` (might be null for e.g. in virtual stops). Example: 2023-04-18T14:55:00+01:00.
            time_rt (Union[Unset, datetime.datetime]): Date/time
                ([ISO-8601](https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) UTC with time-numoffset (like '+02:00'))
                in **realtime** (oversteers related `timeAimed`!).
            delay_text (Union[Unset, str]): Formatted passenger message about the delay (may also relate to
                `ScheduledStopPoint::delayUndefined`) in the role of this call according to SBB business rules. Example: ca.
                +5'.
            quay_aimed (Union[Unset, Quay]): A `Quay` is the **place to board or alight a concrete vehicle by passengers**,
                aka **passenger-platform** for **train (de:Gleis)**, or **bus stand (de:Kante)** or **ship pier (de:Steg)**,
                related to a `ServiceProduct::vehicleMode`. Example: 13.
            quay_rt (Union[Unset, Quay]): A `Quay` is the **place to board or alight a concrete vehicle by passengers**, aka
                **passenger-platform** for **train (de:Gleis)**, or **bus stand (de:Kante)** or **ship pier (de:Steg)**, related
                to a `ServiceProduct::vehicleMode`. Example: 13.
            quay_formatted (Union[Unset, str]): **Currently given on `departure StopCall`**. Principally same as related
                `quayAimed` resp. its `Quay::name` but in case of wing-trains (de:Flügelzüge) specified with **direction
                specific boarding-sections**.<br>(For e.g. 'Bern to Zweisimmen' with a split of train-composition at Spiez where
                customers might reach the wrong destination if they board the wrong car!) Example: 12CD.
            train_stop_assignment (Union[Unset, TrainStopAssignment]): The association of a `TrainComponent` at a
                `ScheduledStopPoint` with a specific `StopPlace` and also possibly a `Quay` and `BoardingPosition`.
            navigation_path_assignment (Union[Unset, NavigationPathAssignment]): The allocation of a **navigation path** to
                a specific `ScheduledStopPoint` assignment, for example to indicate the path to be taken to make a
                connection.<br>Currently a **transfer-hint is given for handicaped people** at alighting at `PTRideLeg`s`
                last/alighting `ScheduledStopPoint` when transfering to next vehicle for boarding.
    """

    quay_changed: bool = False
    time_aimed: Union[Unset, datetime.datetime] = UNSET
    time_rt: Union[Unset, datetime.datetime] = UNSET
    delay_text: Union[Unset, str] = UNSET
    quay_aimed: Union[Unset, "Quay"] = UNSET
    quay_rt: Union[Unset, "Quay"] = UNSET
    quay_formatted: Union[Unset, str] = UNSET
    train_stop_assignment: Union[Unset, "TrainStopAssignment"] = UNSET
    navigation_path_assignment: Union[Unset, "NavigationPathAssignment"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        quay_changed = self.quay_changed
        time_aimed: Union[Unset, str] = UNSET
        if not isinstance(self.time_aimed, Unset):
            time_aimed = self.time_aimed.isoformat()

        time_rt: Union[Unset, str] = UNSET
        if not isinstance(self.time_rt, Unset):
            time_rt = self.time_rt.isoformat()

        delay_text = self.delay_text
        quay_aimed: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.quay_aimed, Unset):
            quay_aimed = self.quay_aimed.to_dict()

        quay_rt: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.quay_rt, Unset):
            quay_rt = self.quay_rt.to_dict()

        quay_formatted = self.quay_formatted
        train_stop_assignment: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.train_stop_assignment, Unset):
            train_stop_assignment = self.train_stop_assignment.to_dict()

        navigation_path_assignment: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.navigation_path_assignment, Unset):
            navigation_path_assignment = self.navigation_path_assignment.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "quayChanged": quay_changed,
            }
        )
        if time_aimed is not UNSET:
            field_dict["timeAimed"] = time_aimed
        if time_rt is not UNSET:
            field_dict["timeRt"] = time_rt
        if delay_text is not UNSET:
            field_dict["delayText"] = delay_text
        if quay_aimed is not UNSET:
            field_dict["quayAimed"] = quay_aimed
        if quay_rt is not UNSET:
            field_dict["quayRt"] = quay_rt
        if quay_formatted is not UNSET:
            field_dict["quayFormatted"] = quay_formatted
        if train_stop_assignment is not UNSET:
            field_dict["trainStopAssignment"] = train_stop_assignment
        if navigation_path_assignment is not UNSET:
            field_dict["navigationPathAssignment"] = navigation_path_assignment

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.navigation_path_assignment import NavigationPathAssignment
        from ..models.quay import Quay
        from ..models.train_stop_assignment import TrainStopAssignment

        d = src_dict.copy()
        quay_changed = d.pop("quayChanged")

        _time_aimed = d.pop("timeAimed", UNSET)
        time_aimed: Union[Unset, datetime.datetime]
        if isinstance(_time_aimed, Unset):
            time_aimed = UNSET
        else:
            time_aimed = isoparse(_time_aimed)

        _time_rt = d.pop("timeRt", UNSET)
        time_rt: Union[Unset, datetime.datetime]
        if isinstance(_time_rt, Unset):
            time_rt = UNSET
        else:
            time_rt = isoparse(_time_rt)

        delay_text = d.pop("delayText", UNSET)

        _quay_aimed = d.pop("quayAimed", UNSET)
        quay_aimed: Union[Unset, Quay]
        if isinstance(_quay_aimed, Unset):
            quay_aimed = UNSET
        else:
            quay_aimed = Quay.from_dict(_quay_aimed)

        _quay_rt = d.pop("quayRt", UNSET)
        quay_rt: Union[Unset, Quay]
        if isinstance(_quay_rt, Unset):
            quay_rt = UNSET
        else:
            quay_rt = Quay.from_dict(_quay_rt)

        quay_formatted = d.pop("quayFormatted", UNSET)

        _train_stop_assignment = d.pop("trainStopAssignment", UNSET)
        train_stop_assignment: Union[Unset, TrainStopAssignment]
        if isinstance(_train_stop_assignment, Unset):
            train_stop_assignment = UNSET
        else:
            train_stop_assignment = TrainStopAssignment.from_dict(_train_stop_assignment)

        _navigation_path_assignment = d.pop("navigationPathAssignment", UNSET)
        navigation_path_assignment: Union[Unset, NavigationPathAssignment]
        if isinstance(_navigation_path_assignment, Unset):
            navigation_path_assignment = UNSET
        else:
            navigation_path_assignment = NavigationPathAssignment.from_dict(_navigation_path_assignment)

        stop_call = cls(
            quay_changed=quay_changed,
            time_aimed=time_aimed,
            time_rt=time_rt,
            delay_text=delay_text,
            quay_aimed=quay_aimed,
            quay_rt=quay_rt,
            quay_formatted=quay_formatted,
            train_stop_assignment=train_stop_assignment,
            navigation_path_assignment=navigation_path_assignment,
        )

        stop_call.additional_properties = d
        return stop_call

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
