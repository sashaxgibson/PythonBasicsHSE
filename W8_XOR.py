import sys
a = sys.stdin.readline().split()
b = sys.stdin.readline().split()
print(*zip(a, b))
#print(*map(lambda x, y: int(x[0]) + int(y[0]), zip(a, b)))
