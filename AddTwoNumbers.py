#You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. 
#Add the two numbers and return the sum as a linked list.
#You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        added=ListNode(val = (l1.val+l2.val) % 10) 
        carry_over = (l1.val+l2.val) // 10
        current_node = added
        
        while(l1.next and l2.next):
            l1 = l1.next
            l2 = l2.next
            current_node.next = ListNode(val = (carry_over + l1.val+ l2.val) % 10) 
            carry_over = (carry_over + l1.val+l2.val) // 10
            current_node=current_node.next

        while(l1.next):
            l1 = l1.next
            current_node.next = ListNode(val = (carry_over + l1.val) % 10) 
            carry_over = (carry_over + l1.val) // 10
            current_node=current_node.next

        while(l2.next):
            l2 = l2.next
            current_node.next = ListNode(val = (carry_over + l2.val) % 10) 
            carry_over = (carry_over + l2.val) // 10
            current_node=current_node.next    

        if (carry_over) > 0 :
            current_node.next = ListNode(val = 1)

        return added        