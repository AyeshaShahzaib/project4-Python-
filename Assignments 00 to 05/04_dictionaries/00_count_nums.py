# Create an empty dictionary to store counts
number_counts = {}

# Loop to collect user inputs
while True:
    user_input = input("Enter a number (or type 'done' to finish): ")

    if user_input.lower() == 'done':
        break

    try:
        number = int(user_input)
        # Increase count if number is already in dictionary, else set to 1
        if number in number_counts:
            number_counts[number] += 1
        else:
            number_counts[number] = 1
    except ValueError:
        print("Please enter a valid number or 'done' to finish.")

# Print the result
for number, count in number_counts.items():
    print(f"{number} appears {count} times.")
