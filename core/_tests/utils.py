
import os
import unittest
from unittest import TestCase

from core.serialize import loads


from core.utils import mount_response_dict, merge_sort

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


    def test_merge_sort(self):
        self.assertEqual(merge_sort([8, 3 ,5, 1, 4, 2, 6, 9, 7]), [1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(merge_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]), [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])
        self.assertEqual(merge_sort([1, 2, 3, 4, 5, 6, 7, 8, 9]), [1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(merge_sort([9, 8, 7, 6, 5, 4, 3, 2, 1]), [1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(merge_sort([42]), [42])
        self.assertEqual(merge_sort([7, 7, 7, 7, 7, 7, 7]), [7, 7, 7, 7, 7, 7, 7])
        self.assertEqual(merge_sort([]), [])
        self.assertEqual(merge_sort([3.1, 2.4, 5.9, 1.2, 4.6]), [1.2, 2.4, 3.1, 4.6, 5.9])
        self.assertEqual(merge_sort([-3, -1, -4, -1, -5, -9, -2, -6, -5, -3, -5]), [-9, -6, -5, -5, -5, -4, -3, -3, -2, -1, -1])
        self.assertEqual(merge_sort([3, -1, 4, 1, -5, 9, -2, 6, -5, 3, -5]), [-5, -5, -5, -2, -1, 1, 3, 3, 4, 6, 9])
        self.assertEqual(merge_sort([12, 11, 45, 21, 0, -5, 34, 76, 89, -2, 99, 54, -33, 28]), [-33, -5, -2, 0, 11, 12, 21, 28, 34, 45, 54, 76, 89, 99])

        self.assertEqual(merge_sort([8, 3, 5, 1, 4, 2, 6, 9, 7], 'desc'), [9, 8, 7, 6, 5, 4, 3, 2, 1])
        self.assertEqual(merge_sort([12, 11, 45, 21, 0, -5, 34, 76, 89, -2, 99, 54, -33, 28], 'desc'), [99, 89, 76, 54, 45, 34, 28, 21, 12, 11, 0, -2, -5, -33])

    def test_recursive_filtering(self):
        pass




if __name__ == '__main__':
    unittest.main()
