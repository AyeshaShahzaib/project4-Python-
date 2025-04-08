def subtract_seven(num):
    # Subtract 7 from the given number and return the result
    return num - 7

def main():
    # Ask the user to input a number
    num = int(input("Enter a number: "))
    
    # Call the subtract_seven function and store the result
    result = subtract_seven(num)
    
    # Print the result
    print(f"After subtracting 7, the result is: {result}")

# Run the program
main()
