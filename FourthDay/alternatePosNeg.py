#Alternate Positive Negative
'''
Given an unsorted array arr containing both positive and negative numbers. Your task is to rearrange the array 
and convert it into an array of alternate positive and negative numbers without changing the relative order.

Note:
- Resulting array should start with a positive integer (0 will also be considered as a positive integer).
- If any of the positive or negative integers are exhausted, then add the remaining integers in the answer 
as it is by maintaining the relative order.
- The array may or may not have the equal number of positive and negative integers.
'''
class Solution:
    def rearrange(self,arr):
        positive = []
        negative = []
        for i in range(len(arr)):
            if arr[i] >= 0:
                positive.append(arr[i])
            else:
                negative.append(arr[i])
                
        for i in range(min(len(positive),len(negative))):
            arr[2*i] = positive[i]
            arr[2*i+1] = negative[i]
            
        k = min(len(positive), len(negative))
        index = 2 * k
        
        for i in range(k, len(positive)):
            arr[index] = positive[i]
            index += 1
        
        for i in range(k, len(negative)):
            arr[index] = negative[i]
            index += 1