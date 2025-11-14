name = "Konstantinos"

print("===== or =====")

valid_user = None or "User"

print("Hello", valid_user)

print("===== and =====")

email = "kappalambda@gmail.com"

valid_email = email and email == "lambda@gmail.com"

print(email == "user@gmail.com")

print("Valid email:", valid_email)

print("===== example_1 =====")

email = "kappalambda@gmail.com"

valid_email = email and email == "lambda@gmail.com"

if valid_email:
    print("Email is valid")
else:
    print("Email is invalid")