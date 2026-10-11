

class FuelDispenser:
    def __init__(self, fuel_prices):
        self.fuel_prices = fuel_prices
        self.dispenser_history = {}

    def display_available_fuel_prices(self):
        return self.fuel_prices

    def dictionary_can_be_updated(self, new_prices):
        self.fuel_prices.update(new_prices)
        return self.fuel_prices

    def total_cost_if_liter_is_passed(self, user_choice, liters):
        if user_choice not in self.fuel_prices:
            raise ValueError("Fule type is invalid")

        if liters <= 1 or liters > 50:
            raise ValueError("Invalid liters")

        unit_price = self.fuel_prices[user_choice]
        return unit_price * liters

    def total_cost_if_amount_is_passed(self, user_choice, amount):
        if user_choice not in self.fuel_prices:
            raise ValueError("Fule type is invalid")

        unit_price = self.fuel_prices[user_choice]

        if amount <= self.fuel_prices[user_choice]:
            raise ValueError("Invalid amount")

        return amount / unit_price

    def record_dispenser_history(self, fuel_type, liters, amount):
        if "Transactions" not in self.dispenser_history:
            self.dispenser_history["Transactions"] = []

        transaction = {"fuel": fuel_type, "price": amount, "liters": liters}
        self.dispenser_history["Transactions"].append(transaction)

        return self.dispenser_history
