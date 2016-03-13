import numpy as np
#import matplotlib as mp

def Partition(arr,left, right):
    i = left
    j = right
    tmp = 0
    pivot = arr[(left+right)/2] #temp value for pivot
    
    while (i<=j):
        while (arr[i] < pivot):
            i+=1
        while (arr[j-1] > pivot):
            j-=1
        if (i <= j):
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
            i+=1
            j-=1
    
    return i

def QuickSort(alist,left,right):
    index = Partition(alist,left,right)
    if(left < index-1):
        QuickSort(alist,left,index-1)
    if(index < right):
        QuickSort(alist,index,right)


def InsertionSort(arr, n):
    i = 0
    k = 0
    j = 0
    for i in xrange(n):
        key = arr[i]
        j-=1
        while(j>=0 and arr[j] > key):
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key


def QuickInsertSort1(alist,k):
    if len(alist) < k:
        InsertionSort(alist)
    else:
        QuickSort(alist,0,len(alist))

QuickInsertSort1([1,3,2,12,9,8,4],2)
#def QuickInsertSort2():

