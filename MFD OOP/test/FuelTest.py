import unittest

from multiple_dispenser_system.Fuel import Fuel


class FuelTest(unittest.TestCase):
    def test_that_fuel_is_created(self):
        fuel = Fuel("petrol", 1350, 500)
        self.assertEqual(fuel.fuel_name,"petrol")
        self.assertEqual(fuel.price_per_liter, 1350)
        self.assertEqual(fuel.quantity, 500)
    def test_that_negative_price_raises_ValueError(self):
        self.assertRaises(ValueError, Fuel, "petrol", -1000, 500)
    def test_that_liter_less_than_one_raises_ValueError(self):
        self.assertRaises(ValueError, Fuel, "petrol", 1350, 0)