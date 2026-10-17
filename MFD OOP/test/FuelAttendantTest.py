from unittest import TestCase

from multiple_dispenser_system.Dispenser import Dispenser
from multiple_dispenser_system.FuelAttendant import FuelAttendant


class FuelAttendantTest(TestCase):

    def setUp(self):
        self.attendant = FuelAttendant("Aderonke Obi", Dispenser({}), [])
        self.attendant.add_new_fuel("petrol", 1350, 300)

    def test_that_attendant_has_full_name(self):
        self.assertEqual(self.attendant.full_name, "Aderonke Obi")

    def test_that_add_new_fuel(self):
        self.attendant.add_new_fuel("diesel", 2100, 300)
        available = self.attendant.get_available_fuel()
        self.assertEqual(available["diesel"].fuel_name, "diesel")

    def test_that_update_fuel_price(self):
        self.attendant.update_fuel_price("petrol", 1300)
        fuel = self.attendant.get_available_fuel()["petrol"]
        self.assertEqual(fuel.price_per_liter, 1300)

    def test_that_restock_fuel(self):
        self.attendant.restock_fuel("petrol", 100)
        fuel = self.attendant.get_available_fuel()["petrol"]
        self.assertEqual(fuel.quantity, 400)

    def test_that_dispense_fuel_by_is_liters_recorded(self):
        self.attendant.dispense_fuel_by_liters("petrol", 10)
        self.assertEqual(len(self.attendant.show_all_transactions()), 1)

    def test_that_dispense_fuel_by_amount_is_recorded(self):
        self.attendant.dispense_fuel_by_amount("petrol", 2700)
        self.assertEqual(len(self.attendant.show_all_transactions()), 1)

    def test_that_multiple_transactions_are_recorded(self):
        self.attendant.dispense_fuel_by_liters("petrol", 5)
        self.attendant.dispense_fuel_by_amount("petrol", 2700)
        self.assertEqual(len(self.attendant.show_all_transactions()), 2)
