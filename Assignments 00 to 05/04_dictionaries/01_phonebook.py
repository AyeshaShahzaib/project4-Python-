# Create an empty phonebook dictionary
phonebook = {}

# Add some contacts
phonebook["Alice"] = "123-456-7890"
phonebook["Bob"] = "987-654-3210"
phonebook["Charlie"] = "555-123-4567"

# Print the entire phonebook
print("Phonebook:")
for name, number in phonebook.items():
    print(f"{name}: {number}")

# Look up a contact
search_name = input("Enter a name to search: ")

if search_name in phonebook:
    print(f"{search_name}'s number is {phonebook[search_name]}")
else:
    print(f"{search_name} not found in phonebook.")
