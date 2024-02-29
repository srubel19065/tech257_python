#Create a frozen set named frozen_set containing elements "hello", "world".
frozen_set = frozenset(["hello", "world"])
print(frozen_set)
#Try to add "!" to frozen_set. What happens?
#frozen_set.add("!")
print(frozen_set)
## Doesnt work
#Create a normal set named normal_set containing elements "let's", "learn".
normal_set = {"let's", "learn"}
#Try to add frozen_set to normal_set. Why does it work? Explain.
normal_set.add(frozen_set)
print(normal_set)
## frozensets are hashable and immutable so can be used as an element in a set

#Print normal_set.
print(normal_set)
#Run your script half a dozen times. What do you notice about where frozen_set is added to normal_set? Hint: Look at the order of the items.
## it is moving through in terms of its index,
#What makes a frozen set different to a normal set? Explain.
## Frozen sets are immutable = cannot be added to or removed, whereas Normal sets are mutable = can be added to or removed.
## Frozen sets are hashable = can be added as keys/elements in other sets whereas sets cannot be used in other sets