# C. Less or Equal
# time limit per test2 seconds
# memory limit per test256 megabytes
# You are given a sequence of integers of length 𝑛
#  and integer number 𝑘
# . You should print any integer number 𝑥
#  in the range of [1;109]
#  (i.e. 1≤𝑥≤109
# ) such that exactly 𝑘
#  elements of given sequence are less than or equal to 𝑥
# .

# Note that the sequence can contain equal elements.

# If there is no such 𝑥
# , print "-1" (without quotes).

# Input
# The first line of the input contains integer numbers 𝑛
#  and 𝑘
#  (1≤𝑛≤2⋅105
# , 0≤𝑘≤𝑛
# ). The second line of the input contains 𝑛
#  integer numbers 𝑎1,𝑎2,…,𝑎𝑛
#  (1≤𝑎𝑖≤109
# ) — the sequence itself.

# Output
# Print any integer number 𝑥
#  from range [1;109]
#  such that exactly 𝑘
#  elements of given sequence is less or equal to 𝑥
# .

# If there is no such 𝑥
# , print "-1" (without quotes).

# Examples
# InputCopy
# 7 4
# 3 7 5 1 10 3 20
# OutputCopy
# 6
# InputCopy
# 7 2
# 3 7 5 1 10 3 20
# OutputCopy
# -1
# Note
# In the first example 5
#  is also a valid answer because the elements with indices [1,3,4,6]
#  is less than or equal to 5
#  and obviously less than or equal to 6
# .

# In the second example you cannot choose any number that only 2
#  elements of the given sequence will be less than or equal to this number because 3
#  elements of the given sequence will be also less than or equal to this number.


========= CODE =============
n, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

if k == 0:
    if arr[0] - 1 >= 1:
        print(1)
    else:
        print(-1)
else:
    if k < n and arr[k - 1] == arr[k]:
        print(-1)
    else:
        print(arr[k - 1])
