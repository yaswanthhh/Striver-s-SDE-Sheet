class Solution:
    def reverseKGroup(self, head, k):
        temp = head
        l = 0
        while temp:
            l += 1
            temp = temp.next
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        while l >= k:
            cur = prev.next
            nex = cur.next
            for i in range(1, k):
                cur.next = nex.next
                nex.next = prev.next
                prev.next = nex
                nex = cur.next
            prev = cur
            l -= k
        return dummy.next
