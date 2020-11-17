'''
Build Tower by the following given argument:
number of floors (integer and always greater than 0).

Tower block is represented as *
for example, a tower of 3 floors looks like below

[
  '  *  ', 
  ' *** ', 
  '*****'
]
and a tower of 6 floors looks like below

[
  '     *     ', 
  '    ***    ', 
  '   *****   ', 
  '  *******  ', 
  ' ********* ', 
  '***********'
]
'''

def tower_builder(n_floors):
    # build here    
    tower = []
    width = (n_floors * 2) - 1
    for _i in range(1, 2 * n_floors, 2):
        stars = _i * "*"
        line = stars.center(width)
        tower.append(line)
    return tower
