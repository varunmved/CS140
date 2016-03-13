import random
import matplotlib.pyplot as plt
import numpy as np
import time

def insertionSort(alist,start,end):
   #for index in range(1,len(alist)):
    for index in range(start+1,end): 
     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

def quickSort2(alist,k):
   quickSortHelper2(alist,0,len(alist)-1,k)
    

def quickSort1(alist,k):
   quickSortHelper(alist,0,len(alist)-1,k)

def quickSortHelper(alist,first,last,k):
   if first<last:
        if last - first < k:
            insertionSort(alist,first,last+1)
        else:
            splitpoint = partition(alist,first,last)
            quickSortHelper(alist,first,splitpoint-1,k)
            quickSortHelper(alist,splitpoint+1,last,k)

def quickSortHelper2(alist,first,last,k):
   if first<last:
        if last - first < k:
            return
        else:
            splitpoint = partition(alist,first,last)
            quickSortHelper2(alist,first,splitpoint-1,k)
            quickSortHelper2(alist,splitpoint+1,last,k)

def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark

#k = 4
alist = random.sample(xrange(1000), 100)
alist2 = alist
#x_axis = list(range(1,100)) 
x_axis = []
y_axis = []
x_axis2 = []
y_axis2 = []

'''
for i in range(1,1000):
    for k in xrange(100):
        x_axis.append(k)
        start = time.time()
        quickSort1(alist,k)
        overhead = time.time() - start
        y_axis.append(overhead)
'''
for i in range(1,1000):
    for k in xrange(100):
        x_axis2.append(k)
        start = time.time()
        quickSort2(alist,k)
        insertionSort(alist2,0,len(alist2))
        overhead = time.time() - start
        y_axis2.append(overhead)
print(x_axis2)
print(y_axis2)
plt.plot(x_axis2,y_axis2)
#plt.plot(x_axis,y_axis)
plt.show()
