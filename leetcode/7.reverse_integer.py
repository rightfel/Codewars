'''
Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
Example 4:

Input: x = 0
Output: 0
 

Constraints:

-231 <= x <= 231 - 1
'''

class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        absolute = abs(x)
        while absolute != 0:
            result = absolute % 10 + result * 10
            absolute = absolute // 10
        if result > (2 ** 31) - 1 or result < (-2 **31) - 1:
            return 0
        elif x < 0:
            return -result
        else:
            return result
