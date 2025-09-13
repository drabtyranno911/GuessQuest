import random

def show_tutorial():
    print("\nWelcome to the tutorial: \n1. The computer will pick a random number between 1 and 100. \n2. You need to guess the number by typing it in. \n3. After each guess, you'll get a hint:")
    print("   → 'Too low!' means try a bigger number.")
    print("   → 'Too high!' means try a smaller number.")
    print("   → 'Correct!' means you won the game")
def play_game():
    print("\nStarting the Number Guessing Game!")
    number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guessed = int(input("Enter your guess: "))
            attempts += 1

            if guessed < number:
                print("Too low! Try again.")
            elif guessed > number:
                print("Too high! Try again.")
            else:
                print("Correct! The number was",number)
                print("Number of tries you took:",attempts)
                break
        except ValueError:
            print("Please enter a valid number....")

if __name__ == "__main__":
    print("Welcome to the Number Guessing Game!")
    print("1. Tutorial")
    print("2. Play Game")
    
    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == "1":
        show_tutorial()
        play_game()
    elif choice == "2":
        play_game()
    else:
        print("Invalid choice. Exiting game.")
