class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            summ=0
            for j in str(nums[i]):
                summ+=int(j)
            if summ==i:
                return i
        return -1



        