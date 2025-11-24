# base^exp
def my_power_to(base, exp):
    return base ** exp

# Lambda function
power_to = lambda base, exp: base ** exp

print(type(power_to))

print(power_to(5, 2))
print(power_to(2, 8))
print(power_to(4, 4))
print(power_to(3, 6))