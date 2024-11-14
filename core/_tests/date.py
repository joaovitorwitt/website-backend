import unittest
from unittest import TestCase, mock

from core.date import DateTime


class DateTimeTestCase(TestCase):

    def test_now(self):
        with mock.patch('core.date.DateTime.now') as mock_now:
            mock_now.return_value = DateTime(2024, 10, 23, 19, 14, 43, 371209)
            result = DateTime.now()
        self.assertEqual(result, DateTime(2024, 10, 23, 19, 14, 43, 371209))

    def test_stringfy_date(self):
        access_date = DateTime(2024, 10, 23, 19, 25, 30)
        self.assertEqual(DateTime.stringfy_date(access_date), '20241023 T19:25:30')
        self.assertEqual(DateTime.stringfy_date(access_date, date_format='%Y-%m-%d'), '2024-10-23')
        self.assertEqual(DateTime.stringfy_date(access_date, date_format='%Y%m%d'), '20241023')
        self.assertEqual(DateTime.stringfy_date(access_date, date_format='%Y%d%m'), '20242310')

    def test_string_to_date(self):
        self.assertEqual(DateTime.string_to_date('20241023 T19:25:30'), DateTime(2024, 10, 23, 19, 25, 30))
        self.assertEqual(DateTime.string_to_date('20241023', date_format='%Y%m%d'), DateTime(2024, 10, 23))
        self.assertEqual(DateTime.string_to_date('20241023120000', date_format='%Y%m%d%H%M%S'), DateTime(2024, 10, 23, 12, 0, 0))

if __name__ == "__main__":
    unittest.main()
