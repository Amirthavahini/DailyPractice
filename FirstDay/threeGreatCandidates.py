#Find the three great candidates
'''
The hiring team aims to find 3 candidates who are great collectively. Each candidate has his or her ability expressed as an integer.
3 candidates are great collectively if the product of their abilities is maximum. Given the abilities of some candidates in an array, 
arr[], return the maximum collective ability from the pool of candidates.
'''
class Solution:
    def maxProduct(self, arr):
        arr.sort()
        max1 = arr[-1] * arr[-2] * arr[-3]
        max2 = arr[0] * arr[1] * arr[-1]
        return max(max1, max2)