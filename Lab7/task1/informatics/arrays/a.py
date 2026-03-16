N = int(input())
arr = list(map(int, input().split()))
result = [str(arr[i]) for i in range(0, N, 2)]
print(' '.join(result))