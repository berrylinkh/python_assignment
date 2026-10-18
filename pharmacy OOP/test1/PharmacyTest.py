
import unittest
from pharmacy1.Pharmacy import Pharmacy


class PharmacyTest(unittest.TestCase):

    def setUp(self):
        self.pharmacy = Pharmacy([], [], "Ada", "HealthPlus")

    def test_that_pharmacy_is_created(self):
        self.assertEqual(self.pharmacy._drugs, [])
        self.assertEqual(self.pharmacy._items, [])

    def test_that_admin_is_stored(self):
        self.assertEqual(self.pharmacy._admin, "Ada")

    def test_that_pharmacy_name_is_stored(self):
        self.assertEqual(self.pharmacy._pharmacy, "HealthPlus")

    def test_that_drugs_and_items_can_be_added(self):
        self.pharmacy.add_drugs("Paracetamol")
        self.pharmacy.add_items("Syringe")

        self.assertEqual(self.pharmacy._drugs, ["Paracetamol"])
        self.assertEqual(self.pharmacy._items, ["Syringe"])

