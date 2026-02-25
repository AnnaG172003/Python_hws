def rectangle_area_calculations(circles):
    # Initializing the bounds using the first circle 
    first = circles[0]
    #edges of the circles
    min_x = first['x'] - first['r'] 
    max_x = first['x'] + first['r']
    min_y = first['y'] - first['r']
    max_y = first['y'] + first['r']
    # updating the remaining circles in the rectangle
    for i in range(1, len(circles)):
        center = circles[i]
        left = center['x'] - center['r']
        right = center['x'] + center['r']
        bottom = center['y'] - center['r']
        top = center['y'] + center['r']
    #if needed will update the overall bound of the edges
        if left < min_x:
            min_x = left
        if right > max_x:
            max_x = right
        if bottom < min_y:
            min_y = bottom
        if top > max_y:
            max_y = top
    #rectangle dimension calculations
    width = max_x - min_x
    height = max_y - min_y
    return round(width * height, 2)
#input
M_lines= int(input("Enter number of circles: "))
circles = []
#reads the circle edge and radius using dictionary
for i in range(M_lines):
    line = input(" ").split()
    x_axis = float(line[0])
    y_axis = float(line[1])
    radius = float(line[2])
    circles.append({'x': x_axis, 'y': y_axis, 'r': radius})

# Output
area = rectangle_area_calculations(circles)
print("Area: ", area)