word = input("Please enter your desired word: ")

word_length = len(word)
character = "#"
vowels = ("a", "e", "o", "i", "u", "A", "E", "O", "I", "U")
exersice = 1

print(f"Exersice:{exersice} Prints the word letter by letter (one character per line).")

for i in range(word_length):
    print(word[i])

exersice += 1
print(f"Exersice:{exersice} Prints a growing triangle made of the word letters (like your 'Factory' example).")

for i in range(word_length):
    print(word[i] * (i + 1))

exersice += 1
print(f"Exersice:{exersice} Prints a shrinking triangle using # instead of missing characters")

for i in range(word_length):
    print(f"{word[i] * (word_length - i) + (i) * character}")

exersice += 1
print(f"Exersice:{exersice} Prints only the vowels in the word, in one line separated by spaces.")

for char in word:
    if char in vowels:
        print(char, end=" ")
    else:
        continue
print()

exersice += 1
print(f" Exersice:{exersice} Prints numbers 1 to 30, but only those divisible by 3 or 5 (not both at the same time).")
for i in range(1, 31):
    if (((i % 3 == 0) or (i % 5 == 0)) and not ((i % 3 == 0) and (i % 5 ==0))):
        print(i, end=" | ") 

print()
print("Thanks! Exiting application now...")