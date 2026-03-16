import math
a = int(input())
b = int(input())
start = math.ceil(math.sqrt(a))
end = math.floor(math.sqrt(b))
result = [str(i*i) for i in range(start, end + 1)]
print(' '.join(result))