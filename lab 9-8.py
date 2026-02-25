number = int(input("Please input a number? "))
for i in range(0, number ):  
    for j in range(number - i):  
        print(" ", end="")
    for k in range(0, 2*i+1):  
        print("*", end="")
    print("")