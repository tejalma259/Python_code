# PALINDROME CHECKER
# A palindrome is a word that reads the SAME forwards and backwards.
# Examples: madam, racecar, level, 121


# METHOD 1: Using slicing (short and simple)
def is_palindrome_slicing(text):
    """Check palindrome by comparing the string with its reverse [::-1]"""
    # text[::-1] gives the reversed string
    return text == text[::-1]


# METHOD 2: Without slicing (using a loop with two pointers)
def is_palindrome_loop(text):
    """
    Check palindrome using two pointers:
    - 'left' starts at the beginning (index 0)
    - 'right' starts at the end (last index)
    We compare them and move toward the middle.
    """
    left = 0                 # first character
    right = len(text) - 1    # last character

    while left < right:      # keep going until pointers meet in the middle
        if text[left] != text[right]:
            return False     # mismatch found -> NOT a palindrome
        left += 1            # move left pointer forward
        right -= 1           # move right pointer backward

    return True              # all characters matched -> it IS a palindrome


# ---------------- Main program ----------------
if __name__ == "__main__":
    string = input("Enter a string: ")

    # (Optional) make it case-insensitive so "Madam" also counts.
    # Remove the .lower() line below if you want it case-sensitive.
    string = string.lower()

    if is_palindrome_slicing(string):
        print("Palindrome")
    else:
        print("Not a palindrome")
