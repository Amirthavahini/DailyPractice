#count distinct elements
'''
You are given a list arr that contains integers. You need to count distinct integers in list.
'''
class Solution:
    def countDistinct(self, arr):
        new_set = set(arr)
        return len(new_set)