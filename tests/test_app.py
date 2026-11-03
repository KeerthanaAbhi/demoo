import unittest
from app import ApplicationHandler


class ApplicationTests(unittest.TestCase):
    def test_handler_has_get_method(self):
        self.assertTrue(callable(getattr(ApplicationHandler, "do_GET", None)))


if __name__ == "__main__":
    unittest.main()
