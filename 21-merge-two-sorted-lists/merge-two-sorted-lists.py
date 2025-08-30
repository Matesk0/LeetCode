# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        l = list1
        r = list2

        dummy = ListNode()
        result = dummy

        curr = dummy

        while l is not None and r is not None:
            if l.val >= r.val:
                curr.next = r
                r = r.next
            
            else:
                curr.next = l
                l = l.next
            
            curr = curr.next

        if l:
            curr.next = l
        
        if r:
            curr.next = r
        
        return result.next
                
        