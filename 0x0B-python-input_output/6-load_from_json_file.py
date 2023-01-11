#!/usr/bin/python3

"""read from a jason file"""
import json


def load_from_json_file(filename):
    """function to load from a json file"""

    with open(filename, "r", encoding="utf-8") as f:
        return json.loads(f.read())
