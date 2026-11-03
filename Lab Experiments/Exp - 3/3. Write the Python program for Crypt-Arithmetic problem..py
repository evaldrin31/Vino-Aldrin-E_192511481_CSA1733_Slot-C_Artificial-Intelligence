from itertools import permutations

w1 = input("Enter first word: ").upper()
w2 = input("Enter second word: ").upper()
res = input("Enter result word: ").upper()
letters = list(set(w1 + w2 + res))

def val(w, d):
    return int("".join(str(d[c]) for c in w))

for p in permutations(range(10), len(letters)):
    d = dict(zip(letters, p))
    if d[w1[0]] == 0 or d[w2[0]] == 0 or d[res[0]] == 0:
        continue
    if val(w1, d) + val(w2, d) == val(res, d):
        print(w1, "=", val(w1, d))
        print(w2, "=", val(w2, d))
        print(res, "=", val(res, d))
        print(d)
        break
else:
    print("No solution")
