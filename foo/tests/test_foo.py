import unittest
from .. import Foo


class TestFoo(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(3, Foo(1, 2).sum())

    def test_fail(self):
        assert True


if __name__ == "__main__":
    unittest.main()
