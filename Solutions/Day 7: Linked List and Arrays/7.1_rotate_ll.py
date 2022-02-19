class Solution:
    def rotateRight(self, head, k):
        if head is None or head.next is None:
            return head
        temp = head
        l = 1
        while temp.next:
            l += 1
            temp = temp.next
        temp.next = head
        k = k%l
        end = l - k
        while (end > 0):
            temp = temp.next
            end -= 1
        head = temp.next
        temp.next = None
        return head
