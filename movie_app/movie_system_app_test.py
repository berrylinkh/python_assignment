

from unittest import TestCase
from movie_system_app import *

class Movie_System_Test (TestCase):
    def test_menu_option_list (self):

        actualResult = display_menu_option_list ()

        expectedResult = """ Welcome to Kanipe Movie System.
        1. Add Movie
        2. Rate a movie
        3. View Average Ratings of a movie
        4. View Average Ratings of all movie
        0. Exit
        """

        self.assertEqual (actualResult.strip(), expectedResult.strip())
        
    def test_add_movie_option (self):

        actualResult = add_movie_choice ()

        expectedResult = "unexpected place"

        self.assertEqual (actualResult, expectedResult)

    def test_for_movie_rating (self):

        actualResult = rate_movie ()

        expectedResult = 5

        self.assertEqual (actualResult, expectedResult)

