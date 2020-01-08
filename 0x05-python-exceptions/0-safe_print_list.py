#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    x = 0
    for s in range(x):
        try:
            print("{}".format(my_list[s]), end='')
        except:
            break
        else:
            x += 1
    print()
    return (x)
