# Dictionary of fruits with their prices
fruit_prices = {
    "apple": 10.0,
    "durian": 25.0,
    "jackfruit": 30.0,
    "kiwi": 12.5,
    "rambutan": 7.0,
    "mango": 8.0
}

total_cost = 0.0

# Loop through the dictionary and ask the user how many of each fruit they want
for fruit, price in fruit_prices.items():
    try:
        quantity = int(input(f"How many ({fruit}) do you want?: "))
        total_cost += quantity * price
    except ValueError:
        print("Please enter a valid number.")

# Print the total
print(f"\nYour total is ${total_cost}")
