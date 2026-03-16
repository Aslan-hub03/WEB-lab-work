N = int(input())
arr = list(map(int, input().split()))
found = False
for i in range(N-1):
    if arr[i] * arr[i+1] > 0:  
        found = True
        break
print("YES" if found else "NO")