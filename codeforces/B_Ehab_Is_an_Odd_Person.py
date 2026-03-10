# B. Ehab Is an Odd Person
# time limit per test1 second
# memory limit per test256 megabytes
# You're given an array 𝑎
#  of length 𝑛
# . You can perform the following operation on it as many times as you want:

# Pick two integers 𝑖
#  and 𝑗
#  (1≤𝑖,𝑗≤𝑛)
#  such that 𝑎𝑖+𝑎𝑗
#  is odd, then swap 𝑎𝑖
#  and 𝑎𝑗
# .
# What is lexicographically the smallest array you can obtain?

# An array 𝑥
#  is lexicographically smaller than an array 𝑦
#  if there exists an index 𝑖
#  such that 𝑥𝑖<𝑦𝑖
# , and 𝑥𝑗=𝑦𝑗
#  for all 1≤𝑗<𝑖
# . Less formally, at the first index 𝑖
#  in which they differ, 𝑥𝑖<𝑦𝑖

# Input
# The first line contains an integer 𝑛
#  (1≤𝑛≤105
# ) — the number of elements in the array 𝑎
# .

# The second line contains 𝑛
#  space-separated integers 𝑎1
# , 𝑎2
# , …
# , 𝑎𝑛
#  (1≤𝑎𝑖≤109
# ) — the elements of the array 𝑎
# .

# Output
# The only line contains 𝑛
#  space-separated integers, the lexicographically smallest array you can obtain.

# Examples
# InputCopy
# 3
# 4 1 7
# OutputCopy
# 1 4 7 
# InputCopy
# 2
# 1 1
# OutputCopy
# 1 1 
# Note
# In the first example, we can swap 1
#  and 4
#  since 1+4=5
# , which is odd.

# == CODE ==

t = int(input())
arr = list(map(int, input().split()))

has_even = False
has_odd = False

for num in arr:
    if num % 2 == 0:
        has_even = True
    else:
        has_odd = True
    
    if has_even and has_odd:
        break

if has_even and has_odd:
    arr.sort()

print(*arr)
