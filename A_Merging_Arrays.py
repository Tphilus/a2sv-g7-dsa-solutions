n,m = map(int, input().split())
first_arr = list(map(int, input().split()))
second_arr = list(map(int, input().split()))

first = 0
second = 0
merge = []

while first < len(first_arr) and second < len(second_arr):
    if first_arr[first] < second_arr[second]:
        merge.append(first_arr[first])
        first += 1
    else:
        merge.append(second_arr[second])
        second += 1

merge.extend(first_arr[first:])
merge.extend(second_arr[second:])

print(*merge)
