# hashmap solution
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # key : sequence of letters
        # value : the anagrams that have said sequence from list 'strs'
        anagrams = defaultdict(list) # if list doresn't exist yet, we want to make every value default to a list
        
        # for string in list of strings
        for s in strs:
            # create a new array to represent each letter
            # initialize each value to 0
            letterSequence = [0] * 26

            # for each character in string
            for c in s:
                # find numeric representation of the character from 0-25
                # do this by subtracting the ascii value of 'a' from the ascii value of the current char
                charNumber = ord(c) - ord('a') 

                # now that we understand the numeric value of the char, we must account for it in the array
                # increment the representative index of the fixed array by 1
                letterSequence[charNumber] += 1

            # once the fixed array holds the sequence of letters
            # add the sequence and/or the string to the dictionary
            # append the string to the dictionary with key : sequence of letters
            anagrams[tuple(letterSequence)].append(s) # changed to a tuple b/c dictionary keys must be non-mutable in python

        return anagrams.values()

# time: O(n * m)
    # n : strings in each list
    # m : letters in each string
