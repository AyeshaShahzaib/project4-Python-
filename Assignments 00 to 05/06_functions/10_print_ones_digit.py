def print_ones_digit(num):
    # Use modulo operator to find the ones digit
    ones_digit = num % 10
    print(f"The ones digit is {ones_digit}")

def main():
    # Prompt the user for an integer input
    num = int(input("Enter a number: "))
    
    # Call the function to print the ones digit
    print_ones_digit(num)

# Call main to run the program
main()
