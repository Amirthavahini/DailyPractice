#Wave Array
'''
Given a sorted array arr[] of distinct integers. Sort the array into a wave-like array(In Place). 
In other words, arrange the elements into a sequence such that arr[1] >= arr[2] <= arr[3] >= arr[4] <= arr[5].....
If there are multiple solutions, find the lexicographically smallest one.

Note: The given array is sorted in ascending order, and you don't need to return anything to change the original array.
'''
from typing import List


class Solution:
    def convertToWave(self, arr : List[int]) -> None:
        temp=0
        for i in range(0, len(arr)-1, 2):
            if arr[i] < arr[i+1]:
                temp=arr[i]
                arr[i]=arr[i+1]
                arr[i+1]=temp
        return arr
    