graph = {'WA': ['NT', 'SA'], 'NT': ['WA', 'SA', 'Q'], 'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
         'Q': ['NT', 'SA', 'NSW'], 'NSW': ['Q', 'SA', 'V'], 'V': ['SA', 'NSW'], 'T': []}
colors = ['Red', 'Green', 'Blue']
result = {}

def solve(regions):
    if not regions:
        return True
    r = regions[0]
    for c in colors:
        if all(result.get(n) != c for n in graph[r]):
            result[r] = c
            if solve(regions[1:]):
                return True
            del result[r]
    return False

solve(list(graph))
for r in result:
    print(r, ":", result[r])
