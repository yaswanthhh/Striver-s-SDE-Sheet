class Solution:
    def detectCycle(self, head):
        if head == None:
            return None
        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = (fast.next).next
            slow = slow.next
            if fast == slow:
                entry = head
                while slow:
                    if entry == slow:
                        return slow
                    entry = entry.next
                    slow = slow.next
        return None
