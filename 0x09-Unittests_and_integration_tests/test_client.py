#!/usr/bin/env python3
"""Parameterize and patch as decorators."""

from unittest import TestCase, mock
from unittest.mock import patch, Mock
from parameterized import parameterized
from client import GithubOrgClient
import client


class TestGithubOrgClient(TestCase):
    """Testing-Github-Client."""

    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    def test_org(self, client, SearchApi):
        """Testing-Output."""
        GithubUser = GithubOrgClient(client)
        GithubUser.org()
        SearchApi.assert_called_once_with("https://api.github.com/orgs/"+client)
