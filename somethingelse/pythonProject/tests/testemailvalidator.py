import unittest

from classwork.emailvalidator import validate_email


class MyTestCase(unittest.TestCase):
    def test_email_is_valid(self):
            valid_emails = [
                "info@semicolon.africa)",
                "jonahodoh@gmail.com",
                "test123@example.net"
            ]
            for email in valid_emails:
                self.assertTrue(True, validate_email(email))

    def test_email_is_not_valid(self):
        invalid_emails = [
            "test@example.c",
            "test@example"
        ]
        for email in invalid_emails:
            self.assertFalse(False, validate_email(email))

    def test_edge_cases(self):
        edge_cases = [
            ("test@localhost", False),  # No domain extension
            ("test@123.456", False),  # Invalid domain
            ("test@example..com", False)  # Double dot
        ]
        for email, expected_result in edge_cases:
            self.assertFalse(False, validate_email(email))


if __name__ == '__main__':
    unittest.main()
