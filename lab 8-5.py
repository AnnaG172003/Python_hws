l1, l2, l3 = input("Please input lengths of three line segments: ").split()
length1 =int(l1)
length2 =int(l2)
length3 =int(l3)
if length1 + length2 > length3 and length1 + length3 > length2 and length2 + length3 > length1:
    print ("Yes")
else:
    print("No")