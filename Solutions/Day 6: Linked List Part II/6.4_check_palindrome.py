#This has space complexity of n :/

class Solution:
    def isPalindrome(self, head):
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        for i in range(int(len(arr)/2)):
            if arr[i] != arr[len(arr)-i-1]: return False
        return True
