'''
Zigzag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 
Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
'''

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1 or numRows >= len(s):
            return s
        
        rows = [''] * min(numRows, len(s))
        curRow, goingDown = 0, False

        for c in s:
            rows[curRow] += c
         
            if curRow == 0 or curRow == numRows - 1:
                goingDown = not goingDown
            curRow += 1 if goingDown else -1

        return ''.join(rows)