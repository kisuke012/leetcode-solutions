class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        s=0
        r=1
        chk=True
        while r<len(nums):
            if nums[r]==nums[s] and chk and r==s+1:
                s+=1
                r+=1
                chk=False
            elif nums[r]==nums[s] and chk:
                s+=1
                nums[s]=nums[r]
                r+=1
                chk=False
            elif nums[r]!=nums[s] and r==s+1:
                s+=1
                r+=1
                chk=True
            elif nums[r]!=nums[s]:
                s+=1
                nums[s]=nums[r]
                r+=1
                chk=True
            else:
                r+=1
        return s+1


            
            

        