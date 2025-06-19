#Third Largest Element
'''
Given an array, arr of positive integers. Find the third largest element in it. Return -1 if the third largest element is not found.
'''
class Solution:
    def thirdLargest(self,arr):
        n1=n2=n3=-1
        for i in range(len(arr)):
            if arr[i]>n1:
                n3=n2
                n2=n1
                n1=arr[i]
            elif arr[i]>n2:
                n3=n2
                n2=arr[i]
            elif arr[i]>n3:
                n3=arr[i]
        if n3!=-1:
            return n3
        else:
            return -1