
from pharmacy1.User import User


class Pharmacist(User):
    def __init__(self, fullname, phone_number, id):
        super().__init__(fullname, phone_number)
        self._Pharmacist_id = id

    def get_pharmacist_id(self):
        return self._Pharmacist_id

    def get_fullname(self):
        return self._fullname

    def get_phone_number(self):
        return self._phone_number

    def set_pharmacist(self, name, phone_number, pharmacist_id):
        if (type(name) == str and
                type(phone_number) == str and
                type(pharmacist_id) == int):

            self._fullname = name
            self._phone_number = phone_number
            self._Pharmacist_id = pharmacist_id

        else:
            raise TypeError("Invalid data")
