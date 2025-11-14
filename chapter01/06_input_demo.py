name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height: "))
is_student = input("Are you a student? (yes/no) ").lower() == 'yes' # this returns True if answer is 'yes'
print(type(is_student))

if is_student:
    print(f"{name} is a student")
else:
    print(f"{name} is not a student")