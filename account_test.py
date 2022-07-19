import unittest

import account


class accountTest(unittest.TestCase):

    def test_that_account_has_a_name(self):
        account1 = account.Account("toh")
        """
            GIVEN: when a deposit is made
            WHEN: when a deposit is made
            THEN: account balance should be reflected

            """

    def test_that_account_can_be_created(self):
        account1 = account.Account("tolani")

        self.assertIsNotNone(account1)
        self.assertIsInstance(account1, account.Account)

        account1.deposit(2000)

        self.assertEqual(2000, account1.balance)

    def test_that_account_can_be_withdraw(self):
        account2 = account.Account("moruf")
        account2.deposit(3000)
        account2.withdraw(2000)
        self.assertEqual(1000, account2.balance)

    def test_that_negative_deposit_raises_error_(self):
        account2 = account.Account("moruf")
        account2.deposit(3000)
        self.assertRaises(ValueError, account2.deposit, -2500)
        self.assertEqual(3000, account2.balance)

    def test_that_negative_withdraw_raises_error_(self):
        account2 = account.Account("moruf")
        account2.deposit(2000)
        self.assertRaises(ValueError, account2.withdraw, -2500)
        self.assertEqual(2000, account2.balance)

    def test_that_account_can_transfer_(self):
        moruf_account = account.Account("moruf")
        wale_account = account.Account("wale")

        moruf_account.deposit(2000)
        moruf_account.transfer(800, wale_account)

        self.assertEqual(1200, moruf_account.balance)
        self.assertEqual(800, wale_account.balance)


if __name__ == '__main__':
    unittest.main()
