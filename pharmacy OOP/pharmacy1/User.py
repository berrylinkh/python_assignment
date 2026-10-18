from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self,fullname,phone_number):
        self._fullname = fullname
        self._phone_number = phone_number

    def get_fullname(self):
        return self._fullname

    def get_phone_number(self):
        return self._phone_number

    def set_phone_number(self, phone_number):
        if type(phone_number) != str:
            raise TypeError("phone_number must be a string")
        else:
            self._phone_number = phone_number
    def set_fullname(self, fullname):
        if type(fullname) != str:
            raise TypeError("fullname must be a string")
        else:
            self._fullname = fullname