
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


def get_letter_from_user(correct_letter_guess_statuses, wrong_guesses_list):
    
    valid_input = False
    user_input = None
    
    while not valid_input:
        user_input = input("Choose a letter: ")
        if len(user_input) > 1 :
            print("Please enter a single character")  
        elif not user_input.isalpha():
            print("Dude! Invalid character please enter a single letter")
        elif (user_input in correct_letter_guess_statuses 
        and correct_letter_guess_statuses[user_input]):
            print("Honey, you have already guessed that letter!")  
        elif user_input in wrong_guesses_list:
            print("Dear, You already guessed that letter and it's not in the word!")
        else:
            valid_input = True
            
    return user_input
    
    
def snowman():
    random_word_generator = RandomWord()
    snowman_word = random_word_generator.word(word_min_length=SNOWMAN_MIN_WORD_LENGTH, word_max_length=SNOWMAN_MAX_WORD_LENGTH)   
    
#Borrar!
    print( snowman_word)
    correct_letter_guess_statuses = build_letter_status_dict(snowman_word)
    wrong_guesses_list = []
    
    while len(wrong_guesses_list) < SNOWMAN_WRONG_GUESSES and len(correct_letter_guess_statuses) < len(snowman_word):
        user_input = get_letter_from_user(correct_letter_guess_statuses, wrong_guesses_list)
        
        if user_input in correct_letter_guess_statuses: 
            print("You guessed a letter that's in the word!")
            correct_letter_guess_statuses[user_input] = True
        else:
            print(f"Puu! the letter {user_input} is not in the word")
            wrong_guesses_list.append(user_input)
            
        print_snowman(len(wrong_guesses_list))
        print(f"Sorry baby, wrong guesses: {wrong_guesses_list}")
        
        
        

        
        
def print_snowman(wrong_guesses_count):
    for i in range(SNOWMAN_WRONG_GUESSES - wrong_guesses_count, SNOWMAN_WRONG_GUESSES):
        print(SNOWMAN_GRAPHIC[i])
        
        
def build_letter_status_dict(snowman_word):
    letter_status_dict = {}

    for letter in snowman_word:
        if letter not in letter_status_dict:
            letter_status_dict[letter] = False
    return  letter_status_dict

def generate_word_progress_string(snowman_word, correct_letter_guess_statuses):
    output_string = ""
    is_not_first_letter = False

    for letter in snowman_word:
        if is_not_first_letter:
            output_string += " "

        if correct_letter_guess_statuses[letter]:
            output_string += letter
        else:
            output_string += "_"

        is_not_first_letter = True

    return output_string

def print_word_progress_string(snowman_word, correct_letter_guess_statuses):
    progress_string = generate_word_progress_string(snowman_word, correct_letter_guess_statuses)
    print(progress_string)
    
def is_word_guessed(snowman_word, correct_letter_guess_statuses):
    for letter in snowman_word:
        if not correct_letter_guess_statuses[letter]:
            return False
    return True

snowman()