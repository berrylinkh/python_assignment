
import unittest
from pharmacy1.User import User


class TestUser(User):
    def get_role(self):
        return "User"


class UserTest(unittest.TestCase):

    def setUp(self):
        self.user = TestUser("Aboki Sule", "08012345678")

    def test_that_user_fullname_is_returned(self):
        self.assertEqual(self.user.get_fullname(), "Aboki Sule")

    def test_that_user_phone_number_is_returned(self):
        self.assertEqual(self.user.get_phone_number(), "08012345678")

    def test_that_user_details_can_be_updated(self):
        self.user.set_fullname("John bull")
        self.user.set_phone_number("08123456789")

        self.assertEqual(self.user.get_fullname(), "John bull")
        self.assertEqual(self.user.get_phone_number(), "08123456789")

    def test_that_invalid_fullname_raises_type_error(self):
        self.assertRaises(TypeError,self.user.set_fullname,123)

    def test_that_invalid_phone_number_raises_type_error(self):
        self.assertRaises(TypeError,self.user.set_phone_number,8012345678)
