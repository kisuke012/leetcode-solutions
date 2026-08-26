class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        cnt=0
        for i in nums:
            if i%k==0:
                cnt+=1
        if cnt==0:
            return k
        for x in range(1,cnt+2):
            if k*x not in nums:
                return k*x

        