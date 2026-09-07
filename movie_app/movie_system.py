from movie_system_app import *

movies =[]
rating =[]
while (True) :
    movie_menu_display = display_menu_option_list ()
    print (movie_menu_display)

    user_choice = int(input("select your option: "))

    match user_choice:
        case 1:
            movies = add_movie_choice()
            if user_choice == 'yes':
                print(movie_menu_display)
            else:
                exit ==0
           
        case 2:
            rating = rate_movie()
               
        case 3:
            average_rating = average_of_a_movie ()
            break
        case 4:
            average_rating = average_of_all_movie ()
        case 0:
            print ("Thank you for using the app,goodbye")
            break
        case _:
            print ("Incorrect input")
            break



