# Populate list
ages = [19, 34, 45, 61, 88]
print("Initial list of ages:", ages)

# For loop
for age in ages:
    print(age, end=" | ")
print()

# Iterate with for and index
# enumerate() -> (index, value)
for index,value in enumerate(ages):
    print(f"Index:{index}, Value:{value}")