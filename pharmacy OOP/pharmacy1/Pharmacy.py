
class Pharmacy:
    def __init__(self, drugs, items, admin, pharmacy):
        self._drugs = []
        self._items = []
        self._admin = admin
        self._pharmacy = pharmacy

    def get_drugs(self):
        return self._drugs

    def get_items(self):
        return self._items

    def get_admin(self):
        return self._admin

    def get_pharmacy(self):
        return self._pharmacy

    def set_admin(self, admin):
        self._admin = admin

    def set_pharmacy(self, pharmacy):
        self._pharmacy = pharmacy

    def add_drugs(self, drug):
        if drug in self._drugs:
            index = self._drugs.index(drug)
            self._drugs[index] = drug
        else:
            self._drugs.append(drug)


    def add_items(self, item):
        if item in self._items:
            index = self._items.index(item)
            self._items[index] = item
        else:
            self._items.append(item)
