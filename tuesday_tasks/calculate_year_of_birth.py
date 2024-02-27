from datetime import datetime
name_str = input(("What is your name? "))
age_int = input(("What is your age? "))

year = (2024 - int(age_int))
dob_str = input("What is your DOB?")

print(f"OMG, You are {age_int} years old so you were born in {year}.")

days = int(age_int) * 365
hours = days * 24
print(f"You have lived for {hours} hours in total!")

