# Reverse string without using slicing and reverse function

# METHOD 1: Using a for loop with len() and negative indexing
def reverse_string_loop(text):
    """Reverse a string by looping through it backwards"""
    reversed_text = ""  # Empty string to store result

    # Loop from the last character to the first
    for i in range(len(text) - 1, -1, -1):
        reversed_text += text[i]  # Add each character to our result

    return reversed_text


# METHOD 2: Using while loop
def reverse_string_while(text):
    """Reverse a string using a while loop"""
    reversed_text = ""
    i = len(text) - 1  # Start at last character

    while i >= 0:  # Loop until we reach the beginning
        reversed_text += text[i]
        i -= 1  # Move to previous character

    return reversed_text


# Test the functions
if __name__ == "__main__":
    # Example input
    my_string = "Hello World"

    print("Original string:", my_string)
    print("Reversed (Method 1 - For Loop):", reverse_string_loop(my_string))
    print("Reversed (Method 2 - While Loop):", reverse_string_while(my_string))

    # You can test with your own string
    user_input = input("\nEnter a string to reverse: ")
    print("Your reversed string:", reverse_string_loop(user_input))
