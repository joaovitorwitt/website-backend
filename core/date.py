
from datetime import datetime


class DateTime(datetime):

    @classmethod
    def now(cls): # pylint: disable=arguments-differ
        return super().now()

    @classmethod
    def stringfy_date(cls, date: 'DateTime', date_format: str = '%Y%m%d T%H:%M:%S' ) -> str:
        to_string = date.strftime(date_format)
        return to_string

    @classmethod
    def string_to_date(cls, date: str, date_format: str = '%Y%m%d T%H:%M:%S') -> 'DateTime':
        return super().strptime(date, date_format)
