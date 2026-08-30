class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return 1
        l1=nums.index(max(nums))
        l2=nums.index(min(nums))
        mini=len(nums)
        if l1>l2:
            if l1+1<mini:
                mini=l1+1
            if (l2+1)+(len(nums)-l1)<mini:
                mini= (l2+1)+(len(nums)-l1)
            if len(nums)-l2<mini:
                mini=len(nums)-l2
        else:
            if l2+1<mini:
                mini=l2+1
            if (l1+1)+(len(nums)-l2)<mini:
                mini= (l1+1)+len(nums)-l2
            if len(nums)-l1<mini:
                mini=len(nums)-l1
        return mini
