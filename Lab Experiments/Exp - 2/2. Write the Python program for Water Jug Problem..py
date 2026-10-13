from collections import deque


def water_jug_problem(capacity_a, capacity_b, target):
    if target > max(capacity_a, capacity_b):
        return None

    if target % __import__("math").gcd(capacity_a, capacity_b) != 0:
        return None

    start = (0, 0)
    queue = deque([start])
    visited = {start}
    parent = {start: None}
    action = {}

    while queue:
        a, b = queue.popleft()

        if a == target or b == target:
            path = []
            current = (a, b)

            while current is not None:
                path.append((current, action.get(current, "Start")))
                current = parent[current]

            return path[::-1]

        next_states = [
            ((capacity_a, b), "Fill Jug A"),
            ((a, capacity_b), "Fill Jug B"),
            ((0, b), "Empty Jug A"),
            ((a, 0), "Empty Jug B"),
        ]

        amount = min(a, capacity_b - b)
        next_states.append(((a - amount, b + amount), "Pour Jug A into Jug B"))

        amount = min(b, capacity_a - a)
        next_states.append(((a + amount, b - amount), "Pour Jug B into Jug A"))

        for state, operation in next_states:
            if state not in visited:
                visited.add(state)
                queue.append(state)
                parent[state] = (a, b)
                action[state] = operation

    return None


# Example: Jug A = 4 litres, Jug B = 3 litres, target = 2 litres
capacity_a = 4
capacity_b = 3
target = 2

solution = water_jug_problem(capacity_a, capacity_b, target)

if solution:
    print("Solution:")
    for state, operation in solution:
        print(f"{operation:25} -> Jug A: {state[0]}, Jug B: {state[1]}")
else:
    print("No solution exists.")
