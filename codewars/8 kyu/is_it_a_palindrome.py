'''
Write function isPalindrome that checks if a given string (case insensitive) is a palindrome.
'''


def is_palindrome(s):
    lower_string = s.lower()
    left = 0
    right = len(s) - 1
    while left < right:
        if lower_string[left] != lower_string[right]:
            return False
        left += 1
        right -= 1
    return True
