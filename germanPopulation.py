case = open("./case.txt", 'r')
arr = []
for line in case:
    arr.append(line.split())

print(arr)


def sor(e):
    return int(e[9]) - int(e[8])


arr.sort(key=sor)

for line in arr:
    print(line)

