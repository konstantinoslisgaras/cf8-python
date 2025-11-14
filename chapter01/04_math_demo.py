import math

name = "Kappa"
age = 34

print("-----")
print("PI =", math.pi)

# String concatenation
print(name + " is " + str(age) + " years old!") # Typecast with str()

print("Python2 style:")
print("PI = %6.2f" % math.pi) # Binds 6 places with 2 decimal digits
print("%s is %d years old" %(name, age))

print("-----")

print("Python3 style using string format:")
print("Age is {0:2d}".format(age)) # 0 is first index, 2d binds the places
print("Pi is {0:.3f}".format(math.pi)) # 3 decimal digits
print("{0} is {1} years old".format(name, age))

print("-----")

print("{0:*^10}:{1:>20}".format(name, age), end="|\n") # caret centers the variable, bigger sign keeps binds right
print(f"{name} is {age} years old") # with "f" for placeholders