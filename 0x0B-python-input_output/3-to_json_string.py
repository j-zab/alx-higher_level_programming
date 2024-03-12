#!/usr/bin/python3
"""Write a function that returns the JSON
visualization of an object (str)"""
import json


def to_json_string(my_obj):
    """Return the JSON representation of a str object."""
    return json.dumps(my_obj)
