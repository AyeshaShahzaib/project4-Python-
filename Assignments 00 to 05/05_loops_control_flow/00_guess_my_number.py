import random

# Generate a random number between 0 and 99
secret_number = random.randint(0, 99)

print("I am thinking of a number between 0 and 99...")

# Loop until the user guesses the number
while True:
    try:
        guess = int(input("Enter a guess: "))

        if guess > secret_number:
            print("Your guess is too high")
        elif guess < secret_number:
            print("Your guess is too low")
        else:
            print(f"Congrats! The number was: {secret_number}")
            break  # Exit the loop if guessed correctly
    except ValueError:
        print("Please enter a valid number.")
