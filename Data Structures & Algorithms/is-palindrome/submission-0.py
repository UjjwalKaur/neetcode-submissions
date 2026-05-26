class Solution:
    def isPalindrome(self, s: str) -> bool:

        news = ""

        for l in s:
            if (l.isalnum()):
                news += l.lower()

        i = 0
        pointer = len(news) - 1
        while (i < len(news) and pointer >= 0):
            if(news[i] != news[pointer]):
                return False
            else:
                i += 1
                pointer -= 1
        return True
        