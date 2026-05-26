class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict = {}

        for c in s:
            if (c in dict.keys()):
                dict[c] += 1
            else:
                dict[c] = 1
            
        for c in t:
            if (c in dict.keys()):
                dict[c] -= 1
            else:
                return False

        for i in dict.values():
            if i != 0:
                return False

        return True

        
        