from enum import Enum


class SubscriptionPeriodDaysInWeekItem(str, Enum):
    FRIDAY = "FRIDAY"
    MONDAY = "MONDAY"
    SATURDAY = "SATURDAY"
    SUNDAY = "SUNDAY"
    THURSDAY = "THURSDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"

    def __str__(self) -> str:
        return str(self.value)
