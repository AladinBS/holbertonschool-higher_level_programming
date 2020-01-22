#!/usr/bin/python3
def pascal_triangle(n):
    """ Pascal tri
        matrix: pascal tri
        n: nmbr lines
    """
    prev = []
    matrix = []
    for ran in range(n):
        res_list = []
        x2 = 0
        x1 = -1
        for z in range(len(prev) + 1):
            if x1 == -1 or x2 == len(prev):
                res_list += [1]
            else:
                res_list += [prev[x1] + prev[x2]]
            x2 += 1
            x1 += 1
        matrix.append(res_list)
        prev = res_list[:]

    return matrix
