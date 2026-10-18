
import unittest
from pharmacy1.Pharmacist import Pharmacist


class PharmacistTest(unittest.TestCase):

    def setUp(self):
        self.pharmacist = Pharmacist("Aboki Sule", "08012345678", 1)

    def test_that_pharmacist_is_created(self):
        self.assertEqual(self.pharmacist.get_fullname(), "Aboki Sule")
        self.assertEqual(self.pharmacist.get_phone_number(), "08012345678")
        self.assertEqual(self.pharmacist.get_pharmacist_id(), 1)

    def test_that_pharmacist_details_can_be_updated(self):
        self.pharmacist.set_pharmacist("John bull", "08123456789", 2)

        self.assertEqual(self.pharmacist.get_fullname(), "John bull")
        self.assertEqual(self.pharmacist.get_phone_number(), "08123456789")
        self.assertEqual(self.pharmacist.get_pharmacist_id(), 2)

    def test_that_invalid_name_raises_type_error(self):
        self.assertRaises(TypeError,self.pharmacist.set_pharmacist,123, "08012345678", 1)

    def test_that_invalid_phone_number_raises_type_error(self):
        self.assertRaises(TypeError,self.pharmacist.set_pharmacist, "Aboki Sule", 8012345678, 1)

    def test_that_invalid_pharmacist_id_raises_type_error(self):
        self.assertRaises(TypeError,self.pharmacist.set_pharmacist,"Aboki Sule", "08012345678", "one")