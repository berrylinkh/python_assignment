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
    def test_that_dictionary_can_be_updated_with_new_product(self):
        new_product = {"petrol": 1300, "Diesel": 2000, "Kerosine": 1250, "gas": 2100}
        actual = self.fuel_dispenser.dictionary_can_be_updated(new_product)
        expected = {"petrol": 1300, "Diesel": 2000, "Kerosine": 1250, "gas": 2100}
        self.assertEqual(actual, expected)

    def test_that_set_fuel_price_updates_price(self):
        self.fuel_dispenser.set_fuel_price("petrol", 1400)
        self.assertEqual(self.fuel_dispenser.fuel_prices["petrol"], 1400)

    def test_that_set_fuel_price_rejects_negative_price(self):
        self.assertRaises(ValueError, self.fuel_dispenser.set_fuel_price, "petrol", -100)
        self.assertEqual(self.fuel_dispenser.fuel_prices["petrol"], 1350)

    def test_that_set_fuel_price_rejects_unknown_fuel(self):
        self.assertRaises(ValueError, self.fuel_dispenser.set_fuel_price, "gas", 1000)

    def test_total_cost_if_liter_is_passed(self):
        actual = self.fuel_dispenser.total_cost_if_liter_is_passed("petrol", 10)
        self.assertEqual(actual, 13500)

    def test_total_cost_if_liter_is_invalid(self):
        self.assertRaises(ValueError, self.fuel_dispenser.total_cost_if_liter_is_passed, "petrol", 0)

    def test_total_cost_if_liter_is_above_limit(self):
        self.assertRaises(ValueError, self.fuel_dispenser.total_cost_if_liter_is_passed, "petrol", 51)

    def test_total_cost_if_fuel_type_is_invalid(self):
        self.assertRaises(ValueError, self.fuel_dispenser.total_cost_if_liter_is_passed, "gas", 10)

    def test_total_cost_if_amount_is_passed(self):
        actual = self.fuel_dispenser.total_cost_if_amount_is_passed("petrol", 2700)
        self.assertEqual(actual, 2)

    def test_total_cost_if_amount_is_too_small(self):
        self.assertRaises(ValueError, self.fuel_dispenser.total_cost_if_amount_is_passed, "petrol", 1200)

    def test_record_dispenser_history(self):
        self.fuel_dispenser.record_dispenser_history("petrol", 5, 6500)
        self.assertEqual(len(self.fuel_dispenser.dispenser_history["Transactions"]), 1)
    def test_record_multiple_dispenser_history(self):
        self.fuel_dispenser.record_dispenser_history("petrol", 5, 6500)
        self.fuel_dispenser.record_dispenser_history("kerosine", 4, 6000)
        self.assertEqual(len(self.fuel_dispenser.dispenser_history["Transactions"]), 2)


