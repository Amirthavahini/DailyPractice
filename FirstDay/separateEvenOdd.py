#Separate even and odd numbers
'''
You are given a list numbers that contains integers. You need to return two lists, one of even numbers and other of odd numbers.
'''
def evenOdd(arr):
    even = []
    odd = []
    for i in range(len(arr)):
        if arr[i]%2 == 0:
            even.append(arr[i])
        else:
            odd.append(arr[i])
    return (even, odd)
