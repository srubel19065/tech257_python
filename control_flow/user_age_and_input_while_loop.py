# SET VARIABLE user_prompt TO TRUE
user_prompt = True


# PUT BEGINNING OF WHILE LOOP HERE - SHOULD LOOP WHILE user_prompt IS TRUE
while user_prompt is True:
    age = input("What is your age? ")
    # PUT IF STATEMENT HERE TO CHECK IF age IS ALL DIGITS
    if age.isdigit() and (int(age) < 118):
        # SET user_prompt TO FALSE
        user_prompt = False
    # ADD ELSE STATEMENT HERE
    else:
        print("You must enter digits mate, and you cant exceed age limit MATE!")
        # TELL USER THE PROBLEM WITH THEIR INPUT

print(f"Your age is {age}")