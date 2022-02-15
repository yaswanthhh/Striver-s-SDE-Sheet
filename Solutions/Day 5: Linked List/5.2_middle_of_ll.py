class Solution:
    def middleNode(self, head):
        if head.next is None:
            return head
        slow, fast = head, head
        while fast.next and fast:
            slow = slow.next
            fast = fast.next.next
        return slow
