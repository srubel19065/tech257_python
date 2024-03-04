import json
import os
import sys
import yaml

if len(sys.argv) > 1:
    if os.path.exists(sys.argv[1]):
        source_file = open(sys.argv[1], "r")
        source_content = yaml.safe_load(source_file)
        source_file.close()
        json_data = json.dumps(source_content)

        with open(sys.argv[2], "w") as jsonFile:
            jsonFile.write(json_data)
            print(json_data)

    else:
        print(f"ERROR {sys.argv[1]} not found")
        exit(1)

else:
    print(f"Usage: python yaml2json.py <source_yaml_file.yaml> <target_json_file.json>")
