#!/usr/bin/python3

"""adds items to json file"""
import sys
import json


load = __import__('6-load_from_json_file').load_from_json_file
save = __import__('5-save_to_json_file').save_to_json_file
args = sys.argv[1:]
jsonfile = "add_item.json"
try:
    my_list = load(jsonfile)
except FileNotFoundError:
    save(args, jsonfile)
else:
    my_list.extend(args)
    save(my_list, jsonfile)
