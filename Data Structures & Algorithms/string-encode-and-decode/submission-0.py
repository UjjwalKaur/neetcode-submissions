class Solution:

    def encode(self, strs: List[str]) -> str: 
        encoded_strs = "";
        for word in strs:
            encoded_strs += str(len(word)) + "#" + word

        return encoded_strs

    def decode(self, s: str) -> List[str]:
        decoded_str = []
        i = 0;
        while i < len(s):
            j = i
            while(s[j] != '#'):
                j += 1
            str_length = int(s[i:j])
            decoded_str.append(s[j + 1 : j + 1 + str_length])
            i = j + 1 + str_length
        return decoded_str

            
