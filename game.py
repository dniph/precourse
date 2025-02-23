import random 

RANGE_LOW = 0
RANGE_HIGH = 100

def guess_the_number():
    
    random_number = (random.randint(RANGE_LOW,RANGE_HIGH))
    user_input_string = input("Guess the number: ")

    if user_input_string.isnumeric():
        user_input = int(user_input_string)
        
        if user_input < RANGE_LOW or user_input > RANGE_HIGH:
            print("Your Guess is out of the bounds")
            print ("You must be between {RANGE_LOW} and {RANGE_HIGH}")
        elif user_input_string == random_number:
            print("Honey, you guessed the number, Good Job! ")
        elif user_input > random_number:
            print("Puu! Your guess is too high")
        elif user_input < random_number:
            print("Puu! Your guess is too low")
        
    else:
        print("You must input a number!")
        
        
guess_the_number()
guess_the_number()
guess_the_number()
guess_the_number()