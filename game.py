import random


print("🎯 Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100...")

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Track number of attempts
guess_count = 0

while True:
    try:
        guess = int(input("Enter your guess number: "))
        guess_count += 1

        if guess < secret_number:
            print("Too  low deear! 📉 Try again.")
        elif guess > secret_number:
            print("Too  high love! 📈 Try again.")
        else:
            print(f"🎉WOOOOOOW Correct! You guessed it in {guess_count} tries.")
            break

    except ValueError:
        print("Please enter a valid number.")
