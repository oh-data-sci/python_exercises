(a,b),c = 1,2,3                      # ERROR -- too many values to unpack
*(a,b), c = 1,2,3                    # a = 1, b = 2, c = 3

*(a,b) = 1,2                         # ERROR -- target must be in a list or tuple
*(a,b), = 1,2                        # a = 1, b = 2

*(a,b) = 'XY'                        # ERROR -- target must be in a list or tuple
*(a,b), = 'XY'                       # a = 'X', b = 'Y'

*(a, b) = 'this'                     # ERROR -- target must be in a list or tuple
*(a, b), = 'this'                    # ERROR -- too many values to unpack
*(a, *b), = 'this'                   # a = 't', b = ['h', 'i', 's']

*(a, *b), c = 'this'                 # a = 't', b = ['h', 'i'], c = 's'

*(a,*b), = 1,2,3,3,4,5,6,7           # a = 1, b = [2, 3, 3, 4, 5, 6, 7]

*(a,*b), *c = 1,2,3,3,4,5,6,7        # ERROR -- two starred expressions in assignment
*(a,*b), (*c,) = 1,2,3,3,4,5,6,7     # ERROR -- 'int' object is not iterable
*(a,*b), c = 1,2,3,3,4,5,6,7         # a = 1, b = [2, 3, 3, 4, 5, 6], c = 7
*(a,*b), (*c,) = 1,2,3,4,5,'XY'      # a = 1, b = [2, 3, 4, 5], c = ['X', 'Y']

*(a,*b), c, d = 1,2,3,3,4,5,6,7      # a = 1, b = [2, 3, 3, 4, 5], c = 6, d = 7
*(a,*b), (c, d) = 1,2,3,3,4,5,6,7    # ERROR -- 'int' object is not iterable
*(a,*b), (*c, d) = 1,2,3,3,4,5,6,7   # ERROR -- 'int' object is not iterable
*(a,*b), *(c, d) = 1,2,3,3,4,5,6,7   # ERROR -- two starred expressions in assignment


*(a,b), c = 'XY', 3                  # ERROR -- need more than 1 value to unpack
*(*a,b), c = 'XY', 3                 # a = [], b = 'XY', c = 3
(a,b), c = 'XY', 3                   # a = 'X', b = 'Y', c = 3

*(a,b), c = 'XY', 3, 4               # a = 'XY', b = 3, c = 4
*(*a,b), c = 'XY', 3, 4              # a = ['XY'], b = 3, c = 4
(a,b), c = 'XY', 3, 4                # ERROR -- too many values to unpack

