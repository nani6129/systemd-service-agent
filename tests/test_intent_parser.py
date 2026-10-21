import unittest

from systemd_agent.intent_parser import parse_request


class TestIntentParser(unittest.TestCase):
    def test_status_request(self):
        self.assertEqual(
            parse_request("Check whether cron is running"),
            {"operation": "status", "service": "cron"},
        )

    def test_restart_request(self):
        self.assertEqual(
            parse_request("Restart cron"),
            {"operation": "restart", "service": "cron"},
        )

    def test_enable_at_boot(self):
        self.assertEqual(
            parse_request("Enable cron at boot"),
            {"operation": "enable", "service": "cron"},
        )

    def test_unknown_request(self):
        self.assertIsNone(parse_request("Tell me a joke"))

    def test_destructive_request(self):
        self.assertIsNone(
            parse_request("Delete everything on my drive")
        )


if __name__ == "__main__":
    unittest.main()
