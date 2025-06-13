#User function Template for python3
class Solution:
    def findKRotation(self, arr):
        index=0
        for i in range(len(arr)-1):
            if arr[i]>arr[i+1]:
                index=i+1
                break
        return index
