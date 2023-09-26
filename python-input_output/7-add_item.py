#!/usr/bin/python3
""""""


import sys
import json
save_to_json = __import__("5-save_to_json_file").save_to_json_file
load_from_json = __import__("6-load_from_json_file").load_from_json_file

if ("add_items.json"):
    jlist = load_from_json("add_items.json")
else:
    jlist = []
jlist.extend(sys.argv[1:])
save_to_json(jlist, "add_item.json")

