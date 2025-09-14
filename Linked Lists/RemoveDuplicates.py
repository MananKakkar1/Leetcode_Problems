class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        numsDict = {}
        if head is None:
            return None
        curr = head
        while curr is not None:
            if curr.val not in numsDict:
                numsDict[curr.val] = 1
            curr = curr.next
        
        newList = []
        for key in numsDict.keys():
            newList.append(key)
            
        newHead = ListNode(newList[0])
        curr = newHead
        for i in range(1, len(newList)):
            curr.next = ListNode(newList[i])
            curr = curr.next
            
        return newHead
    

# Time Complexity: O(n)
# Space Complexity: O(n)


# Explanation:# We use a dictionary to keep track of the unique values in the linked list.
# We then create a new linked list using these unique values and return the head of the new list.
# We traverse the original list once to populate the dictionary, which takes O(n) time.
# Creating the new list also takes O(n) time in the worst case when all values are
# unique. Thus, the overall time complexity is O(n).
# The space complexity is O(n) because we are using a dictionary to store the unique values,
# which in the worst case can store all n values from the original list.
# Note: This solution does not maintain the original order of elements.