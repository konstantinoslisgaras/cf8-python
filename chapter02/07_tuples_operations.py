# Tuple
family_members = ("Athina", "Konstantinos", "Alma", "Reina")
print(family_members, type(family_members))

# Iteration over tuple with index and value
for index, value in enumerate(family_members):
    print(f"{index}: {value}")

# Enchanced for to iterate over tuple
for member in family_members:
    print(member, end=" | ")
print()

# Unpacking into variabe
first_m, second_m, third_m, fourth_m = family_members
print(f"1st: {first_m}")
print(f"2nd: {second_m}")
print(f"3rd: {third_m}")
print(f"4th: {fourth_m}")

# Modifying a tuple (?)
family_members = list(family_members)
family_members[3] = "Nelly"
family_members = tuple(family_members)
print(family_members)