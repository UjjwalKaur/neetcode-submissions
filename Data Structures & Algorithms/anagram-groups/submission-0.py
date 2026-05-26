class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # make a hash map 

        from collections import defaultdict
        dict = defaultdict(list)

        for word in strs:
            word_array = tuple(sorted(word))

            # But a list (mutable type) cannot be a key
            dict[word_array].append(word)

        results = []

        for anagrams in dict.values():
            results.append(anagrams)

        return results



        