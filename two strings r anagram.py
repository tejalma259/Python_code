# CHECK IF TWO STRINGS ARE ANAGRAMS
# An ANAGRAM means both strings use the SAME letters the SAME number of times,
# just arranged in a different order.
#
# Example:  "listen"  and  "silent"   -> ANAGRAM  (same letters: l,i,s,t,e,n)
#           "hello"   and  "world"    -> NOT an anagram


# METHOD 1: Using sorted() (short and simple)
def is_anagram_sorted(a, b):
    """
    If we sort the letters of both strings, anagrams become identical.
    "listen" -> ['e','i','l','n','s','t']
    "silent" -> ['e','i','l','n','s','t']   <- same!
    """
    a = a.lower().replace(" ", "")   # ignore case and spaces
    b = b.lower().replace(" ", "")
    return sorted(a) == sorted(b)


# METHOD 2: Using character counts (no sorting)
def is_anagram_count(a, b):
    """
    Count how many times each letter appears in both strings.
    If the two counts are identical, they are anagrams.
    """
    a = a.lower().replace(" ", "")
    b = b.lower().replace(" ", "")

    # Quick check: different lengths can never be anagrams
    if len(a) != len(b):
        return False

    # Count letters in the first string
    count = {}
    for char in a:
        count[char] = count.get(char, 0) + 1

    # Subtract letters using the second string
    for char in b:
        if char not in count:
            return False        # a letter that 'a' never had
        count[char] -= 1
        if count[char] == 0:
            del count[char]

    # If everything cancelled out, the dictionary is empty -> anagram
    return len(count) == 0


# ---------------- Main program ----------------
if __name__ == "__main__":
    first = input("Enter the first string: ")
    second = input("Enter the second string: ")

    if is_anagram_sorted(first, second):
        print("Yes, they are anagrams")
    else:
        print("No, they are not anagrams")
