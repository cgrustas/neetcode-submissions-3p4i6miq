class Solution:
    # Returns a concatenated string of all strings in 'strs'
    # Before each string, there is: 
        # An integer representing the length of the following string
        # A delimiter '#', indicating that the string begins
        # with the following character
    def encode(self, strs: List[str]) -> str:
        concatenated_str = ""
        for s in strs: 
            concatenated_str += f"{len(s)}#" + s

        return concatenated_str   

    # Returns a list of strings
    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        str_length_str = ""
        decoding_strs = True
        while decoding_strs:
            # stop recording when you have finished traversing through the string
            if i >= len(s):
                break

            # read in each character until you reach the delimiter
            if s[i] != '#':
                str_length_str += s[i]
                i += 1
                continue
            
            # once you have reached the delimeter,
            # transform all the stored characters into an integer
            str_length = int(str_length_str)

            # reset str_length_str for the next str
            str_length_str = ""

            # count 'str_length' characters following the delimeter
            # store each value into a string
            current_str = ""
            for char in s[i + 1 : (i + 1 + str_length)]:
                current_str += char
                
            # increment 'i' to jump to the next 'str_length_str/#' pair
            i += 1 + str_length

            # then, store the string into the array 'strs'
            strs.append(current_str)

        return strs

