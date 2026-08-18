class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        if len(nums)==k:
            return max(nums)
        if k==1:
            maxx=0
            seen=[]
            for i in nums:
                if nums.count(i)==1:
                    seen.append(i)
            if len(seen)==0:
                return -1
            return max(seen)
        f=nums.count(nums[0])
        e=nums.count(nums[-1])
        if f==1 and e==1:
            return max(nums[0],nums[-1])
        elif f==1:
            return nums[0]
        elif e==1:
            return nums[-1]
        else:
            return -1
        