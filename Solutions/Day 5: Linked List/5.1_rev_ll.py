class Solution:    
    def reverseList(self, head):
        ans = None
        while head:
            temp = head
            head = head.next
            temp.next = ans
            ans = temp
        return ans
