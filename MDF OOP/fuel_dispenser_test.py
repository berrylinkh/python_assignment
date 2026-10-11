

from unittest import TestCase
from fuel_dispenser import FuelDispenser


class FuelDispenserTest(TestCase):

    def setUp(self):
        self.fuel_dispenser = FuelDispenser({"petrol": 1350, "Diesel": 2100, "Kerosine": 1500})

    def test_that_display_available_fuel_prices(self):
        actual = self.fuel_dispenser.display_available_fuel_prices()
        expected = {"petrol": 1350, "Diesel": 2100, "Kerosine": 1500}
        self.assertEqual(actual, expected)

    def test_that_dictionary_can_be_updated(self):
        new_prices = {"petrol": 1300, "Diesel": 2000, "Kerosine": 1250}
        actual = self.fuel_dispenser.dictionary_can_be_updated(new_prices)
        expected = {"petrol": 1300, "Diesel": 2000, "Kerosine": 1250}
        self.assertEqual(actual, expected)

    def test_total_cost_if_liter_is_passed(self):
        user_choice = "petrol"
        liters = 0
        with self.assertRaises(ValueError):
            self.fuel_dispenser.total_cost_if_liter_is_passed(user_choice, liters)

    def test_total_cost_if_amount_is_passed(self):
        user_choice = "petrol"
        amount = 1200
        with self.assertRaises(ValueError):
            self.fuel_dispenser.total_cost_if_amount_is_passed(user_choice, amount)

    def test_record_dispenser_history(self):
        user_choice = "petrol"
        liters = 5
        total = 6500
        self.fuel_dispenser.record_dispenser_history(user_choice, liters, total)
        self.assertEqual(len(self.fuel_dispenser.dispenser_history["Transactions"]), 1)
