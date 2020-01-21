#!/usr/bin/python3
class MyList(list):
    """ This inherits the atts of a class l
    Arguments:
    list: A list of the class
    """
	
    def print_sorted(self):
        """ Print out lists """
        l_sorted = self.copy()
        l_sorted.sort()
        print(l_sorted)
