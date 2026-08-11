# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum1=0
        sum2=0
        i=0
        while l1:
            if i==0:
                sum1=l1.val
                l1=l1.next
            else:
                sum1=(l1.val * (10**i))+sum1
                l1=l1.next
            i+=1

        i=0
        while l2:
            if i==0:
                sum2=l2.val
                l2=l2.next
            else:
                sum2=(l2.val * (10**i))+sum2
                l2=l2.next
            i+=1
        total=sum1+sum2
        
        temp=ListNode()
        curr=temp
        for x in str(total)[::-1]:
            
            curr.next=ListNode(int(x))
            curr=curr.next
        return temp.next



        