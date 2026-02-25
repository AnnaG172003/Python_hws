# Step 1: Input number of computers
num_computers = int(input("Enter the number of computers: "))

# Step 2: Input number of connections (edges)
num_edges = int(input("Enter the number of connections: "))

# Step 3: Input each edge manually
edges = []
print("Enter each connection as two numbers separated by a space (e.g., 1 2):")
for _ in range(num_edges):
    edge_input = input()
    u, v = edge_input.strip().split()
    u = int(u)
    v = int(v)
    edges.append((u, v))

# Step 4: Input the infected computer
node_virus = int(input("Enter the infected computer number: "))

# Step 5: Build the adjacency list
graph = {i: [] for i in range(1, num_computers + 1)}
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)

# Step 6: DFS to simulate infection
def infected_DFS_method(graph, node_virus):
    visited = set()
    stack = [node_virus]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
    return visited

# Step 7: Run DFS and count infected computers
infected_computers = infected_DFS_method(graph, node_virus)
infected_count = len(infected_computers) - 1  # Exclude the source

# Step 8: Display result
print("Total infected computers (excluding the source):", infected_count)