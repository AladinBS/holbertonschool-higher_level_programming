#!/usr/bin/python3
""" Appends a line """
def append_after(filename="", search_string="", new_string=""):
    """ appends a new line if a str is found
        search_string: search str
        new_string: appended str
        filename: filename
    """
    res_line = []
    with open(filename, 'r', encoding="utf-8") as f:
        for x in f:
            res_line += [x]
            if x.find(search_string) != -1:
                res_line += [new_string]

    with open(filename, 'w', encoding="utf-8") as f:
        f.write("".join(res_line))
