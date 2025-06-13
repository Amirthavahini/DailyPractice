#Reverse elements in groups
'''
Given an array arr of positive integers. Reverse every sub-array group of size k.
Note: If at any instance, k is greater or equal to the array size, then reverse the entire array. 
You shouldn't return any array, modify the given array in place.
'''
class Solution:
    def reverseInGroups(self,arr, k):
        n=len(arr)
        if k<len(arr):
            for i in range(0,n,k):
                arr[i:i+k]=arr[i:i+k][::-1]
            return arr
        else:
            arr.reverse()
            return arr