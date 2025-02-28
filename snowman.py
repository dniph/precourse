

SNOWMAN_0 = '*   *   *  '
SNOWMAN_1 = ' *   _ *   '
SNOWMAN_2 = '   _[_]_ * '
SNOWMAN_3 = '  * (")    '
SNOWMAN_4 = '  \\( : )/ *'
SNOWMAN_5 = '* (_ : _)  '
SNOWMAN_6 = '-----------'

SNOWMAN_WORD = "broccoli"
correct_guesses = len(SNOWMAN_WORD)
SNOWMAN_WRONG_GUESSES = 7


def get_letter_from_user():
    

    valid_input = False
    
    while not valid_input:
        user_input = input("Choose a letter: ")
        
        if len(user_input) > 1 :
            print("Please enter a single character")  
        elif not user_input.isalpha():
            print("Invalid character please enter a single letter")
            
        else:
            valid_input = True
            
    return user_input
    
    
def snowman():
    num_of_guesses = 0
    wrong_num_of_guesses = 0
    
    while wrong_num_of_guesses <= SNOWMAN_WRONG_GUESSES and num_of_guesses < len(SNOWMAN_WORD):
        user_input = get_letter_from_user()
        
        if user_input in SNOWMAN_WORD :
            print("You guessed a letter that's in the word!")
            num_of_guesses += 1
            
        else:
            print(f"The letter {user_input} is not in the word")
            wrong_num_of_guesses += 1
            
        print_snowman(wrong_num_of_guesses)
        
def print_snowman(wrong_guesses_count):
    for i in range(SNOWMAN_WRONG_GUESSES - wrong_guesses_count, SNOWMAN_WRONG_GUESSES):
        if i == 0:
            print(SNOWMAN_0)
        elif i == 1:
            print(SNOWMAN_1)
        elif i == 2:
            print(SNOWMAN_2)
        elif i == 3:
            print(SNOWMAN_3)
        elif i == 4:
            print(SNOWMAN_4)
        elif i == 5:
            print(SNOWMAN_5)
        elif i == 6:
            print(SNOWMAN_6)
        


snowman()