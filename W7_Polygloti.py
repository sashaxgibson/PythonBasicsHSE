inFile = open('input.txt', 'r', encoding='utf-8')
dataList = []
for line in inFile:
    dataList.append(line.strip())
print(dataList)
numLang = int(dataList[1])
knowledgeList = []
i = 1
while i