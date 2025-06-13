#User function Template for python3


class Solution:
    
    #Function to find the minimum element in sorted and rotated array.
    def minNumber(self, arr,low,high):
        index=0
        for i in range(len(arr)-1):
            if arr[i]>arr[i+1]:
                index=i+1
                break
        return arr[index]
