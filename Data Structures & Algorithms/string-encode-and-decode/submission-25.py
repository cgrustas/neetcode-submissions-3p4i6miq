class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = ""
        for s in strs:
            encodedStr += str(len(s)) + "#" + s
        return encodedStr

    def decode(self, s: str) -> List[str]:
        num = ""
        decodedStrs = []

        i = 0
        while i < len(s):
            if s[i] != "#":
                num += s[i]
                i += 1
                continue

            i += 1 # move past '#'
            endOfStrIdx = int(num) + i # i is currently at the pound index. endOfStrIdx = current index + 1 (skip '#') + specified number of characters to read from the string 
            num = "" # reset num for the next number
            decodedStr = ""
            while i < endOfStrIdx:
                decodedStr += s[i]
                i += 1
            decodedStrs.append(decodedStr)
        
        return decodedStrs
        