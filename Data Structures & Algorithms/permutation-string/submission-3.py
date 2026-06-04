class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count = collections.defaultdict(int)
        s2Count = collections.defaultdict(int)

        for i in range(len(s1)):
            s1Count[s1[i]] += 1
            s2Count[s2[i]] += 1

        matches = 0

        for i in range(26):
            if s1Count[chr(97 + i)] == s2Count[chr(97 + i)]:
                matches += 1

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26: return True

            # starts at the next element outside the window
            s2Count[s2[r]] += 1
            if s1Count[s2[r]] == s2Count[s2[r]]:
                matches += 1
            elif s1Count[s2[r]] + 1 == s2Count[s2[r]]:
                matches -= 1

            s2Count[s2[l]] -= 1
            if s1Count[s2[l]] == s2Count[s2[l]]:
                matches += 1
            elif s1Count[s2[l]] - 1 == s2Count[s2[l]]:
                matches -= 1

            l += 1

        return matches == 26


        