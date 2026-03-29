class Solution:
    # returns true if character is alphanumeric, false if not
    def isAlnum(self, c: str) -> bool:
        return  (48 <= ord(c) <= 57 or
                65 <= ord(c) <= 90 or 
                97 <= ord(c) <= 122)


    def isPalindrome(self, s: str) -> bool:
        # make pointers left, right to point at the first/last 
        # characters of the string
        left, right = 0, len(s) - 1

        # while left < right:
        while left < right:
            # keep incrmenting left/right until they both point to alnum characters
            while left < right and not self.isAlnum(s[left]):
                left += 1
            
            while left < right and not self.isAlnum(s[right]):
                right -= 1

            # if value of left pointer != value of right pointer
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        # if string compared each character and found that all were true
        return True