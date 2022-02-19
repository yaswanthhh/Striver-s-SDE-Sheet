class Solution:
    def addTwoNumbers(self, l1, l2):
        res = ListNode()
        temp = res
        carry = 0
        while (l1 or l2):
            s = 0
            if l1 is not None:
                s += l1.val 
                l1 = l1.next 
            if l2 is not None:
                s += l2.val 
                l2 = l2.next 
            s += carry
            carry = s / 10 
            node = ListNode(int(s % 10)) 
            temp.next = node 
            temp = temp.next
        if int(carry) != 0:
            temp.next = ListNode(int(carry))
        return res.next
