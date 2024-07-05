struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        if(!headA || !headB) return headA;

        auto ta = headA;
        auto tb = headB;

        while(ta != tb){
            ta = ta ? ta-> next : headB;
            tb = tb? tb -> next : headA;
        }

        return ta;
    }
};