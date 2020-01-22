#!/usr/bin/python3
""" 
	Module that contains a function that writes to a text file
"""
def write_file(filename="", text=""):
    	""" 
	Write to a text file
        except: file opened
        text: text to write
        filename: filename
	"""
	with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
