N = int(input())
while N > 1 and N % 2 == 0:
    N //= 2
print("YES" if N == 1 else "NO")