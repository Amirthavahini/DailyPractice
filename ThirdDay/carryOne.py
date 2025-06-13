#Add One
'''
Given a non-negative integer(without leading zeroes) represented as an array arr. Your task is to add 1 to the number 
(increment the number by 1). The digits are stored such that the most significant digit is at the starting index of the array.
'''
class Solution:
    def addOne(self, arr):
        for i in reversed(range(len(arr))):
            if arr[i]<9:
                arr[i]+=1
                return arr
            arr[i]=0
        return [1] + arr