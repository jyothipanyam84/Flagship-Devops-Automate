import subprocess
import unittest

class TestCLI(unittest.TestCase):

	def test_status_command(self):
		result = subprocess.run(
			["python", "src/cli.py", "status"],
			capture_output=True,
			text=True
		)
		self.assertEqual(result.returncode, 0)	
		self.assertIn("Platform status: ready", result.stdout)

	def test_invalid_url_command(self):
		result = subprocess.run(
			["python", "src/cli.py", "deploy", "--repo", "invalid-url"],
			capture_output=True,
			text=True
		)
		self.assertEqual(result.returncode, 1)	
		self.assertIn("Invalid URL", result.stdout)

	def test_valid_url_command(self):
		result = subprocess.run(
			["python", "src/cli.py", "deploy", "--repo", "https://github.com/team/app"],
			capture_output=True,
			text=True
		)
		self.assertEqual(result.returncode, 0)	
		self.assertIn("Deployment request accepted.", result.stdout)

