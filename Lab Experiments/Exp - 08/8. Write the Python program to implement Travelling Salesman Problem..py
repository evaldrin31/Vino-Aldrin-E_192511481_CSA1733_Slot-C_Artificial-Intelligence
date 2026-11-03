from itertools import permutations

d = [[0, 10, 15, 20],
     [10, 0, 35, 25],
     [15, 35, 0, 30],
     [20, 25, 30, 0]]
n = len(d)
best_cost = 9999

for p in permutations(range(1, n)):
    route = (0,) + p + (0,)
    cost = sum(d[route[i]][route[i+1]] for i in range(n))
    if cost < best_cost:
        best_cost = cost
        best_route = route

print("Shortest route:", *best_route)
print("Minimum cost:", best_cost)
