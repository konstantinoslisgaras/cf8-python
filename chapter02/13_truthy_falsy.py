# Falsy - Truthy Values
# Example of falsy values: 0, 0.0, 0j, "", [], {}, (), False, None, set()

empty_dic = {}
print(type(empty_dic))

empty_set = set()
print(type(empty_set))

# Conditional expressions

a = 5

if a >= 0 and a <= 10:
    print("Valid grade.")
else:
    print("Invalid grade.")

# Chained comparisons

if 0 <= a <= 10:
    print("Valid grade.")
else:
    print("Invalid grade.")