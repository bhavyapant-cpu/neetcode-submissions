# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return head
        new_list=None
        tail=head
        temp=head

        x=k

        while temp and x>0:
            next_ptr=temp.next
            temp.next=new_list
            new_list=temp
            temp=next_ptr
            x-=1
        if x>0:
            new_list=self.reverseKGroup(new_list,k-x)
        else:
            tail.next=self.reverseKGroup(temp,k)
        return new_list