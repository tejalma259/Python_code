# FIND THE FIRST NON-REPEATING CHARACTER IN A STRING
# "Non-repeating" means a character that appears EXACTLY ONCE.
# "First" means the earliest such character (left to right).
#
# Example: "swiss"
#   s -> appears 3 times
#   w -> appears 1 time   <-- first one that appears only once
#   i -> appears 1 time
# Answer: "w"


def first_non_repeating(text):
    """Return the first character that appears only once, or None if there is none."""

    # STEP 1: Count how many times each character appears.
    # We use a dictionary:   character : count
    frequency = {}
    for char in text:
        if char in frequency:
            frequency[char] += 1   # seen before -> add 1
        else:
            frequency[char] = 1    # first time -> start at 1

    # STEP 2: Go through the string AGAIN, in order.
    # Return the FIRST character whose count is exactly 1.
    for char in text:
        if frequency[char] == 1:
            return char

    # STEP 3: If the loop finishes, every character repeated.
    return None


# ---------------- Main program ----------------
if __name__ == "__main__":
    text = input("Enter a string: ")

    result = first_non_repeating(text)

    if result is None:
        print("No non-repeating character found (all characters repeat).")
    else:
        print("First non-repeating character:", result)
