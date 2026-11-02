class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        res=0
        nums.sort()
        if len(nums)%2!=0:
            t=nums[len(nums)//2]
        else:
            t=((nums[len(nums)//2]+nums[(len(nums)//2)-1])//2)
        for i in nums:
            res+=abs(t-i)
        return res
        