class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return len(nums)
        l=0
        r=1
        while r<len(nums):
            if nums[r]!=nums[l]:
                if r==l+1:
                    l+=1
                    r+=1
                else:
                    l+=1
                    nums[l]=nums[r]
                    r+=1
            else:
                r+=1
        return l+1   
                

            
                
