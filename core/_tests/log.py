import unittest

from unittest import TestCase

from core.log import Log

class LogTestCase(TestCase):

    def setUp(self) -> None:
        self.log = Log('my-log')

    def test_debug_message(self):
        pass

    def test_info_message(self):
        pass

    def test_warning_message(self):
        pass

    def test_error_message(self):
        pass

    def test_critical_message(self):
        pass

if __name__ == '__main__':
    unittest.main()
