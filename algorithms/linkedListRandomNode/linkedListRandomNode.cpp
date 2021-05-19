class Solution {
private:
    int length;
    ListNode* head;
public:
    /** @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node. */
    Solution(ListNode* head) : head{head} {
        length = 1;
        ListNode* traverse = head;
        while(traverse != nullptr) {
            ++length;
            traverse = traverse->next;
        }
    }
    
    /** Returns a random node's value. */
    int getRandom() {
        int idx = rand() % length;
        ListNode* traverse = head;
        for (int i = 0; i < idx; i++) {
            traverse = traverse->next;
        }
        return traverse->val;
    }
};
