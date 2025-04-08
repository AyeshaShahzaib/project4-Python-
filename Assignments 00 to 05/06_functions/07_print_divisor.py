def print_divisors(num):
    # Loop through all numbers from 1 to num
    print(f"Here are the divisors of {num}")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=" ")

def main():
    # Ask the user for a number
    num = int(input("Enter a number: "))
    
    # Call the print_divisors function to print divisors
    print_divisors(num)

# Call main() to run the program
main()
