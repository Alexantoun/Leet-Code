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
        
//Below is main code
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* l3 = new ListNode;
        ListNode* l2Target = l2, *l1Target = l1, *l3Target = l3;
        int excess = 0;
        
        while(l1Target != NULL || l2Target!=NULL)
        {
            l3Target->val += l1Target->val + l2Target->val + excess;
            excess = 0;
            while (l3Target->val >= 10){
                excess++;
                l3Target->val -= 10;
            }
            l3Target->next = new ListNode;
            l3Target = l3Target->next;  
            l1Target = l1Target->next;
            l2Target = l2Target->next;
        }
        l3Target = l3;
        while(l3Target->next != NULL)
        {
            cout<<l3Target->val<<endl;
            l3Target = l3Target->next;
        }
        
        return l1;
    }
};