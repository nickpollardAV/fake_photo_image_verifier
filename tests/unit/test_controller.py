import boto3

from unittest import mock, TestCase
from unittest.mock import patch

from src.controller import Controller

mock_event = {
        "Records": [
            {
                "eventVersion": "2.1",
                "eventSource": "aws:s3",
                "awsRegion": "xxxxxxxxxxxxx",
                "eventTime": "2021-01-23T14:56:07.335Z",
                "eventName": "ObjectCreated:Put",
                "userIdentity": {
                    "principalId": "xxxxxxxxxxxxxxxxxx"
                },
                "requestParameters": {
                    "sourceIPAddress": "xxxxxxxxxxxxxxxxx"
                },
                "responseElements": {
                    "x-amz-request-id": "xxxxxx",
                    "x-amz-id-2": "xxxxxxxxxxxxxxxxxxxxxxxx"
                },
                "s3": {
                    "s3SchemaVersion": "1.0",
                    "configurationId": "xxxxxxxxxxxxxxxxxxxxxxxxxxx",
                    "bucket": {
                        "name": "test_bucket",
                        "ownerIdentity": {
                            "principalId": "xxxxxxxxxxxxxxxxxx"
                        },
                        "arn": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
                    },
                    "object": {
                        "key": "test_pic.png",
                        "size": 81170,
                        "eTag": "xxxxxxxxxxxxxxxxxx",
                        "sequencer": "xxxxxxxxxxxxxxxxxxxxxx"
                    }
                }
            }
        ]
        }

class ControllerTest(TestCase):

    @mock.patch("boto3.client")
    def test_controller_initialises_s3_client(self, mock_client):
        self.controller = Controller()

        self.controller.run_steps(mock_event)

        mock_client.assert_called_with("s3")
