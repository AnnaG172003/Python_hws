# Read the input file text
with open("input.txt", "r") as file:
    input_lines = file.readlines()


N = int(input_lines[0]) #number of stations on the starting line
M = int(input_lines[1])#numver of bus lines 

# Converts each bus line into a set of covered stations
bus_line_coverage = []

for i in range(2, 2 + M):
    # Reads where the bus line starts and ends
    parts = input_lines[i].split()
    a = int(parts[0])
    b = int(parts[1])

    # Figures out which stations this bus line stops at
    stations_covered = []
    if a <= b:
        # A normal case of the  bus going from a to b without wrapping around
        for station in range(a, b + 1):
            stations_covered.append(station)
    else:
        # A special case where the bus wraps around from a to end, then from start to b
        for station in range(a, N):
            stations_covered.append(station)
        for station in range(0, b + 1):
            stations_covered.append(station)
    
    # Reminder which stations this bus line covers
    bus_line_coverage.append(stations_covered)

# We need to cover all stations from 0 to N-1
all_stations = list(range(N))

# Function to check if we can cover all stations using exactly target_count bus lines
def find_combination(selected_lines, next_indx, count_target):
    # If we've selected the right number of bus lines, check if they cover everything
    if len(selected_lines) == count_target:
        # Combine all stations covered by our selected bus lines
        covered_stations = []
        for line_indx in selected_lines:
            for station in bus_line_coverage[line_indx]:
                # Only add each station once (no duplicates)
                if station not in covered_stations:
                    covered_stations.append(station)
        
        # See if we have covered every single station
        if len(covered_stations) == N:
            return True
        return False
    # Tries adding more bus lines to the selection
    for i in range(next_indx, M):
        # Checks if adding this bus line helps us cover all stations
        if find_combination(selected_lines + [i], i + 1, count_target):
            return True
    return False

# Starts by assuming we need all bus lines, then try to find a smaller number
min_required_lines = M

# Try using 1 bus line, then 2, then 3 and so on until we find the smallest number that works
for line_count in range(1, M + 1):
    # Check if we can cover all stations using exactly line_count bus lines
    if find_combination([], 0, line_count):
        min_required_lines = line_count
        break

# Writes the result in the ouput and print it out on the terminal
with open("output.txt", "w") as file:
    file.write(str(min_required_lines))

print(min_required_lines)