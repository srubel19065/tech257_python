#Explain 2 main ways that sets are different to lists and tuples
## Sets cannot have multiple occurrences of the same element and store unordered values.

#Create a set named 'fruits' containing "apple", "banana", and "cherry".
fruits = {"apple", "banana", "cherry"}
#Print the set 'fruits'
print(fruits)
#Add "orange" to the fruits set using one of the set's methods.
fruits.add("orange")
#Print the set 'fruits' - check it's added
print(fruits)
#Remove "banana" from the fruits set using one of the set's methods.
fruits.remove("banana")
#Print the set 'fruits' - check it's removed
print(fruits)
#Attempt to add another "apple" to the fruits set. What do you observe? Why does this happen?
fruits.add("apple")
print(fruits)
# Does not add as sets cannot have duplicate items

#Print the final fruits set.
print(fruits)
#Print the 2nd item in the set. If there is any problem doing this, explain.
# print(fruits[1])
# Will not work as sets are unordered so dont have specific place to be called

veggies = {"lettuce", "cabbage"}
veggies.add(fruits)
print(veggies)