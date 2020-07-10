import unittest
import boto3
from moto import mock_dynamodb2
from . import index

class TestDynamo(unittest.TestCase):
    def setUp(self):
        pass

    @mock_dynamodb2
    def test_get_visitors_counter(self):
        # Set up a mock dynamodb using ddbmock
        tablename = 'unittest'
        dynamodb = boto3.resource('dynamodb', 'us-east-1')
        index.create_dynamo_table(tablename)
        index.put_table_counters(tablename, 0)
        result = index.get_visitors_counter(tablename)
        self.assertIsNotNone(result)
