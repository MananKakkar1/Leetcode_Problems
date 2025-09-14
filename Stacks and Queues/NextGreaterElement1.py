def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        finalList = []
        flag = False
        for i in range(len(nums1)):
            flag = False
            for j in range(len(nums2) - 1):
                if nums1[i] == nums2[j]:
                    for k in range(j + 1, len(nums2)):
                        if nums2[k] > nums2[j]:
                            finalList.append(nums2[k])
                            flag = True
                            break
            if not flag:
                finalList.append(-1)
        return finalList


# Time Complexity: O(m * n) where m is the length of nums1 and n is the length of nums2
# Space Complexity: O(1) if we don't count the output list, otherwise O(m

# Explanation:
# For each element in nums1, we search for it in nums2.
# Once found, we look for the next greater element to its right in nums2.
# If found, we append it to the result list; otherwise, we append -1.
# We repeat this for all elements in nums1 to build the final result list.
