a = b = 0
x = int(input("Capacity of Jug A: "))
y = int(input("Capacity of Jug B: "))
target = int(input("Target amount: "))

while a != target and b != target:
    if a == 0:
        a = x
    elif b == y:
        b = 0
    else:
        p = min(a, y - b)
        a -= p
        b += p
    print("Jug A:", a, "Jug B:", b)
