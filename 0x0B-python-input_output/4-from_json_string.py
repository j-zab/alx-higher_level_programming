#!/usr/bin/python3
# 6-from_json_string.py
"""Write a function that returns an object
(Python data structure) represented by a JSON str"""
import json


def from_json_string(my_str):
    """Returns the Python object represented of a JSON str."""
    return json.loads(my_str)
