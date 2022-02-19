class Solution:
    def mergeTwoLists(self, list1, list2):
        res = None
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        if list1.val > list2.val:
            res = list2
            res.next = self.mergeTwoLists(list1, list2.next)
        else:
            res = list1
            res.next = self.mergeTwoLists(list1.next, list2)
        return res
