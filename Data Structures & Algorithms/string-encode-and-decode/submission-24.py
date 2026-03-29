class Solution:
    # Returns a concatenated string of all strings in 'strs'
    # Before each string, there is: 
        # An integer representing the length of the following string
        # A delimiter '#', indicating that the string begins
        # with the following character
    def encode(self, strs: List[str]) -> str:
        concatenated_str = ""
        for s in strs: 
            concatenated_str += str(len(s)) + '#' + s
        return concatenated_str   

    # Returns a list of strings
    def decode(self, s: str) -> List[str]:
        strs, i = [], 0

        # stop recording when you have finished traversing through the string
        while i < len(s):
            j = i

            # store the 
            while s[j] != '#':
                j += 1
            
            # store each value into a string
            length = int(s[i:j])
            current_str = s[j + 1 : (j + 1 + length)]
            strs.append(current_str)
                
            # increment 'i' to jump to the next 'str_length_str/#' pair
            i = j + 1 + length

        return strs

