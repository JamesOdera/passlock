import unittest # Import unit test after creating a user class
from user import User # Importing the user class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("James","Odera","0701740229","nyangoma.odera@gmail.com") # create user object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"James")
        self.assertEqual(self.new_user.last_name,"Odera")
        self.assertEqual(self.new_user.phone_number,"0701740229")
        self.assertEqual(self.new_user.email,"nyangoma.odera@gmail.com")


if __name__ == '__main__':
    unittest.main()