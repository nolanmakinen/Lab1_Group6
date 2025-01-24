import random
import string

# Function to get user input within a valid range
def get_user_input(prompt, min_value):
    while True:
        try:
            value = int(input(prompt))
            if value >= min_value:
                return value
            else:
                print(f"Please enter a value of greater than or equal to {min_value} to create a secure password.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Function to generate a password (skeleton)
def generate_password(length, num_letters, num_digits, num_specials):
    # Ensure total requested characters do not exceed length
    # Generate required characters (letters, digits, specials)
    # Fill remaining characters
    # Shuffle and return password
    pass

# Main function
def main():
    print("\n--- Secure Password Generator ---\n")

    # Step 1: Get user inputs
    length = get_user_input("Enter the total length of the password: ", 8)

    while True:
        num_letters = get_user_input("Enter the number of letters desired in the password: ", 2)
        num_digits = get_user_input("Enter the number of digits: ", 1)
        num_specials = get_user_input("Enter the number of special characters: ", 1)

        # Step 2: Validate user inputs
        if num_letters + num_digits + num_specials == length:
            break
        else:
            print("Error: The total of letters, digits, and special characters must exactly match the password length.")

    # Step 3: Generate the password

    # Step 4: Display the password

# Entry point
if __name__ == "__main__":
    main()