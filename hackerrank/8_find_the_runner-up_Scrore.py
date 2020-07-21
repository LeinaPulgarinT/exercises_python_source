"""
link del enunciado del punto:
https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
"""
n = int(input())

arr = map(int, input().split())

arr = list(arr)
num_max = -100
for i in range(len(arr)):
    if arr[i] >= num_max:
        num_max = arr[i]


arr = sorted(arr)
    for i in range(len(arr)):
        if arr[i] < num_max and arr[i] != num_max:
            num_sec = arr[i]

print(num_sec)

