from unittest import TestCase
from multiple_fuel_dispenser import *

class multiple_fuel_dispenser_Test(TestCase):
   
    
    def test_that_display_available_fuel_prices(self):
        fuel_dispenser ={"petrol": 1350, "Diesel": 2100, "Kerosine": 1500}
        actual = display_available_fuel_prices(fuel_dispenser)
        expected = {"petrol": 1350, "Diesel": 2100, "Kerosine": 1500}
        self.assertEqual(actual, expected)

    def test_that_dictionary_can_be_updated(self):
        fuel_dispenser ={"petrol": 1350, "Diesel": 2100, "Kerosine": 1500}
        new_prices = {"petrol": 1300, "Diesel": 2000, "Kerosine": 1250}
        actual = dictionary_can_be_updated(fuel_dispenser, new_prices)
        expected = {"petrol": 1300, "Diesel": 2000, "Kerosine": 1250}
        self.assertEqual(actual, expected)

#    def test_for_fuel_type(self):
#        new_prices = {"petrol": 1300, "Diesel": 2000, "Kerosine": 1250}
#        user_choice ="petrol"
#        liters = 5
#        actual = allow_user_to_choose_fuel_type(new_prices,user_choice, liters)
#        expected = 6500
#        self.assertEqual(actual, expected)

    def test_total_cost_if_liter_is_passed(self):
        fuel_dispenser ={"petrol": 1350, "Diesel": 2100, "Kerosine": 1500}
        user_choice ="petrol"
        liters = 0
        with self.assertRaises(ValueError):total_cost_if_liter_is_passed(fuel_dispenser, user_choice, liters)

    def test_total_cost_if_amount_is_passed(self):
         fuel_dispenser ={"petrol": 1350, "Diesel": 2100, "Kerosine": 1500}
         user_choice ="petrol"
         amount = 1200
         with self.assertRaises(ValueError):total_cost_if_amount_is_passed(fuel_dispenser, user_choice, amount)

    def test_record_dispenser_history(self):
        new_prices = {"petrol": 1300, "Diesel": 2000, "Kerosine": 1250}
        user_choice ="petrol"
        liters = 5
        total = 6500
        dispenser_history ={"Transactions":[]}
        record_dispenser_history(user_choice,liters, amount)
        self.assertEqual(len(dispenser_history["Transactions"]),1)


