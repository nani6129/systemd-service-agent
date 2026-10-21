import unittest
from unittest.mock import patch, Mock

from systemd_agent.tools import (
    validate_service_name,
    run_service_operation,
)


class TestValidation(unittest.TestCase):

    def test_valid_service_name(self):
        self.assertTrue(validate_service_name("cron"))

    def test_invalid_service_name(self):
        self.assertFalse(validate_service_name(""))
        self.assertFalse(validate_service_name("-bad"))
        self.assertFalse(validate_service_name("cron;whoami"))
        self.assertFalse(validate_service_name("cron service"))

    def test_rejects_unknown_operation(self):
        result = run_service_operation("delete", "cron")
        self.assertFalse(result["success"])

    @patch("systemd_agent.tools.subprocess.run")
    def test_status_success(self, mock_run):
        mock_run.return_value = Mock(
            returncode=0,
            stdout="active",
            stderr="",
        )

        result = run_service_operation("status", "cron")

        self.assertTrue(result["success"])
        self.assertEqual(result["service"], "cron")
        mock_run.assert_called_once()


if __name__ == "__main__":
    unittest.main()
