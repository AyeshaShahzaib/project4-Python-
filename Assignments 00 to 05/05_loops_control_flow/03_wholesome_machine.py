# The correct affirmation
affirmation = "I am capable of doing anything I put my mind to."

# Prompt the user
print("Please type the following affirmation:")
print(affirmation)

# Keep asking until the input matches exactly
while True:
    user_input = input()
    if user_input == affirmation:
        print("That's right! :)")
        break
    else:
        print("Hmmm That was not the affirmation. Please type the following affirmation:")
        print(affirmation)
