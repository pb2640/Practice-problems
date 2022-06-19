class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l,r = 0,len(arr)-1
        while(l<=r):
            mid = (l+r)//2
            if(arr[mid]>arr[mid+1] and arr[mid]>arr[mid-1]):
                return mid
            elif(arr[mid]>arr[mid+1]):
                r = mid-1
            else:
                l = mid+1
                
        
        #approach # O(n)
        # for i in range(len(arr)-2):
        #     if(arr[i+1]>arr[i] and arr[i+1]>arr[i+2]):
        #         return i+1
            
        