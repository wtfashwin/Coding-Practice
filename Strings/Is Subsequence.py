'''
Is Subsequence

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
'''

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        c = 0
        
        i , j = 0 , 0

        while i < len(s) and j < len(t):
            if (s[i] == t[j]):
                c += 1
                i += 1
            j += 1

        if c == len (s):
            return  True