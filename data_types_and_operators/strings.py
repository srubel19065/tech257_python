double_quotes_str = "Look! Double quotes!"
single_quotes_str = 'Look! Single quotes!'
print(double_quotes_str)
print(single_quotes_str)

# bad_str = 'I said 'Wow''

good_str = 'I said "Wow"'
print(good_str)

good_single_str = "I said 'Wow'"
print(good_single_str)

escape_str = 'I said \'Wow\''
print(escape_str)

extra_spaces_str = "       Bob       "
print(len(extra_spaces_str))
print(len(extra_spaces_str.strip()))

example_str = "here's some text with lot's of text"
print(example_str)
# count how many times substring occurs in a string
print(example_str.count("text"))

#lowercase
print(example_str.lower())
#upper
print(example_str.upper())

# capitalize first letter
print(example_str.capitalize())

#replace something in string
print(example_str.replace(" with", ","))