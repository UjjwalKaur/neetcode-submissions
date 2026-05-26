class Solution:

    def encode(self, strs: List[str]) -> str: 
        new_string = ""
        for word in strs:
            length = len(word)
            new_string += str(length) + ';' + word
        return new_string 

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while (i < len(s)):
            j = i
            while (s[j] != ';'):
                j += 1
            length = int(s[i:j])
            result.append(s[j + 1: j + length + 1])
            i = j + length + 1
        return result
        

            
