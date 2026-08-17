class Solution:
    def addDigits(self, num: int) -> int:
        if num==0:
            return 0
        res=num%9
        if res!=0:
            return res
        else:
            return 9

