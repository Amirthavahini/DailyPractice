#Remove duplicate sorted array
'''
Given a sorted array arr. Return the size of the modified array which contains only distinct elements.
Note:
1. Don't use set or HashMap to solve the problem.
2. You must return the modified array size only where distinct elements are present and modify the original array 
such that all the distinct elements come at the beginning of the original array.
'''
class Solution:
    def removeDuplicates(self, arr):
        i=0
        for j in range(1,len(arr)):
            if arr[j] != arr[i]:
                i+=1
                arr[i]=arr[j]
        return i+1