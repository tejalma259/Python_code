# using string
sentence = input("I am tejal and I am 25:")
words = sentence.lower().split()
frequency = {}
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1
print("\nWoed Frequencies:")
for word, count in frequency.items():
    print(word, ":", count)      
