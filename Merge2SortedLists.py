# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3 = ListNode()
        headValue = list3
        if list1.val <= list2.val:
            list3.val = list1.val
            list1 = list1.next
        else:
            list3.val = list2.val
            list2 = list2.next
            
        while(list1 != None and list2 != None):
            list3.next = ListNode
            list3 = list3.next
            if list1.val <= list2.val:
                list3.val = list1.val
                list1 = list1.next
            elif list2.val < list1.val:
                list3.val = list2.val
                list2 = list2.next
        
            
        list3 = headValue
        while(list3.next != None):
            print(list3.val, ", ", end="")
            list3=list3.next
        return headValue
            
                
        
        