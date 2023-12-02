from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.operating_period_subscription import OperatingPeriodSubscription
    from ..models.pt_ride_leg_subscription import PTRideLegSubscription


T = TypeVar("T", bound="TripSubscription")


@_attrs_define
class TripSubscription:
    """Details about a previously subscribed `Trip` (aka HCCS ServiceSubscription).

    Attributes:
        trip_id (str): Original subscribed tripId `v3/Trip::id` (format Hafas raw reconstructionContext URL encoded but
            compatible with `/v3/trips/{id}`). Example: %C2%AC%C2%B6BAIM%C2%B6t%C2%AC%C2%B6HKI%C2%B6T%24A%3D1%40O%3DGen%C3%A
            8ve%40X%3D6142455%40Y%3D46210209%40u%3D0%40L%3D8501008%40a%3D128%40%24A%3D1%40O%3DFribourg%2FFreiburg%40X%3D7151
            045%40Y%3D46803146%40u%3D0%40L%3D8504100%40a%3D128%40%24202204081242%24202204081403%24IC+1++++%24%241%24%24%24%2
            4%C2%B6KC%C2%B6%23VE%230%23CF%23100%23CA%230%23CM%230%23SICT%231%23%C2%B6KCC%C2%B6%23VE%230%23ERG%231%23HIN%230%
            23ECK%23172122%7C172122%7C172203%7C172203%7C0%7C0%7C165%7C172093%7C1%7C-2147479534%7C0%23.
        operating_periods (List['OperatingPeriodSubscription']): HCSS ServiceDays.
        legs (List['PTRideLegSubscription']): HCSS ConnectionInfo.
        monitor_flags (List[str]): Type of events that should be / are monitored.<br>- AF: Arrival times at the
            destination station of Consections
            - CF: Flag, if changing is possible
            - DF: Departure times at the start station of Consections
            - DV: Departure and Arrival delays
            - OF: Status of operation e.g. does the train operate or not
            - PF: Platform changes at departure and arrival station
            - ANSF: Guaranteed connection monitoring. Fetcher and corresponding feeder trip will be monitored
            - ALLATTRF: Monitor all attribute changes
            - REQATTRF: Monitor attributes included in the request filter (only monitor attributes relevant to the
            feasibility of a connection)
            - FTF: Freetext changes
            - FTFS: Spontanous freetext changes
            - FTFP: Planned freetext changes
            - INCOMP: Incompatible type - possible, if older and newer clients use the same HCSS
            - ARR: Arrival of train
            - DEP: Departure of train
            - DEP_NO_RT: Train should have left but no message received
            - SDF: Changes to service density frequency
            - RF: Changed routes in private transport sections
            - FF: Monitor changed (train-)formations
            - PLANF: Monitor changes in plan data like changed times, names, rideability
            - TRF Monitor time triggered events (server-defined rules like (train-)change reminders)
            - NDF Monitor notable delays (server defined specific delay values with special impacts)
            - WF: Weather-Flag: monitor weather changes
        data (Union[Unset, str]): Additional data which should be stored for that subscription, will be returned when
            client asked for subscription details. The server does not interpret this field. Warning: Do not write too much
            data in this field as messages might get too large for network communication.
        notices_positive (Union[Unset, str]): Wanted attributes for the whole connection (e.g. has toilet);
            notifications can be send in case these attributes are deactivated.
        notices_negative (Union[Unset, str]): Not wanted attributes (e.g. smoking allowed); notifications can be sent in
            case these attributes are activated.
    """

    trip_id: str
    operating_periods: List["OperatingPeriodSubscription"]
    legs: List["PTRideLegSubscription"]
    monitor_flags: List[str]
    data: Union[Unset, str] = UNSET
    notices_positive: Union[Unset, str] = UNSET
    notices_negative: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        trip_id = self.trip_id
        operating_periods = []
        for operating_periods_item_data in self.operating_periods:
            operating_periods_item = operating_periods_item_data.to_dict()

            operating_periods.append(operating_periods_item)

        legs = []
        for legs_item_data in self.legs:
            legs_item = legs_item_data.to_dict()

            legs.append(legs_item)

        monitor_flags = self.monitor_flags

        data = self.data
        notices_positive = self.notices_positive
        notices_negative = self.notices_negative

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tripId": trip_id,
                "operatingPeriods": operating_periods,
                "legs": legs,
                "monitorFlags": monitor_flags,
            }
        )
        if data is not UNSET:
            field_dict["data"] = data
        if notices_positive is not UNSET:
            field_dict["noticesPositive"] = notices_positive
        if notices_negative is not UNSET:
            field_dict["noticesNegative"] = notices_negative

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.operating_period_subscription import OperatingPeriodSubscription
        from ..models.pt_ride_leg_subscription import PTRideLegSubscription

        d = src_dict.copy()
        trip_id = d.pop("tripId")

        operating_periods = []
        _operating_periods = d.pop("operatingPeriods")
        for operating_periods_item_data in _operating_periods:
            operating_periods_item = OperatingPeriodSubscription.from_dict(operating_periods_item_data)

            operating_periods.append(operating_periods_item)

        legs = []
        _legs = d.pop("legs")
        for legs_item_data in _legs:
            legs_item = PTRideLegSubscription.from_dict(legs_item_data)

            legs.append(legs_item)

        monitor_flags = cast(List[str], d.pop("monitorFlags"))

        data = d.pop("data", UNSET)

        notices_positive = d.pop("noticesPositive", UNSET)

        notices_negative = d.pop("noticesNegative", UNSET)

        trip_subscription = cls(
            trip_id=trip_id,
            operating_periods=operating_periods,
            legs=legs,
            monitor_flags=monitor_flags,
            data=data,
            notices_positive=notices_positive,
            notices_negative=notices_negative,
        )

        trip_subscription.additional_properties = d
        return trip_subscription

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
