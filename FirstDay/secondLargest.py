#Second largest Element
'''
Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.

Note: The second largest element should not be equal to the largest element.
'''
class Solution:
    def getSecondLargest(self, arr):
        n1=n2=0
        for i in range(len(arr)):
            if arr[i]>n1:
                n2=n1
                n1=arr[i]
            elif arr[i]>n2 and arr[i]!=n1:
                n2=arr[i]
        if n2!=0:
            return n2
        else:
            return -1