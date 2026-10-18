
import unittest

from pharmacy1.Customer import Customer


class CustomerTest(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Aboki Sule", "08012345678", "Paracetamol",500 )

    def test_set_fullname(self):
        self.assertEqual(self.customer._fullname, "Aboki Sule")

    def test_set_phone_number(self):
        self.assertEqual(self.customer._phone_number, "08012345678")

    def test_that_product_and_price_are_empty(self):
        self.assertEqual(self.customer._products, [])
        self.assertEqual(self.customer._prices, [])


    def test_that_invalid_name_and_number_raise_type_error(self):
        with self.assertRaises(TypeError):
            self.customer.set_customer_details("Aboki Sule", 8012345678)

    def test_that_a_product_can_be_added(self):
        self.customer.add_product("Paracetamol")
        self.assertEqual(self.customer._products, ["Paracetamol"])

    def test_that_multiple_products_can_be_added(self):
        self.customer.add_product("Paracetamol")
        self.customer.add_product("Amoxicillin")
        self.assertEqual(self.customer._products,["Paracetamol", "Amoxicillin"])

    def test_that_price_can_be_added(self):
        self.customer.add_price(500)
        self.assertEqual(self.customer._prices, [500])

    def test_that_multiple_prices_can_be_added(self):
        self.customer.add_price(500)
        self.customer.add_price(1200.50)
        self.assertEqual(self.customer._prices, [500, 1200.50])
