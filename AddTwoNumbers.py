# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = ""
        curr = l1
        while curr:
            s1 += str(curr.val)
            curr = curr.next
        s2 = ""
        curr = l2
        while curr:
            s2 += str(curr.val)
            curr = curr.next
        x = int(s1) + int(s2)
        s3 = str(x)
        s3 = s3[::-1]
        newList = ListNode(int(s3[0]))
        curr = newList
        for char in s3[1:]:
            curr.next = ListNode(int(char))
            curr = curr.next
        return newList

# Time complexity: O(max(m, n)) where m and n are the lengths of the two linked lists.
# Space complexity: O(max(m, n)) for the new linked list.

# Explanation: 
# s1 contains the number represented by the first linked list in order.
# s2 contains the number represented by the second linked list in order.
# We convert both strings to integers, add them, and convert the result back to a string
# We then reverse the string to match the required order for the linked list and create a new linked list from it.