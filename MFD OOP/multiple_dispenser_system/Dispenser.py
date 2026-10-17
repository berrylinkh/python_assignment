
class Dispenser:
    def __init__(self,fuel_collection):
       self.fuel_collection = {}

    def add_fuel(self, fuel):
        if fuel.fuel_name in self.fuel_collection:
            raise ValueError("Fuel already exists")
        self.fuel_collection[fuel.fuel_name] = fuel

    def get_fuel(self, fuel_name):
        if fuel_name not in self.fuel_collection:
            raise ValueError("Fuel type is invalid")
        return self.fuel_collection[fuel_name]

    def get_available_fuel(self):
        return {name: fuel for name, fuel in self.fuel_collection.items() if fuel.quantity > 0}

    def update_fuel_price(self, fuel_name, new_price):
        if new_price < 0:
            raise ValueError("Price cannot be negative")
        self.get_fuel(fuel_name).price_per_liter = new_price

    def restock_fuel(self, fuel_name, liters):
        if liters <= 0:
            raise ValueError("Restock quantity must be positive")
        self.get_fuel(fuel_name).quantity += liters

    def dispense_by_liters(self, fuel_name, liters):
        fuel = self.get_fuel(fuel_name)
        if liters <= 0:
            raise ValueError("Invalid liters")
        if liters > fuel.quantity:
            raise ValueError("Insufficient fuel in stock")
        fuel.quantity -= liters
        return {"fuel": fuel_name, "liters": liters,
                "amount": liters * fuel.price_per_liter}

    def dispense_by_amount(self, fuel_name, amount):
        fuel = self.get_fuel(fuel_name)
        if amount < fuel.price_per_liter:
            raise ValueError("Invalid amount")
        liters = amount / fuel.price_per_liter
        if liters > fuel.quantity:
            raise ValueError("Insufficient fuel in stock")
        fuel.quantity -= liters
        return {"fuel": fuel_name, "liters": liters, "amount": amount}

