#Array Leaders
'''
You are given an array arr of positive integers. Your task is to find all the leaders in the array. 
An element is considered a leader if it is greater than or equal to all elements to its right. 
The rightmost element is always a leader.
'''
class Solution:
    def leaders(self, arr):
        new_arr=[]
        max=arr[-1]
        new_arr.append(max)
        for i in range(len(arr)-2,-1,-1):
            if arr[i] >= max:
                new_arr.append(arr[i])
                max = arr[i]
        return list(reversed(new_arr))