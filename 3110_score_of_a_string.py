'''
3110. Score of a String


Example 1:

Input: s = "hello"
Output: 13

Explanation:
The ASCII values of the characters in s are: 'h' = 104, 'e' = 101, 'l' = 108, 'o' = 111. So, the score of s would be |104 - 101| + |101 - 108| + |108 - 108| + |108 - 111| = 3 + 7 + 0 + 3 = 13.

Example 2:
Input: s = "zaz"
Output: 50

Explanation:
The ASCII values of the characters in s are: 'z' = 122, 'a' = 97. So, the score of s would be |122 - 97| + |97 - 122| = 25 + 25 = 50.


Constraints:

2 <= s.length <= 100
s consists only of lowercase English letters.
'''

class Solution:
    num_array = []
    def scoreOfString(self, s: str) -> int:
 
        total_sum = 0
        for i in range(0,len(s)-1):
            curr_sum = abs(ord(s[i]) - ord(s[i+1]))
            total_sum = total_sum + curr_sum
        
        return total_sum