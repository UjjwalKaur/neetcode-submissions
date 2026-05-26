class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for word in strs:
            encoded += str(len(word)) + "$" + word
        return encoded

    def decode(self, s: str) -> List[str]:
        i = 0
        results = []
        start = 0

        while i < len(s):
            while (s[i] != "$"):
                i += 1
                continue
            length = int(s[start: i])
            results.append(s[(i + 1) : (i + length + 1)])
            start = i + length + 1
            i = start

        return results

