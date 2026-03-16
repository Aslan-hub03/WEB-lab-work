N = int(input())
p = 1
result = []
while p <= N:
    result.append(str(p))
    p *= 2
print(' '.join(result))