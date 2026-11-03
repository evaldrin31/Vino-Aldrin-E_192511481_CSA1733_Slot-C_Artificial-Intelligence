graph = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'], 'D': [], 'E': ['F'], 'F': []}
start = input("Enter start node: ").upper()
visited = [start]
queue = [start]

print("BFS Traversal:", end=" ")
while queue:
    node = queue.pop(0)
    print(node, end=" ")
    for n in graph[node]:
        if n not in visited:
            visited.append(n)
            queue.append(n)
