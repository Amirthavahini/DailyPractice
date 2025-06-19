#Missing range of numbers
'''
You have an inclusive interval [lower, upper] and a sorted array of unique integers arr[], all of which lie within this interval. 
A number x is considered missing if x is in the range [lower, upper] but not present in arr[]. Your task is to return the 
smallest set of sorted ranges that includes all missing numbers, ensuring no element from arr is within any range, 
and every missing number is covered exactly once.
'''
class Solution:
    def missingRanges(self, arr, lower, upper):
        n = len(arr)
        missing = []
        if lower < arr[0]:
            missing.append([lower, arr[0]-1])
        for i in range(n-1):
            if arr[i+1]-arr[i]!=1:
                missing.append([arr[i]+1, arr[i+1]-1])
        if arr[n-1] < upper:
            missing.append([arr[n-1]+1, upper])
        return missing