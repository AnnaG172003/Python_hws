number = int(input("Please input a number? "))
for i in range(number, 0, -1): 
    for j in range(0, number - i):
        print(" ", end="")  
    for k in range(i):  
        print("*", end="")
    print("")