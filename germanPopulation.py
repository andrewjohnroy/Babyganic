case = open("./case.txt", 'r')
arr = []
for line in case:
    arr.append(line.split())


def sor(e):
    return int(e[8]) - int(e[9])


arr.sort(key=sor)

for line in arr:
    print(line[0] + " " + str(int(line[9]) - int(line[8])) + " population growth from 2010-2015")

