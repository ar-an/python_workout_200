import random


def guessing_game():
    print("welcome to the guessing game! The pc chose a number between 1 and 100. Find the number in 3 tries!")

    random_number = random.randint(1, 100)
    tries = 0

    while tries < 3:
        try:
            choice = int(input("Choose a number between 1 and 100:"))
            tries += 1
            if choice == random_number:
                print(f"You found the number after {tries} tries! Well done!")
                searching_number=False
            elif choice < random_number:
                print("Too low!")
            elif choice > random_number:
                print("Too high!")
            if tries == 3:
                print("Sorry out of luck!")
        except:
            print('Please use an integer between 1 and 100')

if __name__ == "__main__":
    guessing_game()