#User function Template for python3


class Solution:
    def bina(self,arr,lo,hi,x):
        res=-1
        while(lo<=hi):
            mid=(lo+hi)//2
            if arr[mid]<x:
                lo=mid+1
            else:
                res=mid
                hi=mid-1
        return res
    def bina1(self,arr,lo,hi,x):
        res=-1
        while(lo<=hi):
            mid=(lo+hi)//2
            if arr[mid]<=x:
                res=mid
                lo=mid+1
            else:
                hi=mid-1
        return res
    def find(self, arr, x):
        if x not in arr:
            return([-1,-1])
        else:
            arr1=[]
            arr1.append(self.bina(arr,0,len(arr)-1,x))
            arr1.append(self.bina1(arr,0,len(arr)-1,x))
            return arr1
