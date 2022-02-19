class Solution:
    def hasCycle(self, head):
        if head == None:
            return False
        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = (fast.next).next
            slow = slow.next
            if fast == slow:
                return slow
        return False
