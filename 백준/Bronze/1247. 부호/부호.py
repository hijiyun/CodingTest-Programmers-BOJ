from sys import stdin
 
list1 = []
for _ in range(3):
    n = int(stdin.readline())
    data = [int(stdin.readline()) for i in range(n)]
    list1.append(sum(data))
 
for i in range(3):
    if list1[i] == 0:
        print("0")
    elif list1[i] > 0:
        print("+")
    else:
        print("-")