cities = ["mexico city", "cancun", "palenque", "barcelona", "athens"]

my_city = "athens"
print(my_city.title)

cap_cities = list(map(lambda city: city.title(), cities))

for city in cap_cities:
    print(city, sep=" | ")