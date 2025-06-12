#Average of List
'''
You are given a list arr that contains integers. You need to return average of the non negative integers.
'''
def nonNegativeAverage(arr):
    sum=0
    count=0
    for i in range(len(arr)):
        if arr[i]>=0:
            count+=1
            sum+=arr[i]
    average=sum/count
    return average