import os

# Directory
directory = "test_dir"

# Path to parent dir
parent_dir = "C:/Users/rubel"

# path
path = os.path.join(parent_dir, directory)
print(path)

# Create the dir
os.mkdir(path)