#!/usr/bin/env python3
"""
Unittest module
"""
import client
from client import GithubOrgClient
from parameterized import parameterized
from unittest import TestCase, mock
from unittest.mock import patch, Mock, MagicMock, PropertyMock


class TestGithubOrgClient(TestCase):
    """Test class for GithubOrgClient"""

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_json):
        """Test method returns correct output"""
        gc = GithubOrgClient(org_name)
        gc.org()
        mock_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
            )

    def test_public_repos_url(self) -> None:
        """Tests the `_public_repos_url` property"""
        with patch(
                "client.GithubOrgClient.org",
                new_callable=PropertyMock,
                ) as mock_org:
            mock_org.return_value = {
                'repos_url': "https://api.github.com/users/google/repos",
            }
            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/users/google/repos",
            )
