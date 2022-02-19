class Solution:
    def getIntersectionNode(self, headA, headB):
        t1 = headA
        t2 = headB
        while t1 != t2:
            if t1:
                t1 = t1.next
            else:
                t1 = headB
            if t2:
                t2 = t2.next
            else:
                t2 = headA
        return t1
