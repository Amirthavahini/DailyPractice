#Decrement values of the list
'''
You are given a list that contains integers. You need to decrement each element of the list by 1 and return the list.
'''
def decrementList(arr):
    for i in range(len(arr)):
        arr[i]-=1
    return arr