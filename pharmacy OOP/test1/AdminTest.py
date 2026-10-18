
import unittest

from pharmacy1.Admin import Admin


class AdminTest(unittest.TestCase):

    def setUp(self):
        self.admin = Admin("Aboki Sule", "08012345678", 1, [])

    def test_that_customer_list_is_empty(self):
        self.assertEqual(self.admin.get_customer(), [])

    def test_that_admin_is_created(self):
        self.assertEqual(self.admin.get_fullname(), "Aboki Sule")
        self.assertEqual(self.admin.get_phone_number(), "08012345678")
        self.assertEqual(self.admin.get_id(), 1)

    def test_that_admin_id_can_be_changed(self):
        self.admin.set_id(2)
        self.assertEqual(self.admin.get_id(), 2)

    def test_that_invalid_admin_id_raises_type_error(self):
        with self.assertRaises(TypeError):self.admin.set_id("two")


    def test_that_fullname_can_be_changed(self):
        self.admin.set_fullname("John Okon")
        self.assertEqual(self.admin.get_fullname(), "John Okon")

    def test_that_invalid_fullname_raises_type_error(self):
        with self.assertRaises(TypeError):self.admin.set_fullname(123)


    def test_that_phone_number_can_be_changed(self):
        self.admin.set_phone_number("08123456789")
        self.assertEqual(self.admin.get_phone_number(), "08123456789")

    def test_that_invalid_phone_number_raises_type_error(self):
        with self.assertRaises(TypeError):self.admin.set_phone_number(8012345678)

    def test_that_a_customer_can_be_added(self):
        self.admin.add_customer("Aboki")
        self.assertEqual(self.admin.get_customer(), ["Aboki"])

    def test_that_multiple_customers_can_be_added(self):
        self.admin.add_customer("Aboki")
        self.admin.add_customer("John")

        self.assertEqual(self.admin.get_customer(), ["Aboki", "John"])
