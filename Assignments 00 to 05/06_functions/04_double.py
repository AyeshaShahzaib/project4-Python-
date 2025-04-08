def double(num):
    # Multiply the number by 2 and return the result
    return num * 2

def main():
    # Ask the user for a number
    num = int(input("Enter a number: "))
    
    # Call the double function and print the result
    result = double(num)
    print(f"Double that is {result}")

# Call main() to run the program
main()
