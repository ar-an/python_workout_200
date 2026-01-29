from random import randint



def guessing_game():
    rand_number = randint(0,100)

    print("Hi! Try to guess an integer between 0 and 100. Have fun!")

    user_guess = 0

    while user_guess != rand_number:
        try:
            user_guess = int(input("Please guess a number:"))
        except ValueError:
            print("Oops! That wasn't an integer! Try again")
            continue
        
        if user_guess == rand_number:
            print("Just right!")
        elif user_guess < rand_number:
            print("Too low!")
        else:
            print("Too high!")
         
if __name__ == "__main__":
    guessing_game()