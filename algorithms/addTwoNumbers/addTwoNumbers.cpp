class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int carry = 0;
        ListNode* result = NULL;
        ListNode* resultIter = NULL;
        while(l1 != NULL || l2 != NULL || carry) {
            // keep processing until both of them are null
            int l1Val = 0;
            int l2Val = 0;
            if (l1 != NULL) {
                l1Val = l1->val;
                l1 = l1->next;
            }
            if (l2 != NULL) {
                l2Val = l2->val;
                l2 = l2->next;
            }

            int sum = l1Val + l2Val + carry;
            if (sum >= 10) {
                carry = 1;
                sum -= 10;
            } else {
                carry = 0;
            }
            ListNode* n = new ListNode{sum};
            if (result == NULL) {
                resultIter = result = n;
            } else {
                resultIter->next = n;
                resultIter = resultIter->next;
            }
        }
        return result;
    }
};
