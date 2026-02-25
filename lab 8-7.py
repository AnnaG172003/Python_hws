a, b, c, d = input("Please input lengths of four line segments to build a rectangle: ").split()
l1 =int(a)
l2 =int(b)
l3 =int(c)
l4 =int(d)
if (l1 == l2 and l3==l4) or (l1 == l3 and l2 ==l4)  or (l1== l4 and l2== l3):
    print("Yes")
else:
    print("No")

