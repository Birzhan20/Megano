import datetime

from django_diploma.settings import TIME_ZONE
import pytz


def format_date(input_datetime: datetime, month=None) -> str:
    current_tz = pytz.timezone(TIME_ZONE)
    changed_datetime = input_datetime.astimezone(current_tz)
    if month != 'digit':
        output_datetime_str = changed_datetime.strftime(
            '%a %b %d %Y %H:%M:%S GMT%z (Europe/Moscow)'
        )
    else:
        output_datetime_str = changed_datetime.strftime(
            '%Y-%m-%d %H:%M'
        )

    return output_datetime_str
