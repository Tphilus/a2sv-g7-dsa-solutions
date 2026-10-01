# 125. Valid Palindrome

- **Platform:** LeetCode
- **Difficulty:** Easy
- **Language:** Python3
- **Submitted:** 2026-10-01T19:34:07.149Z
- **Problem link:** https://leetcode.com/problems/valid-palindrome/

## Problem Statement

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 
Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.


Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.


Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.


 
Constraints:


	1 <= s.length <= 2 * 105
	s consists only of printable ASCII characters.

## Solution

```python

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char.lower() for char in s if char.isalnum())

        return s == s[::-1]
```

## Complexity

- **Time:** O(1)
- **Space:** O(1)

_Estimated from a static scan of loop nesting and allocation patterns, not true algorithmic analysis — verify before relying on it._
