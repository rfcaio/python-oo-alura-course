from unittest import TestCase

from account import Account


class TestAccount(TestCase):
    def setUp(self):
        self.account = Account(477, 'John Connor', 100.0, 1000.0)


    def test_deposit_should_increase_the_account_balance(self):
        self.account.deposit(150.0)
        self.assertEqual(self.account.balance, 250.0)


    def test_print_balance_should_print_a_message_with_the_owner_balance(self):
        self.assertEqual(self.account.print_balance(), 'Your account balance is $ 100.0.')


    def test_withdraw_should_decrease_the_account_balance(self):
        self.account.withdraw(50.0)
        self.assertEqual(self.account.balance, 50.0)