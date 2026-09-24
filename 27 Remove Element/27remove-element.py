class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        f=0
        r=0
        # if nums.count(val)==len(nums):
        #     return 
        while r<len(nums):
            if nums[f]!=val and nums[r]!=val:
                f+=1
                r+=1
            elif nums[f]==val and nums[r]!=val:
                nums[f],nums[r]=nums[r],nums[f]
                f+=1
                r+=1
            else:
                r+=1
        return f

            
                
        