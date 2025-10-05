def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
        return cleaned == cleaned[::-1]



# Time Complexity: O(n)
# Space Complexity: O(n)

# The function first cleans the input string by removing non-alphanumeric characters and converting all characters to lowercase.
# It then checks if the cleaned string is equal to its reverse. 
# If they are equal, the function returns True, indicating that the string is a palindrome; otherwise, it returns False.
# The time complexity is O(n) because we need to iterate through the entire string to clean it and then again to check if it is a palindrome.
# The space complexity is also O(n) because we create a new string to store the cleaned version of the input string.
# The use of slicing to reverse the string is efficient and concise, making the code easy to read and understand.
# This approach effectively handles various cases, including empty strings and strings with only non-alphanumeric characters
# by treating them as palindromes.# The function is case-insensitive and ignores spaces and punctuation, as required.
