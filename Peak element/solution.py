class Solution:
    def peakElement(self, arr):
        n = len(arr)
        for i in range(n):
            if (i == 0 or arr[i] >= arr[i - 1]) and (i == n - 1 or arr[i] >= arr[i + 1]):
                return i  # Return the index of a peak element
