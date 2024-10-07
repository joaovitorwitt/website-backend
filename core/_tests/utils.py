
import os
import unittest
from unittest import TestCase

from core.serialize import loads


from core.utils import mount_response_dict

class UtilsTestCase(TestCase):

    def setUp(self) -> None:
        self.rows = [[123, 456], [789, 951]]
        self.columns = ['abc', 'def']

        self.complex_columns = [
            "Content",
            "Description",
            "Title",
            "UUID",
            "created_at",
            "date",
            "id",
            "image_url",
            "url_title"
        ]
        return super().setUp()

    def test_mount_response_dict(self):
        expected_data = [{'abc': 123, 'def': 456}, {'abc': 789, 'def': 951}]
        result = mount_response_dict(self.rows, self.columns)

        self.assertEqual(result, expected_data)


    def test_mount_response_dict_with_complex_data(self):
        current_dir = os.path.dirname(__file__)

        with open(f'{current_dir}/fixtures/complex.json', encoding='utf-8') as json:
            complex_json = loads(json.read())

        result = mount_response_dict(complex_json, self.complex_columns)

        with open(f'{current_dir}/fixtures/expected.json', encoding='utf-8') as _json:
            expected_response = loads(_json.read())

        self.assertEqual(result, expected_response)


    def test_mount_response_dict_with_invalid_number_of_elements(self):
        cols = ['abc', 'def', 'ghi']
        rows = [[1,2,3], [4,5,6], [7,8,9,0]]

        with self.assertRaises(ValueError) as context:
            mount_response_dict(rows, cols)

        self.assertEqual(str(context.exception), 'invalid length')


if __name__ == '__main__':
    unittest.main()
