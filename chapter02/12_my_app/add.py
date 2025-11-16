# import my_calculations
from my_calculations import my_add_function as my_add, num1

num2 = 200

res1 = my_add(10, 20)
print(res1)

res2 = my_add(num1, num2)
print(res2)
print(f"Name of __main__ in app.py: {__name__}")