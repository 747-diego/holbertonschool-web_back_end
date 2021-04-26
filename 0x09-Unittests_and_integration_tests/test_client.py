#!/usr/bin/env python3
"""Parameterize and patch as decorators."""

from unittest import mock
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
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
