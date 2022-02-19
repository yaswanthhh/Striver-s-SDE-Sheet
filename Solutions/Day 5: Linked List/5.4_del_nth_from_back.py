class Solution:
    def removeNthFromEnd(self, head, n):
        temp = ListNode()
        temp.next = head
        fast = temp
        slow = temp
        for i in range(n):
            fast = fast.next
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return temp.next
