from unittest import TestCase
from multiple_dispenser_system.Dispenser import Dispenser
from multiple_dispenser_system.Fuel import Fuel

class DispenserTest(TestCase):
    def setUp(self):
        self.dispenser = Dispenser({})
        self.dispenser.add_fuel(Fuel("petrol", 1350, 500))
        # self.dispenser = Dispenser({})
        # self.dispenser.add_fuel(Fuel("petrol", 1350, 50))


    def test_that_add_fuel(self):
        self.dispenser.add_fuel(Fuel("diesel", 2100, 300))
        self.assertEqual(len(self.dispenser.fuel_collection), 2)


    def test_that_adding_duplicate_fuel_raises_error(self):
        self.assertRaises(ValueError, self.dispenser.add_fuel, Fuel("petrol", 1000, 100))


    def test_that_get_available_fuel(self):
        available = self.dispenser.get_available_fuel()
        self.assertIn("petrol", available)


    def test_that_get_available_fuel_excludes_empty_fuel(self):
        self.dispenser.dispense_by_liters("petrol", 500)
        self.assertEqual(self.dispenser.get_available_fuel(), {})


    def test_that_update_fuel_price(self):
        self.dispenser.update_fuel_price("petrol", 1300)
        self.assertEqual(self.dispenser.get_fuel("petrol").price_per_liter, 1300)


    def test_that_negative_price_update_raises_error(self):
        self.assertRaises(ValueError, self.dispenser.update_fuel_price, "petrol", -5)


    def test_that_unknown_fuel_raises_error(self):
        self.assertRaises(ValueError, self.dispenser.update_fuel_price, "gas", 1000)


    def test_that_restock_fuel(self):
        self.dispenser.restock_fuel("petrol", 100)
        self.assertEqual(self.dispenser.get_fuel("petrol").quantity, 600)


    def test_that_restock_with_invalid_quantity_raises_error(self):
        self.assertRaises(ValueError, self.dispenser.restock_fuel, "petrol", 0)


    def test_that_dispense_by_liters(self):
        amount = self.dispenser.dispense_by_liters("petrol", 10)
        self.assertEqual(amount["amount"], 13500)
        self.assertEqual(self.dispenser.get_fuel("petrol").quantity, 490)


    def test_that_dispense_by_liters_above_stock_raises_error(self):
        self.assertRaises(ValueError, self.dispenser.dispense_by_liters, "petrol", 501)


    def test_that_dispense_by_amount(self):
        amount = self.dispenser.dispense_by_amount("petrol", 2700)
        self.assertEqual(amount["liters"], 2)
        self.assertEqual(self.dispenser.get_fuel("petrol").quantity, 498)


    def test_that_raise_error_for_amount_below_dispense_amount(self):
        self.assertRaises(ValueError, self.dispenser.dispense_by_amount, "petrol", 1200)
