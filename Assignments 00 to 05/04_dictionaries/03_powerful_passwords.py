import hashlib

# Function to hash a password using SHA256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# This is your database of emails and their stored password hashes
stored_logins = {
    "user@example.com": hash_password("mysecurepassword"),
    "hello@world.com": hash_password("12345"),
}

# Function to check login
def login(email, password_to_check):
    if email in stored_logins:
        return stored_logins[email] == hash_password(password_to_check)
    return False

# Example usage:
print(login("user@example.com", "mysecurepassword")) 
print(login("hello@world.com", "wrongpassword"))     
print(login("not@found.com", "any"))                  
