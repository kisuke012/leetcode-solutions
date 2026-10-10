class Solution:
    def mySqrt(self, x: int) -> int:
        r=1
        cnt=0
        while x>=(r*r):
            cnt+=1 
            r+=1  
        return cnt
