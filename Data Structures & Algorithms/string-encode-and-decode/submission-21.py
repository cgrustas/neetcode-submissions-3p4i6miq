class Solution:
    def encode(self, strs: List[str]) -> str:
        if strs == [""]:
            return "empty string list"
        if not strs:
            return ""
        
        encoded_words = []
        for s in strs:
            encoded_chars = []
            for c in s:
                # Encode each character's codepoint as a 6-digit hexadecimal number
                encoded_c = f"{ord(c):06x}"
                encoded_chars.append(encoded_c)
            encoded_word = ''.join(encoded_chars)
            encoded_words.append(encoded_word)
        return chr(257).join(encoded_words)

    def decode(self, s: str) -> List[str]:
        if s == "empty string list":
            return [""]
        if not s:
            return []
    
        encoded_words = s.split(chr(257))
        decoded_words = []
        for encoded_word in encoded_words:
            decoded_chars = []
            for i in range(0, len(encoded_word), 6):
                # Convert each 6-digit hexadecimal number back to a character
                char_code = int(encoded_word[i:i+6], 16)
                decoded_chars.append(chr(char_code))
            decoded_word = ''.join(decoded_chars)
            decoded_words.append(decoded_word)

        return decoded_words