N = int(input())
arr = list(map(int, input().split()))
# Reverse in place
for i in range(N // 2):
    arr[i], arr[N-1-i] = arr[N-1-i], arr[i]
print(' '.join(map(str, arr)))