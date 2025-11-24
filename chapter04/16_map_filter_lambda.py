cities = ["mexico city", "oaxaca", "cancun", "palenque", "barcelona", "athens"]

# 1st Step - Filter
big_name_cities = list(filter(lambda city: len(city) > 8, cities))

# 2nd Step - Map
cap_len_cities = list(map(lambda city: city.title(), big_name_cities))

# Both filtering and mapping
cap_len_cities = list(map(lambda city: city.title(), filter(lambda city: len(city) > 8, cities)))

print(cap_len_cities)

def cap_my_city(city):
    return city.title()

print(cap_my_city('athens'))

print("="*50)

cap_len_cities = list(map(cap_my_city, filter(lambda city: len(city) > 8, cities)))
