import uuid

from core.date import DateTime

import unittest
from unittest import TestCase, mock

from unittest.mock import MagicMock

from core.serialize import dumps, loads
from entities.article import Article


class SerializeTestCase(TestCase):

    def setUp(self) -> None:
        self.data = {'outer': {'inner': {'key': 'value'}}}
        self.serialized_json_data = '{"outer": {"inner": {"key": "value"}}}'
        self.serialized_pickle_data = b'\x80\x04\x95(\x00\x00\x00\x00\x00\x00\x00}\x94\x8c\x05outer\x94}\x94\x8c\x05inner\x94}\x94\x8c\x03key\x94\x8c\x05value\x94sss.'
        return super().setUp()

    ##############################################
    # DUMPS TEST CASE
    ##############################################
    def test_dumps_with_json(self):
        expected_data = '{"outer": {"inner": {"key": "value"}}}'
        result = dumps(self.data)

        self.assertEqual(result, expected_data)

    def test_dumps_with_entity(self):
        expected_data = '{"id": "553ef2c44d814982a0ce77e6264113c5", "title": "Something", "description": "description", "creation_time": "20240815 T11:09:15", "date": "August 15, 2024", "content": "content", "image_url": "https://example.com", "url_title": "something"}'

        with mock.patch('uuid.uuid4') as mock_id, \
            mock.patch('core.date.DateTime.now') as mock_date:
            mock_date.return_value = DateTime(2024, 8, 15, 11, 9, 15, 15659)
            mock_id.return_value = uuid.UUID('553ef2c4-4d81-4982-a0ce-77e6264113c5')
            article = Article(title='something', description='description', content='content', image_url='https://example.com')

            result = dumps(article.__dict__)

        self.assertEqual(result, expected_data)

    def test_dumps_with_pickle(self):
        expected_data = b'\x80\x04\x95(\x00\x00\x00\x00\x00\x00\x00}\x94\x8c\x05outer\x94}\x94\x8c\x05inner\x94}\x94\x8c\x03key\x94\x8c\x05value\x94sss.'
        result = dumps(self.data, 'pickle')
        self.assertEqual(result, expected_data)

    def test_dumps_with_invalid_protocol(self):
        with self.assertRaises(ValueError) as context:
            dumps(self.data, 'invalid-protocol')
        self.assertEqual(str(context.exception), 'Invalid protocol type: "invalid-protocol", options are "json" or "pickle".')

    def test_loads_with_json(self):
        expected_data = {'outer': {'inner': {'key': 'value'}}}
        result = loads(self.serialized_json_data)
        self.assertEqual(result, expected_data)

    def test_loads_with_pickle(self):
        expected_data = {'outer': {'inner': {'key': 'value'}}}
        result = loads(self.serialized_pickle_data, 'pickle')
        self.assertEqual(result, expected_data)

    def test_loads_with_invalid_protocol(self):
        with self.assertRaises(ValueError) as context:
            loads(self.serialized_json_data, 'invalid-protocol')
        self.assertEqual(str(context.exception), 'Invalid protocol type: "invalid-protocol", options are "json" or "pickle".')

    def test_dumps_with_loads(self):
        expected_data = {'outer': {'inner': {'key': 'value'}}}
        result = loads(dumps(self.data))
        self.assertEqual(result, expected_data)

    def test_loads_with_dumps(self):
        expected_data = '{"outer": {"inner": {"key": "value"}}}'
        result = dumps(loads(self.serialized_json_data))
        self.assertEqual(result, expected_data)


    def test_loads_with_entity(self):
        expected_data = {'id': '553ef2c44d814982a0ce77e6264113c5', 'title': 'Title', 'description': 'description', 'creation_time': '20240915 T11:09:15', 'date': 'September 15, 2024', 'content': 'content', 'image_url': 'https://example.com', 'url_title': 'title'}

        with mock.patch('uuid.uuid4') as mock_id, \
            mock.patch('core.date.DateTime.now') as mock_date:
            mock_date.return_value = DateTime(2024, 9, 15, 11, 9, 15, 15659)
            mock_id.return_value = uuid.UUID('553ef2c4-4d81-4982-a0ce-77e6264113c5')
            article = Article('title', 'description', 'content', 'https://example.com')
            serialized_entity = dumps(article.__dict__)
            result = loads(serialized_entity)

        self.assertEqual(result, expected_data)

    def test_loads_with_dumps_pickle(self):
        expected_data = b'\x80\x04\x95(\x00\x00\x00\x00\x00\x00\x00}\x94\x8c\x05outer\x94}\x94\x8c\x05inner\x94}\x94\x8c\x03key\x94\x8c\x05value\x94sss.'
        result = dumps(loads(self.serialized_pickle_data, 'pickle'), 'pickle')
        self.assertEqual(result, expected_data)

    def test_dumps_with_loads_pickle(self):
        expected_data = {'outer': {'inner': {'key': 'value'}}}
        result = loads(dumps(self.data, 'pickle'), 'pickle')
        self.assertEqual(result, expected_data)


if __name__ == '__main__':
    unittest.main()
