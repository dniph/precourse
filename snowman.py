

SNOWMAN_WORD = "broccoli"

def get_letter_from_user():
    
    user_input_string = input("Choose a letter: ")
    
    if len(user_input_string) > 1 or not user_input_string.isalpha():
        print("Invalid letter please enter a single character")
        return user_input_string
    
    return user_input_string
    
    

print(get_letter_from_user())
print(get_letter_from_user())