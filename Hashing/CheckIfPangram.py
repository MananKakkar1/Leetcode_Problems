def checkIfPangram(self, sentence: str) -> bool:
        alphabet = {}
        for i in sentence:
            alphabet[i] = 1
            
        return len(alphabet.keys()) == 26


# Time Complexity : O(n) where n is the length of the sentence
# Space Complexity : O(1) since the size of the hashmap will be at max 26 (number of letters in the English alphabet)

# Explanation: We create a hashmap to store the characters in the sentence. If the length of the hashmap is 26, then we have all the characters in the alphabet.
# We can also use a set instead of a hashmap since we only care about the keys.
# We iterate through the sentence and add each character to the set. Finally, we check if the length of the set is 26.
# If it is, we return True, else we return False.