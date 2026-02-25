# Read the input file text
with open("input.txt", "r") as file:
    input_lines = file.readlines()

#  Extract grid size (N) and number of civilizations (K) from the first line
first_line = input_lines[0].split()
N = int(first_line[0])
K = int(first_line[1])

# Store civilization positions
civil = []
for i in range(1, K + 1):
    position = input_lines[i].split()
    x = int(position[0])
    y = int(position[1])
    civil.append([x, y])

# Function to check if all civilizations are connected
def all_connected(civil, year):
    for i in range(len(civil)):
        for j in range(i + 1, len(civil)):
            # Calculate Manhattan distance(using the formula) between two civilizations
            dist = abs(civil[i][0] - civil[j][0]) + abs(civil[i][1] - civil[j][1])
            if dist > year * 2 :
                return False
    return True

# Finds the minimum years using binary search
low = 0
high = 2 * N  # Maximum possible years

# Binary search to find the minimum year when all civilizations are connected
while low <= high:
    mid = (low + high) // 2
    if all_connected(civil, mid):
        high = mid - 1
    else:
        low = mid + 1

# The answer is the lower bound
result = low

# Writes output
with open('output.txt', 'w') as file:
    file.write(str(result))

# Also display on terminal
print(result)