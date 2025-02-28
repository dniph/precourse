
import random
from wonderwords import RandomWord

# https://pypi.org/project/wonderwords/

SNOWMAN_GRAPHIC = [
    '*   *   *  ',
    ' *   _ *   ',
    '   _[_]_ * ',
    '  * (")    ',
    '  \\( : )/ *',
    '* (_ : _)  ',
    '-----------'
]

SNOWMAN_WORD = "broccoli"
SNOWMAN_WRONG_GUESSES = 7
SNOWMAN_MAX_WORD_LENGTH = 8
SNOWMAN_MIN_WORD_LENGTH = 5
correct_guesses_list = []
wrong_guesses_list = []


def get_letter_from_user(wrong_guesses_list):
    
    valid_input = False
    user_input = None
    
    while not valid_input:
        user_input = input("Choose a letter: ")
        if len(user_input) > 1 :
            print("Please enter a single character")  
        elif not user_input.isalpha():
            print("Invalid character please enter a single letter")
        elif user_input in wrong_guesses_list or user_input in correct_guesses_list:
            print("You have already guessed that letter!")  
        else:
            valid_input = True
            
    return user_input
    
    
def snowman():
    random_word_generator = RandomWord()
    snowman_word = random_word_generator.word(word_min_length=SNOWMAN_MIN_WORD_LENGTH, word_max_length=SNOWMAN_MAX_WORD_LENGTH)   
    

    print( snowman_word)
    
    
    while len(wrong_guesses_list) < SNOWMAN_WRONG_GUESSES and len(correct_guesses_list) < len(snowman_word):
        user_input = get_letter_from_user(wrong_guesses_list)
        
        if user_input in snowman_word :
            print("You guessed a letter that's in the word!")
            correct_guesses_list.append(user_input) 
        else:
            print(f"The letter {user_input} is not in the word")
            wrong_guesses_list.append(user_input)
            
        print_snowman(len(wrong_guesses_list))
        print(f"Wrong guesses: {wrong_guesses_list}")
        
        
def print_snowman(wrong_guesses_count):
    for i in range(SNOWMAN_WRONG_GUESSES - wrong_guesses_count, SNOWMAN_WRONG_GUESSES):
        print(SNOWMAN_GRAPHIC[i])
        


snowman()