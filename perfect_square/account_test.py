
from unittest import TestCase
from account import *

class TestAccount(TestCase):
    def test_that_account_can_be_created(self):
        acc = Account("Winifred")
        self.assertEqual(acc.balance, 0)
        self.assertEqual(acc.name, "winifred")
        
    def test_that_account_can_recieve_deposit(self):
        acc = Account("Winifred")
        acc.deposit(2500)
        self.assertEqual(acc.balance, 2500)
        
    def test_that_account_can_not_deposit_amount(self):
        acc = Account("Winifred")
        acc.deposit(2500)
        self.assertRaises(ValueError,acc.deposit, -2500)
        
    def test_that_money_can_be_withdraw(self):
        acc = Account("Winifred")
        acc.deposit(2500)
        self.assertEqual(acc.balance, 2500)
        
    def test_that_withdraw_can_not_be_greater_than_amount(self):
        acc = Account("Winifred")
        acc.deposit(2500)
        self.assertEqual(acc.balance, 2500)
        self.assertRaises(ValueError,acc.withdraw, -4000)
