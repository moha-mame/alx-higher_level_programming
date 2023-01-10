#!/usr/bin/python3

""" save_to_json_file module """
import json


def save_to_json_file(my_obj, filename):
    """
    save_to_json_file function

    Writes an Object to a text file, using a JSON representation
    """

    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(my_obj, f, ensure_ascii=False)
