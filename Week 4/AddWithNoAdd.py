def sum(a, b):
    if b == 0:
        return a
    if b != 0:
        return sum(a + 1, b - 1)


a = int(input())
b = int(input())
print(sum(a, b))
