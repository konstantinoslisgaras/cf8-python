sum = {
    frozenset({1, 2, 3}) : "Konstantinos",
    "key1": "value1",
    "key2": 10,
    3: [1, 2, 3],
    4: {1: "one", 2: "two"}
}

print(sum)

for key, value in sum.items():
    print(key, ":", value, end=" | ")