#pseudocode for Movie Rating System
#
#Start
#
#1. Display a menu of options:
#
#   * Add a movie
#   * Rate a movie
#   * Calculate the average rating for a movie
#   * Calculate the overall average rating of all movies
#   * Exit
#
#2. Write a function that allows the user to add a movie of their choice to the movie list.
#
#3. Write a function that allows the user to select a movie, give it a rating, and record the time and date of the rating.
#
#4. Write a function that calculates the average rating for each movie.
#
#5. Write a function that calculates the average rating of all movies in the list.
#
#End
#




from datetime import datetime
movie_list =[]
movie_rating =[]
average_for_a_movie = 0
total_avaerage = 0

def display_menu_option_list ():
    movie_menu_option ="""Welcome to Kanipe Movie System.
        1. Add Movie
        2. Rate a movie
        3. View Average Ratings of a movie
        4. View Average Ratings of all movie
        0. Exit
    """

    return movie_menu_option
     
def add_movie_choice ():
    movie_title = input("Enter movie title: ")
    movie_list.append(movie_title)
    print(f"{movie_list}  added")
    rating_question = input("Do you want to rate the movie (yes or no): ").lower()
    return movie_title


def rate_movie ():
    movie_title_for_rating = input("Enter movie title to rate: ")

    rating = int(input("Enter 1-5 to rate movie: "))
    current_time = datetime.now().strftime("%Y-%m-%H:%M")
    movie_rating.append((movie_title_for_rating ,rating,current_time))

    print(f"{movie_title_for_rating:>10} rated {rating:>2} at {current_time}.")
    return rating
     

def average_of_a_movie ():
    rating_total =0
    rating_count = 0

    movie = input("Enter the movie title to get the aveage: ")
    for movie_title,rating,current_time in movie_rating_and_time:
        if movie_title == movie:
            rating_count +=1
            rating_total += rating

        if rating_count ==0:
            print("No ratings found for this movie.")
            return None

    average_for_a_movie = rating_total / rating_count
    return average_for_a_movie



