shopping_list = ["eggs", "bread", "bananas", "biscuits", "milk"]
print(shopping_list)
print(type(shopping_list))

print(shopping_list[0])
print(shopping_list[-1])

shopping_list[1] = "rice"
print(shopping_list)

shopping_list.append("carrots")
print(shopping_list)
print(len(shopping_list))

shopping_list = shopping_list + ["toffee", "coffee"]
print(shopping_list)

shopping_list.pop(2)
print(shopping_list)

shopping_list.pop(-1)
print(shopping_list)