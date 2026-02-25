import math

# Input values
x, y = input("Please enter a point for the center of a circle: ").split()
r = int(input("Please enter the radius of the circle: "))
x1, y1, x2, y2 = input("Please enter two points: ").split()

# Convert to integers
x = int(x)
y = int(y)
x1 = int(x1)
y1 = int(y1)
x2 = int(x2)
y2 = int(y2)

# Vertical line case
if x2 == x1:
    large_segment = 0 # no intersection 
else:
    #slope and slope interception
    m = (y2 - y1) / (x2 - x1)
    c = y1 - m * x1

    # Quadratic formula for the intersections
    A = 1 + m**2
    B = 2 * m * (c - y) - 2 * x
    C = x**2 + (c - y)**2 - r**2
    D = B**2 - 4 * A * C

    if D < 0:
        large_segment = 0 # no intersection
    else:
        #The intersection of the two points
        x_1 = (-B + math.sqrt(D)) / (2 * A)
        x_2 = (-B - math.sqrt(D)) / (2 * A)
        y_1 = m * x_1 + c
        y_2 = m * x_2 + c

        # it creates the vectors from the center to the intersection points
        ax, ay = x_1 - x, y_1 - y
        bx, by = x_2 - x, y_2 - y
        # then the dot product to calculate the angles between the vectors
        dot = ax * bx + ay * by
        theta_angle = math.acos(dot / (r * r))

        # calculating the area of the circle segment
        segment_area = 0.5 * r**2 * (theta_angle - math.sin(theta_angle))
        circle_area = math.pi * r**2
        a = circle_area - segment_area

print ("Area: ", a)
