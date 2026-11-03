class Solution:
    def minMoves(self, nums: List[int]) -> int:
        t=max(nums)
        res=0
        for i in nums:
            res+=t-i
        return res
        