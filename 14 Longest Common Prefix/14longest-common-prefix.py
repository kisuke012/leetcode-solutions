class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs[0]:
            return ""
        l=min(len(x) for x in strs)
        for j in range(l):
            chk=strs[0][j]
            for i in strs:
                if i[j]!=chk:
                    return strs[0][:j]
        return strs[0][:l]
        
        

        

        

        