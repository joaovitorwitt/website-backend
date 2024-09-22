import unittest
from unittest import TestCase, mock

import uuid

from core.criptography import generate_unique_id

class CriptographyTestCase(TestCase):

    def test_generate_unique_id(self):
        with mock.patch('uuid.uuid4') as mock_uuid:
            mock_uuid.return_value = uuid.UUID('553ef2c4-4d81-4982-a0ce-77e6264113c5')
            result = generate_unique_id()
        self.assertEqual('553ef2c44d814982a0ce77e6264113c5', result)


if __name__ == '__main__':
    unittest.main()
