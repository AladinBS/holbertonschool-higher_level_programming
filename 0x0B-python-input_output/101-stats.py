#!/usr/bin/python3
""" status code printed """
class Magic:
    """ inst with dictionary and text"""
    def __init__(self):
        """ Init """
        self.size = 0
        self.dic = {}

    def init_dic(self):
        """ Init"""
        self.dic['200'] = 0
        self.dic['301'] = 0
        self.dic['400'] = 0
        self.dic['401'] = 0
        self.dic['403'] = 0
        self.dic['404'] = 0
        self.dic['405'] = 0
        self.dic['500'] = 0

    def add_status_code(self, status):
        """ add the numberes that were repeated """
        if status in self.dic:
            self.dic[status] += 1

    def print_info(self, sig=0, frame=0):
        print("Size: {:d}".format(self.size))
        for z in sorted(self.dic.keys()):
            if self.dic[z] is not 0:
                print("{}: {:d}".format(z, self.dic[z]))

if __name__ == "__main__":
    import sys
    try:
        x = 0
        status_codes = \
            {code: 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}
        for i, line in enumerate(sys.stdin, 1):
            words = line.split()
            x += int(words[-1])
            status_codes[int(words[-2])] += 1
            if i % 10 == 0:
                print("File size: {:d}".format(x))
                print_dict_sorted_nonzero(status_codes)
    finally:
        print("File size: {:d}".format(x))
        print_dict_sorted_nonzero(status_codes)
