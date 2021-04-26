#!/usr/bin/env python3
"""Parameterize and patch as decorators."""

from unittest import mock
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized, parameterized_class
import fixtures
from client import GithubOrgClient
from utils import get_json


class TestGithubOrgClient(unittest.TestCase):
    """Testing-Github-Client."""

    deco = 'client.get_json'

    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch(deco)
    def test_org(self, client, api):
        """Testing-Output."""
        GithubUser = GithubOrgClient(client)
        GithubUser.org()
        api.assert_called_once_with("https://api.github.com/orgs/"+client)

    def test_public_repos_url(self):
        """Making a property."""
        pass

    @patch('client.get_json')
    def test_public_repos(self, mock):
        """More patching."""
        pass

    def test_has_license(self, repo, license, expected):
        """Parameterize."""
        self.assertEqual(GithubOrgClient.has_license(repo, license), expected)


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    fixtures.TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test: fixtures."""

    @classmethod
    def setUpClass(test):
        """Unit-test case API."""
        pass

    @classmethod
    def tearDownClass(test):
        """Unit-test case API."""
        pass

    def test_public_repos(self):
        """Unit-test case API."""
        pass

    def test_public_repos_with_license(self):
        """Unit-test case API."""
        pass
