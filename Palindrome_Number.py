#. Given an integer x, return true if x is a palindrome, and false otherwise

'''
Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
'''
#1st Method
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return(str(x) == str(x)[::-1])
        
#2st Method
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return(False)
        rev_num = 0
        digit = 0
        while(x // (10**digit) != 0 ):
            rev_num = (rev_num *10) + ((x // (10**digit) % 10 ))
            digit+=1
        return (x == rev_num)

        