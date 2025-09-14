class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    

# Time Complexity: O(n)
# Space Complexity: O(1)

# Explanation:
# We use two pointers, slow and fast. The slow pointer moves one step at a time
# while the fast pointer moves two steps at a time. When the fast pointer reaches
# the end of the list, the slow pointer will be at the middle node.