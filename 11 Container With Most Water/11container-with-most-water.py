class Solution:
    def maxArea(self, height: List[int]) -> int:
        vol=0
        f=0
        r=len(height)-1
        while f<=r:
            if height[f]<height[r]:
                voli=height[f]*(r-f)
                f+=1
            else:
                voli=height[r]*(r-f)
                r-=1
            if voli>vol:
                vol=voli
        return vol

        