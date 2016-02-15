#!/usr/bin/env python

#a divide and conquer  with run time T(n) = 2T(n/3) + O(n^2)
#this implies n/3 runtime in our sort, and n^2 runtime within each partion

import matplotlib.pyplot as plt
import numpy as np
import time


def useless_sort(a):
    #check
    al = len(a)
    if al < 3:
        return 

    #split the arrays into n/3
    first_third = (1/3)*al
    second_third = (2/3)*al
    
    a0 = a[0:first_third]
    a1 = a[first_third+1:second_third]
    a2 = a[second_third+1:]
    
    #do 2 sorts of n/3 length
    useless_sort(a1)
    useless_sort(a2)

a = [1,2,3]
x_axis = [1,2,3]
#y_axis = [1455578571.091253,1455578571.091253,1455578571.091253]
y_axis = [0,0,0]
c = 0
total = 0
for i in xrange(4,600):
    a.append(i)
    x_axis.append(i)
    #n^2
    start = time.time()
    useless_sort(a)
    for i in a:
        for j in a:
            c+=(i+j)
    end = time.time()
    total+=(end-start)
    y_axis.append(end-start)

plt.plot(x_axis,y_axis)
plt.show()
print(x_axis)
print(y_axis)
print(c)
print(total)
