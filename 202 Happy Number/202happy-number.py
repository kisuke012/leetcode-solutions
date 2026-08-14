class Solution:
    def isHappy(self, n: int) -> bool:
        seen=[]
        while n!=1:
            summ=0
            for i in str(n):
                summ+=int(i)**2
            if summ in seen:
                return False
            seen.append(summ)
            n=summ
        return True
                
        