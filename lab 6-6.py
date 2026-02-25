
x1, y1 = (input("Please input the first end point: ")).split()
x2, y2 = (input("Please input the second end point: ")).split()
x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)
length = ((x2-x1)**2+(y2-y1)**2)**(1/2)
print(f"Length: {length}")