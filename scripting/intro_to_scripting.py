import sys
import os
import subprocess
import json_AND_yaml


#os.mkdir("test_dir")


# sys
if len(sys.argv) > 1:
    print("You gave me an argument!")

# this is the same as play button
# only runs when you give more than 1 arg
#the first file is index 0 so whatever arg you give after will be 1 and more


# subprocess
subprocess.run(["python", "hello_world.py"])

# json_AND_yaml
x = {
    "name" : "John",
    "age" : 30,
    "city" : "Liverpool"

}

y = json_AND_yaml.dumps(x)
#converted it to str

print(type(x))
print(type(y))