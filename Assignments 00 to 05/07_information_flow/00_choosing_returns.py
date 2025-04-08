# Define the constant for the adult age
ADULT_AGE = 18

def is_adult(age):
    # Check if the age is greater than or equal to ADULT_AGE
    if age >= ADULT_AGE:
        return True
    else:
        return False

def main():
    # Ask the user for the age
    age = int(input("How old is this person?: "))
    
    # Call the is_adult function and print the result
    print(is_adult(age))

# Call main to run the program
main()
