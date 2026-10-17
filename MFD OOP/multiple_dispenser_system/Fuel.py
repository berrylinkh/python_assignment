
class Fuel:
    def __init__(self, fuel_name, price_per_liter, quantity):
        self._validate_fuel(price_per_liter, quantity)
        self.fuel_name = fuel_name
        self.price_per_liter = price_per_liter
        self.quantity = quantity

    def _validate_fuel(self,price_per_liter, quantity):
        if price_per_liter < 0:
            raise ValueError("Price cannot be negative")

        if quantity < 1:
            raise ValueError("Quantity cannot be less than 1")