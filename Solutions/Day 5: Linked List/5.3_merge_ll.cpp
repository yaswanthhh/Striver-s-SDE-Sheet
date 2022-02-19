class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) 
    {
        ListNode * res = NULL;
        if(list1 == NULL) {
            return list2;
        }
        else if(list2 == NULL) {
            return list1;
        }
        
        if(list1->val > list2->val) {
            res = list2;
            res->next = mergeTwoLists(list1, list2->next);
        }
        else {
            res = list1;
            res->next = mergeTwoLists(list1->next, list2);
        }
        return res;
    }   
};
