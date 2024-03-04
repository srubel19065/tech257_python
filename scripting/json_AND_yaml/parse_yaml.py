import os

import yaml

path_to_yaml = "example.yaml"
with open((path_to_yaml), 'r') as file:
    data = yaml.safe_load(file)

print(data)
print(type(data))