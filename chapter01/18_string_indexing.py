message = "Coding Factory"

print(message[0])
print(message[1])
print(message[2])
print(message[3])
print(message[4])
print(message[5])

print(message[0:6])

# Immutability
# message[0] = "K" (Error Message)

# Iterate
for char in message:
    print(char, end="")
print()

# range() a very efficient method that returns object items on the fly
a = range(100_000_001)
print(type(a))

for i in range(100_000_001):
    if i > 9:
        break
    print(i, end="|")
print()

# length of string
str_length = len(message)
print(f"Length of {message} is {str_length}.")

for i in range(str_length):
    print(message[i], end="\t")