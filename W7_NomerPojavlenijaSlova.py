inFile = open('input.txt')
a = inFile.read()
print(a)
print(a.strip())
print(list(map(str, a.split())))
print(len(a.split()))
