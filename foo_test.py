import unittest
from foo import Foo


class TestFoo(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(3, Foo(1, 2).sum())


if __name__ == "__main__":
    unittest.main()
