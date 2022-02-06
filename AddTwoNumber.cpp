/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* indexing(ListNode* node2Find, int i){
        int count = 0;
        while(count < i)
        {
            node2Find = node2Find->next;
            count++;
        }
        return node2Find;
    }
    
//Below is main code
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* l3 = new ListNode;
        ListNode* target = NULL;
        
        cout<<target->val<<endl;
        
        return l1;
    }
};