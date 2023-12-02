from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pagination_cursor import PaginationCursor
    from ..models.service_journey import ServiceJourney
    from ..models.train_stop_assignment_hint import TrainStopAssignmentHint


T = TypeVar("T", bound="PTRideLeg")


@_attrs_define
class PTRideLeg:
    """Public-Transportation Leg (aka OJP TimedLeg).<br>Inherited from `Leg`.

    Attributes:
        id (str): Unique Index ordered within Trip (may be casted to Integer for local indexing). Example: 1.
        mode (str): Mode of the Leg
        type (str): **Inheritance discriminator to proper Subclass** (technical field required by [OpenApi 3
            Discriminator](https://swagger.io/docs/specification/data-models/inheritance-and-polymorphism/)) makes
            deserialization at consumer side easier.
        service_journey (ServiceJourney): A passenger carrying vehicle journey for one specified operation day.
        distance (Union[Unset, int]): Total distance for Leg (in meter).
        duration (Union[Unset, str]): [duration](https://www.w3.org/TR/xmlschema11-2/#duration)
        group_reservation_status (Union[Unset, str]): Denotes if reservations are possible for groups on this specific
            `Trip`. Only given if parameter 'includeGroupReservation' is requested.<br>x-extensible-enum: [see [CAPRE
            ReservationDemandResponse::status](https://developer.sbb.ch/apis/capre/documentation),UNKNOWN] where `UNKNOWN`
            is an additional state by J-S, if requests to CAPRE fail.
        pagination_cursor (Union[Unset, PaginationCursor]): Pagination-cursor for next/previous of the same. By means in
            a Trip context earlier/later.
        train_stop_assignment_hint (Union[Unset, TrainStopAssignmentHint]): Hints which `TrainStopAssignment's` of
            `PTRideLeg` are potentially available for first `StopCall::departure` or last `StopCall::arrival`. Needs
            &includeTrainStopAssignments=NONE
    """

    id: str
    mode: str
    type: str
    service_journey: "ServiceJourney"
    distance: Union[Unset, int] = UNSET
    duration: Union[Unset, str] = UNSET
    group_reservation_status: Union[Unset, str] = UNSET
    pagination_cursor: Union[Unset, "PaginationCursor"] = UNSET
    train_stop_assignment_hint: Union[Unset, "TrainStopAssignmentHint"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        mode = self.mode
        type = self.type
        service_journey = self.service_journey.to_dict()

        distance = self.distance
        duration = self.duration
        group_reservation_status = self.group_reservation_status
        pagination_cursor: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pagination_cursor, Unset):
            pagination_cursor = self.pagination_cursor.to_dict()

        train_stop_assignment_hint: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.train_stop_assignment_hint, Unset):
            train_stop_assignment_hint = self.train_stop_assignment_hint.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "mode": mode,
                "type": type,
                "serviceJourney": service_journey,
            }
        )
        if distance is not UNSET:
            field_dict["distance"] = distance
        if duration is not UNSET:
            field_dict["duration"] = duration
        if group_reservation_status is not UNSET:
            field_dict["groupReservationStatus"] = group_reservation_status
        if pagination_cursor is not UNSET:
            field_dict["paginationCursor"] = pagination_cursor
        if train_stop_assignment_hint is not UNSET:
            field_dict["trainStopAssignmentHint"] = train_stop_assignment_hint

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pagination_cursor import PaginationCursor
        from ..models.service_journey import ServiceJourney
        from ..models.train_stop_assignment_hint import TrainStopAssignmentHint

        d = src_dict.copy()
        id = d.pop("id")

        mode = d.pop("mode")

        type = d.pop("type")

        service_journey = ServiceJourney.from_dict(d.pop("serviceJourney"))

        distance = d.pop("distance", UNSET)

        duration = d.pop("duration", UNSET)

        group_reservation_status = d.pop("groupReservationStatus", UNSET)

        _pagination_cursor = d.pop("paginationCursor", UNSET)
        pagination_cursor: Union[Unset, PaginationCursor]
        if isinstance(_pagination_cursor, Unset):
            pagination_cursor = UNSET
        else:
            pagination_cursor = PaginationCursor.from_dict(_pagination_cursor)

        _train_stop_assignment_hint = d.pop("trainStopAssignmentHint", UNSET)
        train_stop_assignment_hint: Union[Unset, TrainStopAssignmentHint]
        if isinstance(_train_stop_assignment_hint, Unset):
            train_stop_assignment_hint = UNSET
        else:
            train_stop_assignment_hint = TrainStopAssignmentHint.from_dict(_train_stop_assignment_hint)

        pt_ride_leg = cls(
            id=id,
            mode=mode,
            type=type,
            service_journey=service_journey,
            distance=distance,
            duration=duration,
            group_reservation_status=group_reservation_status,
            pagination_cursor=pagination_cursor,
            train_stop_assignment_hint=train_stop_assignment_hint,
        )

        pt_ride_leg.additional_properties = d
        return pt_ride_leg

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
