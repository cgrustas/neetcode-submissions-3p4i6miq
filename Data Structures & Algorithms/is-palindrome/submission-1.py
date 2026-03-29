class Solution:
    def isPalindrome(self, s: str) -> bool:
        # convert string to alphanumeric/lowercase characters
        processedS = ''.join(c.lower() for c in s if c.isalnum())

        # return the comparison of the reverse string to the initial string
        return processedS == processedS[::-1]