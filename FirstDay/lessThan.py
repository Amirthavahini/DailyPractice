#Less than
'''
You are given a number k and a list arr that contains integers. You need to return list of numbers that are less than k.
'''
def lessThan(arr, k):
    ans = []
    for i in range(len(arr)):
        if arr[i]<k:
            ans.append(arr[i])
    return ans