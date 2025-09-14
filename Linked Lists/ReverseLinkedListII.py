class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        curr = prev.next

        for _ in range(left, right):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next
    
# Time Complexity: O(n)
# Space Complexity: O(1)

# Explanation:
# We create a dummy node to handle edge cases where the head might be reversed.
# We move the `prev` pointer to the node just before the `left` position.
# We then reverse the sublist from `left` to `right` by adjusting the pointers.
# Finally, we return the modified list starting from `dummy.next`.   
