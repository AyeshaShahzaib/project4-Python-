# Ask the user to enter a number
curr_value = int(input("Enter a number: "))

# Loop to double the value until it's greater than or equal to 100
while curr_value < 100:
    curr_value = curr_value * 2
    print(curr_value, end=" ")
