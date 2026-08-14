class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        f=0
        r=len(numbers)-1
        while True:
            if numbers[f]+numbers[r]==target:
                return [f+1,r+1]
            elif numbers[f]+numbers[r]>target:
                r-=1
            else:
                f+=1


        