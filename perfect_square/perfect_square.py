
given = [4, 9, 25,49]
given_result =[]

def check_if_it_is_a_perfect_number_and_return_boolean(given_result):
    counter =0
    for number in given:
        for count in range (1 , number):
            if number % count ==0:
                counter = count        
        if counter * counter == number:
            given_result.append(True)
    
        else: 
             given_result.append(False)
    return given_result            
            
print(check_if_it_is_a_perfect_number_and_return_boolean(given_result))               
    
given_element =["madam", "hello", "noon", "racecar"]
given_element_result =[]    
def check_if_it_is_a_palindrome_and_return_boolean(given_element_result):
    reverse =" "
    for element in given_element:
        text = element
        reverse =  text[:: -1]
        if reverse == element:
            given_element_result.append(True)
    
        else: 
             given_element_result.append(False)
    return given_element_result            
            
print(check_if_it_is_a_palindrome_and_return_boolean(given_element_result)) 

given_word ="abcdefgh"
reverse =" "
def reverse_word_in_360_and_return_text(given_element_result):
     
    reverse1 =  given_word[:-6: -1]
    reverse2 =  given_word[-5:: -1]
    return  reverse2+reverse1            
            
print(reverse_word_in_360_and_return_text(given_word)) 


