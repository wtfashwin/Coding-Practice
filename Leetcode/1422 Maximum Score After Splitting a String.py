'''
1422. Maximum Score After Splitting a String

Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).

The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.

'''

class Solution:
    def maxScore(self, s: str) -> int:
        zero=0
        one=0

        l=0
        r=0


        if s[0] and s[0]=='0':
            zero += 1
        
        for i in range(1,len(s)):
            if s[i]=='1':
                one+=1
        
        res=max(zero+one,0)
        
        while r<len(s)-2:
            r+=1    
            
            if s[r]=='0':
                zero+=1
            
            elif s[r]=='1':
                one-=1
            res=max(zero+one,res)
            
        return(res)
                