# A. Merging Arrays
# time limit per test1 second
# memory limit per test256 megabytes
# For educational purposes, in the problems of this block, the time limit is large enough for the solution to pass in 𝑂(𝑛log𝑛)
#  time, but try to write the solution in linear time, which we discussed in the lecture.

# You are given two arrays, sorted in non-decreasing order. Merge them into one sorted array.

# Input
# The first line contains integers 𝑛
#  and 𝑚
# , the sizes of the arrays (1≤𝑛,𝑚≤105
# ). The second line contains 𝑛
#  integers 𝑎𝑖
# , elements of the first array, the third line contains 𝑚
#  integers 𝑏𝑖
# , elements of the second array (−109≤𝑎𝑖,𝑏𝑖≤109
# ).

# Output
# Print 𝑛+𝑚
#  integers, the merged array.

# Example
# InputCopy
# 6 7
# 1 6 9 13 18 18
# 2 3 8 13 15 21 25
# OutputCopy
# 1 2 3 6 8 9 13 13 15 18 18 21 25 

# === CODE ===

n, m = map(int, input().split())
arr_n = list(map(int, input().split()))
arr_m = list(map(int, input().split()))

merged = []
first, second = 0, 0

while first < n and second < m:
    if arr_n[first] < arr_m[second]:
        merged.append(arr_n[first])
        first += 1
    else:
        merged.append(arr_m[second])
        second += 1

merged.extend(arr_n[first:])
merged.extend(arr_m[second:])

print(*merged)
