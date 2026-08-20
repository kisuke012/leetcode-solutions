class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1=[]
        arr2=[]
        cnt=0
        for i in nums:
            if cnt==0:
                arr1.append(i)
                cnt=1
            elif cnt==1:
                arr2.append(i)
                cnt=2
            else:
                if arr1[-1] > arr2[-1]:
                    arr1.append(i)
                else:
                    arr2.append(i)

        res=arr1+arr2
        return res      