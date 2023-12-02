from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.direction import Direction
    from ..models.line_string import LineString
    from ..models.notice import Notice
    from ..models.operating_period import OperatingPeriod
    from ..models.pt_situation import PTSituation
    from ..models.scheduled_stop_point import ScheduledStopPoint
    from ..models.service_alteration import ServiceAlteration
    from ..models.service_product import ServiceProduct


T = TypeVar("T", bound="ServiceJourney")


@_attrs_define
class ServiceJourney:
    """A passenger carrying vehicle journey for one specified operation day.

    Attributes:
        id (str): Underlying system specific unique identifier representing a concrete (partial) route for a specific
            vehicle and time. Be aware this is just a temporary id and may change daily! Additionally check for `notices`
            with `Notice::type=INFO`, `name=JY`, `text=<SwissJourneyId>` for a more standardized permanent [Swiss Journey-ID
            (SJYID)](https://transportdatamanagement.ch/content/uploads/2021/05/SwissJourneyID_DE_1_2.pdf)Data resulting out
            of this MUST NOT be presented to enduser (for e.g. SBB channels), set wisely! within a planning period. Example:
            1|17166|0|85|18032019.
        stop_points (List['ScheduledStopPoint']):
        service_products (List['ServiceProduct']):
        service_alteration (ServiceAlteration): Status (realtime changes) to a `ServiceJourney` and might impact planned
            routing.
        notices (List['Notice']):
        situations (List['PTSituation']):
        operating_periods (List['OperatingPeriod']):
        directions (List['Direction']):
        quay_type_name (Union[Unset, str]): Depending on a train, ship or whatever Vehicle there is a specific
            terminology for its appropriate quay-name. Since all `stopPoints` are passed by the same Vehicle this
            translation is usable for all `ScheduledStopPoint::*Quay*` contained by this `ServiceJourney`. See related
            `quayTypeShortName` for an abbreviated translation.<br>(Translated according to Accept-Language.) Example:
            Gleis.
        quay_type_short_name (Union[Unset, str]): Abbreviation for related `quayTypeName`.<br>(Translated according to
            Accept-Language.) Example: Gl..
        spatial_projection (Union[Unset, LineString]): LineString in
            [GeoJSON](https://datatracker.ietf.org/doc/html/rfc7946) format.
    """

    id: str
    stop_points: List["ScheduledStopPoint"]
    service_products: List["ServiceProduct"]
    service_alteration: "ServiceAlteration"
    notices: List["Notice"]
    situations: List["PTSituation"]
    operating_periods: List["OperatingPeriod"]
    directions: List["Direction"]
    quay_type_name: Union[Unset, str] = UNSET
    quay_type_short_name: Union[Unset, str] = UNSET
    spatial_projection: Union[Unset, "LineString"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        stop_points = []
        for stop_points_item_data in self.stop_points:
            stop_points_item = stop_points_item_data.to_dict()

            stop_points.append(stop_points_item)

        service_products = []
        for service_products_item_data in self.service_products:
            service_products_item = service_products_item_data.to_dict()

            service_products.append(service_products_item)

        service_alteration = self.service_alteration.to_dict()

        notices = []
        for notices_item_data in self.notices:
            notices_item = notices_item_data.to_dict()

            notices.append(notices_item)

        situations = []
        for situations_item_data in self.situations:
            situations_item = situations_item_data.to_dict()

            situations.append(situations_item)

        operating_periods = []
        for operating_periods_item_data in self.operating_periods:
            operating_periods_item = operating_periods_item_data.to_dict()

            operating_periods.append(operating_periods_item)

        directions = []
        for directions_item_data in self.directions:
            directions_item = directions_item_data.to_dict()

            directions.append(directions_item)

        quay_type_name = self.quay_type_name
        quay_type_short_name = self.quay_type_short_name
        spatial_projection: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.spatial_projection, Unset):
            spatial_projection = self.spatial_projection.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "stopPoints": stop_points,
                "serviceProducts": service_products,
                "serviceAlteration": service_alteration,
                "notices": notices,
                "situations": situations,
                "operatingPeriods": operating_periods,
                "directions": directions,
            }
        )
        if quay_type_name is not UNSET:
            field_dict["quayTypeName"] = quay_type_name
        if quay_type_short_name is not UNSET:
            field_dict["quayTypeShortName"] = quay_type_short_name
        if spatial_projection is not UNSET:
            field_dict["spatialProjection"] = spatial_projection

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.direction import Direction
        from ..models.line_string import LineString
        from ..models.notice import Notice
        from ..models.operating_period import OperatingPeriod
        from ..models.pt_situation import PTSituation
        from ..models.scheduled_stop_point import ScheduledStopPoint
        from ..models.service_alteration import ServiceAlteration
        from ..models.service_product import ServiceProduct

        d = src_dict.copy()
        id = d.pop("id")

        stop_points = []
        _stop_points = d.pop("stopPoints")
        for stop_points_item_data in _stop_points:
            stop_points_item = ScheduledStopPoint.from_dict(stop_points_item_data)

            stop_points.append(stop_points_item)

        service_products = []
        _service_products = d.pop("serviceProducts")
        for service_products_item_data in _service_products:
            service_products_item = ServiceProduct.from_dict(service_products_item_data)

            service_products.append(service_products_item)

        service_alteration = ServiceAlteration.from_dict(d.pop("serviceAlteration"))

        notices = []
        _notices = d.pop("notices")
        for notices_item_data in _notices:
            notices_item = Notice.from_dict(notices_item_data)

            notices.append(notices_item)

        situations = []
        _situations = d.pop("situations")
        for situations_item_data in _situations:
            situations_item = PTSituation.from_dict(situations_item_data)

            situations.append(situations_item)

        operating_periods = []
        _operating_periods = d.pop("operatingPeriods")
        for operating_periods_item_data in _operating_periods:
            operating_periods_item = OperatingPeriod.from_dict(operating_periods_item_data)

            operating_periods.append(operating_periods_item)

        directions = []
        _directions = d.pop("directions")
        for directions_item_data in _directions:
            directions_item = Direction.from_dict(directions_item_data)

            directions.append(directions_item)

        quay_type_name = d.pop("quayTypeName", UNSET)

        quay_type_short_name = d.pop("quayTypeShortName", UNSET)

        _spatial_projection = d.pop("spatialProjection", UNSET)
        spatial_projection: Union[Unset, LineString]
        if isinstance(_spatial_projection, Unset):
            spatial_projection = UNSET
        else:
            spatial_projection = LineString.from_dict(_spatial_projection)

        service_journey = cls(
            id=id,
            stop_points=stop_points,
            service_products=service_products,
            service_alteration=service_alteration,
            notices=notices,
            situations=situations,
            operating_periods=operating_periods,
            directions=directions,
            quay_type_name=quay_type_name,
            quay_type_short_name=quay_type_short_name,
            spatial_projection=spatial_projection,
        )

        service_journey.additional_properties = d
        return service_journey

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
