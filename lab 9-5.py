number = int(input("Please input a number? "))
for i in range(1, number + 1):
    for j in range(1):
        print(" ", end="")
    for k in range (i):
        print("*",end="")
    print("")
