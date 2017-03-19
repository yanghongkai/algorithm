#!/usr/bin/env python
# coding=utf-8

from __future__ import print_function

def selecttionSort(arr, n):
    for i in range(n-1):
        #寻找[i,n)区间里的最小值
        minIndex=i
        for j in range(i+1, n):
            if arr[j] < arr[minIndex]:
                minIndex=j
        if minIndex!=i:
            tmp=arr[i]
            arr[i]=arr[minIndex]
            arr[minIndex]=tmp

if __name__=='__main__':
    a=[10,9,8,7,6,5,4,3,2,1]
    selecttionSort(a,len(a))
    print(a)














