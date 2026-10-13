
class FuelDispenser:
    def __init__(self, fuel_prices):
        for price in fuel_prices.values():
            self._validate_price(price)
        self.fuel_prices = dict(fuel_prices)
        self.dispenser_history = {}

    @staticmethod
    def _validate_price(price):
        if price < 0:
            raise ValueError("Price cannot be negative")

    def display_available_fuel_prices(self):
        return self.fuel_prices

    def set_fuel_price(self, fuel_type, new_price):
        if fuel_type not in self.fuel_prices:
            raise ValueError("Fuel type is invalid")
        self._validate_price(new_price)
        self.fuel_prices[fuel_type] = new_price

    def dictionary_can_be_updated(self, new_prices):
        for price in new_prices.values():
            self._validate_price(price)
        self.fuel_prices.update(new_prices)
        return self.fuel_prices

    def total_cost_if_liter_is_passed(self, user_choice, liters):
        if user_choice not in self.fuel_prices:
            raise ValueError("Fuel type is invalid")

        if liters < 1 or liters > 50:
            raise ValueError("Invalid liters")

        unit_price = self.fuel_prices[user_choice]
        return unit_price * liters

    def total_cost_if_amount_is_passed(self, user_choice, amount):
        if user_choice not in self.fuel_prices:
            raise ValueError("Fuel type is invalid")

        unit_price = self.fuel_prices[user_choice]
        if (amount < unit_price):
            raise ValueError("Invalid amount")

        return amount / unit_price

    def record_dispenser_history(self, fuel_type, liters, amount):
        if "Transactions" not in self.dispenser_history:
            self.dispenser_history["Transactions"] = []

        transaction = {"fuel": fuel_type, "price": amount, "liters": liters}
        self.dispenser_history["Transactions"].append(transaction)

        return self.dispenser_history

