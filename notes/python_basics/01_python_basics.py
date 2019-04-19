#!/usr/bin/env python3

# given a vector 
a = [1,2,3,4,5,6,7,8,9,10]

# if we want to do operations on the elements of this array  (say calculate the squares of all the elements) we cannot simply say:
# b=a**2 # generates an error
# instead, we can use a call to 
# map(function, iterable)

# we can calculate the squares using a lambda function
b = map(lambda x: x**2, a)

# 
b = [x**2 for x in a[0:4]]


# panda basics (dataframes)
