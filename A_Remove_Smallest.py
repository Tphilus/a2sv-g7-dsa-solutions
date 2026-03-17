# A. Remove Smallest
# time limit per test1 second
# memory limit per test256 megabytes
# You are given the array 𝑎
#  consisting of 𝑛
#  positive (greater than zero) integers.

# In one move, you can choose two indices 𝑖
#  and 𝑗
#  (𝑖≠𝑗
# ) such that the absolute difference between 𝑎𝑖
#  and 𝑎𝑗
#  is no more than one (|𝑎𝑖−𝑎𝑗|≤1
# ) and remove the smallest of these two elements. If two elements are equal, you can remove any of them (but exactly one).

# Your task is to find if it is possible to obtain the array consisting of only one element using several (possibly, zero) such moves or not.

# You have to answer 𝑡
#  independent test cases.

# Input
# The first line of the input contains one integer 𝑡
#  (1≤𝑡≤1000
# ) — the number of test cases. Then 𝑡
#  test cases follow.

# The first line of the test case contains one integer 𝑛
#  (1≤𝑛≤50
# ) — the length of 𝑎
# . The second line of the test case contains 𝑛
#  integers 𝑎1,𝑎2,…,𝑎𝑛
#  (1≤𝑎𝑖≤100
# ), where 𝑎𝑖
#  is the 𝑖
# -th element of 𝑎
# .

# Output
# For each test case, print the answer: "YES" if it is possible to obtain the array consisting of only one element using several (possibly, zero) moves described in the problem statement, or "NO" otherwise.

# Example
# InputCopy
# 5
# 3
# 1 2 2
# 4
# 5 5 5 5
# 3
# 1 2 4
# 4
# 1 3 4 4
# 1
# 100
# OutputCopy
# YES
# YES
# NO
# NO
# YES
# Note
# In the first test case of the example, we can perform the following sequence of moves:

# choose 𝑖=1
#  and 𝑗=3
#  and remove 𝑎𝑖
#  (so 𝑎
#  becomes [2;2]
# );
# choose 𝑖=1
#  and 𝑗=2
#  and remove 𝑎𝑗
#  (so 𝑎
#  becomes [2]
# ).
# In the second test case of the example, we can choose any possible 𝑖
#  and 𝑗
#  any move and it doesn't matter which element we remove.

# In the third test case of the example, there is no way to get rid of 2
#  and 4
# .


# ======== code =========

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    arr.sort()
    possible = True
    
    for i in range(n - 1):
        if arr[i + 1] - arr[i] > 1:
            possible = False
            break
    
    if possible:
        print("YES")
    else:
        print("NO")