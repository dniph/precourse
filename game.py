import random

RANGE_LOW = 0
RANGE_HIGH = 100

def guess_the_number():

    random_number = random.randint(RANGE_LOW, RANGE_HIGH)
    user_input = get_number_from_user()

    if user_input < RANGE_LOW or user_input > RANGE_HIGH:
        print("Your guess is out of bounds.")
        print(f"It must be between {RANGE_LOW} and {RANGE_HIGH}")
    elif user_input == random_number:
        print("Honey,you guessed the number! Good job!")
    elif user_input > random_number:
        print("Puu!our guess is too high")
    elif user_input < random_number:
        print("Puu! your guess is too low")


def get_number_from_user():
    user_input_string = input("Guess the number: ")
    user_input = None
    if user_input_string.isnumeric():
        user_input = int(user_input_string)
    else:
        print("Dude, you must input a number!")

    return user_input

# Run the guess_the_number function to test it
guess_the_number()      
guess_the_number()
guess_the_number()
guess_the_number()
guess_the_number()