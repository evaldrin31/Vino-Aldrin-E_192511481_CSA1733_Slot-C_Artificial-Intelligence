graph = {'S': [('A', 1), ('B', 4)], 'A': [('B', 2), ('C', 5), ('G', 12)], 'B': [('C', 2)], 'C': [('G', 3)], 'G': []}
h = {'S': 7, 'A': 6, 'B': 2, 'C': 1, 'G': 0}
open_list = [(h['S'], 0, ['S'])]

while open_list:
    open_list.sort()
    f, g, path = open_list.pop(0)
    node = path[-1]
    if node == 'G':
        print("Path:", " -> ".join(path))
        print("Cost:", g)
        break
    for n, cost in graph[node]:
        open_list.append((g + cost + h[n], g + cost, path + [n]))
