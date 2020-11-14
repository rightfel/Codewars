'''
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([False,1,0,1,2,0,1,3,"a"]) # returns[False,1,1,2,1,3,"a",0,0]
'''

def move_zeros(array):
    #your code here
    zero = []
    other = []
    my_list = []
    for _i in array:
        if _i == 0 and type(_i) != bool:
            zero.append(0)
        else:
            other.append(_i)
    my_list = other + zero
    return my_list
