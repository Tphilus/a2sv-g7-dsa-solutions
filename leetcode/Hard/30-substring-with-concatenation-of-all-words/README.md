# 30. Substring with Concatenation of All Words

- **Platform:** LeetCode
- **Difficulty:** Hard
- **Language:** Python3
- **Submitted:** 2026-10-01T20:02:40.603Z
- **Problem link:** https://leetcode.com/problems/substring-with-concatenation-of-all-words/

## Problem Statement

You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.


	For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.


Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.

 
Example 1:


Input: s = "barfoothefoobarman", words = ["foo","bar"]

Output: [0,9]

Explanation:

The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.


Example 2:


Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]

Output: []

Explanation:

There is no concatenated substring.


Example 3:


Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]

Output: [6,9,12]

Explanation:

The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].


 
Constraints:


	1 <= s.length <= 104
	1 <= words.length <= 5000
	1 <= words[i].length <= 30
	s and words[i] consist of lowercase English letters.

## Solution

```python

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_freq = {}
        for word in words:
            word_freq[word] = 1 + word_freq.get(word, 0)

        word_len = len(words[0])
        window_len = len(words) * word_len
        res = []

        for i in range(len(s) - window_len + 1):
            substr_freq = {}
            j = i

            while j < i + window_len:
                cur_word = s[j : j + word_len]

                if cur_word not in word_freq:
                    break
                substr_freq[cur_word] = substr_freq.get(cur_word, 0) + 1

                if substr_freq[cur_word] > word_freq[cur_word]:
                    break
                j += word_len
            
            if j == i + window_len:
                res.append(i)

        return res
```

## Complexity

- **Time:** O(n^2)
- **Space:** O(n)

_Estimated from a static scan of loop nesting and allocation patterns, not true algorithmic analysis — verify before relying on it._
