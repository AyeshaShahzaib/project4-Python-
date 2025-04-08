def get_user_data():
    # Ask the user for their first name
    first_name = input("What is your first name?: ")
    
    # Ask the user for their last name
    last_name = input("What is your last name?: ")
    
    # Ask the user for their email address
    email = input("What is your email address?: ")
    
    # Return the collected data as a tuple
    return first_name, last_name, email

def main():
    # Get the user data by calling the get_user_data function
    user_data = get_user_data()
    
    # Print the received user data
    print(f"Received the following user data: {user_data}")

# Run the program
main()
