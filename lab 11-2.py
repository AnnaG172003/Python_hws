
def triangle_Area ():
    x1, y1, x2, y2, x3, y3 = input("Please input three points: ").split()
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)
    x3 = int(x3)
    y3 = int(y3)
    first_partEquation = (x1 * y2) + (x2 * y3) + (x3 * y1) - (x1 * y3) - (x2 * y1) - (x3 * y2)
    second_partEquation = abs(first_partEquation)*float(0.5)
    return second_partEquation

print("The area is: ", triangle_Area())