from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_product import ServiceProduct


T = TypeVar("T", bound="LineAffected")


@_attrs_define
class LineAffected:
    """Affected line (as given by a `ServiceProduct::line`).

    Attributes:
        service_product_id (Union[Unset, str]): Internal ServiceProduct id for reconstruction (aka pid). All
            `ServiceProduct's` having a `ServiceProduct::line` should provide such a `serviceProductId`.  This value will be
            null if `ServiceProduct::line` is not provided therefore.
        service_product (Union[Unset, ServiceProduct]): A passenger carrying Service (phyisical public transport
            vehicle) provided and operated by a certain Operator allocated to a concrete ServiceJourney on an
            `OperatingDay`.<br>See SBB specific transport-modes: [v580 de:Verkehrsmittelkategorien (aka Transmodel or
            OJP/Siri `VehicleMode`)](https://github.com/SchweizerischeBundesbahnen/journey-
            service/blob/master/TransportMode.md).
        affected_journeys_count (Union[Unset, int]): Concrete operating-day (aka service-day).
    """

    service_product_id: Union[Unset, str] = UNSET
    service_product: Union[Unset, "ServiceProduct"] = UNSET
    affected_journeys_count: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        service_product_id = self.service_product_id
        service_product: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.service_product, Unset):
            service_product = self.service_product.to_dict()

        affected_journeys_count = self.affected_journeys_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if service_product_id is not UNSET:
            field_dict["serviceProductId"] = service_product_id
        if service_product is not UNSET:
            field_dict["serviceProduct"] = service_product
        if affected_journeys_count is not UNSET:
            field_dict["affectedJourneysCount"] = affected_journeys_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.service_product import ServiceProduct

        d = src_dict.copy()
        service_product_id = d.pop("serviceProductId", UNSET)

        _service_product = d.pop("serviceProduct", UNSET)
        service_product: Union[Unset, ServiceProduct]
        if isinstance(_service_product, Unset):
            service_product = UNSET
        else:
            service_product = ServiceProduct.from_dict(_service_product)

        affected_journeys_count = d.pop("affectedJourneysCount", UNSET)

        line_affected = cls(
            service_product_id=service_product_id,
            service_product=service_product,
            affected_journeys_count=affected_journeys_count,
        )

        line_affected.additional_properties = d
        return line_affected

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
