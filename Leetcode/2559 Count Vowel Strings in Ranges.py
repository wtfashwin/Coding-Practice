'''
2559. Count Vowel Strings in Ranges

You are given a 0-indexed array of strings words and a 2D array of integers queries.

Each query queries[i] = [li, ri] asks us to find the number of strings present in the range li to ri (both inclusive) of words that start and end with a vowel.

Return an array ans of size queries.length, where ans[i] is the answer to the ith query.

Note that the vowel letters are 'a', 'e', 'i', 'o', and 'u'
'''

class Solution:
    def isVowel(self, ch: str) -> bool:
        vowels = "aeiou"
        return ch in vowels
    
    def vowelStrings(self, words: list[str], queries: list[list[int]]) -> list[int]:
        n = len(words)
        Pre = [0] * n
        for i in range(n):
            temp = words[i]
            if self.isVowel(temp[0]) and self.isVowel(temp[-1]):
                Pre[i] += 1
        for i in range(1, n):
            Pre[i] += Pre[i - 1]
        ans = []
        for l, r in queries:
            if l == 0:
                ans.append(Pre[r])
            else:
                ans.append(Pre[r] - Pre[l - 1])
        return ans