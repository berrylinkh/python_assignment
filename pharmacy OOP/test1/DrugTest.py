import unittest
from pharmacy1.Drug import Drug


class DrugTest(unittest.TestCase):

    def setUp(self):
        self._drug = Drug("Paracetamol", "2027-12-31", 1500)

    def test_that_drug_name_can_be_retrieved(self):
        self.assertEqual("Paracetamol", self._drug.get_drug())

    def test_that_drug_price_can_be_updated(self):
        self._drug.set_price(2000)
        self.assertEqual(2000, self._drug.get_price())

    def test_that_invalid_drug_name_raises_error(self):
        self.assertRaises(TypeError, self._drug.set_drug, 123)

