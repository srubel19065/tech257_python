name_str = input("What is your name? ")
age_int = input("What is your age? ")
dob_int = input("What is your DOB ")
height_float = input("What is your height? ")

print(f"Hi {name_str}. You are {age_int} years old and was born on {dob_int}")

user_details = [name_str, ((int)(age_int)), dob_int, ((float)(height_float))]
print(user_details)

print(type(user_details[-1]))

