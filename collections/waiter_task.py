# Rationale: To practice lists
# Script should act like a waiter at a restaurant taking orders

# level 1

# Greet the user
greeting = (input("Hi, How are you today? "))
# Print a list of starters
print("This is what we have today for our starters...")
starters = ["samosas", "halloumi", "prawns"]
print(starters)
# Take an input for the user for their starter
user_starters = (input("What would you like? "))
# Print a list of mains
print("This is what we have today for the mains...")
mains = ["peri-peri chicken", "beef burger", "vegan burger"]
print(mains)
# Take an input for the user for their main course
user_mains = (input("What would you like for your main? "))
# Print a list of desserts
print("This is what we have today for the desserts...")
desserts = ["brownies", "fudge cake", "pancakes", "ice cream"]
print(desserts)
# Take an input for the user for their dessert
user_desserts = (input("What would you like for dessert? "))
# Print all of the user's choices
user_choices = [user_starters, user_mains, user_desserts]
print(user_choices)
# level 2
# Use at least one f-string
# Add each item ordered to a list called 'customer_order_list'
customer_order_list = (user_choices)
print(f"You have chosen {customer_order_list}, will be with you soon!")
# if time: level 3 (may need research if we have not covered dictionaries yet)
# Use dictionaries and assign prices to the items. Create a bill at the end of the program.
prices = {
    "samosas" : "£1.50",
    "halloumi" : "£2",
    "chicken" : "£4"
}
# if time: level 4
# Add more to this program. Recommended ways are: Only allow input that is within the list, Add quantities of order etc.