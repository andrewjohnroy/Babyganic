case = open("./case.txt", 'r')
arr = []
for line in case:
    arr.append(line.split())


def sor_growth(e):
    return int(e[8]) - int(e[9])


def sor_max(e):
    return -int(e[9])


arr.sort(key=sor_growth)

for i in range(2):
    print(arr[i][0] + " is a city for a shop with " + str(int(arr[i][9]) - int(arr[i][8])) + " population growth from "
                                                                                           "2010-2015")
print()

arr.sort(key=sor_max)

for i in range(3):
    print(arr[i][0] + " is a city for sales agents with " + str(int(arr[i][9])) + " population in 2015")
