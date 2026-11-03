
import unittest
from src.cli import is_valid_url


class TestURLValidation(unittest.TestCase):

    def test_valid_https_url(self):
        self.assertTrue(is_valid_url("https://github.com/team/app"))

    def test_valid_http_url(self):
        self.assertTrue(is_valid_url("http://github.com/team/app"))

    def test_valid_gitlab_url(self):
        self.assertTrue(is_valid_url("https://gitlab.com/team/project"))

    def test_valid_bitbucket_url(self):
        self.assertTrue(is_valid_url("https://bitbucket.org/team/project"))

    def test_rejects_unsupported_scheme(self):
        self.assertFalse(is_valid_url("ftp://example.com/app"))

    def test_missing_hostname(self):
        self.assertFalse(is_valid_url("https:///app"))

    def test_empty_url(self):
        self.assertFalse(is_valid_url(""))

    def test_missing_scheme(self):
        self.assertFalse(is_valid_url("github.com/team/app"))

    def test_plain_text_input(self):
        self.assertFalse(is_valid_url("hello"))

    def test_incomplete_https_url(self):
        self.assertFalse(is_valid_url("https://"))

    def test_valid_url_without_path(self):
        self.assertTrue(is_valid_url("https://github.com"))

    def test_url_with_port(self):
        self.assertTrue(is_valid_url("https://github.com:8080/app"))

    def test_url_with_query_parameters(self):
        self.assertTrue(is_valid_url("https://gitlab.com/app?version=1"))

    def test_url_with_double_slash_in_path(self):
        self.assertFalse(is_valid_url("https://github.com/team//project"))

    def test_url_with_space(self):
        self.assertFalse(is_valid_url("https://exa mple.com"))

    def test_unsupported_hostname(self):
        self.assertFalse(is_valid_url("https://example.com/team/app"))

    def test_hostname_starts_with_hyphen(self):
        self.assertFalse(is_valid_url("https://-example.com"))

    def test_hostname_ends_with_hyphen(self):
        self.assertFalse(is_valid_url("https://example-.com"))

if __name__ == "__main__":
    unittest.main()
