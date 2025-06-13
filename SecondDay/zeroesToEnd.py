#Move zeroes to end
'''
You are given an array arr[] of non-negative integers. Your task is to move all the zeros in the array to the right end 
while maintaining the relative order of the non-zero elements. The operation must be performed in place, meaning you should not 
use extra space for another array.
'''

class Solution:
    def pushZerosToEnd(self,arr):
        count=0
        empty=[]
        for i in arr:
            if i!=0:
                empty.append(i)
            else:
                count+=1
        empty.extend([0]*count)
        return empty