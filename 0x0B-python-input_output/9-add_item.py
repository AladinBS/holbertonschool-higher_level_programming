#!/usr/bin/python3
""" Add arguments to .py list then to file
"""
import os.path
import sys
save_file = __import__('7-save_to_json_file').save_to_json_file
load_file = __import__('8-load_from_json_file').load_from_json_file
my_list = []
if os.path.exists("add_item.json"):
    my_list = load_file("add_item.json")

for x in sys.argv[1:]:
    my_list.append(x)

save_file(my_list, "add_item.json")
