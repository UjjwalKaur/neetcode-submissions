class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def dfs(i):
            # no more chars left, which means everything is a palindrome!
            if i >= len(s):
                res.append(part.copy())
                return

            for j in range(i, len(s)):
                if self.isPalin(s, i, j):
                    part.append(s[i:j + 1])
                    dfs(j + 1)
                    part.pop()


        dfs(0)
        return res

    def isPalin(self, word, start, end):
        while start < end:
            if word[start] != word[end]:
                return False
            start += 1
            end -= 1
        return True

        