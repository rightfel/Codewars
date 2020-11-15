'''
Your task, is to create NxN multiplication table, of size provided in parameter.

for example, when given size is 3:

1 2 3
2 4 6
3 6 9

for given example, the return value should be: [[1,2,3],[2,4,6],[3,6,9]]
'''

def multiplication_table(size):
    multi = []
    for _i in range(1, size + 1):
        row = []
        for _x in range(1, size + 1):
            row.append(_i * _x)
        multi.append(row)
    return multi
