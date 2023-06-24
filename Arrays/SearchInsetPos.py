class Solution:
        
    def searchInsert(self, nums: List[int], target: int) -> int:
        n=len(nums)
        if target<nums[0]:
            return 0
        if target>nums[n-1]:
            return n
        low,high=0,n-1
        while high>=low:
            mid=low+(high-low)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                high=mid-1
            elif nums[mid]<target:
                  low=mid+1
        
        return low    
        