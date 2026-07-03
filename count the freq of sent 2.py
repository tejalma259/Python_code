# COUNT THE FREQUENCY OF WORDS IN A SENTENCE
# "Frequency" means: how many times each word appears.

# Step 1: Take a sentence from the user
sentence = input("Enter a sentence: ")

# Step 2: Prepare the text
# .lower()  -> makes everything lowercase so "I" and "i" count as the same word
# .split()  -> breaks the sentence into a list of words (splits on spaces)
words = sentence.lower().split()

# Step 3: Create an empty dictionary to store each word and its count
# A dictionary stores data as   word : count
frequency = {}

# Step 4: Go through each word one by one
for word in words:
    if word in frequency:
        frequency[word] += 1   # word seen before -> add 1 to its count
    else:
        frequency[word] = 1    # first time we see this word -> start count at 1

# Step 5: Print the results
print("\nWord Frequencies:")
for word, count in frequency.items():
    print(word, ":", count)


# ---------- SHORTER VERSION using Python's built-in Counter ----------
# (Does the exact same thing in one line. Uncomment to try it.)
#
# from collections import Counter
# print(Counter(sentence.lower().split()))
