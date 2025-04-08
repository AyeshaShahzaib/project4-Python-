def print_multiple(message, repeats):
    # Print the message the given number of times
    for _ in range(repeats):
        print(message)

def main():
    # Prompt the user for a message and number of repeats
    message = input("Please type a message: ")
    repeats = int(input("Enter a number of times to repeat your message: "))
    
    # Call the print_multiple function to repeat the message
    print_multiple(message, repeats)

# Call main() to run the program
main()