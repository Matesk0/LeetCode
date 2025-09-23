# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr = head
        last = None
        seen = set()

        while curr is not None:
            if curr.val not in seen:
                seen.add(curr.val)
                last = curr

            else:
                last.next = curr.next

            curr = curr.next

        return head