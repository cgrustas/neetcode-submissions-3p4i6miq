class Solution:

    # use an array to store the number of characters 
    # for each string in the list

    # use delimeter '#' to indicate a new string

    # this will indicate the length of the str
    # then decode the specified number of characters after the '#',
    # and store in list
    def encode(self, strs: List[str]) -> str:
        # when concatenating the list into a single string, 
        # for each str in strs,
        # precede the str with the number 'len(str)' and '#' delimeter
        concatenated_str = ""
        for s in strs: 
            concatenated_str += f"{len(s)}#" + s

        return concatenated_str   


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

