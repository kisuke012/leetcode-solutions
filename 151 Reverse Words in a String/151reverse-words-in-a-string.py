class Solution:
    def reverseWords(self, s: str) -> str:
        rev=''
        word=''
        for i in s:
            if i.isalnum():
                word+=i
            elif i==' ':
                if word:
                    rev=' '+word+rev
                else:
                    continue
                word=''
        if word:
            rev=' '+word+rev
        return rev[1:]

            
        