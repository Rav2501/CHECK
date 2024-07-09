def reverse_and_uppercase(input_string):
    # Convert the input string to uppercase
    uppercase_string = input_string.upper()
    
    # Reverse the uppercase string
    reversed_string = uppercase_string[::-1]
    
    # Print the reversed, uppercase string
    print(reversed_string)

# Get the input string from the user
input_string = input("Enter a string of lowercase characters: ")

# Call the function to print the reversed, uppercase string
reverse_and_uppercase(input_string)
