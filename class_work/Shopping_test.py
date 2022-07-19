import unittest
from Shopping import Shopping


class MyTestCase(unittest.TestCase):
    def test_that_account_has_a_name(self):
        shopping1 = Shopping("Muruf supermarket")
        shopping1.withdraw(300)
        self.assertEqual(100,shopping1.)


if __name__ == '__main__':
    unittest.main()
