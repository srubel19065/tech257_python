import os

# Directory
directory = "test_dir"

# Path to parent dir
parent_dir = "C:/Users/rubel"

# path
path = os.path.join(parent_dir, directory)

# filename and path
filename = "testfile.txt"
filename = os.path.join(path, filename)


# Make the file
with open(os.path.join(path, filename), "w") as file1:
    toFile = "Contents of the file are here"
    file1.write(toFile)
print(f"File {filename} created in {directory}")