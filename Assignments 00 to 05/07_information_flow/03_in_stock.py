def num_in_stock(fruit):
    # A dictionary of fruits and their corresponding stock quantities
    inventory = {
        "apple": 50,
        "banana": 30,
        "pear": 1000,
        "orange": 200,
        "mango": 0
    }
    
    # Return the quantity of the fruit in stock, or 0 if the fruit is not in stock
    return inventory.get(fruit.lower(), 0)

def main():
    # Prompt user for input
    fruit = input("Enter a fruit: ")
    
    # Get the number of fruits in stock
    stock = num_in_stock(fruit)
    
    # Check if fruit is in stock
    if stock > 0:
        print("This fruit is in stock! Here is how many:")
        print(stock)
    else:
        print("This fruit is not in stock.")

# Run the program
main()
