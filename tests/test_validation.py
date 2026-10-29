
import unittest
from src.cli import is_valid_url

class TestURLValidation(unittest.TestCase):
    def test_valid_https_url(self):
        self.assertTrue(is_valid_url("https://github.com/example/app"))

    def test_invalid_ftp_url(self):
        self.assertFalse(is_valid_url("ftp://example.com/app"))
