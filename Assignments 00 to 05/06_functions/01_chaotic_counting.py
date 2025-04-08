import random

# DONE_LIKELIHOOD is a constant that controls how likely done() will return True
DONE_LIKELIHOOD = 0.3  # 30% chance of returning True

# done() function returns True with a certain probability
def done():
    return random.random() < DONE_LIKELIHOOD

# chaotic_counting() function
def chaotic_counting():
    for i in range(1, 11):
        if done():
            return  # If done() returns True, we stop and return from the function
        print(i, end=" ")

# main() function
def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("I'm done.")

# Call main() to run the program
main()
