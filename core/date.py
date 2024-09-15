
from typing import Any

from datetime import datetime


class DateTime(datetime):

    @classmethod
    def now(cls): # pylint: disable=arguments-differ
        return super().now()

    @classmethod
    def stringfy_date(cls, date: Any) -> str:
        to_string = date.strftime('%Y%m%d T%H:%M:%S')
        return to_string
    