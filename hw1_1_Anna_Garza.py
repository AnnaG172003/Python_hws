# this reads the text file
with open('input.txt', 'r') as file:
    lines = file.readlines()

# reads the file lines
num_computers = int(lines[0])      # First line -> total number of computers
num_edges = int(lines[1])          # Second line -> total number of connections


edges = [] #initilizing and empty list
#starts at line 2 b/c lines 0 and 1 are taken already
for i in range(2, 2 + num_edges):  # Loops through the next num_edges lines
    u, v = lines[i].split()        # Split the line into two parts
    u = int(u)                     # Convert first part -> integer
    v = int(v)                     # Convert second part -> integer
    edges.append((u, v))           # Stores the connections as a tuple

#Reads the infected computer number 
node_virus = int(lines[2 + num_edges])  # Starts at the point of infection

#Building a graph using an adjacency list
# Each computer gets a list of its connected neighbors nodes
graph = {i: [] for i in range(1, num_computers + 1)}  # Initializes empty lists 
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)  # Since the graph is undirected

def infected_DFS_method(graph, node_virus):
#Using a dictionary to be able to track which computers are infected
    node_visit = {node: False for node in graph}  # Will mark the all the nodes as not infected at first
    stack = [node_virus]#Stack will start with the first infected noded
#will repeat the process of which are infected until there are no more
    while stack:
        node = stack.pop() #takes the last node an adds it to the stack
        if not node_visit[node]: #if node NOT infected will mark as infected
            node_visit[node] = True
            for neighbor in graph[node]: #checks the neighbor nodes if they are infected or not
                if not node_visit[neighbor]: #if not infected going to add it to stack
                    stack.append(neighbor)

    # Count infected computers excluding the source
    return sum(node_visit.values()) - 1

infected_count = infected_DFS_method(graph, node_virus)



# result for output
with open('output.txt', 'w') as file:
    file.write(str(infected_count))

print("Total infected computers:", infected_count)