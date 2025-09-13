def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    merged = sorted(nums1 + nums2)
    n = len(merged)
    if n % 2 == 1:
        return merged[n // 2]
    else:
        return (merged[n // 2 - 1] + merged[n // 2]) / 2

# Time complexity: O((m+n) log(m+n)) where m and n are the lengths of the two arrays.
# Space complexity: O(m+n) for the merged array.

# Explanation:
# The function first merges the two input arrays and sorts them.
# It then calculates the length of the merged array.
# If the length is odd, it returns the middle element.
# If the length is even, it returns the average of the two middle elements.

