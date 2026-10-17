
from multiple_dispenser_system.Fuel import Fuel
class FuelAttendant:
    def __init__(self, full_name,dispenser,transactions):
        self.full_name = full_name
        self.dispenser = dispenser
        self.transactions =[]

    def add_new_fuel(self, fuel_name, price_per_liter, quantity):
        self.dispenser.add_fuel(Fuel(fuel_name, price_per_liter, quantity))

    def get_available_fuel(self):
        return self.dispenser.get_available_fuel()

    def update_fuel_price(self, fuel_name, new_price):
        self.dispenser.update_fuel_price(fuel_name, new_price)

    def restock_fuel(self, fuel_name, liters):
        self.dispenser.restock_fuel(fuel_name, liters)

    def dispense_fuel_by_amount(self, fuel_name, amount):
        transaction = self.dispenser.dispense_by_amount(fuel_name, amount)
        self.transactions.append(transaction)
        return transaction

    def dispense_fuel_by_liters(self, fuel_name, liters):
        transaction = self.dispenser.dispense_by_liters(fuel_name, liters)
        self.transactions.append(transaction)
        return transaction

    def show_all_transactions(self):
        return self.transactions
