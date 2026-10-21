import unittest
from unittest.mock import Mock, patch

import cohpy


class TestMatchHistoryByProfileId(unittest.TestCase):
    @patch('cohpy.endpoint.requests.get')
    def test_get_history_by_profile_id(self, get):
        payload = {
            'result': {'code': 0, 'message': 'SUCCESS'},
            'matchHistoryStats': [{'id': 123}],
            'profiles': [{'profile_id': 871}],
        }
        response = Mock(status_code=200)
        response.json.return_value = payload
        get.return_value = response

        result = cohpy.get_api_client().match_history_by_profile_id(profile_id=871)

        self.assertEqual(result, {
            'matchHistoryStats': [{'id': 123}],
            'profiles': [{'profile_id': 871}],
        })
        get.assert_called_once_with(
            'https://coh3-api.reliclink.com/community/leaderboard/'
            'getRecentMatchHistoryByProfileId?title=coh3&profile_id=871'
        )

    @patch('cohpy.endpoint.requests.get')
    def test_can_keep_server_status(self, get):
        payload = {
            'result': {'code': 0, 'message': 'SUCCESS'},
            'matchHistoryStats': [{'id': 123}],
            'profiles': [{'profile_id': 871}],
        }
        response = Mock(status_code=200)
        response.json.return_value = payload
        get.return_value = response

        result = cohpy.get_api_client().match_history_by_profile_id(
            profile_id=871,
            remove_server_status=False,
        )

        self.assertEqual(result, payload)
