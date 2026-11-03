start = (3, 3, 1)
queue = [[start]]
seen = {start}
moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

while queue:
    path = queue.pop(0)
    m, c, b = path[-1]
    if (m, c, b) == (0, 0, 0):
        break
    sign = -1 if b == 1 else 1
    for dm, dc in moves:
        nm, nc = m + sign*dm, c + sign*dc
        if 0 <= nm <= 3 and 0 <= nc <= 3 and (nm == 0 or nm >= nc) and (nm == 3 or 3-nm >= 3-nc):
            s = (nm, nc, 1-b)
            if s not in seen:
                seen.add(s)
                queue.append(path + [s])

for m, c, b in path:
    print("Left:", m, "M", c, "C | Right:", 3-m, "M", 3-c, "C | Boat:", "Left" if b else "Right")
