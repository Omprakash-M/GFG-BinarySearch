class Solution:
    def bina(self, arr, lo, hi, x):
        res = -1  # floor index
        while lo <= hi:
            mid = (lo + hi) // 2
            if arr[mid] <= x:
                res = mid  # update candidate
                lo = mid + 1  # move right to find later floor
            else:
                hi = mid - 1
        return res

    def findFloor(self, arr, x):
        return self.bina(arr, 0, len(arr) - 1, x)
