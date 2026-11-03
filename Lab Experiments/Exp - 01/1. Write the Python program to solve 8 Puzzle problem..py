start = input("Enter start state (0 for blank): ")
goal = "123456780"
queue = [[start]]
seen = {start}

while queue:
    path = queue.pop(0)
    s = path[-1]
    if s == goal:
        break
    i = s.index("0")
    for j in (i-3, i+3, i-1, i+1):
        if 0 <= j < 9 and (i//3 == j//3 or i%3 == j%3):
            t = list(s)
            t[i], t[j] = t[j], t[i]
            t = "".join(t)
            if t not in seen:
                seen.add(t)
                queue.append(path + [t])

for s in path:
    print(s[:3], s[3:6], s[6:], sep="\n", end="\n\n")
print("Solved in", len(path)-1, "moves")
