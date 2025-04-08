def count_even(lst):
    # Count the number of even numbers in the list
    even_count = 0
    for num in lst:
        if num % 2 == 0:
            even_count += 1
    print("Number of even numbers:", even_count)

# Function to collect user input
def collect_numbers():
    lst = []
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        if user_input == "":
            break  # Exit loop when user presses enter without input
        else:
            try:
                num = int(user_input)  # Convert input to an integer
                lst.append(num)  # Add the integer to the list
            except ValueError:
                print("Please enter a valid integer.")
    
    count_even(lst)  # Call count_even() with the list

# Call the function to start collecting numbers
collect_numbers()
