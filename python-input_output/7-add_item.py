#!/usr/bin/python3
"""script that adds all arguments to a Python list,then save them to a file"""


import sys
import json
save_to_json = __import__("5-save_to_json_file").save_to_json_file
load_from_json = __import__("6-load_from_json_file").load_from_json_file
try:
        jlist = load_from_json("add_item.json")
except FileNotFoundError:
    jlist = []
jlist.extend(sys.argv[1:])
save_to_json(jlist, "add_item.json")
