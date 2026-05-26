class Solution:
    def isValid(self, s: str) -> bool:

        if (len(s) % 2 == 1):
            return False

        st = []
        pairs = {
            '(':')',
            '{':'}',
            '[':']'
        }

        for c in s:
            if c in pairs.keys():
                st.append(c)
            else:
                if(not st or c != pairs.get(st.pop(),0)):
                    return False
                else:
                    continue
        if not st:
            return True
        else:
            return False
        