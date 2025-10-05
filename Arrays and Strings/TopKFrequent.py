def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        topK = []
        kDict = {}
        for num in nums:
            if num not in kDict:
                kDict[num] = 0
            kDict[num] += 1
        for key, value in kDict.items():
            curr = (-value, key)
            heapq.heappush(topK, curr)
        result = []
        for i in range(k):
            result.append(heapq.heappop(topK)[1])
        return result


# Time Complexity: O(n log k) where n is the number of elements in nums and k is the number of top frequent elements to return.
# Space Complexity: O(n) for the dictionary storing the frequency of each element.

# The function first counts the frequency of each element in the input list using a dictionary.
# It then uses a max-heap (priority queue) to keep track of the top k frequent elements.
# The frequencies are stored as negative values to simulate a max-heap using Python's min-heap implementation.
# Finally, it pops the top k elements from the heap and returns their corresponding values.
# This approach ensures that we efficiently find the k most frequent elements in the list.
# The time complexity is O(n log k) because we push n elements into the heap, and each push operation takes O(log k) time.
# The space complexity is O(n) due to the dictionary storing the frequency of each unique element.