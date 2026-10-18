
from pharmacy1.User import User


class Admin(User):

    def __init__(self, fullname, phone_number, id, customers):
        super().__init__(fullname, phone_number)
        self._Admin_id = id
        self._Customers = []

    def get_id(self):
        return self._Admin_id

    def get_fullname(self):
        return self._fullname

    def get_phone_number(self):
        return self._phone_number

    def get_customer(self):
        return self._Customers

    def set_id(self, id):
        if type(id) != int:
            raise TypeError("Admin ID must be an integer")
        self._Admin_id = id

    def set_fullname(self, fullname):
        if type(fullname) != str:
            raise TypeError("Full name must be a string")
        self._fullname = fullname

    def set_phone_number(self, phone_number):
        if type(phone_number) != str:
            raise TypeError("Phone number must be a string")
        self._phone_number = phone_number

    def set_customer(self, customers):
        if type(customers) != list:
            raise TypeError("Customers must be a list")
        self._Customers = customers


    def add_customer(self, customer):
        if type(customer) != str:
            raise TypeError("Customer must be a string")

        self._Customers.append(customer)
        return self._Customers
