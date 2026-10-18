from pharmacy1.User import User


class Customer(User):
    def __init__ (self, fullname, phone_number, product, price):
        super().__init__( fullname, phone_number)
        self._products = []
        self._prices = []
    def get_customer_details(self):
        return self._fullname, self._phone_number

    def set_customer_details(self, fullname, phone_number):
        if type(fullname) == str and type(phone_number) ==str:
            self._fullname = fullname
            self._phone_number = phone_number
        else:
            raise TypeError("Invalid data")

    def add_product(self,product):
        self._products.append(product)

    def add_price(self,price):
        self._prices.append(price)
