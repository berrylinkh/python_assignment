class Drug:
    def __init__(self, drug_name, expiry_date, price):
        self._drug_name = drug_name
        self._expiry_date = expiry_date
        self._price = price

    def get_drug(self):
        return self._drug_name

    def set_drug(self, drug):
        if type(drug) != str:
            raise TypeError("Drug name must be a string")
        else:
            self._drug_name = drug

    def get_price(self):
        return self._price

    def set_price(self, price):
        if price <= 0:
            self._price = 0
        else:
            self._price = price

    def get_expiry_date(self):
        return self._expiry_date

    def set_expiry_date(self, expiry_date):
        if type(expiry_date) != str:
            raise TypeError("expiry_date must be a string")
        else:
            self._expiry_date = expiry_date