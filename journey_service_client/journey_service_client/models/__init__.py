""" Contains all the data models used in inputs/outputs """

from .access_end import AccessEnd
from .access_leg import AccessLeg
from .accessibility_boarding_alighting import AccessibilityBoardingAlighting
from .accessibility_enum import AccessibilityEnum
from .affected_by_lines_request_body import AffectedByLinesRequestBody
from .affected_edge import AffectedEdge
from .affected_journeys_at_stop_places_request_body import AffectedJourneysAtStopPlacesRequestBody
from .affected_journeys_request_body import AffectedJourneysRequestBody
from .affected_line_reference import AffectedLineReference
from .affected_lines_at_stop_places_request_body import AffectedLinesAtStopPlacesRequestBody
from .affected_region import AffectedRegion
from .alternate_match_enum import AlternateMatchEnum
from .archive_connection_reliability import ArchiveConnectionReliability
from .arrival import Arrival
from .arrival_journey_status import ArrivalJourneyStatus
from .arrival_response import ArrivalResponse
from .arrival_v3 import ArrivalV3
from .audience import Audience
from .audience_enum import AudienceEnum
from .audience_link import AudienceLink
from .boarding_position import BoardingPosition
from .car import Car
from .car_class import CarClass
from .car_occupancy import CarOccupancy
from .car_type import CarType
from .circle_geofence import CircleGeofence
from .compound_train import CompoundTrain
from .connection import Connection
from .connection_end import ConnectionEnd
from .connection_reliability import ConnectionReliability
from .connection_reliability_alternative import ConnectionReliabilityAlternative
from .connection_reliability_original import ConnectionReliabilityOriginal
from .coordinates_wgs84 import CoordinatesWGS84
from .date_time_interval import DateTimeInterval
from .dated_vehicle_journey import DatedVehicleJourney
from .dated_vehicle_journey_reference import DatedVehicleJourneyReference
from .dated_vehicle_journey_response import DatedVehicleJourneyResponse
from .deck_plan import DeckPlan
from .departure import Departure
from .departure_response import DepartureResponse
from .departure_v2 import DepartureV2
from .departure_v2_journey_status import DepartureV2JourneyStatus
from .direction import Direction
from .direction_v2 import DirectionV2
from .eco_balance import EcoBalance
from .eco_balance_detail import EcoBalanceDetail
from .eco_map import EcoMap
from .equipment import Equipment
from .equipment_type import EquipmentType
from .equipment_type_enum import EquipmentTypeEnum
from .ext_xml_body import ExtXmlBody
from .ext_xml_body_document_language import ExtXmlBodyDocumentLanguage
from .ext_xml_body_stop_behaviour import ExtXmlBodyStopBehaviour
from .ext_xml_response import ExtXmlResponse
from .facility_for_info_portal_response import FacilityForInfoPortalResponse
from .forecast_element import ForecastElement
from .formation_alert import FormationAlert
from .geofence_circle import GeofenceCircle
from .get_affected_journeys_accept_language import GetAffectedJourneysAcceptLanguage
from .get_affected_journeys_at_stop_places_accept_language import GetAffectedJourneysAtStopPlacesAcceptLanguage
from .get_affected_lines_accept_language import GetAffectedLinesAcceptLanguage
from .get_affected_lines_at_stop_places_accept_language import GetAffectedLinesAtStopPlacesAcceptLanguage
from .get_archived_places_by_name_accept_language import GetArchivedPlacesByNameAcceptLanguage
from .get_archived_trips_by_id_accept_language import GetArchivedTripsByIdAcceptLanguage
from .get_archived_trips_by_origin_and_destination_accept_language import (
    GetArchivedTripsByOriginAndDestinationAcceptLanguage,
)
from .get_archived_vehicle_journeys_by_id_accept_language import GetArchivedVehicleJourneysByIdAcceptLanguage
from .get_arrivals_by_origin_accept_language import GetArrivalsByOriginAcceptLanguage
from .get_arrivals_by_origin_response_501 import GetArrivalsByOriginResponse501
from .get_arrivals_by_origin_transport_products_item import GetArrivalsByOriginTransportProductsItem
from .get_dated_vehicle_journey_by_id_accept_language import GetDatedVehicleJourneyByIdAcceptLanguage
from .get_dated_vehicle_journeys_by_service_accept_language import GetDatedVehicleJourneysByServiceAcceptLanguage
from .get_dated_vehicle_journeys_by_vehicle_id_accept_language import GetDatedVehicleJourneysByVehicleIdAcceptLanguage
from .get_delay_confirmation_by_date_and_journey_id_and_transport_product_name_and_station_accept_language import (
    GetDelayConfirmationByDateAndJourneyIdAndTransportProductNameAndStationAcceptLanguage,
)
from .get_delay_confirmation_by_date_and_journey_id_and_transport_product_name_and_station_response_501 import (
    GetDelayConfirmationByDateAndJourneyIdAndTransportProductNameAndStationResponse501,
)
from .get_delay_confirmation_by_date_and_origin_and_destination_accept_language import (
    GetDelayConfirmationByDateAndOriginAndDestinationAcceptLanguage,
)
from .get_delay_confirmation_by_date_and_origin_and_destination_response_501 import (
    GetDelayConfirmationByDateAndOriginAndDestinationResponse501,
)
from .get_delay_confirmation_by_date_and_transport_product_name_accept_language import (
    GetDelayConfirmationByDateAndTransportProductNameAcceptLanguage,
)
from .get_delay_confirmation_by_date_and_transport_product_name_response_501 import (
    GetDelayConfirmationByDateAndTransportProductNameResponse501,
)
from .get_departures_by_origin_accept_language import GetDeparturesByOriginAcceptLanguage
from .get_departures_by_origin_response_501 import GetDeparturesByOriginResponse501
from .get_departures_by_origin_transport_products_item import GetDeparturesByOriginTransportProductsItem
from .get_facility_for_info_portal_accept_language import GetFacilityForInfoPortalAcceptLanguage
from .get_ojp_places_by_coordinates_accept_language import GetOjpPlacesByCoordinatesAcceptLanguage
from .get_ojp_places_by_coordinates_type_item import GetOjpPlacesByCoordinatesTypeItem
from .get_ojp_places_by_name_accept_language import GetOjpPlacesByNameAcceptLanguage
from .get_ojp_places_by_name_type_item import GetOjpPlacesByNameTypeItem
from .get_ojp_trip_leg_by_id_accept_language import GetOjpTripLegByIdAcceptLanguage
from .get_ojp_trips_by_origin_and_destination_accept_language import GetOjpTripsByOriginAndDestinationAcceptLanguage
from .get_ojp_vehicle_journeys_by_arrival_at_destination_accept_language import (
    GetOjpVehicleJourneysByArrivalAtDestinationAcceptLanguage,
)
from .get_ojp_vehicle_journeys_by_departure_at_origin_accept_language import (
    GetOjpVehicleJourneysByDepartureAtOriginAcceptLanguage,
)
from .get_places_by_coordinates_accept_language import GetPlacesByCoordinatesAcceptLanguage
from .get_places_by_coordinates_geojson_accept_language import GetPlacesByCoordinatesGeojsonAcceptLanguage
from .get_places_by_coordinates_geojson_type_item import GetPlacesByCoordinatesGeojsonTypeItem
from .get_places_by_coordinates_type_item import GetPlacesByCoordinatesTypeItem
from .get_places_by_name_accept_language import GetPlacesByNameAcceptLanguage
from .get_places_by_name_type_item import GetPlacesByNameTypeItem
from .get_routes_accept_language import GetRoutesAcceptLanguage
from .get_routes_by_date_and_car_uic_accept_language import GetRoutesByDateAndCarUicAcceptLanguage
from .get_routes_by_date_and_car_uic_response_501 import GetRoutesByDateAndCarUicResponse501
from .get_routes_by_date_and_car_uic_stop_behaviour import GetRoutesByDateAndCarUicStopBehaviour
from .get_routes_by_journey_reference_accept_language import GetRoutesByJourneyReferenceAcceptLanguage
from .get_routes_by_journey_reference_response_501 import GetRoutesByJourneyReferenceResponse501
from .get_routes_by_journey_reference_stop_behaviour import GetRoutesByJourneyReferenceStopBehaviour
from .get_routes_response_501 import GetRoutesResponse501
from .get_routes_stop_behaviour import GetRoutesStopBehaviour
from .get_service_calendar_by_origin_and_destination_accept_language import (
    GetServiceCalendarByOriginAndDestinationAcceptLanguage,
)
from .get_situations_by_ids_accept_language import GetSituationsByIdsAcceptLanguage
from .get_situations_by_rss_feed_accept_language import GetSituationsByRSSFeedAcceptLanguage
from .get_situations_by_rss_feed_language import GetSituationsByRSSFeedLanguage
from .get_situations_by_validity_accept_language import GetSituationsByValidityAcceptLanguage
from .get_situations_by_validity_affected_scope import GetSituationsByValidityAffectedScope
from .get_stations_accept_language import GetStationsAcceptLanguage
from .get_stations_response_501 import GetStationsResponse501
from .get_stations_sort_order import GetStationsSortOrder
from .get_stations_vehicle_types_item import GetStationsVehicleTypesItem
from .get_stop_place_by_id_accept_language import GetStopPlaceByIdAcceptLanguage
from .get_stop_places_accept_language import GetStopPlacesAcceptLanguage
from .get_stop_places_sort_order import GetStopPlacesSortOrder
from .get_train_formation_by_journey_reference_and_stop_accept_language import (
    GetTrainFormationByJourneyReferenceAndStopAcceptLanguage,
)
from .get_train_formation_by_journey_reference_and_stop_stop_type import (
    GetTrainFormationByJourneyReferenceAndStopStopType,
)
from .get_train_formation_by_reconstruction_context_accept_language import (
    GetTrainFormationByReconstructionContextAcceptLanguage,
)
from .get_train_formation_by_reconstruction_context_destination_type import (
    GetTrainFormationByReconstructionContextDestinationType,
)
from .get_train_formation_by_reconstruction_context_origin_type import (
    GetTrainFormationByReconstructionContextOriginType,
)
from .get_train_stop_assignments_accept_language import GetTrainStopAssignmentsAcceptLanguage
from .get_train_stop_assignments_by_service_journey_id_accept_language import (
    GetTrainStopAssignmentsByServiceJourneyIdAcceptLanguage,
)
from .get_trips_by_id_accept_language import GetTripsByIdAcceptLanguage
from .get_trips_by_id_and_partial_search_context_accept_language import (
    GetTripsByIdAndPartialSearchContextAcceptLanguage,
)
from .get_trips_by_leg_accept_language import GetTripsByLegAcceptLanguage
from .get_trips_by_origin_and_destination_accept_language import GetTripsByOriginAndDestinationAcceptLanguage
from .get_trips_by_reconstruction_context_accept_language import GetTripsByReconstructionContextAcceptLanguage
from .get_trips_by_reconstruction_context_alternate_match import GetTripsByReconstructionContextAlternateMatch
from .get_trips_by_reconstruction_context_and_via_accept_language import (
    GetTripsByReconstructionContextAndViaAcceptLanguage,
)
from .get_trips_by_reconstruction_context_and_via_infos import GetTripsByReconstructionContextAndViaInfos
from .get_trips_by_reconstruction_context_and_via_response_501 import GetTripsByReconstructionContextAndViaResponse501
from .get_trips_by_reconstruction_context_and_via_stop_behaviour import (
    GetTripsByReconstructionContextAndViaStopBehaviour,
)
from .get_trips_by_reconstruction_context_infos import GetTripsByReconstructionContextInfos
from .get_trips_by_reconstruction_context_realtime_mode import GetTripsByReconstructionContextRealtimeMode
from .get_trips_by_reconstruction_context_stop_behaviour import GetTripsByReconstructionContextStopBehaviour
from .get_trips_by_redefinition_accept_language import GetTripsByRedefinitionAcceptLanguage
from .get_trips_by_road_accept_language import GetTripsByRoadAcceptLanguage
from .get_trips_interval_by_origin_and_destination_accept_language import (
    GetTripsIntervalByOriginAndDestinationAcceptLanguage,
)
from .get_trips_with_eco_balance_by_reconstruction_context_accept_language import (
    GetTripsWithEcoBalanceByReconstructionContextAcceptLanguage,
)
from .get_trips_with_eco_balance_by_reconstruction_context_car_class import (
    GetTripsWithEcoBalanceByReconstructionContextCarClass,
)
from .get_trips_with_eco_balance_by_reconstruction_context_car_engine import (
    GetTripsWithEcoBalanceByReconstructionContextCarEngine,
)
from .get_trips_with_eco_balance_by_reconstruction_context_car_euro_norm import (
    GetTripsWithEcoBalanceByReconstructionContextCarEuroNorm,
)
from .get_trips_with_eco_balance_by_reconstruction_context_car_fuel_type import (
    GetTripsWithEcoBalanceByReconstructionContextCarFuelType,
)
from .get_trips_with_eco_balance_by_reconstruction_context_car_load import (
    GetTripsWithEcoBalanceByReconstructionContextCarLoad,
)
from .get_trips_with_eco_balance_by_reconstruction_context_flight_feeder import (
    GetTripsWithEcoBalanceByReconstructionContextFlightFeeder,
)
from .get_trips_with_eco_balance_by_reconstruction_context_flight_load import (
    GetTripsWithEcoBalanceByReconstructionContextFlightLoad,
)
from .get_trips_with_eco_balance_by_reconstruction_context_load import GetTripsWithEcoBalanceByReconstructionContextLoad
from .get_trips_with_eco_balance_by_reconstruction_context_public_transport_load import (
    GetTripsWithEcoBalanceByReconstructionContextPublicTransportLoad,
)
from .get_vehicle_journeys_by_arrival_at_destination_accept_language import (
    GetVehicleJourneysByArrivalAtDestinationAcceptLanguage,
)
from .get_vehicle_journeys_by_departure_at_origin_accept_language import (
    GetVehicleJourneysByDepartureAtOriginAcceptLanguage,
)
from .get_weather_accept_language import GetWeatherAcceptLanguage
from .get_weather_location_type import GetWeatherLocationType
from .group_reservation_status_enum import GroupReservationStatusEnum
from .him_message_v2 import HimMessageV2
from .him_message_v2_category import HimMessageV2Category
from .him_summary import HimSummary
from .hysteresis import Hysteresis
from .info import Info
from .inheritance_response import InheritanceResponse
from .journey_detail import JourneyDetail
from .journey_detail_journey_status import JourneyDetailJourneyStatus
from .json_response import JsonResponse
from .leg import Leg
from .leg_v2 import LegV2
from .leg_v2_formation_hint import LegV2FormationHint
from .leg_v2_group_reservation_status import LegV2GroupReservationStatus
from .leg_v2_journey_status import LegV2JourneyStatus
from .leg_v2_type import LegV2Type
from .legend_item import LegendItem
from .legend_item_v3 import LegendItemV3
from .line_affected import LineAffected
from .line_affected_response import LineAffectedResponse
from .line_string import LineString
from .linked_text import LinkedText
from .linked_text_arguments import LinkedTextArguments
from .links import Links
from .local_time import LocalTime
from .location_identity import LocationIdentity
from .location_identity_type import LocationIdentityType
from .message_channel_type import MessageChannelType
from .message_channel_type_name import MessageChannelTypeName
from .message_edge import MessageEdge
from .message_edge_direction import MessageEdgeDirection
from .message_region import MessageRegion
from .navigation_path_assignment import NavigationPathAssignment
from .network_zone import NetworkZone
from .note import Note
from .note_value import NoteValue
from .note_value_arguments import NoteValueArguments
from .notice import Notice
from .notice_attribute_enum import NoticeAttributeEnum
from .occupancy_average_enum import OccupancyAverageEnum
from .operating_period import OperatingPeriod
from .operating_period_subscription import OperatingPeriodSubscription
from .operator import Operator
from .optimisation_method import OptimisationMethod
from .pagination_cursor import PaginationCursor
from .perron import Perron
from .place import Place
from .place_ref_by_name_with_distance import PlaceRefByNameWithDistance
from .place_response import PlaceResponse
from .point import Point
from .point_of_interest import PointOfInterest
from .point_of_interest_category import PointOfInterestCategory
from .postal_address import PostalAddress
from .problem import Problem
from .pt_connection_leg import PTConnectionLeg
from .pt_ride_leg import PTRideLeg
from .pt_ride_leg_subscription import PTRideLegSubscription
from .pt_situation import PTSituation
from .pt_situation_affected_scope import PTSituationAffectedScope
from .pt_situation_message import PTSituationMessage
from .pt_via_no_change_at_reference import PTViaNoChangeAtReference
from .pt_via_no_change_at_reference_status import PTViaNoChangeAtReferenceStatus
from .pt_via_not_reference import PTViaNotReference
from .pt_via_not_reference_status import PTViaNotReferenceStatus
from .pt_via_reference import PTViaReference
from .pt_via_reference_status import PTViaReferenceStatus
from .publication_window import PublicationWindow
from .quay import Quay
from .quay_subscription import QuaySubscription
from .realtime_mode_enum import RealtimeModeEnum
from .scheduled_stop_point import ScheduledStopPoint
from .scheduled_stop_point_reference import ScheduledStopPointReference
from .scheduled_stop_point_subscription import ScheduledStopPointSubscription
from .section import Section
from .service_alteration import ServiceAlteration
from .service_calendar import ServiceCalendar
from .service_calendar_by_origin_and_destination_download_response import (
    ServiceCalendarByOriginAndDestinationDownloadResponse,
)
from .service_calendar_by_origin_and_destination_request_body import ServiceCalendarByOriginAndDestinationRequestBody
from .service_calendar_by_origin_and_destination_request_body_days_in_week_item import (
    ServiceCalendarByOriginAndDestinationRequestBodyDaysInWeekItem,
)
from .service_days_v2 import ServiceDaysV2
from .service_journey import ServiceJourney
from .service_journey_affected import ServiceJourneyAffected
from .service_journey_affected_response import ServiceJourneyAffectedResponse
from .service_journey_subscription import ServiceJourneySubscription
from .service_product import ServiceProduct
from .service_product_subscription import ServiceProductSubscription
from .situation_cause_enum import SituationCauseEnum
from .situation_response import SituationResponse
from .station import Station
from .station_station_type import StationStationType
from .station_type import StationType
from .station_vehicle_types_item import StationVehicleTypesItem
from .stations_page import StationsPage
from .stop_call import StopCall
from .stop_call_subscription import StopCallSubscription
from .stop_formation import StopFormation
from .stop_formation_leaving_direction import StopFormationLeavingDirection
from .stop_place import StopPlace
from .stop_place_classification import StopPlaceClassification
from .stop_place_detailed import StopPlaceDetailed
from .stop_place_detailed_response import StopPlaceDetailedResponse
from .stop_place_subscription import StopPlaceSubscription
from .stop_point_interval import StopPointInterval
from .stop_point_mode_enum import StopPointModeEnum
from .stop_v2 import StopV2
from .stop_v2_accessibility_item import StopV2AccessibilityItem
from .stop_v2_accessibility_most_relevant import StopV2AccessibilityMostRelevant
from .stop_v2_arrival_prognosis_type import StopV2ArrivalPrognosisType
from .stop_v2_avg_occupancy_first_class import StopV2AvgOccupancyFirstClass
from .stop_v2_avg_occupancy_second_class import StopV2AvgOccupancySecondClass
from .stop_v2_boarding_alighting_status import StopV2BoardingAlightingStatus
from .stop_v2_departure_prognosis_type import StopV2DeparturePrognosisType
from .stop_v2_exit_side import StopV2ExitSide
from .stop_v2_stop_status import StopV2StopStatus
from .stop_v2_type import StopV2Type
from .subscription import Subscription
from .subscription_period import SubscriptionPeriod
from .subscription_period_days_in_week_item import SubscriptionPeriodDaysInWeekItem
from .tariff_zone import TariffZone
from .timed_weather_forecast import TimedWeatherForecast
from .train import Train
from .train_component import TrainComponent
from .train_element import TrainElement
from .train_formation import TrainFormation
from .train_stop_assignment import TrainStopAssignment
from .train_stop_assignment_hint import TrainStopAssignmentHint
from .train_stop_assignment_response import TrainStopAssignmentResponse
from .train_stop_assignment_response_train_stop_assignments import TrainStopAssignmentResponseTrainStopAssignments
from .train_stop_assignments_enum import TrainStopAssignmentsEnum
from .transport_mode_enum import TransportModeEnum
from .transport_product_v2 import TransportProductV2
from .transport_product_v2_category import TransportProductV2Category
from .transport_product_v2_vehicle_type import TransportProductV2VehicleType
from .trip import Trip
from .trip_mobility_filter import TripMobilityFilter
from .trip_response import TripResponse
from .trip_status import TripStatus
from .trip_subscription import TripSubscription
from .trip_subscription_deletion_response import TripSubscriptionDeletionResponse
from .trip_subscription_details_response import TripSubscriptionDetailsResponse
from .trip_subscription_request_body import TripSubscriptionRequestBody
from .trip_subscription_response import TripSubscriptionResponse
from .trip_subscription_status_response import TripSubscriptionStatusResponse
from .trip_summary import TripSummary
from .trip_summary_v2 import TripSummaryV2
from .trip_summary_v2_infos_rt import TripSummaryV2InfosRt
from .trip_summary_v2_max_occupancy_first_class import TripSummaryV2MaxOccupancyFirstClass
from .trip_summary_v2_max_occupancy_second_class import TripSummaryV2MaxOccupancySecondClass
from .trip_v2 import TripV2
from .trips_by_leg_request_body import TripsByLegRequestBody
from .trips_by_origin_and_destination_request_body import TripsByOriginAndDestinationRequestBody
from .trips_by_origin_and_destination_request_body_include_ecology_comparison import (
    TripsByOriginAndDestinationRequestBodyIncludeEcologyComparison,
)
from .trips_by_origin_and_destination_request_body_include_intermediate_stops import (
    TripsByOriginAndDestinationRequestBodyIncludeIntermediateStops,
)
from .trips_interval_by_origin_and_destination_request_body import TripsIntervalByOriginAndDestinationRequestBody
from .trips_interval_by_origin_and_destination_request_body_include_intermediate_stops import (
    TripsIntervalByOriginAndDestinationRequestBodyIncludeIntermediateStops,
)
from .url_link_type import UrlLinkType
from .v2_trips_accept_language import V2TripsAcceptLanguage
from .v2_trips_accessibility import V2TripsAccessibility
from .v2_trips_alternate_match import V2TripsAlternateMatch
from .v2_trips_attributes_item import V2TripsAttributesItem
from .v2_trips_destination_type import V2TripsDestinationType
from .v2_trips_infos import V2TripsInfos
from .v2_trips_occupancy_average import V2TripsOccupancyAverage
from .vehicle_mode import VehicleMode
from .vehicle_mode_enum import VehicleModeEnum
from .weather_coordinates import WeatherCoordinates

__all__ = (
    "AccessEnd",
    "AccessibilityBoardingAlighting",
    "AccessibilityEnum",
    "AccessLeg",
    "AffectedByLinesRequestBody",
    "AffectedEdge",
    "AffectedJourneysAtStopPlacesRequestBody",
    "AffectedJourneysRequestBody",
    "AffectedLineReference",
    "AffectedLinesAtStopPlacesRequestBody",
    "AffectedRegion",
    "AlternateMatchEnum",
    "ArchiveConnectionReliability",
    "Arrival",
    "ArrivalJourneyStatus",
    "ArrivalResponse",
    "ArrivalV3",
    "Audience",
    "AudienceEnum",
    "AudienceLink",
    "BoardingPosition",
    "Car",
    "CarClass",
    "CarOccupancy",
    "CarType",
    "CircleGeofence",
    "CompoundTrain",
    "Connection",
    "ConnectionEnd",
    "ConnectionReliability",
    "ConnectionReliabilityAlternative",
    "ConnectionReliabilityOriginal",
    "CoordinatesWGS84",
    "DatedVehicleJourney",
    "DatedVehicleJourneyReference",
    "DatedVehicleJourneyResponse",
    "DateTimeInterval",
    "DeckPlan",
    "Departure",
    "DepartureResponse",
    "DepartureV2",
    "DepartureV2JourneyStatus",
    "Direction",
    "DirectionV2",
    "EcoBalance",
    "EcoBalanceDetail",
    "EcoMap",
    "Equipment",
    "EquipmentType",
    "EquipmentTypeEnum",
    "ExtXmlBody",
    "ExtXmlBodyDocumentLanguage",
    "ExtXmlBodyStopBehaviour",
    "ExtXmlResponse",
    "FacilityForInfoPortalResponse",
    "ForecastElement",
    "FormationAlert",
    "GeofenceCircle",
    "GetAffectedJourneysAcceptLanguage",
    "GetAffectedJourneysAtStopPlacesAcceptLanguage",
    "GetAffectedLinesAcceptLanguage",
    "GetAffectedLinesAtStopPlacesAcceptLanguage",
    "GetArchivedPlacesByNameAcceptLanguage",
    "GetArchivedTripsByIdAcceptLanguage",
    "GetArchivedTripsByOriginAndDestinationAcceptLanguage",
    "GetArchivedVehicleJourneysByIdAcceptLanguage",
    "GetArrivalsByOriginAcceptLanguage",
    "GetArrivalsByOriginResponse501",
    "GetArrivalsByOriginTransportProductsItem",
    "GetDatedVehicleJourneyByIdAcceptLanguage",
    "GetDatedVehicleJourneysByServiceAcceptLanguage",
    "GetDatedVehicleJourneysByVehicleIdAcceptLanguage",
    "GetDelayConfirmationByDateAndJourneyIdAndTransportProductNameAndStationAcceptLanguage",
    "GetDelayConfirmationByDateAndJourneyIdAndTransportProductNameAndStationResponse501",
    "GetDelayConfirmationByDateAndOriginAndDestinationAcceptLanguage",
    "GetDelayConfirmationByDateAndOriginAndDestinationResponse501",
    "GetDelayConfirmationByDateAndTransportProductNameAcceptLanguage",
    "GetDelayConfirmationByDateAndTransportProductNameResponse501",
    "GetDeparturesByOriginAcceptLanguage",
    "GetDeparturesByOriginResponse501",
    "GetDeparturesByOriginTransportProductsItem",
    "GetFacilityForInfoPortalAcceptLanguage",
    "GetOjpPlacesByCoordinatesAcceptLanguage",
    "GetOjpPlacesByCoordinatesTypeItem",
    "GetOjpPlacesByNameAcceptLanguage",
    "GetOjpPlacesByNameTypeItem",
    "GetOjpTripLegByIdAcceptLanguage",
    "GetOjpTripsByOriginAndDestinationAcceptLanguage",
    "GetOjpVehicleJourneysByArrivalAtDestinationAcceptLanguage",
    "GetOjpVehicleJourneysByDepartureAtOriginAcceptLanguage",
    "GetPlacesByCoordinatesAcceptLanguage",
    "GetPlacesByCoordinatesGeojsonAcceptLanguage",
    "GetPlacesByCoordinatesGeojsonTypeItem",
    "GetPlacesByCoordinatesTypeItem",
    "GetPlacesByNameAcceptLanguage",
    "GetPlacesByNameTypeItem",
    "GetRoutesAcceptLanguage",
    "GetRoutesByDateAndCarUicAcceptLanguage",
    "GetRoutesByDateAndCarUicResponse501",
    "GetRoutesByDateAndCarUicStopBehaviour",
    "GetRoutesByJourneyReferenceAcceptLanguage",
    "GetRoutesByJourneyReferenceResponse501",
    "GetRoutesByJourneyReferenceStopBehaviour",
    "GetRoutesResponse501",
    "GetRoutesStopBehaviour",
    "GetServiceCalendarByOriginAndDestinationAcceptLanguage",
    "GetSituationsByIdsAcceptLanguage",
    "GetSituationsByRSSFeedAcceptLanguage",
    "GetSituationsByRSSFeedLanguage",
    "GetSituationsByValidityAcceptLanguage",
    "GetSituationsByValidityAffectedScope",
    "GetStationsAcceptLanguage",
    "GetStationsResponse501",
    "GetStationsSortOrder",
    "GetStationsVehicleTypesItem",
    "GetStopPlaceByIdAcceptLanguage",
    "GetStopPlacesAcceptLanguage",
    "GetStopPlacesSortOrder",
    "GetTrainFormationByJourneyReferenceAndStopAcceptLanguage",
    "GetTrainFormationByJourneyReferenceAndStopStopType",
    "GetTrainFormationByReconstructionContextAcceptLanguage",
    "GetTrainFormationByReconstructionContextDestinationType",
    "GetTrainFormationByReconstructionContextOriginType",
    "GetTrainStopAssignmentsAcceptLanguage",
    "GetTrainStopAssignmentsByServiceJourneyIdAcceptLanguage",
    "GetTripsByIdAcceptLanguage",
    "GetTripsByIdAndPartialSearchContextAcceptLanguage",
    "GetTripsByLegAcceptLanguage",
    "GetTripsByOriginAndDestinationAcceptLanguage",
    "GetTripsByReconstructionContextAcceptLanguage",
    "GetTripsByReconstructionContextAlternateMatch",
    "GetTripsByReconstructionContextAndViaAcceptLanguage",
    "GetTripsByReconstructionContextAndViaInfos",
    "GetTripsByReconstructionContextAndViaResponse501",
    "GetTripsByReconstructionContextAndViaStopBehaviour",
    "GetTripsByReconstructionContextInfos",
    "GetTripsByReconstructionContextRealtimeMode",
    "GetTripsByReconstructionContextStopBehaviour",
    "GetTripsByRedefinitionAcceptLanguage",
    "GetTripsByRoadAcceptLanguage",
    "GetTripsIntervalByOriginAndDestinationAcceptLanguage",
    "GetTripsWithEcoBalanceByReconstructionContextAcceptLanguage",
    "GetTripsWithEcoBalanceByReconstructionContextCarClass",
    "GetTripsWithEcoBalanceByReconstructionContextCarEngine",
    "GetTripsWithEcoBalanceByReconstructionContextCarEuroNorm",
    "GetTripsWithEcoBalanceByReconstructionContextCarFuelType",
    "GetTripsWithEcoBalanceByReconstructionContextCarLoad",
    "GetTripsWithEcoBalanceByReconstructionContextFlightFeeder",
    "GetTripsWithEcoBalanceByReconstructionContextFlightLoad",
    "GetTripsWithEcoBalanceByReconstructionContextLoad",
    "GetTripsWithEcoBalanceByReconstructionContextPublicTransportLoad",
    "GetVehicleJourneysByArrivalAtDestinationAcceptLanguage",
    "GetVehicleJourneysByDepartureAtOriginAcceptLanguage",
    "GetWeatherAcceptLanguage",
    "GetWeatherLocationType",
    "GroupReservationStatusEnum",
    "HimMessageV2",
    "HimMessageV2Category",
    "HimSummary",
    "Hysteresis",
    "Info",
    "InheritanceResponse",
    "JourneyDetail",
    "JourneyDetailJourneyStatus",
    "JsonResponse",
    "Leg",
    "LegendItem",
    "LegendItemV3",
    "LegV2",
    "LegV2FormationHint",
    "LegV2GroupReservationStatus",
    "LegV2JourneyStatus",
    "LegV2Type",
    "LineAffected",
    "LineAffectedResponse",
    "LineString",
    "LinkedText",
    "LinkedTextArguments",
    "Links",
    "LocalTime",
    "LocationIdentity",
    "LocationIdentityType",
    "MessageChannelType",
    "MessageChannelTypeName",
    "MessageEdge",
    "MessageEdgeDirection",
    "MessageRegion",
    "NavigationPathAssignment",
    "NetworkZone",
    "Note",
    "NoteValue",
    "NoteValueArguments",
    "Notice",
    "NoticeAttributeEnum",
    "OccupancyAverageEnum",
    "OperatingPeriod",
    "OperatingPeriodSubscription",
    "Operator",
    "OptimisationMethod",
    "PaginationCursor",
    "Perron",
    "Place",
    "PlaceRefByNameWithDistance",
    "PlaceResponse",
    "Point",
    "PointOfInterest",
    "PointOfInterestCategory",
    "PostalAddress",
    "Problem",
    "PTConnectionLeg",
    "PTRideLeg",
    "PTRideLegSubscription",
    "PTSituation",
    "PTSituationAffectedScope",
    "PTSituationMessage",
    "PTViaNoChangeAtReference",
    "PTViaNoChangeAtReferenceStatus",
    "PTViaNotReference",
    "PTViaNotReferenceStatus",
    "PTViaReference",
    "PTViaReferenceStatus",
    "PublicationWindow",
    "Quay",
    "QuaySubscription",
    "RealtimeModeEnum",
    "ScheduledStopPoint",
    "ScheduledStopPointReference",
    "ScheduledStopPointSubscription",
    "Section",
    "ServiceAlteration",
    "ServiceCalendar",
    "ServiceCalendarByOriginAndDestinationDownloadResponse",
    "ServiceCalendarByOriginAndDestinationRequestBody",
    "ServiceCalendarByOriginAndDestinationRequestBodyDaysInWeekItem",
    "ServiceDaysV2",
    "ServiceJourney",
    "ServiceJourneyAffected",
    "ServiceJourneyAffectedResponse",
    "ServiceJourneySubscription",
    "ServiceProduct",
    "ServiceProductSubscription",
    "SituationCauseEnum",
    "SituationResponse",
    "Station",
    "StationsPage",
    "StationStationType",
    "StationType",
    "StationVehicleTypesItem",
    "StopCall",
    "StopCallSubscription",
    "StopFormation",
    "StopFormationLeavingDirection",
    "StopPlace",
    "StopPlaceClassification",
    "StopPlaceDetailed",
    "StopPlaceDetailedResponse",
    "StopPlaceSubscription",
    "StopPointInterval",
    "StopPointModeEnum",
    "StopV2",
    "StopV2AccessibilityItem",
    "StopV2AccessibilityMostRelevant",
    "StopV2ArrivalPrognosisType",
    "StopV2AvgOccupancyFirstClass",
    "StopV2AvgOccupancySecondClass",
    "StopV2BoardingAlightingStatus",
    "StopV2DeparturePrognosisType",
    "StopV2ExitSide",
    "StopV2StopStatus",
    "StopV2Type",
    "Subscription",
    "SubscriptionPeriod",
    "SubscriptionPeriodDaysInWeekItem",
    "TariffZone",
    "TimedWeatherForecast",
    "Train",
    "TrainComponent",
    "TrainElement",
    "TrainFormation",
    "TrainStopAssignment",
    "TrainStopAssignmentHint",
    "TrainStopAssignmentResponse",
    "TrainStopAssignmentResponseTrainStopAssignments",
    "TrainStopAssignmentsEnum",
    "TransportModeEnum",
    "TransportProductV2",
    "TransportProductV2Category",
    "TransportProductV2VehicleType",
    "Trip",
    "TripMobilityFilter",
    "TripResponse",
    "TripsByLegRequestBody",
    "TripsByOriginAndDestinationRequestBody",
    "TripsByOriginAndDestinationRequestBodyIncludeEcologyComparison",
    "TripsByOriginAndDestinationRequestBodyIncludeIntermediateStops",
    "TripsIntervalByOriginAndDestinationRequestBody",
    "TripsIntervalByOriginAndDestinationRequestBodyIncludeIntermediateStops",
    "TripStatus",
    "TripSubscription",
    "TripSubscriptionDeletionResponse",
    "TripSubscriptionDetailsResponse",
    "TripSubscriptionRequestBody",
    "TripSubscriptionResponse",
    "TripSubscriptionStatusResponse",
    "TripSummary",
    "TripSummaryV2",
    "TripSummaryV2InfosRt",
    "TripSummaryV2MaxOccupancyFirstClass",
    "TripSummaryV2MaxOccupancySecondClass",
    "TripV2",
    "UrlLinkType",
    "V2TripsAcceptLanguage",
    "V2TripsAccessibility",
    "V2TripsAlternateMatch",
    "V2TripsAttributesItem",
    "V2TripsDestinationType",
    "V2TripsInfos",
    "V2TripsOccupancyAverage",
    "VehicleMode",
    "VehicleModeEnum",
    "WeatherCoordinates",
)
