def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = {}
        for c in s1:
            count1[c] = 1 + count1.get(c, 0)
        need = len(count1)
        for i in range(len(s2)):
            count2, cur = {}, 0
            for j in range(i, len(s2)):
                count2[s2[j]] = 1 + count2.get(s2[j], 0)
                if count1.get(s2[j], 0) < count2[s2[j]]:
                    break
                if count1.get(s2[j], 0) == count2[s2[j]]:
                    cur += 1
                if cur == need:
                    return True
        return False



# Time Complexity: O(m * n) where m is the length of s1 and n is the length of s2 in the worst case.
# Space Complexity: O(1) since the size of the character count dictionaries is bounded by the number of unique characters (at most 26 for lowercase English letters).

# The function first counts the occurrences of each character in s1 and stores it in count1.
# It then iterates through each character in s2, using a nested loop to check for permutations of s1 starting from each character in s2.
# For each starting character, it maintains a count of characters seen so far in count2 and a counter cur to track how many unique characters have matched the required count from count1.
# If at any point the count of a character in count2 exceeds that in count1, the inner loop breaks early.
# If the count of a character in count2 matches that in count1, cur is incremented.
# If cur equals need (the number of unique characters in s1), it means a permutation of s1 has been found in s2, and the function returns True.
# If no permutation is found after checking all starting points in s2, the function returns False.
# The time complexity is O(m * n) in the worst case because for each character in s2, we may need to check up to the length of s1.
# The space complexity is O(1) because the character count dictionaries can only contain a fixed number of entries (at most 26 for lowercase English letters), regardless of the input size.