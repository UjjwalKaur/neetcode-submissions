class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict = {}

        def make_dict(s):
            dict = {}
            for c in s:
                if c in dict.keys():
                    dict[c] += 1;
                else:
                    dict[c] = 0;
            return dict
            
        if make_dict(s) == make_dict(t):
            return True
        else:
            return False
        