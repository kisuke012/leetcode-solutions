class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic={}
        f=0
        res=0

        for x in range(len(s)):
            if s[x] in dic:
                f=max(f,dic[s[x]]+1)
            dic[s[x]]=x
            res=max(res,x-f+1)
        return res



        