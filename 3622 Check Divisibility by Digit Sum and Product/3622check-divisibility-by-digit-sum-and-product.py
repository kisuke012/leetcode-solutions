class Solution:
    def checkDivisibility(self, n: int) -> bool:
        summ=0
        prd=1
        for i in str(n):
            summ+=int(i)
            prd*=int(i)
        if n%(summ+prd)==0:
            return True
        return False
            
        